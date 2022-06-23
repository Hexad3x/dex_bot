import discord
from discord.ext import commands
import youtube_dl
from youtube_dl import YoutubeDL
import urllib.request
import re
from functools import partial
import asyncio

YDL_OPTIONS = {'format':"bestaudio"}
ytdl = YoutubeDL(YDL_OPTIONS)

class music(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def greet(self, ctx):
        await ctx.send("Hello UwU")

    @commands.command()
    async def join(self, ctx):
        if ctx.author.voice is None:
            await ctx.send("You are not in a Voice Channel")
        voice_channel = ctx.author.voice.channel
        if ctx.voice_client is None:
            await voice_channel.connect()
        else:
            await ctx.voice_client.move_to(voice_channel)

    @commands.command()
    async def leave(self, ctx):
        await ctx.voice_client.disconnect()


    @commands.command()
    async def play(self, ctx, *, url):

        voice_channel = ctx.author.voice.channel
        if ctx.voice_client is None:
            await voice_channel.connect()
        
        ctx.voice_client.stop()
        
        FFMPEG_OPTIONS = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options': '-vn' }
        YDL_OPTIONS = {'format':"bestaudio"}
        vc = ctx.voice_client

        #find song if it is written
        url = url.replace(" ", "")
        print(url)
        search = "https://www.youtube.com/results?search_query=" + url
        url = urllib.request.urlopen(search)
        video_ids = re.findall(r"watch\?v=(\S{11})", url.read().decode())
        url = "https://www.youtube.com/watch?v=" + video_ids[0]

        with youtube_dl.YoutubeDL(YDL_OPTIONS) as ydl:
            info = ydl.extract_info(url, download=False)
            url2 = info['formats'][0]['url']
            source = await discord.FFmpegOpusAudio.from_probe(url2, **FFMPEG_OPTIONS)
            vc.play(source)

    @commands.command()
    async def pause(self, ctx):
        await ctx.send("I am so Stuffed UwU - Paused")
        await ctx.voice_client.pause()
        

    @commands.command()
    async def resume(self, ctx):
        await ctx.send("It is all dripping out SENPAI ! - un-Paused")
        await ctx.voice_client.resume()
        

    
def setup(client):
    client.add_cog(music(client))
