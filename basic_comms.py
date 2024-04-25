import discord
from discord import app_commands
from discord.ext import commands

intents = discord.Intents.default()
intents.members = True
intents.message_content = True

bot = commands.Bot(command_prefix='/', intents=intents)

# Help command

@bot.tree.command(name="help", description="Command List of Hoshino AI")
async def help(interaction: discord.Interaction):
    embed = discord.Embed(title="User Guide for Hoshino AI", description="Usable commands list of Hoshino AI and it's feature for everyone.\n\n", color=0xFFDB33)
    embed.set_thumbnail(url="https://i.ibb.co/nfXjtQC/1.jpg")
    embed.add_field(name="Default Prefix '/'", value="Use '/' to interact with me :) \n\n", inline=False)
    embed.add_field(name="Say", value="Use /say 'hello' or 'kabar' then I will answer it.", inline=False)
    embed.add_field(name="Info", value="Use /info bot to show information about me!, and /info devs to show information about the developer.", inline=False)
    embed.add_field(name="Check", value="To inspect someone's photo profile in large size, Use /check and then tag someone you want to see it's profile.", inline=False)
    embed.set_footer(text=f"Requested by: {interaction.user.display_name}")
    await interaction.response.send_message(embed=embed, ephemeral=True)

# Information command

@bot.tree.command(name="info", description="Everything about this bot")
@app_commands.describe(who = "Info about bot or devs.")

async def info(interaction: discord.Interaction, who: str):

#Bot Information

    if who == "bot":
        embed = discord.Embed(title="About Me", url="https://discord.com/api/oauth2/authorize?client_id=1128324445178708028&permissions=8&scope=bot", description="Hoshino AI Bot is not your average chatbot, it's been meticulously crafted to simulate human-like interactions.\n\nDeveloped with ❤ by みかず / Yourby", color=0x33DBFF)
        embed.set_author(name="Hoshino AI", url="https://oshinoko.fandom.com/wiki/Ai_Hoshino", icon_url="https://i.ibb.co/dbTN84p/flat-750x-075-f-pad-750x1000-f8f8f8-removebg-preview.png")
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
 
@bot.tree.command(name="say", description= "Type hello or kabar")
@app_commands.describe(say_anything = "say hello, kabar")
async def say(interaction: discord.Interaction, say_anything: str,):
    if say_anything == "hello":
        await interaction.response.send_message(f'Aloo, {interaction.user.mention}')
    elif say_anything == "kabar":
        await interaction.response.send_message(f'Ya begitulah, {interaction.user.mention} gimana?')
    else:
        await interaction.response.send_message(f'Ngomong apa dah {interaction.user.mention}')

# Invite bot to other server command

@bot.tree.command(name="invite", description="Create invite for bot")
async def invite(interaction: discord.Interaction):
    embed = discord.Embed(title="Invite Me (Click Here!)", url="https://discord.com/api/oauth2/authorize?client_id=1128324445178708028&permissions=8&scope=bot", description= f"Hey {interaction.user.mention}, Invite me to your server!", color=0xF8ED62)
    embed.set_author(name="Hoshino AI", icon_url="https://i.ibb.co/w6q0WDY/Screenshot-238.png")
    embed.set_thumbnail(url="https://i.ibb.co/0YxJJN6/ai-hoshino-removebg-preview.png")
    await interaction.response.send_message(embed=embed)