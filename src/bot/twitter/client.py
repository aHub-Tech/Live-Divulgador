import logging
from dataclasses import dataclass
from yaml import load, FullLoader
from tweepy import API, OAuthHandler

logger = logging.getLogger(__name__)


@dataclass
class IClientKeys:
    consumer_key: str
    consumer_secret: str
    access_token: str
    access_token_secret: str


@dataclass
class ITweetMetadata:
    twitter_display_name: str
    twitch_channel: str
    twitch_stream_title: str
    tags: list[str]
    thumbnail: str


class TwitterClient:
    def __init__(self, client_keys: IClientKeys) -> None:
        self.api = __class__.get_api(
            client_keys.consumer_key,
            client_keys.consumer_secret,
            client_keys.access_token,
            client_keys.access_token_secret,
        )

    @staticmethod
    def get_api(
        consumer_key,
        consumer_secret,
        access_token,
        access_token_secret,
    ):
        auth = OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_token, access_token_secret)

        api = API(auth)

        try:
            api.verify_credentials()
        except Exception as err:
            logger.error(f"An error has occurred: {err}")

        return api

    def send_tweet(self, tweet_metadata: ITweetMetadata) -> None:
        with open("message.yml", "r") as file:
            stream = file.read()
            data = load(stream, Loader=FullLoader)

        message = data["message"].format(
            tweet_metadata.twitter_display_name,
            tweet_metadata.twitch_stream_title,
            tweet_metadata.twitch_channel,
            tweet_metadata.tags,
        )

        self.api.update_status(
            status=message, attachment_url=tweet_metadata.thumbnail
        )
