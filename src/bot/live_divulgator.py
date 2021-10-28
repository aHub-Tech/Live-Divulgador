from bot.handlers.post_tweet import PostTweet
from time import sleep


class LiveDivulgator:
    def run():
        while True:
            PostTweet.handle()
            sleep(120)
