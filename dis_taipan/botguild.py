import os
from typing import Optional

from naff import Guild, PartialEmoji, Extension, Client


class SelfGuild(Extension):
    async def get_server(self) -> Guild:
        for guild in self.bot.guilds:
            if guild.name == self.bot.user.username:
                return guild
        return await Guild.create(self.bot.user.username, self.bot)

    async def get_emoji(self, name: str) -> Optional[PartialEmoji]:
        # Get an emoji by name.
        try:
            name = name.replace(" ", "_")
            if self.bot.cache.emoji_cache is None:
                self.bot.cache.emoji_cache = {}
                await (await self.get_server()).fetch_all_custom_emojis()
            for emoji in self.bot.cache.emoji_cache.values():
                if emoji.name == name:
                    return emoji
        except Exception as e:
            await self.bot.on_error("botguild.get_emoji", e)
            return None

        path = os.path.join("emoji_images", name + ".png")
        if not os.path.exists(path):
            await self._fetch_emoji_image(name, path)
        if not os.path.exists(path):
            raise FileNotFoundError(f"Emoji image {path} not found")

        guild = await self.get_server()
        print(f"Uploading {name} to {guild.name}")
        with open(path, "rb") as f:
            return await guild.create_custom_emoji(name=name, imagefile=f)

    async def _fetch_emoji_image(self, name: str, path: str) -> None:  # noqa
        """Virtual method that can be overridden to fetch an emoji from an external source."""
        ...


def setup(bot: Client) -> None:
    if not os.path.exists("emoji_images"):
        os.mkdir("emoji_images")
    SelfGuild(bot)
