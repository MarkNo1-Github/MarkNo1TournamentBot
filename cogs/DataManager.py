from tdbm.logger import GetFileLogger, Success, Error
from tdbm.data import DataManger, IData
from discord.ext.commands import Cog
from discord.ext import commands
from datetime import datetime


__version__ = '0.0.1'

class DataRecord(IData):
    def __init__(self, name, id):
        super().__init__(name)
        self.name = name
        self.id = id


class ExampleDataManager(Cog):
    def __init__(self, bot):
        self.bot = bot
        self.Log = GetFileLogger('logs', __name__)
        self.dm = DataManger('exampleDataManager', DataRecord)

    # Events
    @commands.command()
    async def test_ExampleDataManager(self, ctx, *args):
        self.dm.add(DataRecord(ctx.author.name, ctx.author.id))
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
        for d in self.data:
            await ctx.send(Success(f'{d}'))


def setup(bot):
    bot.add_cog(ExampleDataManager(bot))
