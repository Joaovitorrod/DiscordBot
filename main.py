import discord
from discord.ext import commands,tasks
from random import choice
import os
from keep_alive import keep_alive

token = os.environ['TOKEN']

intents = discord.Intents.default()
intents.members = True

testing = False

client = commands.Bot(command_prefix = "$", case_insensitive = True, intents=intents,strip_after_prefix=True)

client.remove_command('help')

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')


status = ['$help', 'Baguncinha RULEZ', 'Vendo os crimes no lol']
@tasks.loop(seconds=360)
async def change_status():
  await client.change_presence(activity=discord.Game(choice(status)))

@client.event
async def on_ready():
    change_status.start()
    print('Entramos como {0.user}'.format(client))

    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="músicas"))

keep_alive()
client.run(token)



