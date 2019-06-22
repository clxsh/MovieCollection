# coding:utf-8
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import PyQt5
import sys

class TitleLabel(QLabel):
    def __init__(self, parent=None):
        super(TitleLabel, self).__init__(parent)

    def setI_mainWindow(self, mainWin):
        self.I_mainWindow = mainWin

    def setIndex(self, index):
        self.index = index

    def mousePressEvent(self, e):
        self.I_mainWindow.win_message.setMessage(self.index)
        self.I_mainWindow.win_message.exec_()
