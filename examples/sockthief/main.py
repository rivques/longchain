import asyncio
from longchain.core.dataclasses import Message, PathResult, Player
from longchain.core.path import Path
from longchain.core.quest import Quest
from longchain.impl.actionresolver.sequential import SequentialActionResolver
from longchain.impl.agentaction.arbitrary import ArbitraryAgentAction
from longchain.impl.agentaction.end import ChangePathAction, RemovePlayerAction
from longchain.impl.agentaction.message import MessageAgentAction
from longchain.impl.datastore.jsonfile import JsonFileDatastore
from longchain.impl.messager.slack import SlackMessager
from longchain.impl.actionresolver.llm import LlmTool, LlmToolParam, LlmToolResult, OpenAIActionResolver
from longchain.plugins.bag import bag_instance
import os

if "ENVIRONMENT" not in os.environ or os.environ["ENVIRONMENT"] != "production":
    import dotenv
    dotenv.load_dotenv(override=True)

ENV_VARS_REQUIRED = ["ENVIRONMENT", "SLACK_BOT_TOKEN", "SLACK_APP_TOKEN", "HOME_CHANNEL_ID", "DATA_FILEPATH", "BOT_USER_ID", "OPENAI_API_KEY", "OPENAI_API_URL", "ADMINS", "BAG_APP_ID", "BAG_APP_KEY", "QUEST_OWNER_ID"]
if not all([var in os.environ for var in ENV_VARS_REQUIRED]):
    raise Exception(f"Missing the following environment variables: {', '.join([var for var in ENV_VARS_REQUIRED if not var in os.environ])}")

datastore = JsonFileDatastore(os.environ["DATA_FILEPATH"])

bag_instance.configure(int(os.environ["BAG_APP_ID"]), os.environ["BAG_APP_KEY"], os.environ["QUEST_OWNER_ID"])

def player_has_bone(player: Player):
    inventory = bag_instance.get_inventory(player.id)
    has_bone = False
    for item in inventory:
        if item.itemId == "Bone":
            has_bone = True
            break
    return has_bone

quest = Quest(
    name="Sock Thief",
    paths=[
        Path(
            id="welcome",
            starts_without_player_action=True,
            action_resolver=SequentialActionResolver(
                MessageAgentAction("A cloaked figure approaches you. They look like they're trying to be sneaky, but they're not doing a very good job of it. \"Hello, traveller,\" they whisper.", name="Welcome", icon_url="https://example.com/icon.png"),
                ChangePathAction("stocking_initial") # ChangePathAction("stocking_initial")
            )
        ),
        Path(
            id="stocking_initial",
            starts_without_player_action=False,
            action_resolver=OpenAIActionResolver(
                openai_token=os.environ["OPENAI_API_KEY"],
                openai_base_url=os.environ["OPENAI_API_URL"],
                model="gpt-4o-mini",
                system_prompt="You are a game master for an RPG. Right now the player is in a town square. A cloaked figure, Agent Stocking, has approached them. Agent Stocking is a spy, but someone has stolen his lucky socks! Without them, he cannot be stealthy. He needs to convince the player to go find his socks! Agent Stocking should first introduce himself, then ask the player for help.",
                name="Cloaked Figure",
                agent_actions=[
                    LlmTool(
                        name="stocking_agree",
                        description="Call this tool once the player agrees to help Agent Stocking.",
                        params=[],
                        available=lambda ctx: True,
                        action=lambda ctx, params: LlmToolResult(
                            agent_actions=[ChangePathAction("stocking_agree_transistion", next_action="path")],
                            model_feedback="Agent Stocking has convinced the player to help."
                        )
                    ),
                    LlmTool(
                        name="stocking_disagree",
                        description="Call this tool if the player refuses multiple times to help Agent Stocking.",
                        params=[],
                        available=lambda ctx: True,
                        action=lambda ctx, params: LlmToolResult(
                            agent_actions=[ChangePathAction("completed", next_action="path")],
                            model_feedback="The player has refused to help Agent Stocking."
                        )
                    )
                ],
                preload_messages=[{"role": "assistant", "content": "A cloaked figure approaches you. They look like they're trying to be sneaky, but they're not doing a very good job of it. \"Hello, traveller,\" they whisper."}] # give the model context on what's already happened
            )
        ),
        Path(
            id="stocking_agree_transistion",
            starts_without_player_action=True,
            action_resolver=SequentialActionResolver(
                MessageAgentAction("Agent Stocking nods. \"Thank you, traveller. I will be waiting for you in the forest to the east.\" He presses a small green-and-yellow flag into your hands. \"This was left by the perpetrator. My friend, Agent Duke, may be able to help track them down. He lives above the bakery.\" You open your mouth to speak, but Agent Stocking is gone in a not-nearly-as-stealthy-as-it-could-have-been flash.\nWhat do you do?", name="Agree", icon_url="https://example.com/icon.png"),
                ChangePathAction("duke_convince")
            )
        ),
        Path(
            id="duke_convince",
            starts_without_player_action=False,
            action_resolver=OpenAIActionResolver(
                openai_token=os.environ["OPENAI_API_KEY"],
                openai_base_url=os.environ["OPENAI_API_URL"],
                model="gpt-4o-mini",
                system_prompt=lambda ctx: f'You are a game master for an RPG. The player is in a town square. They are helping Agent Stocking, a spy who\'s lost his lucky socks. The player needs to go to the apartment over the bakery where they must convince a dog, Agent Duke, to help them track a thief. Duke cannot speak, but can understand when people speak to him. The player has a small flag that was left by the thief. {"""However, the player has a bone in their inventory, so Duke is distracted and not interested in the flag. The player cannot get rid of the bones by simply saying "I throw the bones away" or something similar. They must remove them from their actual inventory. Do not tell them this directly, let them figure it out by themselves. After you describe what happens in the scene, prompt the player by asking "What do you do now?" Do not provide any specific suggestions to the player when you do this. Make sure to call the appropriate tool if the player resolves this encounter, either by abandoning it or by convincing Duke to help. """ if player_has_bone(ctx.player) else ""}',
                agent_actions=[
                    LlmTool(
                        name="duke_agrees",
                        description="Call this tool once the player has convinced Agent Duke to help them.",
                        params=[],
                        available=lambda ctx: not player_has_bone(ctx.player),
                        action=lambda ctx, params: LlmToolResult(
                            agent_actions=[ChangePathAction("duke_agrees_transition", next_action="path")],
                            model_feedback="Agent Duke has agreed to help the player."
                        )
                    ),
                    LlmTool(
                        name="player_abandons",
                        description="Call this tool if the player refuses to help Agent Duke and walks out of the apartment with no intent to return. DO NOT CALL THIS IF THE PLAYER MIGHT COME BACK TO THE APARTMENT LATER.",
                        params=[],
                        available=lambda ctx: True,
                        action=lambda ctx, params: LlmToolResult(
                            agent_actions=[ChangePathAction("completed", next_action="path")],
                            model_feedback="The player has abandoned the quest."
                        )
                    )
                ],
                preload_messages=[{"role": "assistant", "content": "Agent Stocking nods. \"Thank you, traveller. I will be waiting for you in the forest to the east.\" He presses a small green-and-yellow flag into your hands. \"This was left by the perpetrator. My friend, Agent Duke, may be able to help track them down. He lives above the bakery.\" You open your mouth to speak, but Agent Stocking is gone in a not-nearly-as-stealthy-as-it-could-have-been flash."}]
            )
        ),
        Path(
            id='duke_agrees_transition',
            starts_without_player_action=True,
            action_resolver=SequentialActionResolver(
                MessageAgentAction("Agent Duke has agreed to help! Here's a placeholder for the rest of the quest."),
                ChangePathAction("completed", next_action="path")
            )
        ),
        Path(
            starts_without_player_action=True,
            id="completed",
            action_resolver=SequentialActionResolver(
                MessageAgentAction(f"You have completed the quest! You can try again by pinging <@{os.environ['BOT_USER_ID']}> in <#{os.environ['HOME_CHANNEL_ID']}>.", name="Completed", icon_url="https://example.com/icon.png"),
                RemovePlayerAction()
            )
        )
    ],
    message_sender=SlackMessager(
        bot_token=os.environ["SLACK_BOT_TOKEN"],
        app_token=os.environ["SLACK_APP_TOKEN"],
        start_path="welcome",
        datastore=datastore,
        active_channel=os.environ["HOME_CHANNEL_ID"],
        reset_user_command="/st-reset-user", # CHANGE THIS to something unique to your quest
        admins=os.environ["ADMINS"].split(',')
        ),
    datastore=datastore
)

asyncio.run(quest.run())