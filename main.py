import os
import discord
import dotenv
from discord.ext import commands
from discord import app_commands

dotenv.load_dotenv()

class Client(commands.Bot):
    async def on_ready(self):
        print(f'Logged on as {self.user}!')

        try:
            guild = discord.Object(id=YOUR-DISCORD-ID)
            synced = await self.tree.sync(guild=guild)
            print(f"Synced {len(synced)} commands to guild {guild.id}")
        except Exception as e:
            print(f"Error syncing commands: {e}")
                

    async def on_message(self, message):
        if message.author == self.user:
            return
        if message.content.startswith('hello'):
            await message.channel.send(f'Hi there {message.author}')
        if message.content.startswith('how are you'):
            await message.channel.send(f'Not bad!')
    
    async def on_reaction_add(self, reaction, user):
        await reaction.message.channel.send('You reacted')


GUILD_ID = discord.Object(id=YOUR-DISCORD-ID)

intents = discord.Intents.default()
intents.message_content = True
client = Client(command_prefix="!", intents=intents)

@client.tree.command(name="hello", description="Say hello!", guild=GUILD_ID)
async def sayHello(Interaction: discord.Interaction):
    await Interaction.response.send_message("Hi there!")

@client.tree.command(name="printer", description="I will print wathever you give me!", guild=GUILD_ID)
async def printer(Interaction: discord.Interaction, printer: str):
    await Interaction.response.send_message(printer)

token = os.getenv('DISCORD_TOKEN')
if token is None:
    print("Error: DISCORD_TOKEN not found in environment variables.")
else:
    client.run(token)

