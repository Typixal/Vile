import nextcord
from nextcord.ext import commands

# This prevents staff members from being punished


class Sinner(commands.Converter):
    async def convert(self, ctx, argument):
        argument = await commands.MemberConverter().convert(ctx, argument)  # gets a member object
        # can change into any permission
        permission = argument.guild_permissions.manage_messages
        if not permission:  # checks if user has the permission
            return argument  # returns user object
        else:
            # tells user that target is a staff member
            raise commands.BadArgument("You cannot punish other staff members")

# Checks if you have a muted role


class Redeemed(commands.Converter):
    async def convert(self, ctx, argument):
        argument = await commands.MemberConverter().convert(ctx, argument)  # gets member object
        muted = nextcord.utils.get(
            ctx.guild.roles, name="Muted")  # gets role object
        if muted in argument.roles:  # checks if user has muted role
            return argument  # returns member object if there is muted role
        else:
            raise commands.BadArgument(
                "The user was not muted.")  # self-explainatory

# Checks if there is a muted role on the server and creates one if there isn't


async def mute(ctx, user, reason):
    # retrieves muted role returns none if there isn't
    role = nextcord.utils.get(ctx.guild.roles, name="Muted")
    # retrieves channel named hell returns none if there isn't
    hell = nextcord.utils.get(ctx.guild.text_channels, name="hell")
    if not role:  # checks if there is muted role
        try:  # creates muted role
            muted = await ctx.guild.create_role(name="Muted", reason="To use for muting")
            for channel in ctx.guild.channels:  # removes permission to view and send in the channels
                await channel.set_permissions(muted, send_messages=False,
                                              read_message_history=False,
                                              read_messages=False)
        except nextcord.Forbidden:
            # self-explainatory
            return await ctx.send("I have no permissions to make a muted role")
        await user.add_roles(muted)  # adds newly created muted role
        await ctx.send(f"{user.mention} has been sent to hell for {reason}")
    else:
        await user.add_roles(role)  # adds already existing muted role
        await ctx.send(f"{user.mention} has been sent to hell for {reason}")

    if not hell:  # checks if there is a channel named hell
        overwrites = {ctx.guild.default_role: nextcord.PermissionOverwrite(read_message_history=False),
                      ctx.guild.me: nextcord.PermissionOverwrite(send_messages=True),
                      muted: nextcord.PermissionOverwrite(read_message_history=True)}  # permissions for the channel
        try:  # creates the channel and sends a message
            channel = await ctx.create_channel('hell', overwrites=overwrites)
            await channel.send("Welcome to hell.. You will spend your time here until you get unmuted. Enjoy the silence.")
        except nextcord.Forbidden:
            return await ctx.send("I have no permissions to make #hell")


class Mute(commands.Cog):
    """Commands used to moderate your guild"""

    def __init__(self, client):
        self.client = client

    @commands.command()
    async def mute(self, ctx, user: Sinner, reason=None):
        """Gives them hell."""
        await mute(ctx, user, reason or "treason")  # uses the mute function

    @commands.command()
    async def unmute(self, ctx, user: Redeemed):
        """Unmutes a muted user"""
        await user.remove_roles(nextcord.utils.get(ctx.guild.roles, name="Muted"))  # removes muted role
        await ctx.send(f"{user.mention} has been unmuted")


def setup(client):
    client.add_cog(Mute(client))
