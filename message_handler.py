import discord
from discord.utils import get
import asyncio
import random

cleaned_messages = [
    " te toca sacar la basura chato",
    " você tem que tirar o basura irmao",
    " habla mano, saca la basura",
    " hoy es el dia en el que todos tus pecados seran absueltos si sacas la basura",
    " saca la basura o te mato",
    " tengo a toda tu familia de rehen, saca la basura",
    " la basura te llama, sacala",
    " la gente que saca la basura tiene el pito enorme",
    " basura o clock",
    " si la basura llama yo le voy a llegar",
]

cleaned_reminder = [
    " mano todavia no sacas la basura? que esperas",
    " saca la basura o te mato",
    " mano saca la basura y no te quedes ahi parado porque sino el camion te va a llevar a ti tambien",
    " si no sacas la basura nuestras vecinX te van a castigar",
    " todavia no haz sacado la basura? hazlo por Diane",
]

class MyView(discord.ui.View):
    def __init__(self, completed):
        super().__init__()
        self.completed = completed

    @discord.ui.button(label="Ya la saque!", style=discord.ButtonStyle.success)
    async def button_callback(self, interaction: discord.Interaction, button: discord.ui.Button):
        self.completed[0] = True
        await interaction.response.send_message("Buena crack, hiciste mas que harchi en su vida", ephemeral=True)
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
            await channel.send("Ke e lo q e mamabishos")
        else:
            print("Channel not found")
    
    def get_encouraging_message(self, b_reminder):
        """Get a random encouraging message."""
        return random.choice(cleaned_messages) if not b_reminder else random.choice(cleaned_reminder)

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
                message = f"{user.mention},{self.get_encouraging_message(False)}"
                button_view = MyView(self.completed)
                await channel.send(message, view=button_view)
                await asyncio.sleep(3600)
                if not self.completed[0]:
                    await channel.send(f"{user.mention},{self.get_encouraging_message(True)}")
            else:
                print(f"User with ID {user_id} not found in the server.")
        else:
            print("Channel not found")
