import asyncio
import logging
import sys
import socket
import discord
from discord.ext import commands

import config

# Ensure SINGLE INSTANCE execution using local socket lock
lock_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
try:
    lock_socket.bind(('127.0.0.1', 47382))
except socket.error:
    print("⚠️ Another instance of Arab Albion Bot is already running! Terminating duplicate process.")
    sys.exit(0)

# Configure Logging and Console Encoding
if sys.platform == "win32":
    sys.stdout.reconfigure(encoding="utf-8")

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
    handlers=[logging.StreamHandler(sys.stdout)]
)
logger = logging.getLogger("ArabAlbionBot")

# Define Bot Intents
intents = discord.Intents.default()
intents.message_content = True
intents.members = True

class ArabAlbionBot(commands.Bot):
    def __init__(self):
        super().__init__(
            command_prefix="!",
            intents=intents,
            help_command=None
        )

    async def setup_hook(self):
        """Load Cogs instantly."""
        try:
            await self.load_extension("cogs.events")
            logger.info("Successfully loaded extension: cogs.events")
        except Exception as e:
            logger.error(f"Failed to load extension cogs.events: {e}")

    async def on_ready(self):
        logger.info(f"--- Arab Albion Bot is Online ---")
        logger.info(f"Logged in as: {self.user.name} (ID: {self.user.id})")
        logger.info(f"Connected Guilds: {len(self.guilds)}")

        # Set Activity Status
        activity = discord.Activity(
            type=discord.ActivityType.playing,
            name="Albion Online | /event"
        )
        await self.change_presence(status=discord.Status.online, activity=activity)

        # Sync commands in background
        try:
            if config.GUILD_ID:
                guild = discord.Object(id=config.GUILD_ID)
                self.tree.copy_global_to(guild=guild)
                synced = await self.tree.sync(guild=guild)
                logger.info(f"Synced {len(synced)} slash commands to Guild ID {config.GUILD_ID}")
        except Exception as e:
            logger.error(f"Error syncing application commands: {e}")


async def main():
    if not config.TOKEN:
        logger.error("ERROR: DISCORD_TOKEN is missing! Please set it in your .env file.")
        print("\n========================================================")
        print("⚠️  Please add DISCORD_TOKEN in .env file to run the bot!")
        print("========================================================\n")
        return

    bot = ArabAlbionBot()
    async with bot:
        await bot.start(config.TOKEN)


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        logger.info("Bot execution terminated by user.")
