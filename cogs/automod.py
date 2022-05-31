from msilib.schema import Class
import nextcord
import asyncio
from nextcord.ext import commands

filtered_words = ["Nigga", "Nigger", "N1gga", "nigga", "nigger", "n1gger", "fak"]


class Automod(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_message(self, msg):
        for word in filtered_words:
            if word in msg.content:
                await msg.delete()
                embed = nextcord.Embed(
                    colour=(nextcord.Colour.random()), description=f"{msg.author.mention} Ayo chill <-<")
                await msg.channel.send(embed = embed, delete_after=4)


def setup(client):
    client.add_cog(Automod(client))
