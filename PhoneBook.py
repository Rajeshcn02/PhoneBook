from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot
from Main import MainWidget

import sys

class App(QMainWindow):
    def __init__(self):
        super(App, self).__init__()
        self.setWindowIcon(QIcon('Pictures\\phonebook.png'))
        self.setWindowTitle('Phone book')
        self.setCentralWidget(MainWidget())

        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())