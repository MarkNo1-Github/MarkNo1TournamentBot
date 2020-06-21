from tdb.logger import GetFileLogger
from discord.ext.commands import Cog
from discord.ext import commands
from datetime import datetime
import  discord


__version__ = '0.0.1'


class Menber(Cog):
    def __init__(self, bot):
        self.bot = bot
        self.Log = GetFileLogger('logs', __name__)

    @commands.command()
    @commands.guild_only()
    async def joined(self, ctx, *, member: discord.Member=None):
        """Says when a member joined."""
        if not member:
            member = ctx.author

        embed = discord.Embed(title='Joined:', description=ctx.guild.name, colour=member.colour)
        embed.set_author(icon_url=member.avatar_url, name=str(member))
        embed.add_field(name='\uFEFF', value=f'{member.display_name} joined on {member.joined_at}')
        await ctx.send(content=None, embed=embed)

    @commands.command(name='top_role', aliases=['toprole'])
    @commands.guild_only()
    async def show_toprole(self, ctx, *, member: discord.Member=None):
        """Simple command which shows the members Top Role."""

        if member is None:
            member = ctx.author

        await ctx.send(f'The top role for {member.display_name} is {member.top_role.name}')

    @commands.command(name='perms', aliases=['perms_for', 'permissions'])
    @commands.guild_only()
    async def check_permissions(self, ctx, *, member: discord.Member=None):
        """A simple command which checks a members Guild Permissions.
        If member is not provided, the author will be checked."""

        if not member:
            member = ctx.author

        # Here we check if the value of each permission is True.
        perms = '\n'.join(perm for perm, value in member.guild_permissions if value)

        # And to make it look nice, we wrap it in an Embed.
        embed = discord.Embed(title='Permissions for:', description=ctx.guild.name, colour=member.colour)
        embed.set_author(icon_url=member.avatar_url, name=str(member))

        # \uFEFF is a Zero-Width Space, which basically allows us to have an empty field name.
        embed.add_field(name='\uFEFF', value=perms)

        await ctx.send(content=None, embed=embed)

def setup(bot):
    bot.add_cog(Menber(bot))
