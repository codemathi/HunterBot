import discord
import os

client = discord.Client()
#Ready eveny
@client.event
async def on_ready():
        print('We heve logged in as {0.user}'.format(client))
        activity = discord.Game(name="Beta BOT")
        await client.change_presence(status=discord.Status.idle, activity=activity)
#Message on delete
@client.event
async def on_message_delete(message):
        if message.author == client.user:
                return

        await message.channel.send('[DELETED]{}: {}'.format(message.author.mention, message.content))
                
client.run(str(os.environ.get('BOT_TOKEN')))
