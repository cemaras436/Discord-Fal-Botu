import discord
from discord.ext import commands
from fallar import *

fal = Falim()

intents = discord.Intents(messages=True, reactions=True, guilds=True, members=True, presences=True)
Bot = commands.Bot(command_prefix="?", intents=intents)

TOKEN = open("token.txt", "r").read()


@Bot.event
async def on_ready():
    print("Bot kullanima hazir.")
    #botun aktif durumunu gösterir.
    await Bot.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="Elalemin derdini"))


# @commands.has_role("") tırnakların içerisine mesaj silme komutunu kullanmasını istediğiniz rolü giriniz.
@Bot.command(brief='Mesaj silme')
@commands.has_role("admin")
async def clear(ctx, amount=2):
    await ctx.channel.purge(limit=amount)

@Bot.command(brief='Sakız falı')
async def falım(ctx):
    await ctx.send(fal.fal_sec())


Bot.run(TOKEN)
