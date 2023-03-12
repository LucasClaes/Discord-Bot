import discord
from User_Id import *
from Token import TOKEN
from discord import app_commands
from discord.ext import commands

def Main():
    bot = commands.Bot(command_prefix="!", intents=discord.Intents.all())

    @bot.event
    async def on_ready():
        print("Bot Online")
        await bot.change_presence(activity=discord.Game(name="/spam"))
        try:
            synced = await bot.tree.sync()
            print(f"Synced {len(synced)} command(s)")
        except Exception as e:
            print(e)

    @bot.tree.command(name="spam")
    @app_commands.describe(persoon="Welke persoon ik moet spammen")
    @app_commands.describe(keer="Hoeveel keer ik deze persoon moet spammen")
    async def spam(interaction: discord.Interaction, persoon: str, keer: int):
        await interaction.response.send_message(f"Spamming {persoon} {keer}x",ephemeral =True)
        user = user_ids.get(persoon.lower())
        if user is None:
            await interaction.response.send_message(f"Unknown person: {persoon}")
            return
        channel = interaction.channel
        for i in range(keer):
            await channel.send(f"<@{user}>")

    bot.run(TOKEN)

if __name__ == '__main__':
    Main()
