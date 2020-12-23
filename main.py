from discord.ext import commands
import random
import pyfiglet

token = ''

#if ctx.author.id == idhere:
meth = commands.Bot(command_prefix='/', description='Meth Bot')

@meth.command()
async def ping(ctx):
    await ctx.send('pong')

@meth.command()
async def sum(ctx, num1, num2):
    sum = int(num1) + int(num2)
    await ctx.send(f'{num1} + {num2} = {sum}')
@meth.command()
async def ascii(ctx, *, text):

    ascii = pyfiglet.figlet_format(text)
    await ctx.send(f"```{ascii}```")

@meth.listen()
async def on_message(message):
    if message.author == meth.user:
        return

    if str(message.author) == 'Shadowmeth#6670':
        if message.content.lower() == '/what is the answer to life, universe and everything?':
            await message.channel.send('The answer to the life, universe and everything is 42')
        elif message.content.lower() == '/is life worth living?':
            if random.randint(0, 3) == 0:
                await message.channel.send('No, you should just die!')
            else:
                await message.channel.send('Yes, you should live, life is beautiful!')
    else:
        await message.channel.send('You are not my creator, {message.author}!')

meth.run(token)

