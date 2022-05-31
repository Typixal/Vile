import nextcord
import asyncio
from nextcord.ext import commands


class Snipe(commands.Cog):

    def __init__(self, client):
        self.client = client
    snipe_message_content = None
    snipe_message_author = None

    @commands.Cog.listener()
    async def on_message_delete(self, message):
        global snipe_message_content
        global snipe_message_author

        snipe_message_content = message.content
        snipe_message_author = message.author.name
        await asyncio.sleep(60)
        snipe_message_author = None
        snipe_message_content = None

    @commands.command()
    @commands.has_role('Sniper')
    async def snipe(self, message):
        if snipe_message_content == None:
            await message.channel.send("There's nothing to snipe....")

        else:
            embed = nextcord.Embed(
                colour=(nextcord.Colour.random()), description=f"{snipe_message_content}")
            embed.set_footer(
                text=f"Requested by {message.author.name}#{message.author.discriminator}")
            embed.set_author(
                name=f"Sniped the message deleted by {snipe_message_author}")
            await message.channel.send(embed=embed)
            return


def setup(client):
    client.add_cog(Snipe(client))
