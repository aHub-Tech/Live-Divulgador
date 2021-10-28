from bot.live_divulgator import LiveDivulgator
from logging import getLogger

logger = getLogger(__name__)


def main():
    logger.warning("Starting Live Divulgator bot")
    LiveDivulgator.run()


if __name__ == "__main__":
    main()
