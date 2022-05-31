import nextcord
import time
from nextcord.ext import commands
from nextcord.ext.commands.core import command


class Nuke(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command(name="nuke")
    @commands.is_owner()
    async def nuke(self, ctx):
        """Nuke the server..."""

        await ctx.send("https://tenor.com/view/destory-eexplode-nuke-gif-6073338")

    @nuke.error
    async def nuke_error(self, ctx, error):
        if isinstance(error, commands.NotOwner):
            embed = nextcord.Embed(
                colour=(nextcord.Colour.random()), description='***No access! Developer only command!***'
            )
            await ctx.send(embed=embed)


def setup(client):
    client.add_cog(Nuke(client))
