import os
from dotenv import load_dotenv
from discord.ext import commands
import discord

load_dotenv()

TOKEN = os.getenv("BOT_TOKEN")
bot = commands.Bot(command_prefix="/", intents=discord.Intents.all())

@bot.event
async def on_ready():
    print("I'm ready for action, or breaking, whichever comes first.")

bot.run(TOKEN)