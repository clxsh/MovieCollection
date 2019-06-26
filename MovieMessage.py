# coding:utf-8
from PyQt5.QtWidgets import (QDialog, QHBoxLayout, QWidget, QLabel, QGridLayout, QTextEdit, QLineEdit, QPushButton
                             )
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtCore import Qt
import os

from dirwallthrough import alter_tag, MType
from dbcontroller import query_movie

class MovieMessage(QDialog):
    def __init__(self, parent=None):
        super(MovieMessage, self).__init__(parent)
        # self.setMessage()
        self.selfLayout = QHBoxLayout()
        self.setLayout(self.selfLayout)
        self.buttonWidget = QWidget()
        self.label_poster = QLabel()
        self.t = 1

        icon = QIcon()
        icon.addPixmap(QPixmap("./resource/icon.ico"), QIcon.Normal, QIcon.Off)
        self.setWindowIcon(icon)
    def setIndex(self, index):
        self.index = index
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
        self.setWindowFlags(Qt.WindowCloseButtonHint | Qt.MSWindowsFixedSizeDialogHint)
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

        poster = self.message['cover']
        if poster is None:
            with open("./resource/no_image.png", "rb") as f:
                poster = f.read()
        pm = QPixmap()
        pm.loadFromData(poster, "png")

        self.label_poster.setPixmap(pm)
        # label_image.resize(300, 300)
        self.label_poster.setScaledContents(True)
        self.label_poster.resize(self.regularImageWidth, self.regularImageHeight)




        self.buttonWidget = QWidget(self)
        label_title = QLabel(self.buttonWidget)
        label_title.setText('影片名：')
        label_title.setStyleSheet(fontStyle1)

        self.label_titleName = QLabel(self.buttonWidget)
        self.label_titleName.setText(self.message['title'][:25] + "...")
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
            stringTag = stringTag + string + ",  "
        self.label_tagsName.setText(stringTag[0:-3])
        self.label_tagsName.setStyleSheet('QTextEdit' + self.fontStyle)
        self.label_tagsName.setReadOnly(True)
        self.label_tagsName.setFixedHeight(100)

        self.addLineEdit = QLineEdit(self.buttonWidget)
        self.delLineEdit = QLineEdit(self.buttonWidget)
        # self.lineEdit.move(QTextEdit.End)
        # self.lineEdit.setCursorMoveStyle
        button_addTag = QPushButton('添加标签', self.buttonWidget)
        button_addTag.clicked.connect(self.addTag)

        button_delTag = QPushButton("删除标签", self.buttonWidget)
        button_delTag.clicked.connect(self.delTag)


        button_cancel = QPushButton( '退出', self)
        button_cancel.setStyleSheet(fontStyle1)
        button_cancel.clicked.connect(self.close)

        button_play = QPushButton("播放", self)
        button_play.setStyleSheet(fontStyle1)
        button_play.clicked.connect(self.play_video)


        gridLayout.addWidget(label_title, 0, 0)
        gridLayout.addWidget(self.label_titleName, 0, 1)

        gridLayout.addWidget(label_actor, 1, 0)
        gridLayout.addWidget(self.label_actorName, 1, 1)
        gridLayout.addWidget(label_tag, 2, 0)
        gridLayout.addWidget(self.label_tagsName, 3, 0, 1, 2)
        gridLayout.addWidget(self.addLineEdit, 4, 0, 1, 1)
        gridLayout.addWidget(button_addTag, 4, 1, 1, 1)
        gridLayout.addWidget(self.delLineEdit, 5, 0, 1, 1)
        gridLayout.addWidget(button_delTag, 5, 1, 1, 1)


        gridLayout.addWidget(button_cancel, 6, 0)
        gridLayout.addWidget(button_play, 6, 1)
        

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
        tagtext = self.addLineEdit.text().strip()
        if tagtext == '':
            return

        tags = self.label_tagsName.toPlainText()

        if tagtext not in tags:
            if tags == "":
                self.label_tagsName.append(tagtext)
            else:
                tags = self.label_tagsName.toPlainText() + ',  ' + tagtext
                self.label_tagsName.setPlainText(tags)

            alter_tag(MType.ADD, self.index, tagtext)
            self.I_mainWindow.updateLabelsWidget()

            self.updateMainWindowMovieList(self.index)

    def delTag(self):
        tagtext = self.delLineEdit.text().strip()
        if tagtext == '':
            return

        tags = self.label_tagsName.toPlainText()
        print(len(tags))
        print(len(tagtext))
        if tagtext in tags:
            if len(tags) == len(tagtext):
                tags = ""
            elif tags.endswith(tagtext):
                tags = tags.replace(",  " + tagtext, "")
            else:
                tags = tags.replace(tagtext + ",  ", "")

            self.label_tagsName.setPlainText(tags)
            alter_tag(MType.DEL, self.index, tagtext)
            self.I_mainWindow.updateLabelsWidget()
            self.updateMainWindowMovieList(self.index)
    

    def play_video(self):
        
        cmd = ("PotPlayerMini64.exe " + self.message["video_path"])
        os.popen(cmd)

    def setI_mainWindow(self, mainWin):
        self.I_mainWindow = mainWin
        self.regularImageWidth = self.I_mainWindow.regularImageWidth
        self.regularImageHeight = self.I_mainWindow.regularImageHeight

    def updateMainWindowMovieList(self, movie_id):
        self.I_mainWindow.movieList[movie_id] = query_movie(movie_id=movie_id)[movie_id]

