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
async def on_message(msg):
		if message.author == client.user:
			return
        try:
    		if mmsg.content.startwith('$!join'): 
                if msg.voice_client is None:
                    if msg.author.voice:
    			         await msg.author.voice.channel.connect()
                    else:
                         await msg.channel.send('You are not connected to a voice channel.')
        except:
            await msg.channel.send('Aint')
@client.event
async def on_member_join(self, member):
        guild = member.guild
        if guild.system_channel is not None:
            to_send = 'Welcome {0.mention} to {1.name}!'.format(member, guild)
            await guild.system_channel.send(to_send)
                
client.run(str(os.environ.get('BOT_TOKEN')))
