from discord.ext import commands
import discord
import requests
from time import sleep

# paramètres généraux
prefix="emote."
token = "Nzc0MDAyNDE5NjAwMTk1NjE1.X6Rb7Q.z5GvaaEjH6QeYznkqsN-QmejwXg"
client = commands.Bot(command_prefix=prefix)
channel_id = 754468477267345500

@client.event
async def on_ready():
    print(f"Connected as " + str(client.user))

@client.event
async def on_command_error(ctx, error):
    print(error)
    if ctx.message.content.startswith("emote.emote") or ctx.message.content.startswith("emote.gif"):
        print(error)
        await ctx.message.add_reaction("<:uncheck:754491131106033764>")
        sleep(5)
        await ctx.message.delete()

@client.command()
async def emote(ctx):
    if int(ctx.channel.id) == channel_id:
        emt_id = ctx.message.content.split("<")[1].split(":")[2].replace(">", "")
        emt_name = ctx.message.content.split("``")[1].replace("``", "")
        image = requests.get(f"https://cdn.discordapp.com/emojis/{emt_id}.png")
        await client.guilds[0].create_custom_emoji(name=str(emt_name), image=image.content)
        await ctx.message.add_reaction("<:check:754491458303819776>")

@client.command()
async def gif(ctx):
    if int(ctx.channel.id) == channel_id:
        emt_id = ctx.message.content.split("<")[1].split(":")[2].replace(">", "")
        emt_name = ctx.message.content.split("``")[1].replace("``", "")
        image = requests.get(f"https://cdn.discordapp.com/emojis/{emt_id}.gif")
        await client.guilds[0].create_custom_emoji(name=str(emt_name), image=image.content)
        await ctx.message.add_reaction("<:check:754485575993786468>")

client.run(token)