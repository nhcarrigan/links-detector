"""Regex to check if the string contains a twitch.tv or kick.com link."""
PATTERN = r'(?i)\b(?:https?://)?(?:www\.)?(?:twitch\.tv|kick\.com)(?:/[^\s]+)\b'
