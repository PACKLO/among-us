import discord
from discord.ext import commands
import os

bot = commands.Bot(command_prefix='/')
#ИВЕНТ ЗАПУСКА БОТА
@bot.event
async def on_ready():
	print("Бот запущен")
	await bot.change_presence(status=discord.Status.do_not_disturb, activity=discord.Game('Among Us'))

#КОМАНДА ПОВТОРА
@bot.command(pass_context=True)
@commands.has_role('Администратор') # разрешаем передавать агрументы
async def say(ctx, arg):  # создаем асинхронную фунцию бота
    await ctx.send(arg)  # отправляем обратно аргумент

#КОМАНДА ПИНГА
@bot.command()
async def ping(ctx):
	await ctx.send(f'Понг! Текущий пинг бота: {round(bot.latency * 1000)}ms')
#КОМАНДА ОЧИСТКИ
@bot.command()
@commands.has_role('Администратор')
async def clear(ctx, amount=5):
	await ctx.channel.purge(limit=amount + 1)
#КОМАНДА КИКА
@bot.command()
@commands.has_role('Администратор')
async def kick(ctx, member : discord.Member, *, reason=None):
	await member.kick(reason=reason)
#КОМАНДА БАНА
@bot.command()
@commands.has_role('Администратор')
async def ban(ctx, member : discord.Member, *, reason=None):
	await member.ban(reason=reason)

token = os.environ.get('BOT_TOKEN')

bot.run(str(token))
