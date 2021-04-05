import discord
from discord.ext import commands


class First(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def cogtest(self,ctx):
        await ctx.send("cog is working")


def setup(client):
    client.add_cog(First(client))
