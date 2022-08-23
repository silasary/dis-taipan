"""
Sets up a Sentry Logger

To install, either set an environment variable called SENTRY_TOKEN, or put a string in the sentry_token attribute of your bot,
And then call `bot.load_extension('dis_taipan.sentry')`

This will be depreciated in favour of `naff.ext.sentry`

"""
import logging
import os
from typing import Any, Optional

import sentry_sdk
from naff import Client, Extension, listen


def sentry_filter(event: dict[str, Any], hint: dict[str, Any]) -> Optional[dict[str, Any]]:
    if "log_record" in hint:
        record: logging.LogRecord = hint["log_record"]
        if "dis.snek" in record.name:
            if ": 403" in record.message:
                return None
            if record.message.startswith("Ignoring exception in "):
                return None

    if "exc_info" in hint:
        exc_type, exc_value, tb = hint["exc_info"]
        if isinstance(exc_value, OSError):
            return None
    return event


_default_error_handler = Client.default_error_handler


class SentryScale(Extension):
    @listen()
    async def on_startup(self) -> None:
        sentry_sdk.set_context(
            "bot",
            {
                "name": str(self.bot.user),
                "intents": repr(self.bot.intents),
            },
        )
        sentry_sdk.set_tag("bot_name", str(self.bot.user))

    @staticmethod
    def default_error_handler(source: str, error: BaseException) -> None:
        with sentry_sdk.configure_scope() as scope:
            scope.set_tag("source", source)
            sentry_sdk.capture_exception(error)
        _default_error_handler(source, error)

    setattr(Client, 'default_error_handler', default_error_handler)  # noqa: B010


def setup(bot: Client) -> None:
    token = os.environ.get("SENTRY_TOKEN")
    if not token:
        token = getattr(bot, "sentry_token", None)
    if not token:
        logging.error("Sentry token not found, disabling sentry")
        return
    sentry_sdk.init(token, before_send=sentry_filter)
    SentryScale(bot)
