import discord
import random
import asyncio
from discord.ext import commands, tasks

class CommandHelp(commands.Cog):
	def __init__(self, client):
		self.client = client
		
	pageDesc = [
'''
📚 **Help**\n
Commands must be prefixed with `?`.
Use `?help <command>` to view help for a command.
Use `?help <category>` to view help for a category.
Use `?search <term>` to search for a command.\n
**Index**
• page 2 - **Fun** Commands
• page 3 - **Animal** Commands
• page 4 - **Nice Stats** Commands
• page 5 - **Yiff** Commands
• page 6 - **Music** Commands
• page 7 - **Settings/Misc**''',

'''
📖 **Help** » Fun Commands\n
Plain fun commands.\n
**Commands**
• `choose` - Let me choose for you.
• `coinflip` - Flip a coin.
• `fluff` - Touch fluffy tail. Gently, if you please.
• `headpat` - Pat Senko's head.
• `rate` - Let me rate something.
• `right` - Let me check whether you are correct.
• `roll` - Roll a dice.
• `rps` - Play rock-paper-scissors with me.
• `talk` - Talk to Senko.
• `who` - Find someone.''',

'''
📖 **Help** » Animal Commands\n
Simply cute animals.\n
**Commands**
• `fox` - Floofy foxes ~
• `birb` - Birb memes ~
• `blep` - \*blep* ~
• `panda` - Big fluffy pandas ~''',

'''
📖 **Help** » Nice Word Counter\n
Tracks the usage of the N-word.\n
**Commands**
• `nicepoints` - Stats for self or specific @.
• `nicelist` - Stat ranking of all members.''',

'''
📖 **Help** » Yiff Commands\n
Go to Horni Jail.\n
Use `?yiff` for random horni.
Use `?yiff <tag>` for specific horni.
Use `?yiff tag` for a list of all available tags.\n''',
		
'''
📖 **Help** » Music Commands\n
Plays music using the Youtube API.\n
Use `?play <link>` to search for or play music from a link.
Use `?join` connects Senko to your current voice channel.
Use `?leave` disconnects Senko from your current voice channel\n''',
		
'''
📖 **Help** » Settings/Miscellaneous\n
Senko occasionally sends a message in response to certain words.
*Setting only applies to user, not global server.*\n
• `eventenable` - Enables Senko's messages.
• `eventdisable` - Disables Senko's messages.

Senko's commands are initialized on a cog system with each being allowed to be enabled or disabled at any given time. (Admin)
*All settings are saved via database*\n
• `load` - Loads the stated cog.
• `Unload` - Unloads the stated cog
• `Reload` - Refreshes the stated cog with a newer instance.
• `coglist` - Returns names and statuses of all cogs.

• `prefix` - Sets the prefix for commands.
• `ping` - Reports latency.'''
	]
		
	@commands.command()
	async def help(self, ctx, arg=None):
		def embedFunction(desc):
			print("aa")
			embed = discord.Embed(
				color = 0xf39800,
				description = desc
			)
			print("ab")
			embed.set_thumbnail(
				url=self.client.user.avatar
			)
			print("AC")
			return embed
		print("embed generated")
		#Allows for page argument
		pages = 6
		if arg == None or arg == "0":
			currentpage = 0
		elif int(arg) > 0:
			currentpage = int(arg) - 1
		print("scrolling done")
		pageList = CommandHelp.pageDesc
		print("1")
		embed=embedFunction(pageList[currentpage])
		print("2")
		embed.set_footer(
			text=f"Requested by {ctx.author.name} | Page {currentpage + 1} / {pages + 1}",
			icon_url = ctx.author.avatar
		)
		print("3")
		message = await ctx.send(embed=embed)
		await message.add_reaction('⬅️')
		await message.add_reaction('➡️')

		def check(reaction, user):
			return user == ctx.author and reaction.message.id == message.id and str(reaction.emoji) in ['⬅️', '➡️']
			#Only requester is able to scroll and prevents dupes from clashing

		while True:
			try:
				reaction, user = await self.client.wait_for('reaction_add', timeout=40, check=check)
				if str(reaction.emoji) == '⬅️' and currentpage > 0:
					currentpage -= 1
					embed = embedFunction(pageList[currentpage])
					embed.set_footer(
						text=f"Requested by {ctx.author.name} | Page {currentpage + 1} / {pages + 1}",
						icon_url = ctx.author.avatar
					)
					await message.edit(embed=embed)
					await message.remove_reaction(reaction, user)
				elif str(reaction.emoji) == '➡️' and currentpage != pages:
					currentpage += 1
					embed = embedFunction(pageList[currentpage])
					embed.set_footer(
						text=f"Requested by {ctx.author.name} | Page {currentpage + 1} / {pages + 1}",
						icon_url = ctx.author.avatar
					)
					await message.edit(embed=embed)
					await message.remove_reaction(reaction, user)
				else:
					await message.remove_reaction(reaction, user)
			except asyncio.TimeoutError:
				#Timeout at 40 seconds
				break

	#Latency check command # Might wanna make conditionals depending on latency in future
	@commands.command()
	async def ping(self, ctx):
		await ctx.send(f"Pong! {round(self.client.latency * 1000)}ms")

async def setup(client):
	await client.add_cog(CommandHelp(client))