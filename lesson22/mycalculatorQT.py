import sys
from PyQt5.QtWidgets import (QApplication,
                             QWidget,)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWidget = QWidget()
    mainWidget.setWindowTitle('Calculator1.0')
    mainWidget.show()