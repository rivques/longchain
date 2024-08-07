
import asyncio
from longchain.core.dataclasses import Message
from longchain.core.path import Path
from longchain.core.quest import Quest
from longchain.impl.actionresolver.sequential import SequentialActionResolver
from longchain.impl.agentaction.end import ChangePathAction
from longchain.impl.agentaction.message import MessageAgentAction
from longchain.impl.datastore.jsonfile import JsonFileDatastore
from longchain.impl.messager.slack import SlackMessager
import os

if "ENVIRONMENT" not in os.environ or os.environ["ENVIRONMENT"] != "production":
    import dotenv
    dotenv.load_dotenv(override=True)

ENV_VARS_REQUIRED = ["ENVIRONMENT", "SLACK_BOT_TOKEN", "SLACK_APP_TOKEN", "HOME_CHANNEL_ID", "DATA_FILEPATH", "BOT_USER_ID", "OPENAI_API_KEY", "OPENAI_API_URL", "ST_ADMINS"]
if not all([var in os.environ for var in ENV_VARS_REQUIRED]):
    raise Exception(f"Missing the following environment variables: {', '.join([var for var in ENV_VARS_REQUIRED if not var in os.environ])}")

datastore = JsonFileDatastore(os.environ["DATA_FILEPATH"])

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
            action_resolver=SequentialActionResolver(
                MessageAgentAction("The figure is trying to steal a sock!", name="Initial", icon_url="https://example.com/icon.png"),
                ChangePathAction("completed", next_action='agent')
            )
        ),
        Path(
            starts_without_player_action=True,
            id="completed",
            action_resolver=SequentialActionResolver(
                MessageAgentAction("You have completed the quest!", name="Completed", icon_url="https://example.com/icon.png"),
            )
        )
    ],
    message_sender=SlackMessager(
        bot_token=os.environ["SLACK_BOT_TOKEN"],
        app_token=os.environ["SLACK_APP_TOKEN"],
        start_path="welcome",
        datastore=datastore,
        active_channel=os.environ["HOME_CHANNEL_ID"],
        reset_user_command="/st-reset-user",
        admins=os.environ["ST_ADMINS"].split(',')
        ),
    datastore=datastore
)

asyncio.run(quest.run())