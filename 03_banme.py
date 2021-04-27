import discord
from discord.ext import commands
import random

description = "ACM!!"

bot = commands.Bot(command_prefix='!', description=description)

@bot.event
async def on_ready():
    print('Logged in as')


@bot.command()
async def banme(ctx):
    await ctx.guild.ban(ctx.message.author)


bot.run('')