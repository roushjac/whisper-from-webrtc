import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='!')

@bot.event
async def on_ready():
    print('We have logged in as {0.user}'.format(bot))

@bot.command()
async def join(ctx):
    if ctx.author.voice is None:
        await ctx.send("You're not in a voice channel!")
        return

    voice_channel = ctx.author.voice.channel
    if ctx.voice_client is None:
        await voice_channel.connect()
    else:
        await ctx.voice_client.move_to(voice_channel)

    # Enable receiving voice data
    ctx.voice_client.receive_enabled = True

@bot.command()
async def leave(ctx):
    if ctx.voice_client is not None:
        await ctx.voice_client.disconnect()
    else:
        await ctx.send("I'm not in a voice channel!")

@bot.event
async def on_voice_receive(user, voice_data):
    print(f"Received voice data from {user.name}")

bot.run('your-bot-token')
