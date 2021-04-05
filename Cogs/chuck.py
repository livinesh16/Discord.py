import discord
from discord.ext import commands
import json
import requests


class Chucky(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def chuck(self, ctx, * ,category):
        category = str(category)
        if category == 'random' or category == 'Random' or category == 'RANDOM':
            joke = requests.get("https://api.chucknorris.io/jokes/random")
            joke = json.loads(joke.text)
            await ctx.send(joke['value'])
        else:
            joke = requests.get('https://api.chucknorris.io/jokes/random?category=' + category)
            joke = json.loads(joke.text)
            await ctx.send(joke['value'])


    @commands.command()
    async def chuck_categories(self,ctx):
        await ctx.send(" 1) animal \n 2) career \n 3) celebrity \n 4) dev \n 5) explicit \n 6) fashion \n 7) food \n 8) history \n 9) money \n 10) movie \n 11) music \n 12) political \n 13) religion \n 14) science \n 15) sport \n 16) travel")


def setup(client):
    client.add_cog(Chucky(client))