from tdbm.logger import GetFileLogger, Success, Error
from tdbm.data import DataManager, IData
from discord.ext.commands import Cog
from discord.ext import commands
from datetime import datetime
from tabulate import tabulate

__version__ = '0.0.1'



class ExampleDataManager(Cog):

    def __init__(self, bot):
        self.bot = bot
        self.Log = GetFileLogger('logs', __name__)
        self.dm = DataManager('exampleDataManager', ExampleDataManager.DataRecord)

    # Events
    @commands.command()
    async def testdb(self, ctx, *args):
        self.dm.add(ExampleDataManager.DataRecord(ctx.author.name, ctx.author.id))
        await ctx.send(Success(f'You discovered the secret power ! Congrats {ctx.author.name} !'))

    # Events
    @commands.command()
    async def savedb(self, ctx, *args):
        self.dm.save()
        await ctx.send(Success(f'Saved!'))
        cmd = self.bot.get_command('show_ExampleDataManager')
        print(cmd)
        await ctx.invoke(cmd)


    # Events
    @commands.command()
    async def loaddb(self, ctx, *args):
        self.dm.load()
        await ctx.send(Success(f'Loaded!'))

    # Events
    @commands.command()
    async def show_ExampleDataManager(self, ctx, *args):
        await ctx.send(Success("```" + f'\n\n{tabulate(self.dm.data, headers="keys", tablefmt="plain")}' + "```"))

    class DataRecord(IData):
        def __init__(self, name, id):
            super().__init__(name)
            self.name = name
            self.id = id


def setup(bot):
    bot.add_cog(ExampleDataManager(bot))
