import discord
import os

client = discord.Client()

@client.event
async def on_ready():
    print('We heve logged in as {0.user}'.format(client))
    activity = discord.Game(name="Alpha")
    await client.change_presence(status=discord.Status.idle, activity=activity)
    
@client.event
async def on_message(msg):
    if msg.content.startswith('.move'):           
        try:
            await msg.author.voice.channel.connect()
            await msg.channel.send("Channel: " + msg.channel.name + "\nJoining...")
        except:
            await msg.channel.send("{} Join to channel first".format(msg.author.mention))
       
client.run(str(os.environ.get('BOT_TOKEN')))
