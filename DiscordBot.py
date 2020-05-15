import discord, os
from discord.ext import commands
import random

bot = commands.Bot(command_prefix='$')

send_time='19:36'
file_name='quotes.txt'
message_channel_id='709741775769829433'

if os.path.isfile(file_name):
        with open(file_name, "r") as f:
            message_list = f.read()
            message_list = message_list.strip().split("\n")

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')

async def time_check():
    await bot.wait_until_ready()
    message_channel=bot.get_channel(message_channel_id)
    while not bot.is_closed:
        now=datetime.strftime(datetime.now(),'%H:%M')
        if now == send_time:
            message= random.choice(message_list)
            await bot.send_message(message_channel,message)
            time=90
        else:
            time=1
        await asyncio.sleep(time)

@bot.command()
async def add(ctx, a: int, b: int):
    await ctx.send(a+b)

@bot.command()
async def remainder(ctx, a: int, b: int):
    await ctx.send(a%b)


@bot.command()
async def quotient(ctx, a: int, b: int):
    await ctx.send(a//b)

@bot.command()
async def multiply(ctx, a: int, b: int):
    await ctx.send(a*b)

@bot.command()
async def greet(ctx):
    await ctx.send(":smiley: :wave: Hello, there!")

@bot.command()
async def roll_dice(ctx, number_of_dice: int, number_of_sides: int):
    dice = [
        str(random.choice(range(1, number_of_sides + 1)))
        for _ in range(number_of_dice)
    ]
    await ctx.send(', '.join(dice))

@bot.command()
async def cat(ctx):
    await ctx.send("https://media.giphy.com/media/JIX9t2j0ZTN9S/giphy.gif")

@bot.command()
async def info(ctx):
    embed = discord.Embed(title="RRR Bot", description="Learning..", color=0xeee657)
    embed.add_field(name="RRR", value="Rivaan")
    embed.add_field(name="Server count", value=f"{len(bot.guilds)}")
    embed.add_field(name="Invite", value="https://discord.com/oauth2/authorize?client_id=709739614889574531&permissions=8&scope=bot")
    await ctx.send(embed=embed)

bot.remove_command('help')

@bot.command()
async def help(ctx):
    embed = discord.Embed(title="RRR Bot", description="Control me using:", color=0xeee657)

    embed.add_field(name="$greet", value="Gives a nice greet message", inline=False)
    embed.add_field(name="$cat", value="Gives a cute cat gif to lighten up the mood.", inline=False)
    embed.add_field(name="$roll_dice", value="Give it **number of dices** and **number of sides**", inline=False)
    embed.add_field(name="$add X Y", value="Gives the addition of **X** and **Y**", inline=False)
    embed.add_field(name="$multiply X Y", value="Gives the multiplication of **X** and **Y**", inline=False)
    embed.add_field(name="$remaincer X Y", value="Gives the remainder of **X** and **Y**", inline=False)
    embed.add_field(name="$quotient X Y", value="Gives the quotient of **X** and **Y**", inline=False)
    embed.add_field(name="$info", value="Gives a little info about the bot", inline=False)
    embed.add_field(name="$help", value="Gives this message", inline=False)

    await ctx.send(embed=embed)

bot.loop.create_task(time_check())
bot.run('NzA5NzM5NjE0ODg5NTc0NTMx.XrqS3A.-HDQMv8jb-5BP1Lx0DHE-RwFEIE')