
#disctionary met user id's importen van 'User_Id.py'
from User_Id import *
#Token Importen
from Token import TOKEN


import discord
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
    @app_commands.describe(persoon="Welke persoon ik moet spammen.")
    @app_commands.describe(keer="Hoeveel keer ik deze persoon moet spammen.")
    async def spam(interaction: discord.Interaction, persoon: str, keer: int):
        await interaction.response.send_message(f"Spamming {persoon} {keer}x",ephemeral =True)
        user = user_ids.get(persoon.lower())
        if user is None:
            await interaction.response.send_message(f"Unknown person: {persoon}", )
            return
        channel = interaction.channel
        print(f"Spamming {persoon} {keer}x in opdracht van {interaction.user.name}.")
        for i in range(keer):
            await channel.send(f"<@{user}>")

    @bot.tree.command(name="clear")
    @app_commands.describe(ammount="Hoeveel berichten ik moet verwijderen")
    async def clear(interaction: discord.Interaction, ammount: int):
        await interaction.response.send_message(f"Clearing {ammount} bericht.",ephemeral =True)
        await interaction.channel.purge(limit=ammount)


    @bot.event
    async def on_message(message):
        await bot.process_commands(message) # add this if also using command decorators
        if message.author.id == 1084555252365283441 and "@" in message.content.lower():
            await message.delete()


    bot.run(TOKEN)

if __name__ == '__main__':
    Main()
