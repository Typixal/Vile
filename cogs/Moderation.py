import nextcord
import random
from nextcord.ext import commands


class Moderation(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def ban(self, ctx, member: nextcord.Member, *, reason=None):
        await member.ban(reason=reason)
        embed = nextcord.Embed(
            title=("Banned!"),
            colour=(nextcord.Colour.random()), description=f"User {member} has been banned!"
        )
        await ctx.send(embed=embed)

    @ban.error
    async def ban_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            embed = nextcord.Embed(
                title=("Permission denied!"),
                colour=(nextcord.Colour.random()), description=f"You dont have permissions to do that!"
            )
            await ctx.send(embed=embed)

    @ban.error
    async def ban_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            embed = nextcord.Embed(
                title=("Missing Argument"),
                colour=(nextcord.Colour.random()), description=f"The command is used like : @user [Reason | optional]"
            )
            await ctx.send(embed=embed)

    # @commands.command()
    # @commands.has_permissions(administrator=True)
    # async def unban(self, ctx, *, member):
    #     banned_users = await ctx.guild.bans()
    #     member_name, member_discriminator = member.split("#")

    #     for ban_entry in banned_users:
    #         user = ban_entry.user
    #         if (user.name, user.discriminator) == (member_name, member_discriminator):
    #             await ctx.guild.unban(user)
    #             embed = nextcord.Embed(
    #                 title=("Unabanned"),
    #                 colour=(nextcord.Colour.random()), description=f"{user.mention} has been unbanned!"
    #             )
    #             await ctx.send(embed=embed)
    #             return

    # @unban.error
    # async def unban_error(self, ctx, error):
    #     if isinstance(error, commands.MissingRequiredArgument):
    #         embed = nextcord.Embed(
    #             title=("Missing Argument"),
    #             colour=(nextcord.Colour.random()), description=f"Provide the username with the discriminator! Ex: Vile#1234"
    #         )
    #         await ctx.send(embed=embed)
    #         # await ctx.send("Provide the username with the discriminator! Ex: Vile#1234")

    # @unban.error
    # async def unban_error(self, ctx, error):
    #     if isinstance(error, commands.MissingPermissions):
    #         embed = nextcord.Embed(
    #                 title=("Perission denied"),
    #                 colour=(nextcord.Colour.random()), description=f"You don't have permissions to do that."
    #             )
    #         await ctx.send(embed=embed)
    #         #await ctx.send("Not enough permissions to do that!")

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def kick(self, ctx, member: nextcord.Member, *, reason=None):
        await member.kick(reason=reason)
        embed = nextcord.Embed(
            title=("Kicked Member"),
            colour=(nextcord.Colour.random()), description=f"User {member} has been kicked!"
        )
        await ctx.send(embed=embed)
        #await ctx.send(f'User {member} has been kicked!')

    @kick.error
    async def kick_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            embed = nextcord.Embed(
                title=("Permission denied"),
                colour=(nextcord.Colour.random()), description=f"You dont have permissions to do that!")
            await ctx.send(embed=embed)

    @kick.error
    async def kick_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            embed = nextcord.Embed(
                title=("Missing required argument"),
                colour=(nextcord.Colour.random()), description=f"Mention the user to kick.")
            await ctx.send(embed=embed)
            
    @kick.error
    async def kick_error(self, ctx, error):
        if isinstance(error, commands.BotMissingPermissions):
            embed = nextcord.Embed(
                title=("Bot Missing Permissions"),
                colour=(nextcord.Colour.random()), description=f"Bot is missing required permissions to do that!\n Make sure the bot's role is above the user's role you wan to kick\n Also make sure the bot has the requirement permissions : Kick Members")
            await ctx.send(embed=embed)
            


    @commands.command()
    @commands.has_permissions(administrator=True)
    async def purge(self, ctx, limit: int):
        await ctx.channel.purge(limit=limit+1)
        await ctx.message.delete()
        embed = nextcord.Embed(
                title=("Permission denied"),
                colour=(nextcord.Colour.random()), description=f"Messages has been purged!", delete_after=5)
        await ctx.send(embed=embed)
        #await ctx.send('Messages has been purged by {}'.format(ctx.author.mention), delete_after=5)
        

    @purge.error
    async def clear_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            embed = nextcord.Embed(
                title=("Permission denied"),
                colour=(nextcord.Colour.random()), description=f"You cant do that!", delete_after=5)
            await ctx.send(embed=embed)
            #await ctx.send("You cant do that!", delete_after=5)

    @purge.error
    async def clear_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            embed = nextcord.Embed(
                title=("Missing required argument"),
                colour=(nextcord.Colour.random()), description=f"Please specify the amount of messages to purge!", delete_after=5)
            await ctx.send(embed=embed)
            #await ctx.send('Please specify the amount of messages to purge!', delete_after=5)


def setup(client):
    client.add_cog(Moderation(client))
