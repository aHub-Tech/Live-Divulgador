import logging
from dataclasses import dataclass

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
    self.api = __class__.get_api(*client_keys)

  @staticmethod
  def get_api(consumer_key, consumer_secret, access_token, access_token_secret):
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    api = API(auth)

    try:
      api.verify_credentials()
    except Exception as err:
      logger.error(f"An error has occurred: {err}")

    return api
