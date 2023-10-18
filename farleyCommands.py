import random


async def sit(ctx):
    await ctx.send("`* sits *`")
    return


async def fetch(ctx):
    await ctx.send("`* looks confused *`")
    return


async def rollover(ctx):
    await ctx.send(f"`* rolls over {random.randint(1, 69)} times *`")
    return


async def speak(ctx):
    await ctx.send("BARK BARK BARK")
    return


async def walton(ctx):
    await ctx.send("`* BARK BARK is fat BARK BARK *`")
    return


async def brad(ctx):
    await ctx.send("Really nice guy, love that guy")
    return
