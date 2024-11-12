import discord

class Client(discord.Client):
    async def on_ready(self):
        print(f'Logged on as {self.user}!')

    async def on_message(self, message):
        # Ignore messages from the bot itself
        if message.author == self.user:
            return
        print(f'Message from {message.author}: {message.content}')

# Enable intents to allow the bot to read message content
intents = discord.Intents.default()
intents.message_content = True

# Create the client with the specified intents
client = Client(intents=intents)
client.run('TYPE-YOUR-TOKEN')


