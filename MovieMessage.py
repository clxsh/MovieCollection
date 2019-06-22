# coding:utf-8
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import PyQt5
import sys

class MovieMessage(QDialog):
    def __init__(self, parent=None):
        super(MovieMessage, self).__init__(parent)

        self.init()

    def init(self):
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowMinimizeButtonHint | Qt.WindowStaysOnTopHint)
        # layout =
