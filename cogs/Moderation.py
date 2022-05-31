import nextcord
from nextcord.ext import commands

# This prevents staff members from being punished 
class Sinner(commands.Converter):
    async def convert(self, ctx, argument):
        argument = await commands.MemberConverter().convert(ctx, argument) # gets a member object
        permission = argument.guild_permissions.manage_messages # can change into any permission
        if not permission: # checks if user has the permission
            return argument # returns user object
        else:
            raise commands.BadArgument("You cannot punish other staff members") # tells user that target is a staff member
            
            
class Moderation(commands.Cog):
    """Commands used to moderate your guild"""
    
    def __init__(self, client):
        self.client = client
    
    async def __error(self, ctx, error):
        if isinstance(error, commands.BadArgument):
            await ctx.send(error)
            
    @commands.command(aliases=["banish"])
    @commands.has_permissions(ban_members=True)
    async def ban(self, ctx, user: Sinner=None, reason=None):
        """Casts users out of heaven."""
        
        if not user: # checks if there is a user
            return await ctx.send("You must specify a user")
        
        try: # Tries to ban user
            await ctx.guild.ban(user, f"By {ctx.author} for {reason}" or f"By {ctx.author} for None Specified")
            await ctx.send(f"{user.mention} was cast out of heaven for {reason}.")
        except nextcord.Forbidden:
            return await ctx.send("Are you trying to ban someone higher than the bot")

    @commands.command()
    async def softban(self, ctx, user: Sinner=None, reason=None):
        """Temporarily restricts access to heaven."""
        
        if not user: # checks if there is a user
            return await ctx.send("You must specify a user")
        
        try: # Tries to soft-ban user
            await ctx.guild.ban(user, f"By {ctx.author} for {reason}" or f"By {ctx.author} for None Specified") 
            await ctx.guild.unban(user, "Temporarily Banned")
        except nextcord.Forbidden:
            return await ctx.send("Are you trying to soft-ban someone higher than the bot?")
    
    
    @commands.command()
    async def kick(self, ctx, user: Sinner=None, reason=None):
        if not user: # checks if there is a user 
            return await ctx.send("You must specify a user")
        
        try: # tries to kick user
            await ctx.guild.kick(user, f"By {ctx.author} for {reason}" or f"By {ctx.author} for None Specified") 
        except nextcord.Forbidden:
            return await ctx.send("Are you trying to kick someone higher than the bot?")

    @commands.command()
    async def purge(self, ctx, limit: int):
        """Bulk deletes messages"""
        
        await ctx.purge(limit=limit + 1) # also deletes your own message
        await ctx.send(f"Bulk deleted `{limit}` messages") 
    
    @commands.command()
    async def block(self, ctx, user: Sinner=None):
        """
        Blocks a user from chatting in current channel.
           
        Similar to mute but instead of restricting access
        to all channels it restricts in current channel.
        """
                                
        if not user: # checks if there is user
            return await ctx.send("You must specify a user")
                                
        await ctx.set_permissions(user, send_messages=False) # sets permissions for current channel
    
    @commands.command()
    async def unblock(self, ctx, user: Sinner=None):
        """Unblocks a user from current channel"""
                                
        if not user: # checks if there is user
            return await ctx.send("You must specify a user")
        
        await ctx.set_permissions(user, send_messages=True) # gives back send messages permissions
                                
                                
def setup(client):
    client.add_cog(Moderation(client))