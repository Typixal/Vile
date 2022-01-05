import discord
import time
from discord.ext import commands
from discord.ext.commands.core import command

class Dangerous_shit(commands.Cog):

    def __init__(self, client):
        self.client = client
    
    @commands.command(name="ping")
    async def nuke(self, ctx):
        """Nuke the server..."""
        
        await ctx.send("https://tenor.com/view/rick-roll-rick-ashley-never-gonna-give-you-up-gif-22113173")

    
    # @commands.command()
    # async def ping(self, ctx):
    #     await ctx.send(f':ping_pong: | Latency is : {round(command.latency * 1000)}ms')

def setup(client):
    client.add_cog(Dangerous_shit(client))