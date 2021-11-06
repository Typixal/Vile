import discord
from discord.ext import commands

class Moderation(commands.Cog):

    def __init__(self, client):
        self.client = client    
    
    
    @commands.command()
    @commands.has_permissions(administrator=True)
    async def clear(self, ctx, limit: int):
            await ctx.channel.purge(limit=limit+1)
            #await ctx.send('Cleared by {}'.format(ctx.author.mention))
            await ctx.message.delete()

    @clear.error
    async def clear_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            await ctx.send("You cant do that!")
    
    @clear.error
    async def clear_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send('Please specify the amount of messages to clear!') 

            
def setup(client):
    client.add_cog(Moderation(client))