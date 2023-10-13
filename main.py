import settings
import discord
import responses
import random
from discord.ext import commands, tasks

logger = settings.logging.getLogger("bot")


def run():
    intents = discord.Intents.default()
    intents.message_content = True
    intents.members = True

    bot = commands.Bot(command_prefix="!", intents=intents)

    @bot.event
    async def on_ready():
        logger.info(f"User: {bot.user}, (ID: {bot.user.id})")

    @bot.command()
    async def ping(ctx):
        await ctx.send(f"Pong! {round(bot.latency * 1000)}ms")
        return

    @bot.event
    async def on_member_join(member):
        logger.info(f"{member} has joined the server.")
        await responses.welcome(member, member.guild.system_channel)
        return

    @bot.event
    async def on_member_remove(member):
        logger.info(f"{member} has left the server.")
        await responses.kick(member, member.guild.system_channel)
        return

    @bot.event
    async def on_member_ban(member):
        logger.info(f"{member} has been banned.")
        await responses.ban(member, member.guild.system_channel)

    @bot.event
    async def on_message(message):
        if message.author == bot.user:
            return

        if 480978208884391938 in [member.id for member in message.mentions]:
            # Add heart emoji to message
            await message.add_reaction("❤️")

        if 1161770952514863104 in [member.id for member in message.mentions]:
            await responses.send_message(message)
            logger.info(f"Message sent by {message.author}.")
            return

        else:
            if (random.randint(0, 20) == 20):
                await responses.random_message(message.channel)
                await message.add_reaction("🐶")
                return

    # This must be at the end or commands will not be registered with the bot
    bot.run(settings.DiscordToken, root_logger=True)


if __name__ == "__main__":
    run()
