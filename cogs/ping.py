import nextcord
import time
from nextcord.ext import commands
from nextcord.ext.commands.core import command


class Ping(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command(name="ping")
    async def ping(self, ctx):
        """Get the bot's current websocket and API latency."""
        #start_time = time.time()
        #await ctx.send(embed=message)
        #end_time = time.time()
        embed = nextcord.Embed(
            title="Pong!",
            colour=(nextcord.Colour.random()), description=f":ping_pong: | Bot Latency = {round(self.client.latency * 1000)}ms"
        )
        await ctx.send(embed=embed)

    # @commands.command()
    # async def ping(self, ctx):
    #     await ctx.send(f':ping_pong: | Latency is : {round(command.latency * 1000)}ms')


def setup(client):
    client.add_cog(Ping(client))
