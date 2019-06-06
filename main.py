import discord

client = discord.Client()

@client.event
async def on_ready():
        print('We heve logged in as {0.user}'.format(client))
@client.event
async def on_message_delete(message):
        if message.author == client.user:
                return

        await message.channel.send('Message deleted: ')
        await message.channel.send('{}: {}'.format(message.author.mention, message.content))
                
client.run('NTc1NjE2MzM0NzU1NTI4NzE0.XOW2mA.2fWt4kXExGP2VfKZZ8UliwNWj1A')
