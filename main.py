"""Entrypoint module, instantiates the bot and
   subscribes to gateway events."""
import os
import re

import discord

from pattern import LINKS, PATTERN


class MyClient(discord.Client):
    """The bot's instance."""
    async def on_ready(self):
        """Fires when the bot is ready to receive gateway events."""
        print(f'Logged on as {self.user}')

    async def on_message(self, message: discord.Message):
        """Fires when the bot receives a MESSAGE_CREATE event.
           Checks if the message is in the promo channel, then validates links."""
        if message.author.bot:
            return
        if message.channel.id == int(os.environ.get("CHANNEL_ID")):
            if (message.channel.permissions_for(message.author).manage_messages
                    or message.channel.permissions_for(message.author).administrator):
                return
            print("Found message in right channel")
            valid_links = len(re.findall(PATTERN, message.content))
            invalid_links = len(re.findall(LINKS, message.content))
            if invalid_links > valid_links:
                await message.reply(
                    content="So sorry, but only `twitch.tv` and `kick.com`"
                    + " links are allowed in this channel."
                )
                await message.delete()
                webhook = discord.Webhook.from_url(
                    os.environ.get("WH_URL"), client=self)
                quoted = message.content.replace('\n', '\n> ')
                await webhook.send(
                    content="Deleted message for failing link test:"
                    + f"\n\n> {quoted}"
                    + f"\n- Links found: {invalid_links}"
                    + f"\n- Valid links: {valid_links}"
                )

    async def on_message_edit(self, _old: discord.Message, message: discord.Message):
        """Fires when the bot receives a MESSAGE_EDIT event.
           Checks if the message is in the promo channel, then validates links."""
        if message.author.bot:
            return
        if message.channel.id == int(os.environ.get("CHANNEL_ID")):
            if (message.channel.permissions_for(message.author).manage_messages
                    or message.channel.permissions_for(message.author).administrator):
                return
            print("Found message in right channel")
            valid_links = len(re.findall(PATTERN, message.content))
            invalid_links = len(re.findall(LINKS, message.content))
            if invalid_links > valid_links:
                await message.reply(
                    content="So sorry, but only `twitch.tv` and `kick.com`"
                    + " links are allowed in this channel."
                )
                await message.delete()
                webhook = discord.Webhook.from_url(
                    os.environ.get("WH_URL"), client=self)
                quoted = message.content.replace('\n', '\n> ')
                await webhook.send(
                    content="Deleted message for failing link test:"
                    + f"\n\n> {quoted}"
                    + f"\n- Links found: {invalid_links}"
                    + f"\n- Valid links: {valid_links}"
                )


intents = discord.Intents.default()
intents.message_content = True

client = MyClient(intents=intents)
client.run(os.environ.get("BOT_TOKEN"))
