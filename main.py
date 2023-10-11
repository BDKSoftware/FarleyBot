import settings
import discord
from discord.ext import commands

logger = settings.logging.getLogger("bot")


def run():
    intents = discord.Intents.default()
    intents.members = True
    intents.message_content = True
    bot = commands.Bot(command_prefix="!", intents=intents)

    @bot.event
    async def on_ready():
        print("Bot is up and running!")
        logger.info(f"User: {bot.user}, (ID: {bot.user.id})")

    bot.run(settings.DiscordToken, root_logger=True)


if __name__ == "__main__":
    run()
