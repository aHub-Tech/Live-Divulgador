from src.bot.live_divulgator import LiveDivulgator
from logging import getLogger
from src.bot.plugins.twitter import TwitterPlugin

logger = getLogger(__name__)


def main():
    logger.warning("Starting Live Divulgator bot")

    config = [TwitterPlugin]

    live_divulgator = LiveDivulgator(config)
    live_divulgator.run()


if __name__ == "__main__":
    main()
