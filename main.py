import discord
from discord.ext import commands
import music


cogs = [music]


client = commands.Bot(command_prefix="kas?", intents = discord.Intents.all())

for i in range(len(cogs)):
    cogs[i].setup(client)

client.run(ENTER TOKEN HERE)

