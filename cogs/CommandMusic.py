import discord, asyncio
#import youtube_dl
from discord.ext import commands, tasks
import discord.utils
import random

class CommandMusic(commands.Cog):
	def __init__(self, client):
		self.client = client
		self.song_queue = []
		self.current_song = []
		self.YDL_OPTIONS = {
			'format': 'bestaudio/best', 
			'noplaylist': True, 
			'default_search': 'auto', 
			'outtmpl': '%(id)s-%(title)s.%(ext)s',
			'ignoreerrors': False,
			'force-ipv4': True,
			'cachedir': False
		}
		self.FFMPEG_OPTIONS = {
			'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 
			'options': '-vn'
		}

	# #Returns information on song(URL, TITLE, THUMB)	
	# async def infoGet(self, ctx, url):
	# 	with youtube_dl.YoutubeDL(self.YDL_OPTIONS) as ydl:
	# 		async with ctx.channel.typing():
	# 			info = ydl.extract_info(url, download = False)
	# 			if 'entries' in info: #Direct Search
	# 				url2 = info['entries'][0]['url']
	# 				title = info['entries'][0]['title']
	# 				thumbnail = info['entries'][0]['thumbnail']
	# 			else: #Direct Link
	# 				url2 = info['formats'][0]['url']
	# 				title = info.get('title', None)
	# 				thumbnail = info.get('thumbnail', None)
	# 			return [url2, title, thumbnail]
	# #Relay function used to loop for main music player
	# async def check_queue(self, ctx):
	# 	if len(self.song_queue) > 0:
	# 		ctx.voice_client.stop()
	# 		await self.play_song(ctx, self.song_queue[0][1])
	# 		self.song_queue.pop(0)
	# #Function to handle playing music
	# async def play_song(self, ctx, url):
	# 	sauce = await self.infoGet(ctx, url)
	# 	self.current_song = [sauce[1], sauce[2]]
	# 	source = await discord.FFmpegOpusAudio.from_probe(sauce[0], **self.FFMPEG_OPTIONS)
	# 	#Currently playing message
	# 	embed = discord.Embed(
	# 		color = 0xf39800,
	# 		description = f"Now Playing: **{sauce[1]}**"
	# 	)
	# 	embed.set_image(
	# 		url=sauce[2]
	# 	)
	# 	await ctx.send(embed=embed)
	
	# 	try:
	# 		ctx.voice_client.play(source, after=lambda error: self.client.loop.create_task(self.check_queue(ctx)))
	# 	except:
	# 		await ctx.send("API error occured. Try again.")
				
	# @commands.command(aliases=['p'])
	# async def play(self, ctx, *, url):
	# 	if ctx.author.voice is None:
	# 		return await ctx.send("You're not in a voice channel!")
	# 	elif discord.utils.get(ctx.bot.voice_clients, guild=ctx.guild) == None:
	# 		await ctx.author.voice.channel.connect()
	# 	elif ctx.voice_client.is_playing(): #Adds to queue
	# 		queue_list = len(self.song_queue)
	# 		sauce = await self.infoGet(ctx, url)
	# 		self.song_queue.append([sauce[1], url])
	# 		return await ctx.send(f"{sauce[1]} been added to your queue, position {queue_list + 1}.")
			
	# 	await self.play_song(ctx, url)
		
	# @commands.command(aliases=['s'])
	# async def skip(self, ctx):
	# 	if discord.utils.get(ctx.bot.voice_clients, guild=ctx.guild) == None:
	# 		return await ctx.send("Senko isn't in a voice channel!")
	# 	if ctx.author.voice is None:
	# 		return await ctx.send("You're not in a voice channel!")
	# 	ctx.voice_client.pause()
	# 	await ctx.send("Skipped!")
	# 	await self.play_song(ctx, self.song_queue[0][1])
	# 	self.song_queue.pop(0)

	# @commands.command()
	# async def remove(self, ctx, arg):
	# 	if discord.utils.get(ctx.bot.voice_clients, guild=ctx.guild) == None:
	# 		return await ctx.send("Senko isn't in a voice channel!")
	# 	if ctx.author.voice is None:
	# 		return await ctx.send("You're not in a voice channel!")
	# 	if int(arg) == 0 or int(arg) < len(self.song_queue):
	# 		self.song_queue.pop(int(arg)-1)
	# 		await ctx.send('ahhahahaha')
	# 	else:
	# 		await ctx.send("There is no such position in the queue!")
			
	# @commands.command(aliases=['q'])
	# async def queue(self, ctx):
	# 	if discord.utils.get(ctx.bot.voice_clients, guild=ctx.guild) == None:
	# 		return await ctx.send("Senko isn't in a voice channel!")
	# 	queue_list = []
	# 	for x in self.song_queue:
	# 		queue_list.append(f"`{1 + len(queue_list)}.` {x[0]}")
	# 	if len(queue_list) == 0:
	# 		return await ctx.send("There are no songs queued!")
	# 	queue_list = '\n'.join(queue_list)
		
	# 	embed = discord.Embed(
	# 		color=0xf39800,
	# 		description=f"Up next: \n{queue_list}"
	# 	)
	# 	embed.set_thumbnail(
	# 		url=self.client.user.avatar_url
	# 	)
	# 	embed.set_image(
	# 		url=self.current_song[1]
	# 	)
	# 	embed.set_footer(
	# 		text=f"Requested by {ctx.author.name} | Now playing: {self.current_song[0]}",
	# 		icon_url = ctx.author.avatar_url
	# 	)
	# 	await ctx.send(embed=embed)	
		
	# @commands.command()
	# async def join(self, ctx):
	# 	if ctx.author.voice is None:
	# 		return await ctx.send("You're not in a voice channel!")
	# 	elif discord.utils.get(ctx.bot.voice_clients, guild=ctx.guild):
	# 		return await ctx.send("Senko is already in a voice channel!")
	# 	await ctx.author.voice.channel.connect()
		
	# @commands.command(aliases=['dc'])
	# async def leave(self, ctx):
	# 	if ctx.author.voice is None:
	# 		return await ctx.send("You're not in a voice channel!")
	# 	if discord.utils.get(ctx.bot.voice_clients, guild=ctx.guild):
	# 		self.song_queue = []
	# 		await ctx.voice_client.disconnect()
	# 		dcList = [
	# 			"Farewell my dear!",
	# 			"As you wish dear.",
	# 			"Later nerdddd!",
	# 			"We shall talk another time!",
	# 			"I shall take my leave.",
	# 			"You want me to leave...? Ok...",
	# 			"But we had so much fun...",
	# 			"Till next time!",
	# 			"I found Among Us",
	# 			"Bruh"
	# 		]
	# 		await ctx.send(random.choice(dcList))
	# 	else:
	# 		await ctx.send("Senko isn't connected to a voice channel!")
					
async def setup(client):
	await client.add_cog(CommandMusic(client))