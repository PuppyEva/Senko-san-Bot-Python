import discord
from pybooru import Danbooru
from Functions import helperbois
from discord.ext import commands, tasks


class CommandDanbooru(commands.Cog):
	def __init__(self, client):
		self.client = client
	# clientDan = Danbooru('danbooru', username='ThatAsanIvan', api_key='DtPoBRh4aVNjN5jSWRPKCDw5')
	# #Embed Function
	# def createEmbed(self, ctx, apiLink, mPages, cPages, endpoint, name):
	# 	embed = discord.Embed(
	# 		color = 0xf39800
	# 	)
	# 	embed.set_image(
	# 		url = apiLink[cPages][endpoint]
	# 	)
	# 	embed.set_author(
	# 		name=name,
	# 		icon_url=self.client.user.avatar_url
	# 	)
	# 	embed.set_footer(
	# 		text=f"Requested by {ctx.author.name} | Page {cPages + 1} / {mPages + 1}",
	# 		icon_url = ctx.author.avatar_url
	# 	)
	# 	return embed

	# async def danImageFunction(self, ctx, apiLink, lenPage):
	# 	#Values of pages
	# 	cPages = 0
	# 	totalPages = lenPage - 1
	# 	#Starter Embed; Initializes reactions
	# 	message = await ctx.send(
	# 		embed=CommandDanbooru.createEmbed(
	# 			self, ctx, apiLink, totalPages, cPages, "large_file_url", apiLink[cPages]['id']
	# 		)
	# 	)
	# 	await message.add_reaction('⬅️')
	# 	await message.add_reaction('➡️')
	# 	def check(reaction, user): #Only requester is able to scroll and prevents dupes from clashing
	# 		return user == ctx.author and reaction.message.id == message.id and str(reaction.emoji) in ['⬅️', '➡️']
	# 	#Main Function Block	
	# 	while True:
	# 		try:
	# 			reaction, user = await self.client.wait_for('reaction_add', timeout=25, check=check)
	# 			if str(reaction.emoji) == '⬅️' and cPages > 0:
	# 				cPages -= 1
	# 				#Updates embed
	# 				await message.edit(
	# 					embed=CommandDanbooru.createEmbed(
	# 						self, ctx, apiLink, totalPages, cPages, "large_file_url", apiLink[cPages]['id']
	# 					)
	# 				)
	# 				await message.remove_reaction(reaction, user)
	# 			elif str(reaction.emoji) == '➡️' and cPages != totalPages:
	# 				cPages += 1
	# 				#Updates embed
	# 				await message.edit(
	# 					embed=CommandDanbooru.createEmbed(
	# 						self, ctx, apiLink, totalPages, cPages, "large_file_url", apiLink[cPages]['id']
	# 					)
	# 				)
	# 				await message.remove_reaction(reaction, user)
	# 			else:
	# 				await message.remove_reaction(reaction, user)
	# 		except asyncio.TimeoutError:
	# 			#Timeout at 25 seconds
	# 			break	
				
	# @commands.command()
	# async def dan(self, ctx, arg=None):
	# 	sus = [] #The list containing the URLs
	# 	confirm = 0
	# 	sampleError = 0
	# 	tagInvalid = False
	# 	while len(sus) != 5 and tagInvalid == False:
	# 		if arg == None: #Requests posts from API(Random pool)
	# 			sus = CommandDanbooru.clientDan.post_list(limit=5, random=True)
	# 		elif arg.casefold() == 'scat': #The Hugo Incident
	# 			break
	# 		else:
	# 			sus = CommandDanbooru.clientDan.post_list(limit=5, random=True, tags=arg)
				
	# 		#Determines if enough valid URLs
	# 		confirm = 0
	# 		for tags in sus: 
	# 			if 'large_file_url' in tags.keys():
	# 				confirm += 1
	# 		#Responses
	# 		if len(sus) == 0: #Invalid tags
	# 			tagInvalid = True
	# 			await ctx.send("Danbooru has returned no such results.")
	# 		elif confirm != 5: #Invalid amount of valid results
	# 			if sampleError > 5: #Returns all available images on hand
	# 				await ctx.send('Danbooru has returned an insufficient sample size.')
	# 				if len(sus) > 0:
	# 					await CommandDanbooru.danImageFunction(self, ctx, sus, len(sus))
	# 				tagInvalid = True
	# 			sampleError += 1
	# 			sus = []
	# 		else: #No errors response
	# 			await CommandDanbooru.danImageFunction(self, ctx, sus, len(sus))
			


async def setup(client):
	await client.add_cog(CommandDanbooru(client))