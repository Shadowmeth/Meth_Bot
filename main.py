from discord.ext import commands
import discord
import random
import pyfiglet

token = ''

#if ctx.author.id == idhere:
meth = commands.Bot(command_prefix='!', description='Meth Bot')

symbol_table = {}

@meth.command()
async def ping(ctx):
    await ctx.send('pong')

@meth.command()
async def sum(ctx, num1, num2):
    try:
        num1 = int(num1)
        num2 = int(num2)
    except:
        # one of them or both of them are variables
        if num1 in symbol_table.keys():
            num1 = symbol_table[num1]
        if num2 in symbol_table.keys():
            num2 = symbol_table[num2]
    sum = int(num1) + int(num2)
    await ctx.send(f'{num1} + {num2} = {sum}')
@sum.error
async def error_sum(ctx, error):
    if isinstance(error, discord.ext.commands.errors.MissingRequiredArgument):
        await ctx.send('Syntax Error: proper usage is !sum <variable/value> <variable/value>')


@meth.command()
async def mult(ctx, num1, num2):
    try:
        num1 = int(num1)
        num2 = int(num2)
    except:
        # one of them or both of them are variables
        if num1 in symbol_table.keys():
            num1 = symbol_table[num1]
        if num2 in symbol_table.keys():
            num2 = symbol_table[num2]
    prod = int(num1) * int(num2)
    await ctx.send(f'{num1} * {num2} = {prod}')
@sum.error
async def error_mult(ctx, error):
    if isinstance(error, discord.ext.commands.errors.MissingRequiredArgument):
        await ctx.send('Syntax Error: proper usage is !mult <variable/value> <variable/value>')

@meth.command()
async def ascii(ctx, *, text):

    ascii = pyfiglet.figlet_format(text)
    await ctx.send(f"```{ascii}```")

@meth.command()
async def define(ctx, var, val):
    try:
        symbol_table[var] = int(val)
    except:
        symbol_table[var] = val

@define.error
async def error_define(ctx, error):
    if isinstance(error, discord.ext.commands.errors.MissingRequiredArgument):
        await ctx.send('Syntax Error: proper usage is !define <variable> <value>')

@meth.command()
async def print(ctx, var):
    if var in symbol_table.keys():
        await ctx.send(f'{symbol_table[var]}')
        return
    await ctx.send(f'{var}')
    return
@print.error
async def error_print(ctx, error):
    if isinstance(error, discord.ext.commands.errors.MissingRequiredArgument):
        await ctx.send('Syntax Error: proper usage is !print <variable/values>')
    if isinstance(error, discord.ext.commands.errors.TooManyArguments):
        await ctx.send('Syntax Error: too many arguments to !print, proper usage is !print <variable/value>')

@meth.command()
async def slap(ctx, members: commands.Greedy[discord.Member], *, reason='no reason'):
    slapped = ', '.join(x.name for x in members)
    await ctx.send(f'{slapped} just got slapped for {reason}!')
@slap.error
async def error_slap(ctx, error):
    if isinstance(error, discord.ext.commands.MissingRequiredArgument):
        await ctx.send('Specify at least one person to be slapped')

@meth.command()
async def info(ctx):
    await ctx.send('Hello. I am the meth bot created by Shadowmeth')
    await ctx.send('For a full list of supported commands, type !usage')

@meth.command()
async def usage(ctx):
    await ctx.send('1. !ping: you get ponged by bot for pinging e.e')
    await ctx.send('2. !sum <variable/value> <variable/value>')
    await ctx.send('3. !mult <variable/value> <variable/value>')
    await ctx.send('4. !ascii <text>: converts the text into ascii text')
    await ctx.send('5. !define <variable> <value>: create variables and assign values')
    await ctx.send('6. !print <variable>: print values of variables')
    await ctx.send('7. !slap <members> <reason>')

@meth.listen()
async def on_message(message):
    if message.author == meth.user:
        return

    """
    if str(message.author) == 'Shadowmeth#6670':
        await message.channel.send(f'Hello {message.author}, you entered an invalid command!')
        
        if message.content.lower() == '/what is the answer to life, universe and everything?':
            await message.channel.send('The answer to the life, universe and everything is 42')
        elif message.content.lower() == '/is life worth living?':
            if random.randint(0, 3) == 0:
                await message.channel.send('No, you should just die!')
            else:
                await message.channel.send('Yes, you should live, life is beautiful!')

    else:
        await message.channel.send('You are not my creator, {message.author}!')
    """

meth.run(token)

