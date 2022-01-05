import discord
import time
from discord.ext import commands
from discord.ext.commands.core import command

class Dangerous_shit(commands.Cog):

    def __init__(self, client):
        self.client = client
    
    @commands.command(name="Nuke")
    async def nuke(self, ctx):
        """Nuke the server..."""
        
        await ctx.send("https://tenor.com/view/rick-roll-rick-ashley-never-gonna-give-you-up-gif-22113173")

    
def setup(client):
    client.add_cog(Dangerous_shit(client))

