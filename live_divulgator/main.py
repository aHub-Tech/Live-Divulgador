from live_divulgator.bots.live_divulgator import LiveDivulgator
from logging import getLogger
from live_divulgator.plugins.twitter import TwitterPlugin

logger = getLogger(__name__)


def main():
    logger.warning("Starting Live Divulgator bot")

    config = [TwitterPlugin]

    live_divulgator = LiveDivulgator(config)
    live_divulgator.run()


if __name__ == "__main__":
    main()
