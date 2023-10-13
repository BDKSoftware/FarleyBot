import discord
import random


async def send_message(message: discord.Message):

    print(message.content)

    if message.content.endswith(">"):
        await message.channel.send("BARK BARK BARK")
        await message.add_reaction("🐶")
        return

    data = message.content.split(" ", 1)[1:][0].lower()
    match(data):
        case "speak":
            await message.channel.send("BARK BARK BARK")
            await message.add_reaction("🐶")
        case "is walton fat?":
            await message.channel.send("`* nods head vigorously *`")
            await message.add_reaction("🐶")
        case "is matt communist?":
            await message.channel.send("`* nods head vigorously *`")
            await message.add_reaction("🐶")
        case "is brad the coolest?":
            await message.channel.send("`* nods head vigorously *`")
            await message.add_reaction("🐶")
        case "whos a good boy?":
            await message.channel.send("`* wags tail *`")
            await message.add_reaction("🐶")
        case _:
            await message.channel.send("BARK BARK BARK")
            await message.add_reaction("🐶")

    return


async def welcome(member, channel):
    await channel.send(f"BARK BARK BARK {member} has joined the server.")
    return


async def ban(member, channel):
    await channel.send(f"`* bites off users dick *` {member} has been banned .")
    return


async def kick(member, channel):
    await channel.send(f"`* Grrrrrrr *` {member} has been kicked from the server.")
    return


async def random_message(channel: int):
    randomMsgs = ["BARK", "WOOF", "GRRRRRRR"]

    # pick a number between 1 and 3 randomly
    randomInt = random.randint(0, 2)

    msg = randomMsgs[randomInt]
    await channel.send(msg)
