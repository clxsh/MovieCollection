# coding:utf-8
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import PyQt5
import sys

class ImageLabel(QLabel):
    def __init__(self, parent=None):
        super(ImageLabel, self).__init__(parent)

    def mouseDoubleClickEvent(self, e):
        a = 3
