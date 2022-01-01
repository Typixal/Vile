import asyncio
import functools
import itertools
import math
import random

import discord
from discord import client
import youtube_dl
from async_timeout import timeout
from discord.ext import commands

# from cogs.music import Music


class Music(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command(pass_context=True)
    async def musichelp(self, ctx):
        channel = ctx.message.channel
        embed = discord.Embed(
            title='Music',
            discription='These are the bot music commands.',
            colour=discord.colour.blue()
        )

        embed.set_footer(text='Hope you have a nice day!.')
        embed.set_image(
            url='https://cdn.discordapp.com/avatars/270904126974590976/d60c6bd5971f06776ba96497117f7f58.webp?size=4096')
        embed.set_thumbnail(
            url='https://cdn.discordapp.com/avatars/270904126974590976/d60c6bd5971f06776ba96497117f7f58.webp?size=4096')
        embed.set_author(name='Typicalwolf',
                         icon_url='https://cdn.discordapp.com/avatars/270904126974590976/d60c6bd5971f06776ba96497117f7f58.webp?size=4096')
        embed.add_field(
            name='join', value='Joins a voice channel.', inline=True)
        embed.add_field(
            name='leave', value='Clears the queue and leaves the voice channel.', inline=True)
        embed.add_field(
            name='loop', value='Loops the currently playing song.', inline=True)
        embed.add_field(
            name='now', value='Displays the currently playing song.', inline=True)
        embed.add_field(
            name='pause', value='Pauses the currently playing song.', inline=True)
        embed.add_field(name='play', value='Plays a song.', inline=True)

        embed.add_field(
            name='queue', value='Shows the player queue.', inline=True)

        embed.add_field(
            name='remove', value='Removes a song from the queue at a given index.', inline=True)
        embed.add_field(
            name='resume', value='Resumes a currently paused song.', inline=True)
        embed.add_field(
            name='shuffle', value='Shuffles the queue.', inline=True)
        embed.add_field(
            name='skip', value='Vote to skip a song. The requester can automatically skip.', inline=True)
        embed.add_field(
            name='stop', value='Stops playing song and clears the queue.', inline=True)
        embed.add_field(
            name='summon', value='Summons the bot to a voice channel. (Admin command)', inline=True)


# @commands.command(pass_context=True)
        embed.add_field(
            name='volume', value='Sets the volume of the player.', inline=True)

        await ctx.send(channel, embed=embed)


def setup(client):
    client.add_cog(Music(client))
