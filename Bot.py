import discord
from discord.ext import commands
import traceback
import sys

intents = discord.Intents.all()
intents.members = True

#intents = discord.Intents.default()
#intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

bot.remove_command("help")

#DISCORD_TOKEN = 'NzQ4NjY4NTI3NDU5ODI3ODcy.GlkWFZ.ClR9ghxb8rssNeSjEXr3JPqDuBBQPyxIyB3GIU'

initial_extensions = ['cogs.voice']

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')
    
    for extension in initial_extensions:
        try:
            await bot.load_extension(extension)
            print(f'Loaded {extension}')
        except Exception as e:
            print(f'Failed to load extension {extension}.', file=sys.stderr)
            traceback.print_exc()

bot.run('MTA3Nzk3OTQwOTg0NTMzMDAzMQ.GyMJGf.fd5JCk-nUjH0gA0Ms5f0BxzjqtDT3TQNSXQx3M')
