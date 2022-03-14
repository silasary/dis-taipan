from io import IOBase
from pathlib import Path
from typing import Any, List, Optional, Protocol, Union, runtime_checkable

from dis_snek import Snake
from dis_snek.models import (TYPE_MESSAGEABLE_CHANNEL, AllowedMentions, BaseComponent, Embed, File, Member, Message,
                             MessageFlags, MessageReference, Snowflake_Type, Sticker, User)


@runtime_checkable
class SendableContext(Protocol):
    channel: TYPE_MESSAGEABLE_CHANNEL
    bot: Snake
    invoked_name: str

    author: Union[Member, User]
    guild_id: Snowflake_Type
    message: Message

    async def send(
        self,
        content: Optional[str] = None,
        embeds: Optional[Union[List[Union['Embed', dict]], Union['Embed', dict]]] = None,
        components: Optional[
            Union[List[List[Union['BaseComponent', dict]]], List[Union['BaseComponent', dict]], 'BaseComponent', dict]
        ] = None,
        stickers: Optional[Union[List[Union['Sticker', 'Snowflake_Type']], 'Sticker', 'Snowflake_Type']] = None,
        allowed_mentions: Optional[Union['AllowedMentions', dict]] = None,
        reply_to: Optional[Union['MessageReference', 'Message', dict, 'Snowflake_Type']] = None,
        file: Optional[Union['File', 'IOBase', 'Path', str]] = None,
        tts: bool = False,
        flags: Optional[Union[int, 'MessageFlags']] = None,
        **kwargs: Any,
    ) -> 'Message':
        ...
