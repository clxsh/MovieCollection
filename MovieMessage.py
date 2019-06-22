# coding:utf-8
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import PyQt5
import sys

class MovieMessage(QDialog):
    def __init__(self, parent=None):
        super(MovieMessage, self).__init__(parent)
        # self.setMessage()
        self.init()

    def setMessage(self, index):
        # self.message = self.I_mainWindow.movieList[index]
        print(self.message)

    def init(self):

        self.regularImageWidth = 250
        self.regularImageHeight = 250 * 1.4
        self.fontStyle = "{ font-family:'Microsoft YaHei';" + \
            "font-size:25px;color:#666666;}"
# Qt.FramelessWindowHint | Qt.WindowMinimizeButtonHint |
        self.setWindowFlags( Qt.WindowStaysOnTopHint)
        self.setWindowTitle('影片信息')
        self.setAutoFillBackground(True)
#         QPalette palette;
    
#  QPalette palette;//创建一个调色板对象
#  palette.setBrush(frame->backgroundRole(),QBrush(pixmap));//用调色板的画笔把映射到pixmap上的图片画到frame.backgroundRole()这个背景上
# //palette.setColor(frame->backgroundRole(),QColor(192,253,123));
#  frame->setPalette(palette);//设置窗口调色板为palette，窗口和画笔相关联
#  frame->setMask(pixmap.mask()); //可以将图片中透明部分显示为透明的
#  frame->setAutoFillBackground(true);//设置窗体自动填充背景
        self.setStyleSheet('0')


        self.message = {
            'actress': 'actorName1',
            'title': '影片1',
            'video_path': 'videoPath1',
            'cover_path': 'E:\图片\Menhera酱 四套日文白底版 by明日素晴\Menhera酱 by明日素晴 (7).jpg',
            'tags': ['tag1', 'tag2', 'tag3', 'tag4']
        }

        widget = QWidget(self)
        # widget.setGeometry(0, 0, self.width(), self.height())

        # 布局
        gridLayout = QGridLayout()
        gridLayout.setAlignment(Qt.AlignmentFlag.AlignCenter)

        fontStyle1 = "QLabel" + self.fontStyle
        self.label_poster = QLabel(self)
        self.label_poster.setScaledContents(True)

        poster = QImage(300, 300, QImage.Format_RGB888)
        poster.load(self.message['cover_path'])
        self.label_poster.setPixmap(QPixmap.fromImage(poster))
        # label_image.resize(300, 300)
        self.label_poster.setScaledContents(True)
        self.label_poster.resize(self.regularImageWidth, self.regularImageHeight)

        a = QFormLayout()

        buttonWidget = QWidget(self)
        label_title = QLabel(buttonWidget)
        label_title.setText('影片名：')
        label_title.setStyleSheet(fontStyle1)

        self.label_titleName = QLabel(buttonWidget)
        self.label_titleName.setText(self.message['title'])
        self.label_titleName.setStyleSheet(fontStyle1)


        label_actor = QLabel(buttonWidget)
        label_actor.setStyleSheet(fontStyle1)
        label_actor.setText('演员：')
        self.label_actorName = QLabel(buttonWidget)
        self.label_actorName.setStyleSheet(fontStyle1)

        self.label_actorName.setText(self.message['actress'])

        # buttonBox = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
        # buttonBox.button(QDialogButtonBox.Ok).setText('确认')
        # buttonBox.button(QDialogButtonBox.Cancel).setText('退出')
        label_tag = QLabel('标签:')
        label_tag.setStyleSheet(fontStyle1)
    
        self.label_tagsName = QTextEdit(buttonWidget)
        stringTag = ''
        for string in self.message['tags']:
            stringTag = stringTag + string + ", "
        self.label_tagsName.setText(stringTag)
        self.label_tagsName.setStyleSheet('QTextEdit' + self.fontStyle)

        self.lineEdit = QLineEdit(buttonWidget)
        
        button_addTag = QPushButton('添加标签', buttonWidget)
        



        button_cancel = QPushButton( '退出', self)
        button_cancel.setStyleSheet(fontStyle1)

        button_cancel.clicked.connect(self.reject)

        # gridLayout.addWidget(self.label_poster, 0, 0, 8, 2)
        # gridLayout.addWidget(label_title, 9, 0)
        # gridLayout.addWidget(self.label_titleName, 9, 1)

        # gridLayout.addWidget(label_actor, 6, 0)
        # gridLayout.addWidget(self.label_actorName, 6, 1)
        # gridLayout.addWidget(button_cancel, 7, 0)

        gridLayout.addWidget(label_title, 0, 0)
        gridLayout.addWidget(self.label_titleName, 0, 1)

        gridLayout.addWidget(label_actor, 1, 0)
        gridLayout.addWidget(self.label_actorName, 1, 1)
        gridLayout.addWidget(label_tag, 2, 0)
        gridLayout.addWidget(self.label_tagsName, 3, 0, 1, 2)
        gridLayout.addWidget(self.lineEdit, 4, 0, 1, 1)
        gridLayout.addWidget(button_addTag, 4, 1, 1, 1)


        gridLayout.addWidget(button_cancel, 5, 0)
        
        # gridLayout.addWidget(label_title)
        # gridLayout.addWidget(self.label_titleName)

        # gridLayout.addWidget(label_actor)
        # gridLayout.addWidget(self.label_actorName)
        # gridLayout.addWidget(button_cancel)

        
        # splitterMain = QSplitter(Qt.Vertical, self)


        # widget.adjustSize()
        buttonWidget.setLayout(gridLayout)

        selfLayout = QHBoxLayout(self)
        selfLayout.setAlignment(Qt.AlignCenter)
        
        # posterLayout = QVBoxLayout(self)
        # posterLayout.addWidget(self.label_poster)
        # selfLayout.addLayout(posterLayout)
        # selfLayout.addWidget(self.label_poster)
        selfLayout.addWidget(self.label_poster, 1, Qt.AlignLeft)
        # self.addDockWidget(Qt.LeftDockWidgetArea, self.label_poster)
        # self.addDockWidget(Qt.RightDockWidgetArea, self.dock_movieList)
        
        selfLayout.addWidget(buttonWidget, 1, Qt.AlignCenter)
        # selfLayout.addLayout(gridLayout, 1)
        self.setLayout(selfLayout)
        # selfLayout.addWidget()
        # movieListWidget.setFixedWidth(1000)
        # self.setWidget(movieListWidget)

    def setI_mainWindow(self, mainWin):
        self.I_mainWindow = mainWin
        self.regularImageWidth = self.I_mainWindow.regularImageWidth
        self.regularImageHeight = self.I_mainWindow.regularImageHeight

