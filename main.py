import discord
import os
import time
import random
from discord import activity
from discord.ext import commands, tasks
from itertools import cycle
from dotenv import load_dotenv
# Intents
intents = discord.Intents().all()
client = commands.Bot(command_prefix='>', intents=intents)
status = cycle(['Vile | ..help', 'TypicalWolf'])
load_dotenv()

@client.event
async def on_ready():
    change_status.start()
    # await client.change_presence(status=discord.Status.idle, activity=discord.Game(name="Vile | ..help"))


@client.command()
async def load(ct, extension):
    client.load_extension(f'cogs.{extension}')


@client.command()
async def unload(ct, extension):
    client.unload_extension(f'cogs.{extension}')

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')


@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        await ctx.send('That command is non-existent. Try ..help for a list of available commands!')


@tasks.loop(seconds=15)
async def change_status():
    await client.change_presence(activity=discord.Game(next(status)))


client.run(os.getenv("DISCORD_TOKEN"))

