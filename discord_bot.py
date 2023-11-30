import discord
from discord.ext import commands
from jokeapi import Jokes # Import the Jokes class
import asyncio


client = commands.Bot(command_prefix='!',intents = discord.Intents.all())

async def get_random_joke():
    j = await Jokes()  # Initialise the class
    joke = await j.get_joke()  # Retrieve a random joke
    if joke["type"] == "single": # Print the joke
        return joke["joke"],""
    else:
        return joke["setup"],joke["delivery"]



@client.event
async def on_ready():
    print("The bot is now ready for use")

@client.command()
async def hello(ctx):
    await ctx.send("Hello I am a discord bot")

@client.command()
async def joke(ctx):
    j = await Jokes()  # Initialise the class
    joke = await j.get_joke()  # Retrieve a random joke
    if joke["type"] == "single": # Print the joke
         await ctx.send(joke["joke"])
    else:
        await ctx.send(joke["setup"]+" "+joke["delivery"])
    
client.run('MTE3NjIyODY2MjM0NTk5ODQwNw.GkFe0G.7x8fsEXvkJtGFFoKRjh_zLzmp0rAkh3zJsS-Y0')