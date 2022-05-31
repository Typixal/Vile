from ast import alias
from http import client
import nextcord
import random
from nextcord.ext import commands
import asyncio


class Fun(commands.Cog):

    def __init__(self, client):
        self.client = client

    snipe_message_content = None
    snipe_message_author = None

    @commands.command(aliases=['8ball'])
    async def _8ball(self, ctx, *, question):
        responses = ["It is certain.",
                     "It is decidedly so.",
                     "Without a doubt.",
                     "Yes - definitely.",
                     "You may rely on it.",
                     "As I see it, yes.",
                     "Most likely.",
                     "Outlook good.",
                     "Yes.",
                     "Signs point to yes.",
                     "Reply hazy, try again.",
                     "Ask again later.",
                     "Better not tell you now.",
                     "Cannot predict now.",
                     "Concentrate and ask again.",
                     "Don't count on it.",
                     "My reply is no.",
                     "My sources say no.",
                     "Outlook not so good.",
                     "Very doubtful."]

        embed = nextcord.Embed(
            colour=(nextcord.Colour.random()), description=f"Question: {question}\nAnswer : {random.choice(responses)}")
        embed.set_footer(
            text=f"Requested by {ctx.author.name}#{ctx.author.discriminator}")
        embed.set_author(
            name=f"Asked by {ctx.author.name}")
        await ctx.channel.send(embed=embed)


def setup(client):

    client.add_cog(Fun(client))
