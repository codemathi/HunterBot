import discord
import os

client = discord.Client()

@client.event
async def on_ready():
    print('We heve logged in as {0.user}'.format(client))
    activity = discord.Game(name="Beta BOT v1")
    await client.change_presence(status=discord.Status.idle, activity=activity)
    
@client.event
async def on_message(msg):
    if msg.content.startswith('.move'):
        try:
            vc = await msg.author.voice.channel.connect()
            #vc.play(discord.FFmpegPCMAudio(executable="C:/ffmreg/bin/ffmpeg.exe", source="C:/Users/Assil/Desktop/follow/testing.mp3"), after=lambda e: print('done', e), volume=100)
            vc.is_playing()
        except: await msg.channel.send('Aint')   
       
client.run(str(os.environ.get('BOT_TOKEN')))
