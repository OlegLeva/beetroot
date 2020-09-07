import asyncio
import json
import sys

from PyQt5.QtWidgets import (QWidget,
                             QLineEdit,
                             QLabel,
                             QTextEdit,
                             QPlainTextEdit, 
                             QPushButton,
                             QHBoxLayout,
                             QVBoxLayout,
                             QApplication)
from quamash import QEventLoop

from test_tasks.clientProtocol_1 import EchoClientProtocol


class Gui(QWidget):
    def __init__(self, loop,  client, **kwargs):
        super(__class__, self).__init__(**kwargs)
        self.client = client
        self.client.output = self.output
        self.loop = loop
        self.resize(400, 300)
        self.setWindowTitle("chat")
        self.initialize()
        self.show()



    def send(self, *obj):
        data = json.dumps({'sender': self.client.user, 'message': self.userInput.text()})
        self.client.send(data)
        self.userInput.setText("")

    def output(self, data):
        self.chatArea.insertPlainText(f'{data["sender"]}: {data["message"]}')
        self.chatArea.insertPlainText('\n')

    def initialize(self):
        userLabel = QLabel(self.client.user, self)
        userLabel.move(5, 5)

        self.chatArea = QTextEdit("", self)
        self.chatArea.setReadOnly(True)
        self.chatArea.setMouseTracking(True)
        self.chatArea.resize(362, 200)
        self.chatArea.textSelected = False
        self.chatArea.move(25, 37)
        self.userInput = QLineEdit()

        sendButton = QPushButton("send")
        sendButton.clicked.connect(self.send)

        hbox = QHBoxLayout()
        hbox.addStretch(1)
        hbox.addWidget(self.userInput)
        hbox.addWidget(sendButton)

        vbox = QVBoxLayout()
        vbox.addStretch(1)
        vbox.addLayout(hbox)

        self.setLayout(vbox)


class App(QApplication):
    def __init__(self):
        QApplication.__init__(self, sys.argv)
        self.loop = QEventLoop(self)
        asyncio.set_event_loop(self.loop)
        self.userClient = EchoClientProtocol(self.loop, 'user')

        self.loop.create_task(self.start())
        self.gui = Gui(self.loop, self.userClient)

        self.loop.run_forever()

    async def start(self):
        clientConnection = self.loop.create_connection(lambda: self.userClient, '127.0.0.1', 8888)
        await asyncio.wait_for(clientConnection, 1000)
        transport, protocol = clientConnection
        self.userClient.connection_made(transport)


if __name__ == '__main__':
    App()
