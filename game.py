#!/usr/bin/python3
from PyQt5.QtWidgets import QApplication
from main import Game
import sys

app = QApplication(sys.argv)
win = Game()
win.setFixedHeight(469)
win.setFixedWidth(490)
win.show()
app.exec_()
