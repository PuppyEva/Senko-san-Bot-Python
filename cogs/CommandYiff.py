import discord
import os
import random
import json, requests
from discord.ext import commands, tasks

class CommandYiff(commands.Cog):
	def __init__(self, client):
		self.client = client
	
	# #Furry Command
	# @commands.command()
	# async def yiff(self, ctx, arg=None, size=2):
	# 	animalList = {
	# 		'birb': "Here's a floofy birb!",
	# 		'blep': "~blep~"
	# 	}
	# 	furryList = {
	# 		'boop': "Here's some nose booping!",
	# 		'cuddle': "Here's some cuddling uwu~",
	# 		'flop': "Here's some flopping~",
	# 		'fursuit': "Here's some fursuits!",
	# 		'hold': "Here's some embracing!",
	# 		'howl': "Awoooo~",
	# 		'hug': "Huggie wuggies~",
	# 		'kiss': "Here's some fluffy smooching!",
	# 		'lick': "Here's some licking!",
	# 		'propose': "owo",
	# 		'bulge': "~Bolgy wolgy~"
	# 	}
	# 	furryOWO = {
	# 		"gay": "*visible sweating*",
	# 		"straight": "OWO~",
	# 		"lesbian": "Is it me or is it hot in here?",
	# 		"gynomorph": "OWO~"
	# 	}
	# 	authentication = {
	# 		'User-Agent': os.getenv("YiffCred"),
	# 		'Authorization': os.getenv("YiffKey")
	# 	}
	# 	#Sets up Api endpoints
	# 	if arg == None:
	# 		if random.randint(1,2) == 1:
	# 			endpoint = "furry"
	# 			default1 = random.choice(list(furryList.keys()))
	# 			caption = furryList[default1]
	# 		else:
	# 			endpoint = "furry/yiff"
	# 			default1 = random.choice(list(furryOWO.keys()))
	# 			caption = furryOWO[default1]
	# 		response = requests.get(f"https://v2.yiff.rest/{endpoint}/{default1}?sizeLimit=<{size}>", 
	# 		headers = authentication)
	# 		caption = caption
	# 	elif arg.casefold() == "tags":
	# 		text = []
	# 		text.append("**SFW Tags**")
	# 		for x in furryList.keys():
	# 			text.append(x)
	# 		text.append("**NSFW Tags**")
	# 		for x in furryOWO.keys():
	# 			text.append(x)
	# 		text = '\n'.join(text)
	# 		return await ctx.message.author.send(f"```{text}```")
	# 	elif arg.casefold() in animalList:
	# 		print(arg)
	# 		response = requests.get(f"https://v2.yiff.rest/animals/{arg}?sizeLimit=<{size}>", 
	# 		headers = authentication)
	# 		caption = animalList[arg]
	# 	elif arg.casefold() in furryList:
	# 		response = requests.get(f"https://v2.yiff.rest/furry/{arg}?sizeLimit=<{size}>", 
	# 		headers = authentication)
	# 		caption = furryList[arg]
	# 	elif arg.casefold() in furryOWO:
	# 		response = requests.get(f"https://v2.yiff.rest/furry/yiff/{arg}?sizeLimit=<{size}>", 
	# 		headers = authentication)
	# 		caption = furryOWO[arg]

	# 	#Embed
	# 	yiff = response.json()
	# 	embed = discord.Embed(
	# 		color = 0xf39800
	# 	)
	# 	embed.set_image(
	# 		url = yiff['images'][0]['yiffMediaURL']
	# 	)
	# 	embed.set_author(
	# 		name=caption,
	# 		icon_url=self.client.user.avatar_url
	# 	)
	# 	embed.set_footer(
	# 		text=f"Requested by {ctx.author.name}~",
	# 		icon_url = ctx.author.avatar_url
	# 	)
	# 	await ctx.send(embed=embed)

	# @yiff.error
	# async def yiff_error(self, ctx, error):
	# 	if isinstance(error, commands.MissingRequiredArgument):
	# 		await ctx.send("Please enter a valid tag!")
		

async def setup(client):
	await client.add_cog(CommandYiff(client))