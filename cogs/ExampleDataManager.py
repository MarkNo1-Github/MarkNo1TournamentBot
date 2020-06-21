from tdbm.logger import GetFileLogger, Success, Error
from tdbm.data import DataManager, IData
from discord.ext.commands import Cog
from discord.ext import commands
from datetime import datetime
from tabulate import tabulate

__version__ = '0.0.1'




class ExampleDataManager(Cog):
    def __init__(self, bot):
        self.Log = GetFileLogger('logs', __name__)
        self.dm = DataManager('exampleDataManager', IData)

    # Events
    @commands.command()
    async def test_ExampleDataManager(self, ctx, *args):
        self.dm.add(IData(ctx.author.name))
        await ctx.send(Success(f'You discovered the secret power ! Congrats {ctx.author.name} !'))

    # Events
    @commands.command()
    async def save_ExampleDataManager(self, ctx, *args):
        self.dm.save()
        await ctx.send(Success(f'Saved!'))

    # Events
    @commands.command()
    async def load_ExampleDataManager(self, ctx, *args):
        self.dm.load()
        await ctx.send(Success(f'Loaded!'))

    # Events
    @commands.command()
    async def show_ExampleDataManager(self, ctx, *args):
        await ctx.send(Success(f'\n\n{tabulate(self.dm.data, headers="keys", tablefmt="plain")}'))




def setup(bot):
    bot.add_cog(ExampleDataManager(bot))
