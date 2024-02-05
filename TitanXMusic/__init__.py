from TitanXMusic.core.bot import Titan
from TitanXMusic.core.dir import dirr
from TitanXMusic.core.git import git
from TitanXMusic.core.userbot import Userbot
from TitanXMusic.misc import dbb, heroku

from .logging import LOGGER

dirr()
git()
dbb()
heroku()

app = Titan()
userbot = Userbot()


from .platforms import *

Apple = AppleAPI()
Carbon = CarbonAPI()
SoundCloud = SoundAPI()
Spotify = SpotifyAPI()
Resso = RessoAPI()
Telegram = TeleAPI()
YouTube = YouTubeAPI()
