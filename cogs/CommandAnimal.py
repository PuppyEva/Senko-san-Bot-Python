import discord
import os
import json
import asyncio
from discord.ext import commands, tasks
import random
from Functions import helperbois

class CommandAnimal(commands.Cog):
	def __init__(self, client):
		self.client = client

	#Random fox command
	@commands.command()
	@commands.cooldown(1, 6, commands.BucketType.user)
	async def fox(self, ctx):
		await helperbois.basicImageFunction(
			self, ctx,
			"https://randomfox.ca/floof", 
			"Here's a ball of floof!", 
			'image'
		)
	@fox.error
	async def fox_error(self, ctx, error):
		if isinstance(error, commands.CommandOnCooldown):
			await ctx.send(f"Slow down dear! Try again in {error.retry_after:.2f} seconds.")

	#Random panda command
	@commands.command(aliases=['po'])
	@commands.cooldown(1, 6, commands.BucketType.user)
	async def panda(self, ctx):
		await helperbois.basicImageFunction(
			self, ctx,
			"https://some-random-api.ml/img/panda", 
			"Here's a big fluffy panda!", 
			'link'
		)
	@panda.error
	async def panda_error(self, ctx, error):
		if isinstance(error, commands.CommandOnCooldown):
			await ctx.send(f"Slow down dear! Try again in {error.retry_after:.2f} seconds.")

	#Hugo's birb command
	@commands.command(aliases=['bird'])
	@commands.cooldown(1, 6, commands.BucketType.user)
	async def birb(self, ctx):
		await helperbois.basicImageFunction(
			self, ctx,
			"https://v2.yiff.rest/animals/birb",
			"Here's a fockin birb!",
			'url',
		)
	@birb.error
	async def birb_error(self, ctx, error):
		if isinstance(error, commands.CommandOnCooldown):
			await ctx.send(f"Slow down dear! Try again in {error.retry_after:.2f} seconds.")


	@commands.command()
	async def apitest(self, ctx, error):
		await ctx.send("https://v2.yiff.rest/animals/birb")
async def setup(client):
	await client.add_cog(CommandAnimal(client))