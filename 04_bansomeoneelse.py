import discord
from discord.ext import commands
import random

description = "ACM!!"

bot = commands.Bot(command_prefix='!', description=description)

@bot.event
async def on_ready():
    print('Logged in as')

#changed to kick so its easier to rejoin
@bot.command()
async def ban(ctx, user: discord.User):
    await ctx.guild.kick(user)
    await ctx.send("Banned!")


bot.run('')