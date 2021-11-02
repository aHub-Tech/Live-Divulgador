# create a bot that accepts modules as plugins
from abc import ABC


class Bot(ABC):
    def __init__(self, config=None):
        self.config = config
        self.plugins = []
        self.load_plugins()

    def add_plugin(self, plugin):
        self.plugins.append(plugin)

    def load_plugins(self):
        for plugin in self.config.plugins:
            self.add_plugin(plugin(self.config))

    def run(self):
        for plugin in self.plugins:
            plugin.run()


config = ["messages", "commands"]

bot = Bot(config)
