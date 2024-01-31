from dotenv import load_dotenv
load_dotenv()

import discord
import os
import re
from pattern import pattern

class MyClient(discord.Client):
    async def on_ready(self):
        print(f'Logged on as {self.user}')

    async def on_message(self, message):
        if (message.author.bot):
            return
        if message.channel.id == 1202280249128386610:
            print("Found message in right channel")
            if re.search(pattern, message.content):
              await message.add_reaction("💜")
            else:
              await message.reply("So sorry, but only `twitch.tv` and `kick.com` links are allowed in this channel.")
              await message.delete()
              webhook = discord.Webhook.from_url(os.environ.get("WH_URL"), client=self)
              await webhook.send(content=f"Deleted message for failing link test:\n\n> {message.content}")

intents = discord.Intents.default()
intents.message_content = True

client = MyClient(intents=intents)
client.run(os.environ.get("BOT_TOKEN"))