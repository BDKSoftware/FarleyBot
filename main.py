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
        random_farley_message.start()

    @bot.command()
    async def ping(ctx):
        await ctx.send(f"Pong! {round(bot.latency * 1000)}ms")

    @bot.event
    async def on_member_join(member):
        logger.info(f"{member} has joined the server.")
        await responses.welcome(member, member.guild.system_channel)

    @bot.event
    async def on_member_remove(member):
        logger.info(f"{member} has left the server.")
        await responses.kick(member, member.guild.system_channel)

    @bot.event
    async def on_member_ban(member):
        logger.info(f"{member} has been banned.")
        await responses.ban(member, member.guild.system_channel)

    @bot.event
    async def on_message(message):
        if message.author == bot.user:
            return

        if 1161770952514863104 in [member.id for member in message.mentions]:
            await responses.send_message(message)
            logger.info(f"Message sent by {message.author}.")

    @tasks.loop(hours=float(random.radnint(6, 10)))
    async def random_farley_message():
        await responses.random_message(bot.get_channel(1161774559557595290))

    @random_farley_message.before_loop
    async def before_random_farley_message():
        await bot.wait_until_ready()

    # This must be at the end or commands will not be registered with the bot
    bot.run(settings.DiscordToken, root_logger=True)


if __name__ == "__main__":
    run()
