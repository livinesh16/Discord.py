import discord
from discord.ext import commands
import urllib.parse, http.client
import json

class Geo(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def geo_fwd(self, ctx, query, *, region):
        conn = http.client.HTTPConnection('api.positionstack.com')

        parameters = urllib.parse.urlencode({
            'access_key': 'ACCESS_KEY',
            'query': query,
            'region': region,
            'limit': 1, })

        conn.request('GET', '/v1/forward?{}'.format(parameters))
        result = conn.getresponse()
        data = result.read()
        data = data.decode('utf-8')
        data = json.loads(data)
        data = data['data']
        data = data[0]
        geo_fwd = discord.Embed(title = 'Geographic Details')
        geo_fwd.set_thumbnail(url = 'https://upload.wikimedia.org/wikipedia/commons/thumb/9/97/The_Earth_seen_from_Apollo_17.jpg/1200px-The_Earth_seen_from_Apollo_17.jpg')
        geo_fwd.set_author(name = 'Dream Bot', icon_url = 'https://i.pinimg.com/originals/33/11/92/3311924db62ceef62a4a7ee87017280f.jpg')
        geo_fwd.add_field(name = 'County', value = data['county'])
        geo_fwd.add_field(name = 'Region',value = data['region'], inline = True)
        geo_fwd.add_field(name = 'Country', value = data['country'])
        geo_fwd.add_field(name = 'Continent', value = data['continent'], inline = True)
        geo_fwd.add_field(name = 'Latitude', value = data['latitude'])
        geo_fwd.add_field(name = 'Longitude', value = data['longitude'])
        await ctx.send(embed = geo_fwd)


    @geo_fwd.error
    async def geo_fwd_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send("Enter the correct arguments")
            geo_fwd = discord.Embed(title = 'Geolocating', description = 'This Command takes two arguments about a and gives more information on that location')
            geo_fwd.set_author(name = 'Dream Bot', icon_url = 'https://i.pinimg.com/originals/33/11/92/3311924db62ceef62a4a7ee87017280f.jpg')
            geo_fwd.set_thumbnail(url = 'https://upload.wikimedia.org/wikipedia/commons/thumb/9/97/The_Earth_seen_from_Apollo_17.jpg/1200px-The_Earth_seen_from_Apollo_17.jpg')
            geo_fwd.add_field(name = 'Syntax', value = '*geo_fwd<space><query><space><region>')
            await ctx.send(embed = geo_fwd)

    @commands.command()
    async def geo_rev(self, ctx, latitude, *, longitude):
        conn = http.client.HTTPConnection('api.positionstack.com')


        parameters = ({
            'access_key': 'ACCESS_KEY',
            'query': f'{latitude,longitude}'
             })
        conn.request('GET', '/v1/reverse?{}'.format(parameters))
        result = conn.getresponse()
        data = result.read()
        await ctx.send(data.decode('utf-8'))


def setup(client):
    client.add_cog(Geo(client))
