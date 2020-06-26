import sys
from PyQt5.QtWidgets import (QApplication,
                             QWidget,
                             QLabel)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWidget = QWidget()
    mainWidget.setWindowTitle('Calculator1.0')
    mainWidget.setGeometry(0, 0, 500, 300)
    digitLabel = QLabel('12-DIGIT', parent=mainWidget)
    mainWidget.show()
    return_code = app.exec()
    sys.exit(return_code)