
error = 0
debug = True

#Libraries laden
import colorama
from colorama import Fore

#Token Importen
try:
    from Token import TOKEN
except Exception as e:
    if debug is True:
        print(e)
        print(Fore.RED + "Encountered an issue while loading token.")
        error += 1
    else:
        print(Fore.RED + "Encountered an issue while loading token.")
        error += 1


try:
    import discord
    from discord import app_commands
    from discord.ext import commands
except Exception as e:
    if debug is True:
        print(e)
        print(Fore.RED + "Encountered an issue while loading discord library.")
        error += 1
    else:
        print(Fore.RED + "Encountered an issue while loading discord library.")
        error += 1


#Main loop
def Main():
    bot = commands.Bot(command_prefix="!", intents=discord.Intents.all())

    @bot.event
    async def on_ready():
        print("Bot Online")
        await bot.change_presence(activity=discord.Game(name="/spam"))
        try:
            synced = await bot.tree.sync()
            print(f"Synced {len(synced)} command(s)")
            if debug is True:
                print(synced)
        except Exception as e:
            print(e)

    @bot.tree.command(name="spam")
    @app_commands.describe(persoon="Welke persoon ik moet spammen.")
    @app_commands.describe(keer="Hoeveel keer ik deze persoon moet spammen.")
    async def spam(interaction: discord.Interaction, persoon: str, keer: int):
        await interaction.response.send_message(f"Spamming {persoon} {keer}x",ephemeral =True)
        channel = interaction.channel
        print(f"Spamming {str(persoon)} {keer}x requested by @{interaction.user.name}.")
        for i in range(keer):
            await channel.send(f"{persoon}")

    @bot.tree.command(name="clear")
    @app_commands.describe(ammount="Hoeveel berichten ik moet verwijderen")
    async def clear(interaction: discord.Interaction, ammount: int):
        await interaction.response.send_message(f"Clearing {ammount} bericht.",ephemeral =True)
        await interaction.channel.purge(limit=ammount)


    @bot.event
    async def on_message(message):
        await bot.process_commands(message)
        if message.author.id == 1084555252365283441 and "@" in message.content.lower():
            try:
                await message.delete()
            except Exception as e:
                if debug is True:
                    print(e)
                else:
                    print("Non fatal error occured while deleting a message")
    

    bot.run(TOKEN)

if error > 0:
    print(f"Aborting startup {error} error(s)")
elif __name__ == '__main__':
    print(Fore.GREEN + "No errors while loading\nContinuing to startup")
    Main()
