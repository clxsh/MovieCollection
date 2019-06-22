# coding:utf-8
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import PyQt5
import sys

class MovieMessage(QDialog):
    def __init__(self, parent=None):
        super(MovieMessage, self).__init__(parent)
        self.setMessage()
        self.init()

    def setMessage(self):
        self.message = {
            'movieImagePath': 'E:\图片\Menhera酱 四套日文白底版 by明日素晴\Menhera酱 by明日素晴 (7).jpg',
            'actor': 'actorName1',
            'title': '影片1',
            'videoPath': 'videoPath1',
            'tag': 'tag1',
        }
    def init(self):
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowMinimizeButtonHint | Qt.WindowStaysOnTopHint)
        self.setWindowTitle('影片信息')

        widget = QWidget(self)

        # 布局
        gridLayout = QGridLayout()
        gridLayout.setAlignment(Qt.AlignmentFlag.AlignCenter)

        label_poster = QLabel(widget)
        label_poster.setScaledContents(True)

        poster = QImage(500, 500, QImage.Format_RGB888)
        poster.load(self.message['movieImagePath'])
        label_poster.setPixmap(QPixmap.fromImage(poster))
        # label_image.resize(300, 300)
        label_poster.setFixedSize((int)(poster.width() * 0.6),
        (int)(poster.height() * 0.6))

        label_title = QLabel(widget)
        label_title.setText('影片名：')
        label_titleName = QLabel(widget)
        label_titleName.setText(self.message['title'])

        label_actor = QLabel(widget)
        label_actor.setText('演员：')
        label_actorName = QLabel(widget)
        label_actorName.setText(self.message['actor'])

        button_cancel = QPushButton( '退出', self)
        # button_cancel.clicked.connect(self.reject())

        # gridLayout.addWidget(label_poster, 0, 0)
        gridLayout.addWidget(label_title, 0, 0)
        gridLayout.addWidget(label_titleName, 0, 1)

        gridLayout.addWidget(label_actor, 1, 0)
        gridLayout.addWidget(label_actorName, 1, 1)
        gridLayout.addWidget(button_cancel, 3, 0)

        widget.adjustSize()
        widget.setLayout(gridLayout)

        selfLayout = QVBoxLayout(self)
        selfLayout.addWidget(label_poster)

        selfLayout.addLayout(gridLayout)
        self.setLayout(selfLayout)
        # selfLayout.addWidget()
        # movieListWidget.setFixedWidth(1000)
        # self.setWidget(movieListWidget)
