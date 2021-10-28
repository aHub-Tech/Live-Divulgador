from dotenv import load_dotenv
from os import getenv

from bot.twitter.client import ClientKeys, TweetMetadata, TwitterClient
from bot.handlers.verify_online_streamers import VerifyOnlineStreamers

load_dotenv()


CONSUMER_KEY_A = getenv("CONSUMER_KEY_A")
CONSUMER_SECRET_A = getenv("CONSUMER_SECRET_A")
ACCESS_TOKEN_A = getenv("ACCESS_TOKEN_A")
ACCESS_TOKEN_SECRET_A = getenv("ACCESS_TOKEN_SECRET_A")

TWITCH_CLIENT_ID = getenv("CLIENT_ID")
TWITCH_CLIENT_SECRET = getenv("CLIENT_SECRET")

from logging import getLogger

logger = getLogger(__name__)


class PostTweet:
    client_keys = ClientKeys(
        CONSUMER_KEY_A, CONSUMER_SECRET_A, ACCESS_TOKEN_A, ACCESS_TOKEN_SECRET_A
    )

    twitter_client = TwitterClient(client_keys)

    @classmethod
    def handle(cls) -> None:
        try:
            data = VerifyOnlineStreamers.handle()
            logger.info("Tweeting about `data`")
            cls.tweet(data)
        except Exception as e:
            logger.error(e)
            raise e

    @classmethod
    def set_tweet_metadata(cls, data: dict):
        user_name = data["user_name"]
        live_title = data["title"]
        twitch_channel = f"https://twitch.tv/{data['user_name']}"
        tags = "#Twitch #live"
        thumbnail = ""

        cls.tweet_metadata = TweetMetadata(
            twitter_display_name=user_name,
            twitch_channel=twitch_channel,
            twitch_stream_title=live_title,
            tags=tags,
            thumbnail=thumbnail,
        )

    @classmethod
    def tweet(cls, live_list: list[dict]) -> None:
        for live in live_list:
            cls.set_tweet_metadata(live)
            cls.twitter_client.send_tweet(cls.tweet_metadata)
