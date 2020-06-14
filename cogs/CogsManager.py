from tdbm.logger import GetLogger, Success, Error
from discord.ext.commands import Cog
from discord.ext import commands
from string import Template


__version__ = '0.0.2'


class CogsManager(Cog):
    def __init__(self, bot):
        self.bot = bot
        self.Log = GetLogger('logs', __name__)

    async def lets_try_do(self, fx, ext, ctx, succ, err):
        ext = f'cogs.{ext}'
        try:
            fx(ext)
        except Exception as e:
            err = err.substitute(name=type(e).__name__, exception=e)
            await ctx.send(err)
            self.Log.error(err)
        else:
            succ = succ.substitute(extension=ext)
            await ctx.send(succ)
            self.Log.debug(succ)


    @commands.command()
    @commands.is_owner()
    async def load(self, ctx, extension):
        """Laod a Cog extension runtime."""
        err_msg = Template(Error('$name - $exception'))
        suc_msg = Template(Success('loading $extension'))
        await self.lets_try_do(self.bot.load_extension,
                         extension,
                         ctx,
                         suc_msg,
                         err_msg)

    @commands.command()
    @commands.is_owner()
    async def unload(self, ctx, extension):
        """Unlaod a Cog extension runtime."""
        err_msg = Template(Error('$name - $exception'))
        suc_msg = Template(Success('unloading $extension'))
        await self.lets_try_do(self.bot.unload_extension,
                         extension,
                         ctx,
                         suc_msg,
                         err_msg)


    @commands.command()
    async def reload(self, ctx, extension):
        """Reload a Cog extension runtime."""
        await self.unload(ctx, extension)
        await self.load(ctx, extension)


def setup(bot):
    bot.add_cog(CogsManager(bot))
