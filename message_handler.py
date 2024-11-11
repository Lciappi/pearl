import discord
from discord.utils import get
import asyncio

class MyView(discord.ui.View):
    def __init__(self, completed):
        super().__init__()
        self.completed = completed

    @discord.ui.button(label="Click me!", style=discord.ButtonStyle.success)
    async def button_callback(self, interaction: discord.Interaction, button: discord.ui.Button):
        self.completed[0] = True
        await interaction.response.send_message("You clicked the button!")
        button.disabled = True
        self.stop()  
        await interaction.message.edit(view=self)



class MessageHandler:
    def __init__(self, bot):
        self.bot = bot
        self.completed = [False]

    async def send_welcome_message(self, channel_id):
        """Send a welcome message to a specific channel."""
        channel = self.bot.get_channel(channel_id)
        if channel:
            await channel.send("Hello! The bot is now online and ready to assist you.")
        else:
            print("Channel not found")

    async def send_custom_message(self, channel_id, user_id, custom_logic):
        """Send a custom message based on provided logic, tagging the user."""
        channel = self.bot.get_channel(channel_id)
        if channel:
            guild = channel.guild
            user = None
            for member in self.bot.get_all_members():
                print(member.id, member.name)
                if str(member.id) == user_id:
                    user = member
                    break
            
            if user:
                message = f"{user.mention}, don't forget to complete your tasks today!"
                button_view = MyView(self.completed)
                await channel.send(message, view=button_view)
                await asyncio.sleep(8)
                if not self.completed[0]:
                    await channel.send(f"{user.mention}, you didn't complete your tasks!")
            else:
                print(f"User with ID {user_id} not found in the server.")
        else:
            print("Channel not found")
