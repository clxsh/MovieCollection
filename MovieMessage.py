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
        self.selfLayout = QHBoxLayout()
        self.setLayout(self.selfLayout)
        self.buttonWidget = QWidget()
        self.label_poster = QLabel()
        self.t = 1

    def setMessage(self, message):
        # self.message = self.I_mainWindow.movieList[index]
        # print(self.message)
        self.message = message

        # print(message)
        # while(child = self.layout().takeAt(0)):
        #     if child != None:
        #         del child
        # k = 0
        # for j in range(0, 2):
        #     for i in reversed(range(self.selfLayout.count())):
        #         self.selfLayout.itemAt(i).widget().deleteLater()
        #         print(k)
        #         k+=1
        # self.selfLayout = QHBoxLayout()
        # # self.setLayout(self.selfLayout)
        # self.buttonWidget = QWidget()
        # self.label_poster = QLabel()

        # self.label_poster.deleteLater()
        # del self.label_poster

        # self.setLayout(self.selfLayout)
        

        # self.buttonWidget = None
        # self.setwi
        # self.setLayout(None)
        # if(self.t == 1 ):
        self.init()
        # self.repaint()


    def init(self):
        self.t  = 3
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
        # self.setStyleSheet('0')


        # self.message = {
        #     'actress': 'actorName1',
        #     'title': '影片1',
        #     'video_path': 'videoPath1',
        #     'cover_path': 'E:\图片\Menhera酱 四套日文白底版 by明日素晴\Menhera酱 by明日素晴 (7).jpg',
        #     'tags': ['tag1', 'tag2', 'tag3', 'tag4']
        # }

        # self.widget = QWidget(self)
        # widget.setGeometry(0, 0, self.width(), self.height())

        # 布局
        gridLayout = QGridLayout()
        gridLayout.setAlignment(Qt.AlignmentFlag.AlignCenter)

        fontStyle1 = "QLabel" + self.fontStyle
        self.label_poster = QLabel(self)
        self.label_poster.setScaledContents(True)

        # poster = QImage(300, 300, QImage.Format_RGB888)
        # poster.load(self.message['cover_path'])

        posterPath = self.message['cover_path']
        if posterPath == "":
            posterPath = "./source/no_image.jpg"

        self.label_poster.setPixmap(QPixmap(posterPath))
        # label_image.resize(300, 300)
        self.label_poster.setScaledContents(True)
        self.label_poster.resize(self.regularImageWidth, self.regularImageHeight)




        self.buttonWidget = QWidget(self)
        label_title = QLabel(self.buttonWidget)
        label_title.setText('影片名：')
        label_title.setStyleSheet(fontStyle1)

        self.label_titleName = QLabel(self.buttonWidget)
        self.label_titleName.setText(self.message['title'])
        self.label_titleName.setStyleSheet(fontStyle1)


        label_actor = QLabel(self.buttonWidget)
        label_actor.setStyleSheet(fontStyle1)
        label_actor.setText('演员：')
        self.label_actorName = QLabel(self.buttonWidget)
        self.label_actorName.setStyleSheet(fontStyle1)
        self.label_actorName.setText(self.message['actress'])

        # buttonBox = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
        # buttonBox.button(QDialogButtonBox.Ok).setText('确认')
        # buttonBox.button(QDialogButtonBox.Cancel).setText('退出')
        label_tag = QLabel('标签:')
        label_tag.setStyleSheet(fontStyle1)
    
        self.label_tagsName = QTextEdit(self.buttonWidget)
        stringTag = ''
        for string in self.message['tags']:
            stringTag = stringTag + string + ", "
        self.label_tagsName.setText(stringTag)
        self.label_tagsName.setStyleSheet('QTextEdit' + self.fontStyle)
        self.label_tagsName.setReadOnly(True)

        self.lineEdit = QLineEdit(self.buttonWidget)
        # self.lineEdit.move(QTextEdit.End)
        # self.lineEdit.setCursorMoveStyle
        button_addTag = QPushButton('添加标签', self.buttonWidget)
        button_addTag.clicked.connect(self.addTag)



        button_cancel = QPushButton( '退出', self)
        button_cancel.setStyleSheet(fontStyle1)

        button_cancel.clicked.connect(self.close)


        gridLayout.addWidget(label_title, 0, 0)
        gridLayout.addWidget(self.label_titleName, 0, 1)

        gridLayout.addWidget(label_actor, 1, 0)
        gridLayout.addWidget(self.label_actorName, 1, 1)
        gridLayout.addWidget(label_tag, 2, 0)
        gridLayout.addWidget(self.label_tagsName, 3, 0, 1, 2)
        gridLayout.addWidget(self.lineEdit, 4, 0, 1, 1)
        gridLayout.addWidget(button_addTag, 4, 1, 1, 1)


        gridLayout.addWidget(button_cancel, 5, 0)
        

        # splitterMain = QSplitter(Qt.Vertical, self)


        # widget.adjustSize()
        self.buttonWidget.setLayout(gridLayout)

        # self.selfLayout = QHBoxLayout()
        self.selfLayout.setAlignment(Qt.AlignCenter)
        
        # posterLayout = QVBoxLayout(self)
        # posterLayout.addWidget(self.label_poster)
        # selfLayout.addLayout(posterLayout)
        # selfLayout.addWidget(self.label_poster)
        self.selfLayout.addWidget(self.label_poster, 1, Qt.AlignLeft)
        # self.addDockWidget(Qt.LeftDockWidgetArea, self.label_poster)
        # self.addDockWidget(Qt.RightDockWidgetArea, self.dock_movieList)
        
        self.selfLayout.addWidget(self.buttonWidget, 1, Qt.AlignCenter)
        # selfLayout.addLayout(gridLayout, 1)

        # selfLayout.addWidget()
        # movieListWidget.setFixedWidth(1000)
        # self.setWidget(movieListWidget)

    def addTag(self):
        # self.label_tagsName.setCursor
        # self.label_tagsName.append(self.lineEdit.text() + ', ')
        if self.lineEdit.text().strip(' ') == '':
            return
        self.label_tagsName.insertPlainText(self.lineEdit.text().strip(' ') + ', ')
    def setI_mainWindow(self, mainWin):
        self.I_mainWindow = mainWin
        self.regularImageWidth = self.I_mainWindow.regularImageWidth
        self.regularImageHeight = self.I_mainWindow.regularImageHeight

