import discord
from discord.ext import commands

client = commands.Bot(command_prefix = "!")

@client.event
async def on_ready():
    print("Bot is online.")

@client.command()
async def ping(ctx):
    await ctx.send(f"{round(client.latency * 1000)}ms")



client.run(### ENTER TOKEN HERE ###)
