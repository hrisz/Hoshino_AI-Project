import discord
from discord import app_commands
from discord.ext import commands

intents = discord.Intents.default()
intents.members = True
intents.message_content = True

# Command prefix for bot

bot = commands.Bot(command_prefix='/', intents=intents)

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