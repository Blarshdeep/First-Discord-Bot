import discord
from discord.ext import commands

client = commands.Bot(command_prefix = "!")

# Bot is ready to go
@client.event
async def on_ready():
    print("Bot is online.")

# Checks user's latency
@client.command()
async def ping(ctx):
    await ctx.send(f"{round(client.latency * 1000)}ms")

# Deletes messages in channel. Default is the LAST message sent.
@client.command()
async def delete(ctx, ammount = 2):
    await ctx.channel.purge(limit=ammount)

# Kick member
@client.command()
async def kick(ctx, member : discord.Member, *, reason=None):
  await member.kick(reason=reason)
  await ctx.send(f"{member.mention} has been kicked.")

# Ban member
@client.command()
async def ban(ctx, member : discord.Member, *, reason=None):
  await member.ban(reason=reason)
  await ctx.send(f"{member.mention} has been banned.")

client.run(### ENTER BOT TOKEN HERE ###)
