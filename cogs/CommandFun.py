import discord
import asyncio
from discord.ext import commands, tasks
import random

class CommandFun(commands.Cog):
	def __init__(self, client):
		self.client = client

	#Choose Command
	@commands.command()
	@commands.cooldown(1, 2, commands.BucketType.user)
	async def choose(self, ctx, *args):
		listChoices = ' '.join(args).split(' or ')
		emojiBulb = '<:choose:820499609105334292>'
		lolwut = '<:questionbubble:817891080800043019>'
		embed = discord.Embed(
			color=0xf39800,
			description=f"{emojiBulb} I choose {random.choice(listChoices)}."
		)
		#When no choices are provided
		if len(args) == 0:
			embed = discord.Embed(
				color=0xf39800,
				description=f"{lolwut} But... there is nothing for me to choose from?"
			)
			embed.set_thumbnail(
				url='https://i.imgur.com/LAU289z.png'
			)
		#When all choices are the same
		elif (listChoices.count(listChoices[0]) == len(listChoices)) == True:
			embed = discord.Embed(
				color=0xf39800,
				description=f"❔ I choose {random.choice(listChoices)}...\n\n{emojiBulb} What is the point in making me choose from one option?"
			)
			embed.set_thumbnail(
				url='https://i.imgur.com/LAU289z.png'
			)

		await ctx.send(embed=embed)

	@choose.error
	async def choose_error(self, ctx, error):
		if isinstance(error, commands.CommandOnCooldown):
			await ctx.send(f"Slow down dear! Try again in {error.retry_after:.2f} seconds.")

	#Coinflip Command
	@commands.command()
	@commands.cooldown(1, 2, commands.BucketType.user)
	async def coinflip(self, ctx):
		coinChance = random.randint(1,2)
		secretChance = random.randint(1,350)
		if secretChance == 1:
			shiro = '<:Shiro:818270736832528394>'
			speaking = '<:speaking:818270087567638589>'
			blank = '<:blank:817913093429395456>'

			embed = discord.Embed(
				color=0xf39800,
				description=f"{shiro}You flip a coin, but before it can land,\n{blank} it is snatched out of the air by Shiro!\n\n{speaking} I shall accept this offering ~"
			)
			embed.set_thumbnail(
				url='https://i.imgur.com/e5Plew5.png'
			)
			await ctx.send(embed=embed)
		else:
			embed = discord.Embed(
				color=0xf39800
			)
			#Heads chance
			if coinChance == 1:
				embed.set_footer(
					text='Heads.'
				)
				embed.set_thumbnail(
					url='https://i.imgur.com/lDHVkVe.png'
				)
				await ctx.send(embed=embed)
			#Tails chance
			if coinChance == 2:
				embed.set_footer(
					text='Tails.'
				)
				embed.set_thumbnail(
					url='https://i.imgur.com/QjDjSUO.png'
				)
				await ctx.send(embed=embed)

	@coinflip.error
	async def coinflip_error(self, ctx, error):
		if isinstance(error, commands.CommandOnCooldown):
			await ctx.send(f"Slow down dear! Try again in {error.retry_after:.2f} seconds.")

	#Fluffing Tail Command
	cooldownList = {}
	@commands.command()
	@commands.cooldown(3, 360, commands.BucketType.user)
	async def fluff(self, ctx):
		#Emoji variables
		tail = '<:fluffytail:817891080954970122>'
		t1 = '<:alertbubble3:817891081202696193>'
		t2 = '<:alertbubble:817891081110683658>'
		t3 = '<:alertbubble2:817891081140174848>'
		#Tier 1
		t1List = [
			"traces Senko's tail with their fingers.", 
			"gently strokes Senko's tail.", 
			"gently fluffs Senko's tail.", 
			"follows Senko's tail with their hands.",
			"gently caresses Senko's tail."
		]
		t1List2 = [
			"Uya!",
			"Uh-Uya!",
			"Uyan!"
		]
		#Tier 2
		t2List = [
			"gently pushes their fingers into Senko's tail.",
			"lightly sinks their fingers into Senko's tail."
		]
		t2List2 = [
			"D-dear, p-please be more gentle.",
			"D-dear, p-please be careful."
		]
		#Tier 3
		t3List = [
			"presses their face into Senko's tail.",
			"takes a deep whiff of Senko's tail."
		]
		t3List2 = [
			"Uyaaaaaan!",
			"Uh-Uyaaaa!"
		]
		if ctx.author.id not in CommandFun.cooldownList:
			CommandFun.cooldownList.update({ctx.author.id : 1})
			fluffmeter = f"{tail}**{ctx.author.name}** {random.choice(t1List)}\n\n{t1}{random.choice(t1List2)}"
			link='https://i.imgur.com/5u1CHcb.png'
		elif CommandFun.cooldownList.get(ctx.author.id) == 1:
			CommandFun.cooldownList.update({ctx.author.id : 2})
			fluffmeter = f"{tail}**{ctx.author.name}** {random.choice(t2List)}\n\n{t2}{random.choice(t2List2)}"
			link='https://i.imgur.com/dc6wFKL.png'
		elif CommandFun.cooldownList.get(ctx.author.id) == 2:
			CommandFun.cooldownList.pop(ctx.author.id)
			fluffmeter = f"{tail}**{ctx.author.name}** {random.choice(t3List)}\n\n{t3}{random.choice(t3List2)}"
			link='https://i.imgur.com/BhhvJzc.png'
		
		#Embed for fluff uwu
		embed = discord.Embed(
			color=0xf39800,
			description=fluffmeter
		)
		embed.set_thumbnail(
			url=link
		)

		await ctx.send(embed=embed)	

	@fluff.error
	async def fluff_error(self, ctx, error):
		if isinstance(error, commands.CommandOnCooldown):
			flufflimit = '<:swirlbubble:817891080908308492>'
			blank = '<:blank:817913093429395456>'
			stoplewdList = [
				f"D-do not go overboard, **{ctx.author.name}**.",
				f"**{ctx.author.name}**, I think that was enough for now.",
				f"S-surely you jest, **{ctx.author.name}**."
			]
			embed = discord.Embed(
				color=0xf39800,
				description=f"{flufflimit}{random.choice(stoplewdList)}\n{blank}... perhaps again in **{error.retry_after:.2f} seconds**."
			)
			embed.set_image(
				url='https://i.imgur.com/ZRjO9jz.png'
			)
			await ctx.send(embed=embed)
	
	#Headpat Command
	@commands.command()
	@commands.cooldown(1, 2, commands.BucketType.user)
	async def headpat(self, ctx):
		crown = '<:crownbubble:817891081118416916>'
		textList = [
			f"**{ctx.author.name}** slowly strokes Senko's hair.",
			f"**{ctx.author.name}** gently strokes Senko's hair."
			f"**{ctx.author.name}** gently plays with Senko's hair.",
			f"**{ctx.author.name}** carefully pats Senko's head.",
			f"**{ctx.author.name}** carefully plays with Senko's ears."
		]
		textList2 = [
			"Mofu~",
			"Uya~",
			"Umu~",
			"Uyan~",
			"This is nice every now and then~"
		]
		embed = discord.Embed(
			color=0xf39800,
			description=f"🖐️ {random.choice(textList)}\n\n{crown} {random.choice(textList2)}"
		)
		embed.set_thumbnail(
			url='https://i.imgur.com/dJv9Esp.png'
		)
		await ctx.send(embed=embed)
	
	#Rate Command
	@commands.command()
	@commands.cooldown(1,2, commands.BucketType.user)
	async def rate(self, ctx, *args):
		shiroEmoji = '<:blowingbubble:817891081144107049>'
		randomrate = random.randint(1,10)
		if randomrate >= 8:
			mood = 'https://i.imgur.com/UPCgLiR.png'
			hearttype = '<:loveheart:817891762558730262>'
		elif randomrate >= 4:
			mood = 'https://i.imgur.com/FngAy3U.png'
			hearttype = '<:likeheart:817891762743410698>'
		else:
			mood = 'https://i.imgur.com/uYB093L.png'
			hearttype = '<:hateheart:817891762713526292>'
		args = list(args)
		if len(args) == 0:
			bubbleEmoji = '<:questionbubble:817891080800043019>'
			embed = discord.Embed(
				color=0xf39800,
				description=f"{bubbleEmoji} But... **{ctx.author.name}**, what am I supposed to rate?"
			)
			embed.set_thumbnail(
				url='https://i.imgur.com/COK9CeJ.png'
			)

			await ctx.send(embed=embed)
		else:
			thefluffherself = False
			shirochan = False
			for gems in args:
				if "senko" in args or gems.lower() == 'you' or gems.lower() == 'yourself':
					thefluffherself = True
					sentence = 'myself'
					randomrate = '10'
					hearttype = '<:fluffytail:817891080954970122>'
					mood = 'https://i.imgur.com/Nri7psS.png'
					break
				elif gems.lower() == 'shiro':
					shirochan = True
				elif gems.lower() == 'your':
					args[args.index(gems)] = 'my'
				elif gems.lower() == 'myself':
					args[args.index(gems)] = 'yourself'
				elif gems.lower() == "i've":
					args[args.index(gems)] = "you've"
				elif gems.lower() == "i'm":
					args[args.index(gems)] = "you're"
				elif gems.lower() == "you've":
					args[args.index(gems)] = "I've"
				elif gems.lower() == 'my':
					args[args.index(gems)] = 'your'
				elif gems.lower() == 'me':
					args[args.index(gems)] = 'you'

			if thefluffherself == False:
				sentence = ' '.join(args)

			embed = discord.Embed(
				color=0xf39800,
				description=f"{hearttype} I would give {sentence} a {randomrate} out of 10."
			)
			embed.set_thumbnail(
				url=mood
			)
			shiroEmbed = discord.Embed(
				color=0xf39800,
				description=f"{shiroEmoji} Shiro is a 10 out of 10, obviously."
			)
			shiroEmbed.set_thumbnail(
				url='https://i.imgur.com/e5Plew5.png'
			)

			if shirochan == True:
				await ctx.send(embed=shiroEmbed)
			else:
				await ctx.send(embed=embed)

	@rate.error
	async def rate_error(self, ctx, error):
		if isinstance(error, commands.CommandOnCooldown):
			await ctx.send(f"Slow down dear! Try again in {error.retry_after:.2f} seconds.")

	#Right Command
	@commands.command()
	@commands.cooldown(1, 2, commands.BucketType.user)
	async def right(self, ctx):
		negativeList = [
			f"That seems unlikely, **{ctx.author.name}**.",
			f"Very doubtful, **{ctx.author.name}**.",
			f"Hmm... no, **{ctx.author.name}**, I don't think so.",
			f"I do not think that is quite right, **{ctx.author.name}**.",
			f"I do not quite believe it, **{ctx.author.name}**."
		]
		positiveList = [
			f"I think so, **{ctx.author.name}**.",
			f"That might be, **{ctx.author.name}**.",
			f"With great certainty, **{ctx.author.name}**.",
			f"Probably, **{ctx.author.name}**.",
			f"It is decidedly so, **{ctx.author.name}**.",
			f"Indeed, **{ctx.author.name}**."
		]
		if random.randint(1,2) == 1:
			currentText = random.choice(negativeList)
			emoji = '<:down_arrow:817891080980660276>'
		else:
			currentText = random.choice(positiveList)
			emoji = '<:uparrow:825863471865790514>'
		
		embed = discord.Embed(
			color=0xf39800,
			description=f"{emoji} {currentText}"
		)
		await ctx.send(embed=embed)
	
	#Dice Roll Command
	@commands.command()
	@commands.cooldown(1, 3, commands.BucketType.user)
	async def roll(self, ctx):
		blank = '<:blank:817913093429395456>'
		rollnum = random.randint(1,6)
		embed = discord.Embed(
			color=0xf39800,
			description=f"🎲 **{ctx.author.name}** rolls a die from 1 to 6...\n{blank} **{rollnum}**!"
		)
		await ctx.send(embed=embed)

	@roll.error
	async def roll_error(self, ctx, error):
		if isinstance(error, commands.CommandOnCooldown):
			await ctx.send(f"Slow down dear! Try again in {error.retry_after:.2f} seconds.")

	#Rock-Paper-Scissors Command
	@commands.command()
	@commands.cooldown(1, 4, commands.BucketType.user)
	async def rps(self, ctx, arg):
		#Generate randint and assigns opponent choice
		if arg.casefold() == "rock" or arg.casefold() == 'r':
			player = "✊"
		elif arg.casefold() == "paper" or arg.casefold() == 'p':
			player = "✋"
		elif arg.casefold() == "scissors" or arg.casefold() == 's':
			player = "✌️"
		else:
			bubbleEmoji = '<:questionbubble:817891080800043019>'
			tail = '<:fluffytail:817891080954970122>'
			whooshlmao = '<:blowingbubble:817891081144107049>'
			embed = discord.Embed(
				color=0xf39800,
				description=f"✊ **{ctx.author.name}** and **Senko** play rock-paper-scissors.\n\n{bubbleEmoji} You throw **{arg}**.\n{tail} Senko throws **tail**.\n\n🥈 Tail beats {arg}.\n\n{whooshlmao} You were not trying to cheat, were you?"
			)
			embed.set_thumbnail(
				url='https://i.imgur.com/SrfbWu4.png'
			)
			await ctx.send(embed=embed)
			return
		questionEmoji = '<:questionbubble:817891080800043019>'
		swirlEmoji = '<:swirlbubble:817891080908308492>'
		sparkleEmoji = '<:shinybubble:817887378349752331>'
		sVictory = [
			f"{sparkleEmoji} Did I win?",
			f"{sparkleEmoji} It is my win.",
			f"{sparkleEmoji} It is my victory."
		]
		sLoss = [
			f"{swirlEmoji} You won.",
			f"{swirlEmoji} I shall win the next one.",
			f"{swirlEmoji} It is your win."
		]
		sDraw = [
			f"{questionEmoji} We are both winners.",
			f"{questionEmoji} A surprising outcome.",
			f"{swirlEmoji} I was not sure whether I could win at all."
		]
		randNum = random.randint(1,3)
		if randNum == 1:
			opponent = "✊"
			opponent2 = 'rock'
		if randNum == 2:
			opponent = "✋"
			opponent2 = 'paper'
		if randNum == 3:
			opponent = "✌️"
			opponent2 = 'scissors'

		if player == opponent:
			winCond = "❌ It's a draw."
			textrandint = random.choice(sDraw)
		elif player == '✊':
			if opponent == '✋':
				winCond = f"🥈 **Paper** beats **Rock**."
				textrandint = random.choice(sVictory)
			if opponent == '✌️':
				winCond = f"🥇 **Rock** beats **Scissors**."
				textrandint = random.choice(sLoss)
		elif player == '✋':
			if opponent == '✊':
				winCond = f"🥇 **Paper** beats **Rock**."
				textrandint = random.choice(sLoss)
			if opponent == '✌️':
				winCond = f"🥈 **Scissors** beats **Paper**."
				textrandint = random.choice(sVictory)
		elif player == '✌️':
			if opponent == '✊':
				winCond = f"🥈 **Rock** beats **Scissors**."
				textrandint = random.choice(sVictory)
			if opponent == '✋':
				winCond = f"🥇 **Scissors** beats **Paper**."
				textrandint = random.choice(sLoss)

		images = [
			'https://i.imgur.com/ijGcBZ2.png', 
			'https://i.imgur.com/yZXJKaD.png'
		]
		embed = discord.Embed(
			description=f"**{ctx.author.name}** and **Senko** play rock-paper-scissors.\n\n{player} You throw **{arg}**.\n{opponent} Senko throws **{opponent2}**.\n{winCond}\n\n{textrandint}",
			color=0xeed03a
		)
		embed.set_thumbnail(
			url= random.choice(images)
		)
		await ctx.send(embed=embed)

	@rps.error
	async def rps_error(self, ctx, error):
		if isinstance(error, commands.MissingRequiredArgument):
			bubbleEmoji = '<:questionbubble:817891080800043019>'
			embed = discord.Embed(
				color=0xf39800,
				description=f"✊ **{ctx.author.name}** and **Senko** play rock-paper-scissors.\n\n❔ You throw nothing.\n\n{bubbleEmoji} Is something wrong, dear?"
			)
			embed.set_thumbnail(
				url='https://i.imgur.com/COK9CeJ.png'
			)
			await ctx.send(embed=embed)
		if isinstance(error, commands.CommandOnCooldown):
			await ctx.send(f"Slow down dear! Try again in {error.retry_after:.2f} seconds.")

	#Talk command(I'll finish later...)
	@commands.command()
	@commands.cooldown(1, 1, commands.BucketType.user)
	async def talk(self, ctx, *args):
		await ctx.send(' '.join(args))
	
	@talk.error
	async def talk_error(self, ctx, error):
		if isinstance(error, commands.CommandOnCooldown):
			await ctx.send(f"Slow down dear! Try again in {error.retry_after:.2f} seconds.")

	#Who command lmao
	@commands.command()
	@commands.cooldown(1, 1, commands.BucketType.user)
	async def who(self, ctx):
		emoji = '<:speaking:818270087567638589>'
		bruh = [
			str(random.choice(tuple(member for member in ctx.guild.members if not member.bot)))[:-5],
			'me'
		]
		coom = ''.join(random.choices(bruh, weights=[25, 1]))
		if coom == ctx.author.name:
			coom == 'you'
		variation = [
			f"Hmm... That may be **{coom}**.",
			f"As it seems, **{coom}**.",
			f"I think it could be **{coom}**.",
			f"That could be **{coom}**.",
			f"That might be **{coom}**.",
			f"Possibly **{coom}**.",
			f"Maybe **{coom}**."
		]
		embed = discord.Embed(
			color=0xf39800,
			description=f"{emoji} {random.choice(variation)}"
		)
		await ctx.send(embed=embed)

	@who.error
	async def who_error(self, ctx, error):
		if isinstance(error, commands.CommandOnCooldown):
			await ctx.send(f"Slow down dear! Try again in {error.retry_after:.2f} seconds.")

async def setup(client):
	await client.add_cog(CommandFun(client))