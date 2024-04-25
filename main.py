import discord
from discord import app_commands
from discord.ext import commands
import logging
import os
import advance_comms
import basic_comms
from dotenv import load_dotenv

intents = discord.Intents.default()
intents.members = True
intents.message_content = True

# Command prefix for bot

bot = commands.Bot(command_prefix='/', intents=intents)

# Bot logging

handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')

# Call basic commands function

helps = basic_comms.help
bot.tree.add_command(helps)

info = basic_comms.info
bot.tree.add_command(info)

say = basic_comms.say
bot.tree.add_command(say)

# Call advance commands function

profileimg = advance_comms.profileimg
bot.tree.add_command(profileimg)

# Execute when bot is ready

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')
    await bot.tree.sync()

# Running
load_dotenv()
token = os.environ.get("TOKEN")
bot.run(token, log_handler=handler)