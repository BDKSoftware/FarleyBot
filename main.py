import settings
import discord
from discord.ext import commands


def run():
    intents = discord.Intents.default()
    intents.members = True
    intents.message_content = True
    bot = commands.Bot(command_prefix="!", intents=intents)

    @bot.event
    async def on_ready():
        print("Bot is up and running!")

    bot.run(settings.DiscordToken)


if __name__ == "__main__":
    run()
