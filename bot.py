import discord
from discord.ext import commands
from yahoo_fin import stock_info as si
from yahoo_fin.stock_info import *
TOKEN = 'Insert your own token'
client = commands.Bot(command_prefix = '!')
# api_key = 'NJF29BB3PLB7NLKQ'
def stock(ticker):
    try:
        return str(round(si.get_live_price(ticker), 2))
    except:
        return 'stock not found'

@client.event
async def on_ready():
    print('Bot is ready')

@client.command()
async def price(ctx, *, ticker):
    await ctx.send('latest price is: ' + stock(ticker))

@client.command()
async def quote(ctx, *, ticker):
    await ctx.send(si.get_quote_table(ticker, dict_result = False))

@client.command()
async def balance_sheet(ctx, *, ticker):
    await ctx.send(si.get_balance_sheet(ticker))

@client.command()
async def cash_flow(ctx, *, ticker):
    await ctx.send(si.get_cash_flow(ticker))

@client.command()
async def day_gainers(ctx):
    await ctx.send(si.get_day_gainers())

@client.command()
async def day_losers(ctx):
    await ctx.send(si.get_day_losers())

@client.command()
async def day_day_most_active(ctx):
    await ctx.send(si.get_day_most_active())

@client.command()
async def income_statement(ctx, *, ticker):
    await ctx.send(si.get_income_statement(ticker))

@client.command()
async def live_price(ctx, *, ticker):
    await ctx.send(si.get_live_price(ticker))



client.run(TOKEN)
