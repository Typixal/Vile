from setuptools import extension
import nextcord
import os
import time
import random
from nextcord import activity
from nextcord.ext import commands, tasks
from itertools import cycle
from nextcord import Embed
# from dotenv import load_dotenv
import asyncio
import aiohttp


os.environ["JISHAKU_NO_DM_TRACEBACK"] = "true"


# from matplotlib.style import context
# Intents
intents = nextcord.Intents().all()
client = commands.Bot(command_prefix='--', intents=intents, help_command=None)
status = cycle(['Tile | --help', 'Night Vibe',
               'TypicalWolf', 'Cuties', 'Himiko Toga'])
# load_dotenv()


@client.event
async def on_ready():
    change_status.start()
    await client.change_presence(status=nextcord.Status.idle, activity=nextcord.Game(name="Vile | ..help"))
    print('Tester is online!')


@client.command()
@commands.is_owner()
async def load(stx, extension):
    await client.load_extension(f'cogs.{extension}')


@client.command()
@commands.is_owner()
async def unload(ctx, extension):
    await client.unload_extension(f'cogs.{extension}')


@load.error
async def load_error(ctx, error):
    if isinstance(error, commands.NotOwner):
        embed = nextcord.Embed(
            colour=(nextcord.Colour.random()), description='***No access! Developer only command!***'
        )
        await ctx.send(embed=embed)


@unload.error
async def unload_error(ctx, error):
    if isinstance(error, commands.NotOwner):
        embed = nextcord.Embed(
            colour=(nextcord.Colour.random()), description='***No access! Developer only command!***'
        )
        await ctx.send(embed=embed)

# async def load_extensions():
#     for filename in os.listdir('./cogs'):
#         if filename.endswith('.py'):
#             await client.load_extension(f'cogs.{filename[:-3]}')


for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')


@client.event
async def on_command_error(ctx, error):
    pass
#     if isinstance(error, commands.CommandNotFound):
#         await ctx.send('That command is non-existent. Try ..help for a list of available commands!')


@tasks.loop(seconds=15)
async def change_status():
    await client.change_presence(activity=nextcord.Activity(type=nextcord.ActivityType.watching, name=(next(status))))
    return


# async def main():
#     async with client:
#         # change_status.start()
#         await load_extensions()
#         print('Vile is online.')
#         await client.start('OTcxMDU3ODYxOTc3MzI1NTg5.GcSxwJ.I0C1g-n_qYsZx_rLHIIfvOw4qTA9XzFIXn8WMg')

# asyncio.run(main())
client.run(os.getenv("DISCORD_TOKEN"))
