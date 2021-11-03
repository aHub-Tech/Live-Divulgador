from pytest import fixture
from src.bot.bots.live_divulgator import LiveDivulgator
from src.bot.plugins.twitter import TwitterPlugin


@fixture
def livedivulgator():
    plugins_list = [TwitterPlugin]

    bot = LiveDivulgator()

    bot.add_plugins(plugins_list)

    yield bot

    del bot


def test_livedivulgator_init(livedivulgator):
    livedivulgator.run()
