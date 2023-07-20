import os
import discord
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv("./.env")

intents = discord.Intents.default()
intents.members = True
bot = commands.Bot(command_prefix='!WhisperBot', intents=intents)

@bot.event
async def on_ready():
    print('We have logged in as {0.user}'.format(bot))

@bot.event
async def on_message(message):
    channel = message.author.voice.channel
    await channel.connect()

@bot.command()
async def leave(ctx):
    if ctx.voice_client is not None:
        await ctx.voice_client.disconnect()
    else:
        await ctx.send("I'm not in a voice channel!")

@bot.event
async def on_voice_receive(user, voice_data):
    print(type(voice_data))
    print(dir(voice_data))
    print(f"Received voice data from {user.name}")

bot.run(os.environ["BOT_TOKEN"])
