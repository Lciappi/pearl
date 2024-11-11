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
    ("2024-11-11", "20:00:00"),  # Reminder for Garbage Collection on 11/12/2024
    ("2024-11-17", "20:00:00"),  # Reminder for Garbage Collection on 11/18/2024
    ("2024-11-24", "20:00:00"),  # Reminder for Garbage Collection on 11/25/2024
    ("2024-12-01", "20:00:00"),  # Reminder for Garbage Collection on 12/02/2024
    ("2024-12-08", "20:00:00"),  # Reminder for Garbage Collection on 12/09/2024
    ("2024-12-15", "20:00:00"),  # Reminder for Garbage Collection on 12/16/2024
    ("2024-12-22", "20:00:00"),  # Reminder for Garbage Collection on 12/23/2024
    ("2024-12-24", "20:00:00"),  # Reminder for Garbage Collection on 12/25/2024
    ("2025-01-05", "20:00:00"),  # Reminder for Garbage Collection on 01/06/2025
    ("2025-01-19", "20:00:00"),  # Reminder for Garbage Collection on 01/20/2025
    ("2025-02-02", "20:00:00"),  # Reminder for Garbage Collection on 02/03/2025
    ("2025-02-16", "20:00:00"),  # Reminder for Garbage Collection on 02/17/2025
    ("2025-03-02", "20:00:00"),  # Reminder for Garbage Collection on 03/03/2025
    ("2025-03-16", "20:00:00"),  # Reminder for Garbage Collection on 03/17/2025
    ("2025-03-30", "20:00:00"),  # Reminder for Garbage Collection on 03/31/2025
    ("2025-04-13", "20:00:00"),  # Reminder for Garbage Collection on 04/14/2025
    ("2025-04-27", "20:00:00"),  # Reminder for Garbage Collection on 04/28/2025
    ("2025-05-11", "20:00:00"),  # Reminder for Garbage Collection on 05/12/2025
    ("2025-05-25", "20:00:00"),  # Reminder for Garbage Collection on 05/26/2025
    ("2025-06-08", "20:00:00"),  # Reminder for Garbage Collection on 06/09/2025
    ("2025-06-22", "20:00:00"),  # Reminder for Garbage Collection on 06/23/2025
    ("2025-07-06", "20:00:00"),  # Reminder for Garbage Collection on 07/07/2025
    ("2025-07-20", "20:00:00"),  # Reminder for Garbage Collection on 07/21/2025
    ("2025-08-03", "20:00:00"),  # Reminder for Garbage Collection on 08/04/2025
    ("2025-08-17", "20:00:00"),  # Reminder for Garbage Collection on 08/18/2025
    ("2025-08-31", "20:00:00"),  # Reminder for Garbage Collection on 09/01/2025
    ("2025-09-14", "20:00:00"),  # Reminder for Garbage Collection on 09/15/2025
    ("2025-09-28", "20:00:00"),  # Reminder for Garbage Collection on 09/29/2025
    ("2025-10-12", "20:00:00"),  # Reminder for Garbage Collection on 10/13/2025
    ("2025-10-26", "20:00:00"),  # Reminder for Garbage Collection on 10/27/2025
    ("2025-11-09", "20:00:00"),  # Reminder for Garbage Collection on 11/10/2025
    ("2025-11-23", "20:00:00"),  # Reminder for Garbage Collection on 11/24/2025
    ("2025-12-07", "20:00:00"),  # Reminder for Garbage Collection on 12/08/2025
    ("2025-12-21", "20:00:00"),  # Reminder for Garbage Collection on 12/22/2025
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
