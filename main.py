import discord
from discord import app_commands
from discord.ext import commands
import logging
import os
from dotenv import load_dotenv

intents = discord.Intents.default()
intents.members = True
intents.message_content = True

# Command prefix for bot

bot = commands.Bot(command_prefix='/', intents=intents)

# Bot logging

handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')

# Execute when bot is ready

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')
    await bot.tree.sync()

# Help commands

@bot.tree.command(name="help", description="Command List of Hoshino AI")
async def help(interaction: discord.Interaction):
    embed = discord.Embed(title="User Guide for Hoshino AI", description="Usable commands list of Hoshino AI and it's feature for everyone.\n\n", color=0xFFDB33)
    embed.set_thumbnail(url="https://upload.wikimedia.org/wikipedia/commons/thumb/a/ae/Question_mark_white-transparent.svg/1024px-Question_mark_white-transparent.svg.png")
    embed.add_field(name="Default Prefix '/'", value="Use '/' to interact with me :) \n\n", inline=False)
    embed.add_field(name="Say", value="Use /say 'hello' or 'kabar' then I will answer it.", inline=False)
    embed.add_field(name="Info", value="Use /info bot to show information about me!, and /info devs to show information about the developer.", inline=False)
    embed.add_field(name="Check", value="To inspect someone's photo profile in large size, Use /check and then tag someone you want to see it's profile.", inline=False)
    embed.set_footer(text=f"Requested by: {interaction.user.display_name}")
    await interaction.response.send_message(embed=embed, ephemeral=True)

#Information command

@bot.tree.command(name="info", description="Everything about this bot")
@app_commands.describe(who = "Info about bot or devs.")

#Bot Information

async def info(interaction: discord.Interaction, who: str):
    if who == "bot":
        embed = discord.Embed(title="About Me", url="https://discord.com/api/oauth2/authorize?client_id=1128324445178708028&permissions=8&scope=bot", description="Hoshino AI Bot is not your average chatbot, it's been meticulously crafted to simulate human-like interactions.\n\nDeveloped with ❤ by みかず / Yourby", color=0x33DBFF)
        embed.set_author(name="Hoshino AI", url="https://oshinoko.fandom.com/wiki/Ai_Hoshino", icon_url="https://i.ibb.co/w6q0WDY/Screenshot-238.png")
        embed.set_thumbnail(url="https://i.ibb.co/F8bgSxB/Screenshot-237.png")
        embed.add_field(name="Command Prefix", value="Use '/' to interact with me :)", inline=False)
        embed.add_field(name="Help", value="Use /help for interact ", inline=True)
        embed.add_field(name="Info", value="Use /info to see any information about me.", inline=True)
        embed.set_footer(text= f"Requested by: {interaction.user.display_name}")
        await interaction.response.send_message(embed=embed)

#Devs Information

    elif who == "devs":
        embed = discord.Embed(title="About Devs", url="https://discord.com/api/oauth2/authorize?client_id=1128324445178708028&permissions=8&scope=bot", description="みかず / Yourby, known as Mikazu is the one and only developer of this bot. Nothing special about him but I know he raise me with all of his ❤\n", color=0x33DBFF)
        embed.set_author(name="みかず / Yourby", url="https://instagram.com/mikazuumi", icon_url="https://yt3.googleusercontent.com/ADWGcbxpQdPjeMPpxT26tdWrU6Quot4bQi9UGxheYhhXZk568w5Pq16hAUX3wE0te3ENp13WHA=s176-c-k-c0x00ffffff-no-rj")
        embed.set_thumbnail(url="https://i.ibb.co/0QtfNCH/pfp.png")
        embed.add_field(name="Future Update", value="I will update this later...", inline=True)
        embed.add_field(name="Help Command", value="Use /help to see all commands", inline=True)
        embed.set_footer(text= f"Requested by: {interaction.user.display_name}")
        await interaction.response.send_message(embed=embed)

#Unavailable/error commands

    else:
        embed = discord.Embed(title=f"Command error :(", description="Looks like you type the wrong command, or this command is not yet existed.", color=0xFF0000)
        await interaction.response.send_message(embed=embed)

# Say command
#  
@bot.tree.command(name="say", description= "Type hello or kabar")
@app_commands.describe(say_anything = "say hello, kabar")
async def say(interaction: discord.Interaction, say_anything: str,):
    if say_anything == "hello":
        await interaction.response.send_message(f'Aloo, {interaction.user.mention}')
    elif say_anything == "kabar":
        await interaction.response.send_message(f'Ya begitulah, {interaction.user.mention} gimana?')
    else:
        await interaction.response.send_message(f'Ngomong apa dah {interaction.user.mention}')

# Send photo profile of user

@bot.tree.command(name="check", description="Check someone's profile picture")
@app_commands.describe(profileimg = "Tag someone you want to check!")
async def profileimg(interaction: discord.Interaction, profileimg: discord.Member):
    if profileimg:
        embed = discord.Embed(title=f"Photo pofile of {profileimg.name}", description="Here you go!", color=0xDB33FF)
        embed.set_image(url=profileimg.avatar)
        embed.set_footer(text=f"Requested by: {interaction.user.display_name}")
        await interaction.response.send_message(embed=embed)
    else:
        embed = discord.Embed(title=f"User Not Found :(", description="Looks like you tag the wrong people, or they already leave this server.", color=0xFF0000)
        await interaction.response.send_message(embed=embed)

# Invite bot to other server

@bot.tree.command(name="invite", description="Create invite for bot")
async def invite(interaction: discord.Interaction):
    embed = discord.Embed(title="Invite Me", url="https://discord.com/api/oauth2/authorize?client_id=1128324445178708028&permissions=8&scope=bot", description= f"Hey {interaction.user.mention} Invite me to your server!", color=0xF8ED62)
    embed.set_author(name="Hoshino AI", icon_url="https://i.ibb.co/w6q0WDY/Screenshot-238.png")
    embed.set_thumbnail(url="https://i.ibb.co/F8bgSxB/Screenshot-237.png")
    await interaction.response.send_message(embed=embed)

# Running

load_dotenv()
token = os.getenv('TOKEN')
bot.run(token, log_handler=handler)