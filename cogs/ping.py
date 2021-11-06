import discord
import time
from discord.ext import commands
from discord.ext.commands.core import command

class Ping(commands.Cog):

    def __init__(self, client):
        self.client = client
    
    @commands.command(name="ping")
    async def ping(self, ctx):
        """Get the bot's current websocket and API latency."""
        start_time = time.time()
        message = await ctx.send("Testing Ping...")
        end_time = time.time()

        await message.edit(content=f":ping_pong: | Pong! {round(self.client.latency * 1000)}ms\n:ping_pong: | API: {round((end_time - start_time) * 1000)}ms")

    
    # @commands.command()
    # async def ping(self, ctx):
    #     await ctx.send(f':ping_pong: | Latency is : {round(command.latency * 1000)}ms')

def setup(client):
    client.add_cog(Ping(client))