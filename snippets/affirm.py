import discord
from discord.ext import commands
from affirmtoken import Token
from Personal.website.assets.snippits.affirm import affirm
from Personal.website.assets.snippits.affirm import names
import random
import asyncio

bot = commands.Bot(command_prefix = "$", case_insensitive = True, intents = discord.Intents.all())

channels = [1297291502023741580]  # put IDs here
minute_bounds = (1*60, 432000) # 10s to 60s, change this (1m - 1h)
stop = False

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user.name}")
    print("---------------------")
    #await bot.change_presence(status = discord.Status.online, activity = discord.ActivityType.playing("with my wheel!"))
    bot.loop.create_task(random_affirm())

async def random_affirm():
    await asyncio.sleep(1)
    while not stop:
        print("Sending an affirmation...")
        channel = bot.get_channel(random.choice(channels))
        await channel.send(random.choice(names))
        await channel.send(random.choice(affirm))
        await asyncio.sleep(random.randint(minute_bounds[0], minute_bounds[1]))
        
@bot.command()
async def quit(ctx):
    global stop
    stop = True
    await ctx.send("Stopping affirmations.")

bot.run(Token)