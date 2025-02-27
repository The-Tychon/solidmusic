from dotenv import load_dotenv
from os import path, getenv, mkdir


if path.exists("local.env"):
    load_dotenv("local.env")
else:
    load_dotenv()

if not path.exists("search"):
    mkdir("search")


class Configs:
    API_ID = int(getenv("API_ID", "0"))
    API_HASH = getenv("API_HASH", "abc123")
    BOT_TOKEN = getenv("BOT_TOKEN", "123:abc")
    OWNER_ID = int(getenv("OWNER_ID", "0123"))
    SESSION = getenv("SESSION", "session")
    CHANNEL_LINK = getenv("CHANNEL_LINK", "https://t.me/electro_updates")
    GROUP_LINK = getenv("GROUP_LINK", "https://t.me/electrobot_support")
    UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/the-tychon/solidmusic")
    AUTO_LEAVE = int(getenv("AUTO_LEAVE", "1800"))


config = Configs()
