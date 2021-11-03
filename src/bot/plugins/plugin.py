from abc import ABC


class Plugin(ABC):
    def __init__(self, bot):
        self.bot = bot

    def run(self):
        pass

    def stop(self):
        pass
