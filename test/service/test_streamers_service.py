from src.bot.service.streamers_service import StreamersService

from src.bot.database.engine import Session

from src.bot.database.entities.streamer import Streamer

from src.bot.database.entities.streamer import Base, Streamer

from src.bot.service.streamers_service import StreamersService


# Base.metadata.create_all(engine)


def test_create_streamer():
    streamer = Streamer(
        twitch_id=23452356,
        twitter_id=234232345,
        name="Dornelles"
    )

    StreamersService.create_streamer(streamer)

    response = StreamersService.get_streamer(streamer.id)

    assert streamer.id == response.id


def test_database_session():
    session = Session()


def test_database_get_streamers():
    ...
