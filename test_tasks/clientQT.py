
from PyQt5.QtWidgets import (QWidget,
                             QLabel,
                             QTextEdit,
                             QPushButton,
                             QLineEdit,
                             QHBoxLayout,
                             QVBoxLayout,
                             QApplication)
from quamash import QEventLoop
import asyncio, sys, json
import client

class Gui(QWidget):
    def __init__(self, loop, client, **kwargs):
        super(__class__, self).__init__(**kwargs)
        self.client = client
        self.client.output = self.output
        self.loop = loop
        self.resize(400, 300)
        self.setWindowTitle("chat")
        self.initialize()
        self.show()

    def send(self, *obj):
        data = json.dumps({'sender': self.client.user, 'messag': self.userInput.text()})
        self.client.send(data)
        self.userInput.setText("")

    def output(self, data):
        self.chatArea.insertPlainText(data)

    def initialize(self):
        userLabel = QLabel(self.client.user, self)
        userLabel.move(5,5)

        self.chatArea = QTextEdit("", self)
        self.chatArea.setReadOnly(True)
        self.chatArea.setMouseTracking(True)
        self.chatArea.resize(362, 200)
        self.chatArea.move(25, 37)

        sendButton = QPushButton("send")
        sendButton.clicked.connect(self.send)

        hbox = QHBoxLayout()
        hbox.addStretch(1)
        hbox.addWidget(self.userInput)
        hbox.addWidget(sendButton)

        vbox = QVBoxLayout()
        vbox.addstretch(1)
        vbox.addLayout(hbox)

        self.setLayout(vbox)

class App(QApplication):
    def __init__(self):
        QApplication.__init__(self, sys.argv)
        loop = QEventLoop(self)
        self.loop = loop
        asyncio.set_event_loop(self.loop)
        self.userClient = Client(self.loop, 'user')

        self.loop.create_task(self.start())

        self.

    async def start






