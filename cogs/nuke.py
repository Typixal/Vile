import discord
import time
from discord.ext import commands
from discord.ext.commands.core import command

class Dangerous_shit(commands.Cog):

    def __init__(self, client):
        self.client = client
    
    
    @commands.command(name="nuke")
    async def nuke(self, ctx):
        """Nuke the server..."""
        
        await ctx.send("https://tenor.com/view/who-the-hell-do-you-think-youre-talking-to-dog-talking-who-do-you-think-you-are-gif-13502177")

    
def setup(client):
    client.add_cog(Dangerous_shit(client))

