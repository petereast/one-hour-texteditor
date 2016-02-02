from PyQt4 import QtCore, QtGui
import sys, os

# Import the new defined class here.
from MainScreen import *


def _init():
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()
    window.raise_()
    app.exec_()

_init()
