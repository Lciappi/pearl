import os
import discord
import time
import asyncio

from discord.ext import commands
from dotenv import load_dotenv
from datetime import datetime, timedelta
from message_handler import MessageHandler


# Load environment variables from .env
load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")

intents = discord.Intents.default()
intents.message_content = True
intents.members = True 

# Initialize the bot with intents
bot = commands.Bot(command_prefix="!", intents=intents)
message_handler = MessageHandler(bot)

async def execute_at_specific_time(target_date, target_time, func, user):
    target_datetime = datetime.strptime(f"{target_date} {target_time}", "%Y-%m-%d %H:%M:%S")
    current_datetime = datetime.now()
    time_diff = (target_datetime - current_datetime).total_seconds()

    if time_diff > 0:
        print(f"Waiting until {target_datetime} to execute the function...")
        await asyncio.sleep(time_diff)

    await func(user)

async def send_message(user):
    await message_handler.send_custom_message(1303271594881454143, user, "remind")

@bot.event
async def on_ready():
    print("Bot is ready")
    #TODO: update channel id
    await message_handler.send_welcome_message(1303271594881454143)

    schedule = [    
        ("2024-11-11", "02:44:00"),
        ("2024-11-11", "02:44:15"),
        ("2024-11-11", "02:44:30"),
        ("2024-11-11", "02:44:35"),
        ("2024-11-11", "02:44:40"),
        ("2024-11-11", "02:44:45"),
    ]

    users = ['267033445883052053', '361260852772339712', '812851217834967100']
    last_user = 0

    for target_date, target_time in schedule:
        await execute_at_specific_time(target_date, target_time, send_message, users[last_user])
        last_user = (last_user + 1) % len(users)

def main():
    bot.run(TOKEN)

if __name__ == "__main__":
    main()
