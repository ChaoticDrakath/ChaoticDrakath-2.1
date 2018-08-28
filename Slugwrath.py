import disco
import asyncio
import json
import os
from discord.ext import commands

client = discord.Client()

@client.event
async def on_ready():
    print('bot online')
  
@client.event
async def on_member_join(member):
    ...
  
@client.event
async def on_message(message):
    ...
   
client.run(os.getenv('Token.'))
