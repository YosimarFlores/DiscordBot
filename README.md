# Discord Bot - Command and Reaction Bot 🤖

This Discord bot is built using Python and the `discord.py` library. It demonstrates basic functionalities such as handling simple slash commands and responding to user messages and reactions.

## Features

### 1. **Slash Commands**
    The bot supports the following slash commands:
   
     - `/hello`: Responds with a friendly "Hi there!" message.
     - `/printer <text>`: Echoes back the text that the user provides. For example, if you type `/printer Hello World`, the bot will respond with "Hello World".

### 2. **Message Reactions**
   - The bot listens for message reactions. When a user reacts to a message, the bot sends a message in the same channel saying "You reacted".

### 3. **Keyword Responses**
    The bot automatically responds to specific keywords in user messages:
    
     - If a message starts with "hello", it will reply with "Hi there {user}".
     - If a message starts with "how are you", it will reply with "Not bad!".

## Requirements

- Python 3.8 or higher
- Install the required dependencies:
  
  ```
  pip install discord.py python-dotenv
  Setup
  ```
## Setup

1. Clone this repository or copy the code into your local machine.

2. Create a .env file in the project root directory, and add your Discord bot token:
```
DISCORD_TOKEN=your-bot-token-here
```

3. Update the bot with your server (guild) ID: In the code, replace 123456789012345678 with your actual Discord server's (guild's) ID.
```
GUILD_ID = discord.Object(id=123456789012345678)  # Replace with your actual guild ID
```

4. Enable the Message Content Intent: To ensure the bot can read the content of messages, go to the Discord Developer Portal, select your bot, and enable the Message Content Intent under the "Bot" settings.

5. Run the bot:
```
python bot.py
```
## Usage

### Once the bot is running, you can interact with it in your Discord server:

- Use the /hello slash command to receive a friendly greeting.
- Use the /printer <text> slash command to make the bot repeat anything you type.
- Type "hello" or "how are you" in the chat to trigger automatic responses.
- React to messages to see the bot's response to reactions.

## Notes

- The bot only syncs commands to a specific guild (server) for quick testing during development. If you want to deploy it globally, you can modify the sync logic to sync commands globally, but this may take up to an hour - for changes to propagate.
- Make sure your bot has the necessary permissions to send messages, manage reactions, and use slash commands in your server.



