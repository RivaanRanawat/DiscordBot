import discord, os
from discord.ext import commands
import random
import phonenumbers
from phonenumbers import carrier
import pywhatkit as kit

bot = commands.Bot(command_prefix='$')

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')

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
    await ctx.send(":smiley: :wave: Hello there!")

@bot.command()
async def carriername(ctx, mobileNo: str):
    service_provider = phonenumbers.parse(mobileNo)
    await ctx.send(carrier.name_for_number(service_provider, "en"))

@bot.command()
async def roll_dice(ctx, number_of_dice: int, number_of_sides: int):
    dice = [
        str(random.choice(range(1, number_of_sides + 1)))
        for _ in range(number_of_dice)
    ]
    await ctx.send(', '.join(dice))

@bot.command()
async def mood(ctx):
    await ctx.send("https://media.tenor.com/images/c9710cb6a2b1e96aae29fbf2bdde608e/tenor.gif")

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
    embed.add_field(name="$mood", value="Shows my current moood", inline=False)
    embed.add_field(name="$roll_dice", value="Give it **number of dices** and **number of sides**", inline=False)
    embed.add_field(name="$add X Y", value="Gives the addition of **X** and **Y**", inline=False)
    embed.add_field(name="$multiply X Y", value="Gives the multiplication of **X** and **Y**", inline=False)
    embed.add_field(name="$remainder X Y", value="Gives the remainder of **X** and **Y**", inline=False)
    embed.add_field(name="$quotient X Y", value="Gives the quotient of **X** and **Y**", inline=False)
    embed.add_field(name="$carriername X", value="Give it **phone number** and it will show you your carrier", inline=False)
    embed.add_field(name="$info", value="Gives a little info about me", inline=False)
    embed.add_field(name="$help", value="Gives this message", inline=False)

    await ctx.send(embed=embed)

bot.run('NzA5NzM5NjE0ODg5NTc0NTMx.Xr5T9g.YdHX0qaRDbkdQTkTmz-3QtivPbA')
