from src.bot.twitch.client import TwitchClient
from pytest import fixture
from dotenv import load_dotenv
from os import getenv

load_dotenv()

TWITCH_CLIENT_ID=getenv("CLIENT_ID")
TWITCH_CLIENT_SECRET=getenv("CLIENT_SECRET")


@fixture
def twitch_client():
    client = TwitchClient(TWITCH_CLIENT_ID, TWITCH_CLIENT_SECRET)
    return client

def test_get_oauth():
    oauth = TwitchClient.get_oauth(TWITCH_CLIENT_ID, TWITCH_CLIENT_SECRET)
    assert oauth == "banana"

def test_get_streamer_id(twitch_client):
    streamer_id = twitch_client.get_streamer_id("dornellestv")
    assert streamer_id == "518380427"

def test_get_stream(twitch_client):
    responses = []
    lista_streamers = ["170078760", "40531480", "518380427", "30672329"] # session.query(Streamer).select(Streamer.twitch_id).all()

    for s in lista_streamers:
        response = twitch_client.get_stream(s)
        responses.append(response)

    assert responses == "banana"

# def test_
