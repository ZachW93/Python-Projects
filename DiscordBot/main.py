import discord
import ImgurBot 
import random
from discord.ext import commands
import nest_asyncio
import os
from dotenv import load_dotenv

nest_asyncio.apply()

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN');
GUILD = os.getenv('DISCORD_GUILD');

bot = commands.Bot(command_prefix='!')

@bot.event
async def on_ready():
    for guild in bot.guilds:
        if guild.name == GUILD:
            break

    print(
        f'{bot.user} is connected to the following guild:\n'
        f'{guild.name}(id: {guild.id})'
    )

@bot.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(
        f'Welcome {member.name}. I am a Bot, please do not reply.'
    )

@bot.command(description='For when you wanna settle the score some other way')
async def choose(*choices : str):
    """Chooses between multiple choices."""
    await bot.say(random.choice(choices))
    
@bot.command()
async def test(ctx, *, arg):
    await ctx.send(arg)
    
@bot.command()
async def add(ctx, a: int, b: int):
    await ctx.send(a + b)

@bot.command()
async def subtract(ctx, a: int, b: int):
    await ctx.send(a - b)    
    
@bot.command()
async def multiply(ctx, a: int, b: int):
    await ctx.send(a * b)

@bot.command()
async def divide(ctx, a: int, b: int):
    if b == 0:
        await ctx.send("Can not divide by 0")
    else:
        await ctx.send(a / b)    

@bot.command(description="Answers a yes/no question.")
async def eight_ball(ctx, context):
    choices = [ 'As I see it, yes.',
                'Ask again later.',
                'Better not tell you now.',
                'Cannot predict now.',
                'Concentrate and ask again.',
                'Don’t count on it.',
                'It is certain.',
                'It is decidedly so.',
                'Most likely.',
                'My reply is no.',
                'My sources say no.',
                'Outlook not so good.',
                'Outlook good.',
                'Reply hazy, try again.',
                'Signs point to yes.',
                'Very doubtful.',
                'Without a doubt.',
                'Yes.',
                'Yes – definitely.',
                'You may rely on it.'
    ]
    await ctx.send(random.choice(choices))
    
@bot.command(description="Posts a random image from the front page of imgur.")
async def front_page(ctx):
    image = ImgurBot.random_image()
    await ctx.send(image)
    
@bot.command(description="Posts a random image from the subreddit 'BikiniBottomTwitter'.")
async def BKT(ctx):
    image = ImgurBot.BikiniBottomTwitter()
    await ctx.send(image)
    
    
'''
ADD COMMAND FOR UPDATES ON PYTHON FILES HERE
'''

@bot.command(description="users can add what needs to be done for scripts on GitHub")
async def addToDo(ctx, usermessage):
    toDoFile = open("todofile.txt","a")
    params = usermessage.split(" ")
    #command = params[0][1:]
    message = " ".join(params[1:])
    print(message)
    toDoFile.write(message)
    toDoFile.close()
    await ctx.send('item has been added to "To Do" List')
    
@bot.command(description='Lets users view the "To Do" List')
async def toDo(ctx):
    try:
        toDoFile = open("todofile.txt", "r")
        await ctx.send(toDoFile.readlines())
    except:
        await ctx.send('no items in "To Do" list')


@bot.command(description='Help function')
async def help()
        
bot.run(TOKEN)
