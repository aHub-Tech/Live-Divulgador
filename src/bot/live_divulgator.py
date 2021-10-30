from time import sleep

from bot.handlers.post_tweet import PostTweet


class LiveDivulgator:
    def run():
        while True:
            PostTweet.handle()
            sleep(60)
