from nextcord.ext import commands
import nextcord


    
class WrongRole(commands.CommandError):
    """Thrown when user has wrong role for command."""
    pass

def __init__(self, client):
        self.client = client
        
async def is_owner_check(ctx):
    if str(ctx.author.id) in ctx.client.config.get('OWNERS'):
        return True
    raise WrongRole(message="bot owner")


async def is_moderator_check(ctx):
    for role in ctx.author.roles:
        if str(role.id) in ctx.client.config.get('MOD_ROLES'):
            return True
    raise WrongRole(message="moderator")


async def is_helper_check(ctx):
    for role in ctx.author.roles:
        if (str(role.id) in ctx.client.config.get('MOD_ROLES')) or (
                str(role.id) in ctx.client.config.get('HELPER_ROLES')):
            return True
    raise WrongRole(message="moderator or helper")


def owner_id_check(client, _id):
    return str(_id) in client.config.get('OWNERS')


def owner():
    return commands.check(is_owner_check)


def moderator():
    return commands.check(is_moderator_check)


def helper():
    return commands.check(is_helper_check)
