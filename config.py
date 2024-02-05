import re
import random
from os import getenv

from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

# Get this value from my.telegram.org/apps
API_ID = int(getenv("API_ID"))
API_HASH = getenv("API_HASH")

# Get your token from @BotFather on Telegram.
BOT_TOKEN = getenv("BOT_TOKEN")

# Get your mongo url from cloud.mongodb.com
MONGO_DB_URI = getenv("MONGO_DB_URI", None)

DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", 60000000))

# Chat id of a group for logging bot's activities
LOG_GROUP_ID = int(getenv("LOG_GROUP_ID", None))

# Get this value from @MissRose_Bot on Telegram by /id
OWNER_ID = int(getenv("OWNER_ID", None))

# Fill Queue Limit . Example - 15
QUEUE_LIMIT = int(getenv("QUEUE_LIMIT", "60"))

## Fill these variables if you're deploying on heroku.
# Your heroku app name
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
# Get it from http://dashboard.heroku.com/account
HEROKU_API_KEY = getenv("HEROKU_API_KEY")

UPSTREAM_REPO = getenv(
    "UPSTREAM_REPO",
    "https://github.com/PIRATE303/TitanXMusic",
)
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "master")
GIT_TOKEN = getenv(
    "GIT_TOKEN", None
)  # Fill this variable if your upstream repository is private

UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "main")
GIT_TOKEN = getenv(
    "GIT_TOKEN", None
)  # Fill this variable if your upstream repository is private

SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/TitanNetwrk")
SUPPORT_GROUP = getenv("SUPPORT_GROUP", "https://t.me/TitanXSupport")

# Set this to True if you want the assistant to automatically leave chats after an interval
AUTO_LEAVING_ASSISTANT = bool(getenv("AUTO_LEAVING_ASSISTANT", False))


# Get this credentials from https://developer.spotify.com/dashboard
SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID", None)
SPOTIFY_CLIENT_SECRET = getenv("SPOTIFY_CLIENT_SECRET", None)


# Maximum limit for fetching playlist's track from youtube, spotify, apple links.
PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", 25))


# Telegram audio and video file size limit (in bytes)
TG_AUDIO_FILESIZE_LIMIT = int(getenv("TG_AUDIO_FILESIZE_LIMIT", 104857600))
TG_VIDEO_FILESIZE_LIMIT = int(getenv("TG_VIDEO_FILESIZE_LIMIT", 1073741824))
# Checkout https://www.gbmb.org/mb-to-bytes for converting mb to bytes


# Get your pyrogram v2 session from Replit
STRING1 = getenv("STRING_SESSION", None)
STRING2 = getenv("STRING_SESSION2", None)
STRING3 = getenv("STRING_SESSION3", None)
STRING4 = getenv("STRING_SESSION4", None)
STRING5 = getenv("STRING_SESSION5", None)


BANNED_USERS = filters.user()
adminlist = {}
lyrical = {}
votemode = {}
autoclean = []
confirmer = {}


START_IMG_URL = ["https://telegra.ph/file/c626ca60bc13f87550b0d.jpg",
"https://telegra.ph/file/d51131e02f6503a257e12.jpg",
"https://telegra.ph/file/e61ca48f9b71223352881.jpg",
"https://telegra.ph/file/4a0139f17532ae2c363a8.jpg",
"https://telegra.ph/file/b6d76633998f6a1e00e84.jpg",
"https://telegra.ph/file/dbfe62fb4e7209024a709.jpg",
"https://telegra.ph/file/bed13eaf3f2a7377c2a60.jpg",
"https://telegra.ph/file/b48daa91391a286df2c15.jpg",
"https://telegra.ph/file/f8d96f6a5493ea0572283.jpg",
"https://telegra.ph/file/b116456b672fbbf31a16d.jpg",
"https://telegra.ph/file/5df15f2a0cce45bb417c3.jpg",
"https://telegra.ph/file/988f921e28b0b5f9f6f08.jpg",
"https://telegra.ph/file/045e0b69ff903a455600f.jpg",
"https://telegra.ph/file/831f3a20f5ca7acc16f24.jpg",
"https://telegra.ph/file/fb39820a80c2d7538216a.jpg",
"https://telegra.ph/file/6b7aa0d191efde2298ced.jpg",
"https://telegra.ph/file/311066c271a4ed19031d2.jpg",
"https://telegra.ph/file/5a687d5d18f5fcf7ae4d1.jpg",
"https://telegra.ph/file/f539b8871a80ad98aa429.jpg",
"https://telegra.ph/file/9dabb5bf55fb9a9e50845.jpg",
"https://telegra.ph/file/12e2118f0df74df0ec464.jpg",
"https://telegra.ph/file/366aa08c49179b4e8c753.jpg",
"https://telegra.ph/file/228081480bd2e7788d6dd.jpg",
"https://telegra.ph/file/baf2e2fc6c5d540ded908.jpg",
"https://telegra.ph/file/ac887c35420f7e877dae6.jpg",
"https://telegra.ph/file/d2380fdcbe051fd75d1ce.jpg",
"https://telegra.ph/file/0fefa1f6cc18dad00baa8.jpg",]
PING_IMG_URL = ["https://telegra.ph/file/c626ca60bc13f87550b0d.jpg",
"https://telegra.ph/file/d51131e02f6503a257e12.jpg",
"https://telegra.ph/file/e61ca48f9b71223352881.jpg",
"https://telegra.ph/file/4a0139f17532ae2c363a8.jpg",
"https://telegra.ph/file/b6d76633998f6a1e00e84.jpg",
"https://telegra.ph/file/dbfe62fb4e7209024a709.jpg",
"https://telegra.ph/file/bed13eaf3f2a7377c2a60.jpg",
"https://telegra.ph/file/b48daa91391a286df2c15.jpg",
"https://telegra.ph/file/f8d96f6a5493ea0572283.jpg",
"https://telegra.ph/file/b116456b672fbbf31a16d.jpg",
"https://telegra.ph/file/5df15f2a0cce45bb417c3.jpg",
"https://telegra.ph/file/988f921e28b0b5f9f6f08.jpg",
"https://telegra.ph/file/045e0b69ff903a455600f.jpg",
"https://telegra.ph/file/831f3a20f5ca7acc16f24.jpg",
"https://telegra.ph/file/fb39820a80c2d7538216a.jpg",
"https://telegra.ph/file/6b7aa0d191efde2298ced.jpg",
"https://telegra.ph/file/311066c271a4ed19031d2.jpg",
"https://telegra.ph/file/5a687d5d18f5fcf7ae4d1.jpg",
"https://telegra.ph/file/f539b8871a80ad98aa429.jpg",
"https://telegra.ph/file/9dabb5bf55fb9a9e50845.jpg",
"https://telegra.ph/file/12e2118f0df74df0ec464.jpg",
"https://telegra.ph/file/366aa08c49179b4e8c753.jpg",
"https://telegra.ph/file/228081480bd2e7788d6dd.jpg",
"https://telegra.ph/file/baf2e2fc6c5d540ded908.jpg",
"https://telegra.ph/file/ac887c35420f7e877dae6.jpg",
"https://telegra.ph/file/d2380fdcbe051fd75d1ce.jpg",
"https://telegra.ph/file/0fefa1f6cc18dad00baa8.jpg",]
STATS_IMG_URL = ["https://telegra.ph/file/c626ca60bc13f87550b0d.jpg",
"https://telegra.ph/file/d51131e02f6503a257e12.jpg",
"https://telegra.ph/file/e61ca48f9b71223352881.jpg",
"https://telegra.ph/file/4a0139f17532ae2c363a8.jpg",
"https://telegra.ph/file/b6d76633998f6a1e00e84.jpg",
"https://telegra.ph/file/dbfe62fb4e7209024a709.jpg",
"https://telegra.ph/file/bed13eaf3f2a7377c2a60.jpg",
"https://telegra.ph/file/b48daa91391a286df2c15.jpg",
"https://telegra.ph/file/f8d96f6a5493ea0572283.jpg",
"https://telegra.ph/file/b116456b672fbbf31a16d.jpg",
"https://telegra.ph/file/5df15f2a0cce45bb417c3.jpg",
"https://telegra.ph/file/988f921e28b0b5f9f6f08.jpg",
"https://telegra.ph/file/045e0b69ff903a455600f.jpg",
"https://telegra.ph/file/831f3a20f5ca7acc16f24.jpg",
"https://telegra.ph/file/fb39820a80c2d7538216a.jpg",
"https://telegra.ph/file/6b7aa0d191efde2298ced.jpg",
"https://telegra.ph/file/311066c271a4ed19031d2.jpg",
"https://telegra.ph/file/5a687d5d18f5fcf7ae4d1.jpg",
"https://telegra.ph/file/f539b8871a80ad98aa429.jpg",
"https://telegra.ph/file/9dabb5bf55fb9a9e50845.jpg",
"https://telegra.ph/file/12e2118f0df74df0ec464.jpg",
"https://telegra.ph/file/366aa08c49179b4e8c753.jpg",
"https://telegra.ph/file/228081480bd2e7788d6dd.jpg",
"https://telegra.ph/file/baf2e2fc6c5d540ded908.jpg",
"https://telegra.ph/file/ac887c35420f7e877dae6.jpg",
"https://telegra.ph/file/d2380fdcbe051fd75d1ce.jpg",
"https://telegra.ph/file/0fefa1f6cc18dad00baa8.jpg",]
PLAYLIST_IMG_URL = getenv(
    "PLAYLIST_IMG_URL", "https://telegra.ph/file/045e0b69ff903a455600f.jpg"
)
TELEGRAM_AUDIO_URL = getenv(
    "TELEGRAM_AUDIO_URL", "https://telegra.ph/file/831f3a20f5ca7acc16f24.jpg"
)
TELEGRAM_VIDEO_URL = getenv(
    "TELEGRAM_VIDEO_URL", "https://telegra.ph/file/6b7aa0d191efde2298ced.jpg"
)
STREAM_IMG_URL = getenv(
    "STREAM_IMG_URL", "https://te.legra.ph/file/693694b0d94afa372ca5a.jpg"
)
SOUNCLOUD_IMG_URL = getenv(
    "SOUNCLOUD_IMG_URL", "https://te.legra.ph/file/f72ea4bd955c418c724e1.jpg"
)
YOUTUBE_IMG_URL = getenv(
    "YOUTUBE_IMG_URL", "https://telegra.ph/file/5547c6a0bcfc016089088.png"
)
SPOTIFY_ARTIST_IMG_URL = getenv(
    "SPOTIFY_ARTIST_IMG_URL", "https://te.legra.ph/file/c3682dc6fd740b2dac969.jpg"
)
SPOTIFY_ALBUM_IMG_URL = getenv(
    "SPOTIFY_ALBUM_IMG_URL", "https://te.legra.ph/file/c3682dc6fd740b2dac969.jpg"
)
SPOTIFY_PLAYLIST_IMG_URL = getenv(
    "SPOTIFY_PLAYLIST_IMG_URL", "https://te.legra.ph/file/c3682dc6fd740b2dac969.jpg"
)


def time_to_seconds(time):
    stringt = str(time)
    return sum(int(x) * 60**i for i, x in enumerate(reversed(stringt.split(":"))))


DURATION_LIMIT = int(time_to_seconds(f"{DURATION_LIMIT_MIN}:00"))


if SUPPORT_CHANNEL:
    if not re.match("(?:http|https)://", SUPPORT_CHANNEL):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHANNEL url is wrong. Please ensure that it starts with https://"
        )

if SUPPORT_GROUP:
    if not re.match("(?:http|https)://", SUPPORT_GROUP):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_GROUP url is wrong. Please ensure that it starts with https://"
        )
