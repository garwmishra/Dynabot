from Dynabot.core.bot import JARVIS
from Dynabot.core.dir import dirr
from Dynabot.core.git import git
from Dynabot.core.userbot import Userbot
from Dynabot.misc import dbb, heroku

from SafoneAPI import SafoneAPI
from .logging import LOGGER

dirr()
git()
dbb()
heroku()

app = JARVIS()
api = SafoneAPI()
userbot = Userbot()


from .platforms import *

Apple = AppleAPI()
Carbon = CarbonAPI()
SoundCloud = SoundAPI()
Spotify = SpotifyAPI()
Resso = RessoAPI()
Telegram = TeleAPI()
YouTube = YouTubeAPI()
