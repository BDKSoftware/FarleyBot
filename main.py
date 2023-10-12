import settings
import discord
from discord.ext import commands

logger = settings.logging.getLogger("bot")


def run():
    intents = discord.Intents.default()
    intents.message_content = True

    bot = commands.Bot(command_prefix="!", intents=intents)

    @bot.event
    async def on_ready():
        logger.info(f"User: {bot.user}, (ID: {bot.user.id})")

    @bot.command()
    async def ping(ctx):
        await ctx.send(f"Pong! {round(bot.latency * 1000)}ms")

    # This must be at the end or commands will not be registered with the bot
    bot.run(settings.DiscordToken, root_logger=True)


if __name__ == "__main__":
    run()
