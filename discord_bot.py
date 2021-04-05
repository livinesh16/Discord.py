import discord
from discord.ext import commands
import json
import requests
import urllib.parse
import urllib.request
import re
import youtube_dl
import os
from instagramy import InstagramUser
import kitsu
from imgurpython import ImgurClient
import http.client
from datetime import datetime
import asyncio
import random
from googletrans import Translator
import pypokedex
kitsu = kitsu.Client()

status = "Up and Running"

client = commands.Bot(command_prefix="*")
client.remove_command('help')


@client.event
async def on_ready():
    await client.change_presence(activity=discord.Game(name='*help'))
    #for filename in os.listdir(r"C:\Users\logan\PycharmProjects\pythonProject\Cogs"):
        #if filename.endswith('.py'):
            #client.load_extension(f'Cogs.{filename[:-3]}')
            #print(f'Loaded Cogs.{filename[:-3]}')

    print('Bot is Ready')

client.remove_command('help')


@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        await ctx.send("The Specified Command is not found")


@client.event
async def on_member_join(member):
    await member.send(f'{member} has Infiltrated the Server')


@client.event
async def on_member_remove(member):
    await member.send(f'{member} Neutralized')


@client.command()
@commands.has_any_role('Manager', 'Server Owner', 'Server Dictator')
async def load(ctx, extension):
    client.load_extension(f'Cogs.{extension}')
    await ctx.send(f'Loaded {extension}')


@client.command()
@commands.has_any_role('Manager', 'Server Owner', 'Server Dictator')
async def unload(ctx, extension):
    client.unload_extension(f'Cogs.{extension}')
    await ctx.send(f'Unloaded {extension}')


@client.command()
async def cog(ctx, *, argument):
    if argument in ['list', 'List', 'LIST']:
        num = 1
        cogs = discord.Embed(title='Cogs', description='This is a list of the cogs available in this bot')
        cogs.set_author(name='Dream Bot', icon_url='https://i.pinimg.com/originals/33/11/92/3311924db62ceef62a4a7ee87017280f.jpg')
        cogs.set_thumbnail(url='https://i.pinimg.com/originals/b1/0e/17/b10e1773b3f8fb334b8c9472c2ae3336.png')
        for filename in os.listdir(r"C:\Users\logan\PycharmProjects\pythonProject\Cogs"):
            if filename.endswith('.py'):

                cogs.add_field(name=str(num), value=f'{filename[:-3]}', inline=False)
                num += 1

        await ctx.send(embed=cogs)

    else:
        await ctx.send('The Specified Argument is not available')


@client.command(aliases=['Help', 'HELP'])
async def help(ctx, *, category):
    category = str(category)

    if category in ['Clear', 'clear', 'CLEAR', '1']:
        clear = discord.Embed(title = 'Clear Chat', description = 'This command clears a specified number of messages')
        clear.add_field(name = 'Syntax', value = r'*clear<space><number of messages to be deleted>', inline = False)
        clear.add_field(name = 'Note', value = 'You need to have permission to manage messages in order to use this command', inline = False)
        clear.set_author(name='Dream Bot',icon_url='https://i.pinimg.com/originals/33/11/92/3311924db62ceef62a4a7ee87017280f.jpg')
        await ctx.send(embed = clear)

    if category in ['Music', 'music', 'MUSIC', '2']:
        pass



    if category in ['moderation', 'Moderation', 'MODERATION', '3']:
        mod = discord.Embed(name='Moderation',
                                description='These are the moderation commands available in this bot')
        mod.set_author(name='Dream Bot',
                           icon_url='https://i.pinimg.com/originals/33/11/92/3311924db62ceef62a4a7ee87017280f.jpg')
        mod.set_thumbnail(url='https://discord.com/assets/a6193089fb762c7874fffcc9e61fa91e.svg')
        mod.add_field(name='Kick', value=r'*kick<username>', inline=False)
        mod.add_field(name='Ban', value=r'*ban<username>', inline=False)
        mod.add_field(name='Unban', value=r'*unban<username>#<discriminator>', inline=False)
        mod.add_field(name='List of Banned Users', value=r'*ban_list', inline=False)
        await ctx.send(embed=mod)

    if category in ['Search', 'search', 'SEARCH', '6']:
        search = discord.Embed(title='Youtube Search', description='This command lets you search videos on youtube')
        search.set_thumbnail(url='https://logodownload.org/wp-content/uploads/2014/10/youtube-logo-5-2.png')
        search.set_author(name='Dream Bot', icon_url='https://i.pinimg.com/originals/33/11/92/3311924db62ceef62a4a7ee87017280f.jpg')
        search.add_field(name='Syntax ', value=r'*youtube<space><query>', inline=False)
        await ctx.send(embed=search)



@help.error
async def help_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        help = discord.Embed(title='Categories ', description='1) Clear \n2) Music \n3) Moderation \n4) Ping \n5) Geographical \n 6) Search')
        help.set_author(name='Dream Bot', icon_url='https://i.pinimg.com/originals/33/11/92/3311924db62ceef62a4a7ee87017280f.jpg')

        await ctx.send(embed=help)


#await ctx.send(''' Bot prefix : \" \* \" \n\nPing = \" \*ping \" \n\nClear chat : \"  \*clear<space><number of messages> Note: This command has a cooldown of 60 seconds,
#which is triggered if when you spam it more than five times. You must have one of the following roles to use this command:      Server Owner, Manager, Server Dictator\" \n
#Search Gif :\n*gif<space><query> \n\n Search Youtube :\n \*youtube<space><query> \n\nTo Play music: \nStep 1: Join a VoiceChannel and  use the command \"\*join\"  \nStep 2:\"*play<space><Song Name>\"  \nWait few seconds for the song to play \nQueing songs is not available at the moment
#i)To stop the music : *stop \nii)To pause the music : *pause  \niii)To make the bot leave the VoiceChannel : *leave \niv)To make the bot join VoiceChannel : *join   \n
#Moderation: \nTo Kick a Member : *kick<Username> \nTo Ban a Member : *ban<username> \nTo Unban a User : *unban<username>#<discriminator> \nTo get the list of Banned Users : *ban_list
#\n ''')


@client.command()
async def hello(ctx):
    await ctx.send("hi")


@client.command()
async def who_is(ctx, *, name):
    if name in ['Snehal', 'snehal', 'SNEHAL', 'SPOP', 'spop', 'Spop']:
        await ctx.send("He is \"vengeance\" apparently. It's too small, that's what she said.")


    elif name in ['Junaidh', 'Mohammed', 'mohammed junaidh', 'junaidh', 'MOHAMMED', 'MOHAMMED JUNAIDH', 'Mohammed Junaidh']:
        await ctx.send(
            "If you know what mathematics is, then you know him. If you don't know him you have no idea what math is"
            )

    elif name in ['Aneesh', 'aneesh', 'ANEESH', 'R.N.S.Aneesh', 'r.n.s.aneesh']:
        await ctx.send("I heard that he's a great chemist")


    elif name in ['Harshit', 'harshit', 'HARSHIT']:
        await ctx.send("he's Just SAVAGE")


    elif name in ['Livinesh', 'livi', 'Livi', 'LIVINESH', 'LIVI', 'livinesh']:
        await ctx.send("My Daddy")

    else:
        await ctx.send('The details about {} is not in my database'.format(name))


@client.command(aliases=['Ping', 'PING'])
async def ping(ctx):
    await ctx.send(f'{round(client.latency * 1000)}ms')


@client.command()
async def wait_gif(ctx):
    await ctx.send(
        'https://tenor.com/view/master-vijay-angry-master-master-iam-waiting-master-wait-pandra-master-vijay-gif-20187354')


@client.command()
async def spiderman_gif(ctx):
    await ctx.send('https://giphy.com/gifs/yes-GgL288OGdmkGA')


@client.command()
async def waitwhat_gif(ctx):
    await ctx.send('https://i.kym-cdn.com/photos/images/newsfeed/001/443/919/223.gif')


@client.command()
@commands.has_guild_permissions(manage_messages=True)
async def clear(ctx, amount=5):
    # to clear chat
    amount = amount+1
    await ctx.channel.purge(limit=amount)

@clear.error
async def clear_error(error, ctx):
    if isinstance(error, PermissionError):
        await ctx.send(r"You Don't have permission to do that !")


@client.command()
async def gif(ctx, *, search):
    # to search for a gif
    apikey = "HCB7UEV7JFX5"
    lmt = 1
    search_term = search

    r = requests.get(
        "https://api.tenor.com/v1/search?q=%s&key=%s&limit=%s" % (search_term, apikey, lmt))

    if r.status_code == 200:
        # load the GIFs using the urls for the smaller GIF sizes
        top_gif = json.loads(r.content)
        await ctx.send(top_gif['results'][0]['url'])
    else:
        top_gif = None


@gif.error
async def gif_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("Please Specify the search query")


@client.command()
async def youtube(ctx, *, search):
    # to search for a youtube video
    search_query = search.replace(' ', '+')
    htm_content = urllib.request.urlopen(
        'https://www.youtube.com/results?search_query=' + search_query
    )

    search_results = re.findall(r"watch\?v=(\S{11})", htm_content.read().decode())
    await ctx.send('https://www.youtube.com/watch?v=' + search_results[0])


@client.command()
async def eng_link(ctx):
    # To get English link
    await ctx.send("https://meetingsapac10.webex.com/meet/lrks7022")


@client.command()
async def ip_link(ctx):
    # to get I.P link
    await ctx.send("https://meetingsapac14.webex.com/meet/vanithaacj02")


@client.command()
async def chem_link(ctx):
    # to get chemistry link
    await ctx.send("https://meetingsapac17.webex.com/meetingsapac17/j.php?MTID=mec6d949106fd548f1c3e879b235fa3c9")


@client.command()
async def phy_link(ctx):
    # to get physics link
    await ctx.send("https://meetingsapac17.webex.com/join/marteen.augnella")


@client.command()
async def maths_link(ctx):
    #to get math link
    await ctx.send("https://meetingsapac8.webex.com/join/krishnakkiran10")


@client.command()
async def join(ctx):
    # to make the bot join author's channel

    channel = ctx.message.author.voice.channel
    if (ctx.author.voice):
        channel = ctx.message.author.voice.channel

        await channel.connect()
        await ctx.send("Bot joined")

    else:
        await ctx.send('Please Join a voice channel')


@client.command()
async def leave(ctx):
    # To make the bot leave the channel

    await ctx.voice_client.disconnect()
    await ctx.send("Bot has left the VoiceChannel")


@client.command()
async def play(ctx, *, search):

    #joining VC
    voice_channel = discord.utils.get(ctx.guild.voice_channels, name = 'General')
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
    channel = ctx.message.author.voice.channel





    # searching query and saving url
    search_query = search.replace(' ', '+')
    htm_content = urllib.request.urlopen(
        'https://www.youtube.com/results?search_query=' + search_query
    )

    search_results = re.findall(r"watch\?v=(\S{11})", htm_content.read().decode())
    url = ('https://www.youtube.com/watch?v=' + search_results[0])

    # playing song
    song = os.path.isfile("C:/Users/logan/PycharmProjects/pythonProject/Music/song.mp3")
    try:
        if song:
            os.remove('C:/Users/logan/PycharmProjects/pythonProject/Music/song.mp3')
    except PermissionError:
        await ctx.send("Wait until the current song ends. You can't create playlists in this bot as of now ")
        return

    ydl_opts = {
        'format': 'bestaudio/best',

        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }]
    }
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])
    for file in os.listdir("C:/Users/logan/PycharmProjects/pythonProject/Music"):
        if file.endswith(".mp3"):
            os.rename(file, "song.mp3")
    voice.play(discord.FFmpegPCMAudio("song.mp3"))
    await ctx.send('Playing  ' + url)


@client.command()
async def pause(ctx):
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
    if voice.is_playing():
        voice.pause()
        await ctx.send("Paused")
    else:
        await ctx.send("The Bot is not playing anything right now")


@client.command()
async def resume(ctx):
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
    if voice.is_paused():
        voice.resume()
        await ctx.send("Resuming")
    else:
        await ctx.send("The audio is not paused")


@client.command()
async def stop(ctx):
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
    voice.stop()
    await ctx.send("Stopped the music")


@client.command()
async def say(ctx, *, text):
    await ctx.channel.purge(limit=1)
    await ctx.send(text)


@client.command()
@commands.has_guild_permissions(kick_members = True)
async def kick(ctx, member: discord.Member, *, reason=None):
    await member.kick(reason=reason)
    await ctx.send(f'Kicked {member.mention}')

@kick.error
async def kick_error(error, ctx):
    if isinstance(error, PermissionError):
        await ctx.send(r"You Don't have permission to Kick members !")




@client.command()
@commands.has_guild_permissions(ban_members = True)
async def ban(ctx, member: discord.Member, *, reason=None):
    await member.ban(reason=reason)
    await ctx.send(f'Banned {member.mention}')

@ban.error
async def ban_error(error, ctx):
    if isinstance(error, PermissionError):
        await ctx.send(r"You don't have permission to Ban members")


@client.command()
async def ban_list(ctx):
    banned_users = await ctx.guild.bans()
    await ctx.send(banned_users)


@client.command()
@commands.has_guild_permissions(ban_members = True)
async def unban(ctx, *, member):
    banned_users = await ctx.guild.bans()
    member_name, member_discriminator = member.split('#')

    for ban_entry in banned_users:
        user = ban_entry.user

        if (user.name, user.discriminator) == (member_name, member_discriminator):
            await ctx.guild.unban(user)
            await ctx.send(f'Unbanned {user.mention}')
            return

@unban.error
async def unban_error(error, ctx):
    if isinstance(error, PermissionError):
        await ctx.send(r"You don't have permission to Unban members")


@client.command()
async def tts(ctx, *, message):
    await ctx.send(f'{"/tts:"+ message}\t')

@client.command()
async def multiplication(ctx , num):
    num1 = int(num)
    for i in range(1,13):
        line = num1, 'x', i,'=', num1*i
        await ctx.send(line)

@client.command(aliases = ['Instagram','INSTAGRAM'])
async def instagram(ctx, *, username:str):
    #defining variables
    session_id = '35385143302%3AUufG9duDPBLc7h%3A27'
    #Scraping Data
    user = InstagramUser(username, session_id)
    userinfo = user.user_data

    #Embed
    insta = discord.Embed(name = 'Instagram User Details', description = ' ')
    insta.set_author(name = 'Dream bot', icon_url = 'https://i.pinimg.com/originals/33/11/92/3311924db62ceef62a4a7ee87017280f.jpg')

    if userinfo['is_verified']:
        insta.add_field(name = 'Username', value = f'{userinfo["username"] + ":ballot_box_with_check:"}', inline = False )
    else:
        insta.add_field(name = 'Username', value = userinfo["username"], inline = False)

    insta.add_field(name = 'Followers', value = f'{userinfo["edge_followed_by"]["count"]}', inline = False)

    insta.add_field(name = 'Following', value = f'{userinfo["edge_follow"]["count"]}', inline = False)
    insta.add_field(name = 'Bio', value = f'{user.biography}', inline = False)
    insta.set_thumbnail(url = userinfo['profile_pic_url_hd'])
    await ctx.send(embed = insta)

@client.command()
async def anime(ctx, *, query):


    entries = await kitsu.search('anime', query, limit = 1)
    if not entries:
        await ctx.send(f'{"No results found for the query " + query}')
    else:
        for i, anime in enumerate(entries, 1):
            anime_embed = discord.Embed(title = f'{anime.title}', description = f'{anime.synopsis}', colour = discord.Colour.blue())
            anime_embed.add_field(name=':hourglass_flowing_sand: Status', value=f'{anime.status}', inline = True)
            anime_embed.add_field(name=':dividers: Type', value = f'{anime.subtype}', inline = True)
            anime_embed.add_field(name =':calendar_spiral: Aired', value = f'from {anime.started_at.strftime("%d-%m-%Y")} to {anime.ended_at.strftime("%d-%m-%Y") }', inline = False)
            anime_embed.add_field(name =':minidisc: Total Episodes', value = f'{anime.episode_count}', inline = False )
            anime_embed.add_field(name = ':trophy: Rank', value = f'#{anime.rating_rank}', inline = True)
            anime_embed.add_field(name=':heart: Popularity', value=f'#{anime.popularity_rank}', inline=True)

            r = requests.get("https://api.qwant.com/api/search/images",
                             params={
                                 'count': 50,
                                 'q': anime.title,
                                 't': 'images',
                                 'safesearch': 1,
                                 'locale': 'en_US',
                                 'uiv': 4
                             },
                             headers={
                                 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'
                             }
                             )

            response = r.json().get('data').get('result').get('items')
            urls = [r.get('media') for r in response]
            anime_cover = urls[0]

            anime_embed.set_thumbnail(url=anime_cover)

            await ctx.send(embed=anime_embed)


@client.command()
async def imgur(ctx, *, query):
    client_id = '88ae741b01592db'
    client_secret = '0bb22a688bbc5d800dd57cd9cc80521770f031fc'
    imgur_1 = ImgurClient(client_id, client_secret)
    items = imgur_1.gallery_search(query)
    await ctx.send(items[0].link)

@client.command()
async def qwant_image(ctx, *, query):
    r = requests.get("https://api.qwant.com/api/search/images",
                     params={
                         'count': 50,
                         'q': query,
                         't': 'images',
                         'safesearch': 0,
                         'locale': 'en_US',
                         'uiv': 4
                     },
                     headers={
                         'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'
                     }
                     )

    response = r.json().get('data').get('result').get('items')
    urls = [r.get('media') for r in response]
    await ctx.send(urls[0])


@client.command()
async def geo_fwd(ctx, query, *, region):
    r = requests.get("https://api.qwant.com/api/search/images",
                     params={
                         'count': 50,
                         'q': query,
                         't': 'images',
                         'safesearch': 1,
                         'locale': 'en_US',
                         'uiv': 4
                     },
                     headers={
                         'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'
                     }
                     )

    response = r.json().get('data').get('result').get('items')
    urls = [r.get('media') for r in response]

    conn = http.client.HTTPConnection('api.positionstack.com')

    parameters = urllib.parse.urlencode({
            'access_key': 'd1e4e5547bceef63abb78812f825d3fc',
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
    geo_fwd.set_thumbnail(url = urls[0])
    geo_fwd.set_author(name = 'Dream Bot', icon_url = 'https://i.pinimg.com/originals/33/11/92/3311924db62ceef62a4a7ee87017280f.jpg')
    geo_fwd.add_field(name = 'County', value = data['county'])
    geo_fwd.add_field(name = 'Region',value = data['region'], inline = True)
    geo_fwd.add_field(name = 'Country', value = data['country'])
    geo_fwd.add_field(name = 'Continent', value = data['continent'], inline = True)
    geo_fwd.add_field(name = 'Latitude', value = data['latitude'])
    geo_fwd.add_field(name = 'Longitude', value = data['longitude'])
    await ctx.send(embed = geo_fwd)


@geo_fwd.error
async def geo_fwd_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("Enter the correct arguments")
        geo_fwd = discord.Embed(title = 'Geolocating', description = 'This Command takes two arguments about a and gives more information on that location')
        geo_fwd.set_author(name = 'Dream Bot', icon_url = 'https://i.pinimg.com/originals/33/11/92/3311924db62ceef62a4a7ee87017280f.jpg')
        geo_fwd.set_thumbnail(url = 'https://upload.wikimedia.org/wikipedia/commons/thumb/9/97/The_Earth_seen_from_Apollo_17.jpg/1200px-The_Earth_seen_from_Apollo_17.jpg')
        geo_fwd.add_field(name = 'Syntax', value = '*geo_fwd<space><query><space><region>')
        await ctx.send(embed = geo_fwd)

@client.command()
async def geo_rev(ctx, latitude, *, longitude):
    conn = http.client.HTTPConnection('api.positionstack.com')


    parameters = ({
            'access_key': 'd1e4e5547bceef63abb78812f825d3fc',
            'query': f'{latitude,longitude}'
             })
    conn.request('GET', '/v1/reverse?{}'.format(parameters))
    result = conn.getresponse()
    data = result.read()
    await ctx.send(data.decode('utf-8'))

@client.command()
async def chuck(ctx, *, category):
    category = str(category)
    if category == 'random' or category == 'Random' or category == 'RANDOM':
        joke = requests.get("https://api.chucknorris.io/jokes/random")
        joke = json.loads(joke.text)
        await ctx.send(joke['value'])
    else:
        joke = requests.get('https://api.chucknorris.io/jokes/random?category=' + category)
        joke = json.loads(joke.text)
        await ctx.send(joke['value'])


@chuck.error
async def chuck_categories_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        categories = discord.Embed(title = 'Categories', description = '\n1) animal \n2) career \n3) celebrity \n4) dev \n5) explicit \n6) fashion \n7) food \n8) history \n9) money \n10) movie \n11) music \n12) political \n13) religion \n14) science \n15) sport \n16) travel', colour = discord.Colour.blue())
        await ctx.send(embed=categories)



'''@client.command()
async def manga(ctx, *, query):'''

@client.command()
async def wiki(ctx, *, Query:str):
    Query = Query.replace(' ','_')
    url = 'https://en.wikipedia.org/wiki/' + Query
    await ctx.send(url)


@wiki.error
async def wiki_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send('Enter the search Query')

@client.command()
async def reverse(ctx, *, message):
    reversed_string = message[::-1]
    await ctx.send(reversed_string)

@client.command()
async def remainder(ctx, date_time, * , message:str):
    date = datetime.now()
    while date < date_time:
        date = datetime.now()

    await ctx.send(message)


@client.command()
async def countdown(ctx, num):
    try:
        num = int(num)
        num_msg = await ctx.send(num)
        await asyncio.sleep(1)
        while True:
            num = num-1
            if num < 0:
                break
            else:
                await num_msg.edit(content = num)
                await asyncio.sleep(1)

    except ValueError:
        await ctx.send("Enter a number")

@client.command()
async def dm_me(ctx, *, message):
    await ctx.author.send(message)

@client.command()
async def dm(ctx, member: discord.Member, *, message):
    await member.send(f'{message} \n\n from {ctx.author}')
    await ctx.send('Message sent')



@client.command()
async def tell(ctx, *,message):
    answers =['Yes', 'No',"I don\'t know"]
    await ctx.send(random.choice(answers))

@client.command()
async def embed(ctx, *, message):
    message_embed = discord.Embed(title = f'{ctx.author}', description = f'{message}')
    await ctx.send(embed = message_embed)


@client.command()
async def translate(ctx, lang, *,message):
    translator = Translator()
    translation = translator.translate(text = message, dest = lang)
    translate_embed = discord.Embed(title = 'Translator', description = f'{translation.origin}({translation.src}) ---> {translation.text}({translation.dest})', colour = discord.Colour.purple())
    translate_embed.add_field(name = translation.src, value = translation.origin , inline = True)
    translate_embed.add_field(name = translation.dest, value = translation.text, inline = True)
    translate_embed.set_footer(text = 'powered by Google', icon_url = 'https://assets.materialup.com/uploads/82eae29e-33b7-4ff7-be10-df432402b2b6/preview')
    await ctx.send(embed = translate_embed)

@client.command()
async def pokedex(ctx, *, name):
    name = str(name)
    pokemon = pypokedex.get(name = name)
    name = pokemon.name.upper()
    dex = pokemon.dex; string = ' '
    types = pokemon.types
    types = string.join(types).upper()
    base_xp = str(pokemon.base_experience)
    hp = pokemon.base_stats[0]
    attack = pokemon.base_stats[1]
    defense = pokemon.base_stats[2]
    sp_attack = pokemon.base_stats[3]
    sp_defense = pokemon.base_stats[4]
    speed = pokemon.base_stats[5]
    ability = pokemon.abilities[0][0].upper()
    hidden = pokemon.abilities[0][1]

    pokemon_pic = pokemon.sprites[0]['default']; weight = str(pokemon.weight/10); height = str(pokemon.height/10)
    pokedex_embed = discord.Embed(title = name , description = f'Dex : {dex}', colour = discord.Colour.red())
    pokedex_embed.set_thumbnail(url = pokemon_pic)

    pokedex_embed.add_field(name = 'Types', value = types, inline = False )
    pokedex_embed.add_field(name='Height', value=f'{height}m', inline=False)
    pokedex_embed.add_field(name='Weight', value=f'{weight}kg', inline=True)
    pokedex_embed.add_field(name = 'Base stats',value = 'Stats:', inline = False)
    pokedex_embed.add_field(name = 'Base XP', value = base_xp , inline = False )
    pokedex_embed.add_field(name = 'HP', value = hp, inline = True)
    pokedex_embed.add_field(name = 'Attack', value = attack, inline = True)
    pokedex_embed.add_field(name = 'Defense', value = defense, inline = True)
    pokedex_embed.add_field(name = 'Special Attack', value = sp_attack, inline = True)
    pokedex_embed.add_field(name = 'Special Defense', value = sp_defense, inline = True)
    pokedex_embed.add_field(name ='Speed', value = speed)
    pokedex_embed.add_field(name = 'Ability', value = ability, inline = False)
    pokedex_embed.add_field(name = 'Hidden', value = str(hidden), inline = True )


    await ctx.send(embed = pokedex_embed)


@client.command()
async def advice(ctx):
    adv = requests.get('https://api.adviceslip.com/advice')
    output = adv.json().get('slip')
    result = output.get('advice')
    advice_embed = discord.Embed(title = 'Advice', description = result, colour = discord.Colour.purple())
    advice_embed.set_thumbnail(url = 'https://englishlive.ef.com/blog/wp-content/uploads/sites/2/2015/05/how-to-give-advice-in-english-768x512.jpg')
    await ctx.send(embed = advice_embed)

@client.command(aliases = ['8ball', '8BALL', '8Ball'])
async def ball(ctx, *, message):

    conn = http.client.HTTPSConnection("8ball.delegator.com")
    question = urllib.parse.quote(message)
    conn.request('GET', '/magic/JSON/' + question)
    response = conn.getresponse()
    result = json.loads(response.read())
    answer = result['magic']['answer']
    await ctx.send(':8ball: ' + answer)






















client.run("ODAzODMxNjA0MzQ2MzU1NzQz.YBDghA.fcllH2CxfR1JNn5YXWqtnv23NV8")