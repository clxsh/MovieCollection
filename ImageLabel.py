# coding:utf-8
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import PyQt5
import sys
import os

class ImageLabel(QLabel):
    def __init__(self, parent=None):
        super(ImageLabel, self).__init__(parent)

    def setI_mainWindow(self, mainWin):
        self.I_mainWindow = mainWin
    def setIndex(self, index):
        self.index = index
    
    def setVideoPath(self, path):
        self.videoPath = path

    def mouseDoubleClickEvent(self, e):
        # cmd = ("PotPlayerMini64.exe " + self.videoPath)
        # os.popen(cmd)
        a = 3