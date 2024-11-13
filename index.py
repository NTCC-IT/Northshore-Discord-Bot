# This file was converted from index.js from discord.js

import discord
import re
import os
from discord.ext import commands
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Regular expression for URL detection
url_regex = re.compile(r"(https?:\/\/[^\s]+)")

# Set intents
intents = discord.Intents.default()
intents.message_content = True
intents.guilds = True
intents.guild_messages = True
intents.guild_members = True

# Initialize bot with command prefix and intents
bot = commands.Bot(command_prefix='!', intents=intents)

# Event to signify when the bot is ready
@bot.event
async def on_ready():
    print(f'{bot.user} is ready!')
    await bot.change_presence(
        status=discord.Status.online, 
        activity=discord.Activity(type=discord.ActivityType.listening, name="Listening")
    )

# Event listener for message creation
@bot.event
async def on_message(message):
    # Ignore messages from bots
    if message.author.bot:
        return

    # Check if the message content contains a URL
    if url_regex.search(message.content):
        print('Hyperlink detected:', message.content)
        
        # Delete the message containing the hyperlink and send a response
        try:
            await message.delete()
            await message.channel.send(f'I see you posted a link!\nThat\'s not allowed! :D')
        except discord.DiscordException as e:
            print(f"Failed to delete message: {e}")

    # Ensure other commands can be processed
    await bot.process_commands(message)

# Run the bot
bot.run(os.getenv("BOT_TOKEN"))
