import discord
import os

client = discord.Client()

@client.event
async def on_ready():
        print('We heve logged in as {0.user}'.format(client))
@client.event
async def on_message_delete(message):
        if message.author == client.user:
                return

        await message.channel.send('{}: {}'.format(message.author.mention, message.content))
                
client.run(str(os.environ.get('BOT_TOKEN')))
