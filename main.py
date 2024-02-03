"""Entrypoint module, instantiates the bot and
   subscribes to gateway events."""
import os
import re

import discord

from pattern import PATTERN


class MyClient(discord.Client):
    """The bot's instance."""
    async def on_ready(self):
        """Fires when the bot is ready to receive gateway events."""
        print(f'Logged on as {self.user}')

    async def on_message(self, message):
        """Fires when the bot receives a MESSAGE_CREATE event.
           Checks if the message is in the promo channel, then validates links."""
        if message.author.bot:
            return
        if message.channel.id == int(os.environ.get("CHANNEL_ID")):
            if (message.author.guild_permissions.manage_messages
                    or message.author.guild_permissions.administrator):
                return
            print("Found message in right channel")
            if not re.search(PATTERN, message.content):
                await message.reply(
                    "So sorry, but only `twitch.tv` and `kick.com` "
                    + "links are allowed in this channel."
                )
                await message.delete()
                webhook = discord.Webhook.from_url(
                    os.environ.get("WH_URL"), client=self)
                await webhook.send(
                    content=f"Deleted message for failing link test:\n\n> {message.content}"
                )


intents = discord.Intents.default()
intents.message_content = True

client = MyClient(intents=intents)
client.run(os.environ.get("BOT_TOKEN"))
