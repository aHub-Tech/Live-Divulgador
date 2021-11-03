from logging import getLogger
from typing import Callable

from src.bot.handlers.post_tweet import PostTweet
from src.bot.plugins.plugin import Plugin

logger = getLogger(__name__)


class TwitterPlugin(Plugin):
    @staticmethod
    def run():
        logger.info("Running twitter plugin")
        PostTweet.handle()
