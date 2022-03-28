"""
Things to make static typing easier.
"""
from io import IOBase
from pathlib import Path
from typing import Any, List, Optional, Protocol, Union, runtime_checkable

from dis_snek import Snake
from dis_snek.models import (TYPE_MESSAGEABLE_CHANNEL, AllowedMentions,
                             BaseComponent, Embed, File, Guild, Member,
                             Message, MessageFlags, MessageReference,
                             Snowflake_Type, Sticker, User)

__all__ = ['SendableContext']


@runtime_checkable
class SendableContext(Protocol):
    """
    A protocol that supports any context that can send messages.
    """

    channel: TYPE_MESSAGEABLE_CHANNEL
    invoked_name: str

    author: Union[Member, User]
    guild_id: Snowflake_Type
    message: Message

    @property
    def bot(self) -> Snake:
        ...

    @property
    def guild(self) -> Optional["Guild"]:
        ...

    async def send(
        self,
        content: Optional[str] = None,
        embeds: Optional[
            Union[List[Union["Embed", dict]], Union["Embed", dict]]
        ] = None,
        components: Optional[
            Union[
                List[List[Union["BaseComponent", dict]]],
                List[Union["BaseComponent", dict]],
                "BaseComponent",
                dict,
            ]
        ] = None,
        stickers: Optional[
            Union[List[Union["Sticker", "Snowflake_Type"]], "Sticker", "Snowflake_Type"]
        ] = None,
        allowed_mentions: Optional[Union["AllowedMentions", dict]] = None,
        reply_to: Optional[
            Union["MessageReference", "Message", dict, "Snowflake_Type"]
        ] = None,
        file: Optional[Union["File", "IOBase", "Path", str]] = None,
        tts: bool = False,
        flags: Optional[Union[int, "MessageFlags"]] = None,
        **kwargs: Any,
    ) -> "Message":
        ...
