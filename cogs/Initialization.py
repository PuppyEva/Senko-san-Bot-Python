import discord
import asyncio
import os
from discord.ext import commands, tasks
import random

class Initialization(commands.Cog):
	def __init__(self, client):
		self.client = client

	@tasks.loop(seconds=300.0)
	async def statusLoop(self):
		#Generates list of member names
		memberList = []
		guild = self.client.get_guild(632938120307933184)
		async for member in guild.fetch_members(limit=150):
			if not member.bot: 
				memberList.append(member.name)
				
		#Randomizes status
		randStatus = random.randint(1,3)
		if randStatus == 1: #Listening to X's problems~
			await self.client.change_presence(
				activity=discord.Activity(type=discord.ActivityType.listening, name=f"{random.choice(memberList)}'s problems~")
			)
		elif randStatus == 2: #Watching over X~
			await self.client.change_presence(
				activity=discord.Activity(type=discord.ActivityType.watching, name=f"over {random.choice(memberList)}~")
			)
		elif randStatus == 3: #Playing with X's hair~
			await self.client.change_presence(
				activity=discord.Game(f"with {random.choice(memberList)}'s hair~")
			)

	@commands.Cog.listener()
	async def on_ready(self):
		print("{0.user} is now running and operational.".format(self.client))
		#user = await self.client.fetch_user(323182727576682496)
		# await user.send("Senko-san is now running and operational.")
		self.statusLoop.start()
		
async def setup(client):
	await client.add_cog(Initialization(client))