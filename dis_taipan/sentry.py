"""
Sets up a Sentry Logger
"""
from typing import Any
import logging
from dis_snek import Snake
import sentry_sdk
import os

def sentry_filter(event: dict[str, Any], hint: dict[str, Any]):  # type: ignore
    if 'log_record' in hint:
        record: logging.LogRecord = hint['log_record']
        if 'dis.snek' in record.name and '/commands/permissions: 403' in record.message:
            return None

    if 'exc_info' in hint:
        exc_type, exc_value, tb = hint['exc_info']
        if isinstance(exc_value, OSError):
            return None
    return event

def setup(bot: Snake) -> None:
    token = os.environ.get('SENTRY_TOKEN')
    if not token:
        logging.error('Sentry token not found, disabling sentry')
    sentry_sdk.init(token, before_send=sentry_filter)
