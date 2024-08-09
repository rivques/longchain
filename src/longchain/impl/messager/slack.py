from collections.abc import Awaitable, Callable, Sequence
import re
from typing import Never
from longchain.core.dataclasses import Player, PlayerAction
from longchain.core.datastore import Datastore
from longchain.core.messager import Messager

try:
    from slack_bolt.app.async_app import AsyncApp
    from slack_bolt.adapter.socket_mode.async_handler import AsyncSocketModeHandler
    from slack_sdk.web.async_client import AsyncWebClient
except ImportError:
    raise ImportError("The `slack` messager is not available when the `slack` extra is not installed.")

class SlackMessager(Messager):
    def __init__(self, bot_token: str, app_token: str, start_path: str, datastore: Datastore, active_channel: str, reset_user_command: str, admins: list[str], workspace_name: str = 'hackclub'):
        self.start_path = start_path
        self.datastore = datastore
        self.active_channel = active_channel
        self.reset_user_command = reset_user_command
        self.admins = admins
        self.app_token = app_token
        self.app = AsyncApp(token=bot_token)
        self.workspace_name = workspace_name

    async def send_messages(self, messages, do_send_message_hint):
        for i, message in enumerate(messages):
            player = await self.datastore.get_player_by_interaction_id(message.interaction_id)
            if player is None:
                print(f"ERROR: Player not found for message {message.interaction_id}")
                # this should be unreachable, but just in case
                continue
            blocks = [
                {
                    "type": "section",
                    "text": {
                        "type": "mrkdwn",
                        "text": message.text
                    }
                }
            ]
            if i == len(messages) - 1 and do_send_message_hint:
                blocks.append({
                    "type": "context",
                    "elements": [
                        {
                            "type": "mrkdwn",
                            "text": "It's your turn to send a message now!"
                        }
                    ]
                })
            await self.app.client.chat_postMessage(channel=player.messager_state["channel"], text=message.text, thread_ts=message.interaction_id, username=message.name, icon_url=message.icon, blocks=blocks)

    async def handle_thread_message(self, client, body, tick: Callable[[Player, Sequence[PlayerAction]], Awaitable[None]]):
        player = await self.datastore.get_player_by_interaction_id(body["event"]["thread_ts"])
        if player is None:
            # this thread is not a game thread, ignore it
            return
        if player.id != body["event"]["user"]:
            await client.chat_postEphemeral(channel=body["event"]["channel"], thread_ts=body["event"]["thread_ts"], user=body["event"]["user"], text=f"Hey, you're not <@{player.id}>! You're being ignored, you hear me? Ignored!")
            return
        if player.messager_state["last_unprocessed_message"] is not None and (player.messager_state["last_unprocessed_message"] < float(body["event"]["ts"]) or (player.messager_state["last_processed_message"] is not None and player.messager_state["last_processed_message"] < float(body["event"]["ts"]))):
            # okay that logic is a bit of a doozy but:
            # if last_unprocessed_message is None, then this is the first message and we're fine
            # if the last unprocessed message is older than this one, then we're still processing the last one
            # or, if the last processed message is older than this one, then we're still processing another one
            # in either case, we should ignore this message
            await client.reactions_add(channel=body["event"]["channel"], name="tw_x", timestamp=body["event"]["ts"])
            await client.chat_postEphemeral(channel=body["event"]["channel"], thread_ts=body["event"]["thread_ts"], user=body["event"]["user"], text="I'm still processing your last message. This message was ignored. Please don't send multiple messages in a row.")
            if player.messager_state["last_processed_message"] is None or player.messager_state["last_processed_message"] < float(body["event"]["ts"]):
                # this counts as processing the message, so update the last processed message time if it's newer
                player.messager_state["last_processed_message"] = float(body["event"]["ts"])
            return
        await client.reactions_add(channel=body["event"]["channel"], name="loading-dots", timestamp=body["event"]["ts"])
        player.messager_state["last_unprocessed_message"] = float(body["event"]["ts"])

        if player.current_path in player.path_states and player.path_states[player.current_path].get("messages") is not None:
            print(f"Player {player.name} is on path {player.current_path} with {len(player.path_states[player.current_path]['messages'])} messages")
        # okay by this point we should be good to actually process the message
        # with the gurantees that this player is real, the plaayer is the one who sent
        # the message, and that we're not processing another of the same player's message already
        # start by creating player actions
        # for now, we'll just assume the player is sending a message
        # TODO: support buttons, somehow
        player_actions = [PlayerAction(name="say", data={"message": body["event"]["text"]})]
        # tick the quest
        try:
            await tick(player, player_actions)
        except Exception as e:
            await client.reactions_add(channel=body["event"]["channel"], name="tw_no_entry_sign", timestamp=body["event"]["ts"])
            raise
        else:
            await client.reactions_add(channel=body["event"]["channel"], name="tw_white_check_mark", timestamp=body["event"]["ts"])
        finally:
            await client.reactions_remove(channel=body["event"]["channel"], name="loading-dots", timestamp=body["event"]["ts"])
            # update the message processing state
            player.messager_state["last_processed_message"] = float(body["event"]["ts"])
            player.messager_state["last_unprocessed_message"] = None
            if await self.datastore.get_player_by_id(player.id) is not None:
                # make sure the player wasn't deleted out from under us
                await self.datastore.save_player(player)
        
    async def start(self, tick, start_interaction) -> Never:
        self.handler = AsyncSocketModeHandler(app=self.app, app_token=self.app_token)
        @self.app.event("app_mention")
        async def handle_app_mention(client, body, say, ack):
            await ack()
            if "thread_ts" in body["event"]:
                pass # we were pinged in a thread, the other handler'll catch it
            elif body["event"]["channel"] == self.active_channel:
                player = await self.datastore.get_player_by_id(body["event"]["user"])
                if player is not None:
                    await client.chat_postEphemeral(channel=body["event"]["channel"], user=body["event"]["user"], text=f"You're already in a conversation with me. Please continue that conversation <https://{self.workspace_name}.slack.com/archives/{self.active_channel}/p{str(player.interaction_id).replace('.','')}|here>.")
                    return
                player_name = await client.users_info(user=body["event"]["user"])
                player = Player(id=body["event"]["user"], current_path=self.start_path, name=player_name["user"]["profile"]["display_name"], interaction_id=body["event"]["ts"], path_states={}, messager_state={"channel": body["event"]["channel"], "last_unprocessed_message": None, "last_processed_message": float(body["event"]["ts"])}, plugin_state={})
                await self.datastore.save_player(player)
                await start_interaction(player)
            else:
                await say(f"I can't speak here. Try pinging me in <#{self.active_channel}>.")
        
        username_re = re.compile(r"<@(.*)\|.*>")

        @self.app.command(self.reset_user_command)
        async def handle_reset_user_command(ack, command, client, respond):
            await ack()
            print(f"Got reset user command from {command['user_id']}")
            if command["user_id"] not in self.admins:
                await respond(f"Sorry, you're not allowed to do that.", responce_type="ephemeral")
                return
            
            mo = username_re.match(command["text"])
            if mo is None or len(mo.groups()) != 1:
                await respond(f"That didn't parse properly. Make sure you're @ing a user.", response_type="ephemeral")
                return
            
            user_id_to_reset = mo.group(1)
            
            player = await self.datastore.get_player_by_id(user_id_to_reset)
            if player is None:
                await respond(f"Player not found. Why are you running this command?", response_type="ephemeral")
                return
            
            await self.datastore.remove_player(user_id_to_reset)
            print(f"Player {user_id_to_reset} reset.")
            await respond(f"Player <@{player.id}> reset.", response_type="ephemeral")
        
        @self.app.message()
        async def handle_message(client, body, say):
            if "thread_ts" in body["event"]:
                await self.handle_thread_message(client, body, tick)

        await self.handler.start_async()
        while True: # unreachable, the above call never returns
            pass