from __future__ import annotations

from typing import TYPE_CHECKING

import donphan  # type: ignore

from discord.ext import commands

if TYPE_CHECKING:
    from .bot import Bot

__all__ = ("Context",)


class Context(commands.Context):
    bot: Bot

    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs)  # type: ignore
        self.db = donphan.MaybeAcquire(pool=self.bot.pool)