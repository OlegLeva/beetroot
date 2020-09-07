import asyncio
import json


class Client(asyncio.Protocol):
    def __init__(self, loop, user):
        self.user = user
        self.is_open = False
        self.loop = loop
        self.last_message = ""

    def connection_made(self, transport):
        self.transport = transport
        self.is_open = True

    def connection_lost(self, exc):
        self.is_open = False
        self.loop.stop()

    def data_received(self, data):
        if data:
            message = json.loads(data.decode())
            self.process_message(message)

    def process_message(self, message):
        self.output(message)

    def send(self, data):
        self.transport.write(data.decode())
