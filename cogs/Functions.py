from threading import Thread
import json, requests
import os
import discord
import asyncio
import time

class helperbois:
	async def basicImageFunction(self, ctx, apiLink, caption, endpoint='link'):
		#Stores all links; Prevent dupes
		urlList = []
		authentication = {
			'User-Agent': os.getenv("YiffCred"),
			'Authorization': os.getenv("YiffKey")
		}
		async with ctx.channel.typing():
			while len(urlList) < 5:
				response = requests.get(apiLink, 
				headers = authentication)
				image = response.json()
				if image not in urlList:
					urlList.append(image)
					print(image)
				if endpoint == 'url':
					time.sleep(.35)

		#Basic variables for conditionals
		pages = 4
		currentpage = 0
		if endpoint == 'url':
			url = urlList[currentpage]['images'][0][endpoint]
		else:
			url = urlList[currentpage][endpoint]
		#Embed
		embed = discord.Embed(
			color = 0xf39800
		)
		embed.set_image(
			url = url
		)
		embed.set_author(
			name=caption,
			icon_url=self.client.user.avatar_url
		)
		embed.set_footer(
			text=f"Requested by {ctx.author.name} | Page {currentpage + 1} / {pages + 1}",
			icon_url = ctx.author.avatar_url
		)

		message = await ctx.send(embed=embed)
		await message.add_reaction('⬅️')
		await message.add_reaction('➡️')

		def check(reaction, user):
			return user == ctx.author and reaction.message.id == message.id and str(reaction.emoji) in ['⬅️', '➡️']
			#Only requester is able to scroll and prevents dupes from clashing

		while True:
			try:
				reaction, user = await self.client.wait_for('reaction_add', timeout=25, check=check)
				if str(reaction.emoji) == '⬅️' and currentpage > 0:
					currentpage -= 1
					#Updates embed
					if endpoint == 'url':
						url = urlList[currentpage]['images'][0][endpoint]
					else:
						url = urlList[currentpage][endpoint]
					embed.set_image(
						url = url
					)
					embed.set_footer(
						text=f"Requested by {ctx.author.name} | Page {currentpage + 1} / {pages + 1}",
						icon_url = ctx.author.avatar_url
					)
					await message.edit(embed=embed)
					await message.remove_reaction(reaction, user)
				elif str(reaction.emoji) == '➡️' and currentpage != pages:
					currentpage += 1
					#Updates embed
					if endpoint == 'url':
						url = urlList[currentpage]['images'][0][endpoint]
					else:
						url = urlList[currentpage][endpoint]
					embed.set_image(
						url = url
					)
					embed.set_footer(
						text=f"Requested by {ctx.author.name} | Page {currentpage + 1} / {pages + 1}",
						icon_url = ctx.author.avatar_url
					)
					await message.edit(embed=embed)
					await message.remove_reaction(reaction, user)
				else:
					await message.remove_reaction(reaction, user)
			except asyncio.TimeoutError:
				#Timeout at 25 seconds
				break
					

	