import os
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv("DISCORD_TOKEN", "")
CLIENT_ID = os.getenv("CLIENT_ID", "")
GUILD_ID = int(os.getenv("GUILD_ID")) if os.getenv("GUILD_ID") else None

DEFAULT_GUILD_NAME = os.getenv("DEFAULT_GUILD_NAME", "Arab Albion")
DEFAULT_REGION = os.getenv("DEFAULT_REGION", "europe").lower()

# Color Theme - Sky Blue / Cyan Accent
COLOR_PRIMARY = 0x00E5FF    # Sky Blue / Electric Cyan
COLOR_SUCCESS = 0x2ECC71    # Emerald Green
COLOR_DANGER = 0xE74C3C     # Crimson Red
COLOR_INFO = 0x3498DB       # Royal Blue
COLOR_ALBION = 0xD4AF37     # Golden Accent
