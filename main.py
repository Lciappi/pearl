import discord
from discord.ext import commands
from message_handler import MessageHandler
import os
from dotenv import load_dotenv
import asyncio
from datetime import datetime, timedelta

# Load environment variables from .env
load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")

intents = discord.Intents.default()
intents.message_content = True
intents.members = True 

# Initialize the bot with intents
bot = commands.Bot(command_prefix="!", intents=intents)
message_handler = MessageHandler(bot)

@bot.event
async def on_ready():
    print("Bot is ready")
    #TODO: update channel id
    await message_handler.send_welcome_message(1305347901416800336)
    bot.loop.create_task(trash_reminder())

async def trash_reminder():
    #TODO: update users
    users = ['267033445883052053', '267033445883052053', '267033445883052053']
    last_user = 0

    print("Reminding the next user to take out the trash.")
    user = users[last_user]
    last_user = (last_user + 1) % len(users)
    
    await message_handler.send_custom_message(1305347901416800336, user, "remind")
    await asyncio.sleep(5)  # Wait 5 seconds before the next reminder

if __name__ == "__main__":
    bot.run(TOKEN)
