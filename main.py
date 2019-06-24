# coding:utf-8
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import PyQt5
import sys
import os

from dbcontroller import query_movie
from ImageLabel import ImageLabel
from MovieMessage import MovieMessage
from TitleLabel import TitleLabel
#import test1

# listWidget 是视频列表， labelWidget是标签页面
# listWidget, dock_listWidget, movieList
class mainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.init()

    def CreateLayout(self):
        # 允许嵌套
        self.setDockNestingEnabled(True)
        icon = QIcon()
        icon.addPixmap(QPixmap("./resource/icon.ico"), QIcon.Normal, QIcon.Off)
        self.setWindowIcon(icon)
        #去掉标题栏,去掉任务栏显示，窗口置顶  Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint  Tool
        # self.setWindowFlags(Qt.Tool)
        # self.menuBar.hide()
        # self.ui.menuAdmin.hide()
        # a = self.menuBar()
        # a = QMenuBar(self)
        # menu1 = QMenu("dsf", self)
        # action1 = QAction("dfd", self)
        # menu1.addAction(action1)
        # a.addMenu(menu1)
        # self.setMenuBar(a)
        # # a.setVisible(True)

        self.WinMain()
        self.WinLabels()
        self.WinMovieMessage()

        # self.dock_movieList.setFixedWidth(1000)
        self.dock_labels.setFixedWidth(400)

        # PyQt5.QtCore.Qt
        self.addDockWidget(Qt.LeftDockWidgetArea, self.dock_labels)
        self.addDockWidget(Qt.RightDockWidgetArea, self.dock_movieList)
        self.splitDockWidget(self.dock_labels, self.dock_movieList, Qt.Horizontal)
        # self.splitDockWidget(self.dock_movieList, self.dock_labels, Qt.Horizontal)


    def WinMovieMessage(self):
        self.win_message = MovieMessage()
        self.win_message.setI_mainWindow(self)
        self.win_message.resize(700, 800)

    def WinLabels(self):
        self.dock_labels = QDockWidget(self)

        self.dock_labels.setFeatures(QDockWidget.NoDockWidgetFeatures)

        # 删除dock窗口标题
        self.dock_labels.setTitleBarWidget(QWidget())

        # 设置按钮
        self.actor_labels = [
            'actorName1',
            'actorName2',
            'actorName3',
            'actorName3',
            'actorName3',
        ]
        self.labels = [
            'label1',
            'label2',
            'label3',
            'label1',
            'label1',
        ]

        widget = self.updateLabelsWidget()
        self.dock_labels.setWidget(widget)

        # self.actor_labels.pop()
        # self.actor_labels.pop()
        # widget = self.updateLabelsWidget()
        # self.dock_labels.setWidget(widget)


#         labelsWidget.setLayout(labelsLayout)
#         # labelsWidget.setFixedWidth(300)
#         self.dock_labels.setWidget(labelsWidget)

#         scrollArea.setWidget(labelsWidget)
#         self.dock_labels.setWidget(scrollArea)
    def updateLabelsWidget(self):

        labelsLayout = QVBoxLayout()

        label_actor = QLabel(self.dock_labels)
        label_actor.setText('演员:')
        label_actor.setFixedSize(100, 40)
        label_actor.setStyleSheet('QLabel' + self.fontStyle)
        actorWidget = self.addLabelsActorWidget()

        label_tag = QLabel(self.dock_labels)
        label_tag.setText('标签：')
        label_tag.setFixedSize(100, 40)
        label_tag.setStyleSheet('QLabel' + self.fontStyle)


        tagWidget = self.addLabelsTagWidget()

        labelsLayout.addWidget(label_actor)
        labelsLayout.addWidget(actorWidget)
        labelsLayout.addWidget(label_tag)
        labelsLayout.addWidget(tagWidget)


        widget = QWidget(self.dock_labels)
        widget.setLayout(labelsLayout)
        return widget



    def WinMain(self):



        # 初始化电影列表和便签列表
        self.movieList = query_movie()
        # model1 =  {
        #     'movieImagePath': 'E:\图片\Menhera酱 四套日文白底版 by明日素晴\Menhera酱 by明日素晴 (7).jpg',
        #     'actor': 'actorName1',
        # }
        # model2 =  {
        #     'movieImagePath': 'E:\图片\Menhera酱 四套日文白底版 by明日素晴\Menhera酱 by明日素晴 (15)',
        #     'actor': 'actorName2',
        # }
        #
        # for i in range(1, 5):
        #     self.movieList['videoName' + str(i)] = model1
        # self.movieList['videoName' + str(5)] = model2
        self.dock_movieList  = QDockWidget(self)
        self.dock_movieList.setFeatures(QDockWidget.NoDockWidgetFeatures)
        self.dock_movieList.setAllowedAreas(Qt.RightDockWidgetArea)
        self.dock_movieList.setMinimumWidth(300)

        # 删除dock窗口标题
        self.dock_movieList.setTitleBarWidget(QWidget())


        # 布局
        # movieListLayout = QGridLayout()
        # movieListLayout = QVBoxLayout(self.dock_movieList)
        movieListLayout = QVBoxLayout()
        movieListLayout.setAlignment(Qt.AlignmentFlag.AlignCenter)


        # movieListWidget.setLayout(movieListLayout)
        # # movieListWidget.setFixedWidth(1000)
        # movieListWidget.adjustSize()
        movieListWidget = self.addMovieWidget()
        movieListLayout.addWidget(movieListWidget)
        self.dock_movieList.setWidget(movieListWidget)


    def updateMovieListWidget(self):
        # self.movieList.pop(1)        
        # self.movieList.pop(3)        
        # self.movieList.pop(2)        
        movieListWidget = self.addMovieWidget()
        self.dock_movieList.setWidget(movieListWidget)



    def init(self):
        self.setWindowTitle('Movie Collection')
        width = QApplication.desktop().width()
        height = QApplication.desktop().height()
        self.move(int(width * 0.05), int(height * 0.01) )
        self.resize(int(width * 0.8), int(height * 0.8) )

        self.penWidth = 25
        self.regularImageWidth = 330
        self.regularImageHeight = int(330 * 1.4) 
        self.fontStyle = "{ font-family:'Microsoft YaHei';" + "font-size:25px;color:#666666;}"

        self.CreateLayout()
        # ~ setCenterWindow()

        self.show()

    def addLabelsTagWidget(self):
        listwidget = QListWidget(self.dock_labels)

        # listwidget.setItemAlignment(Qt.AlignCenter)
        # listwidget.setIconSize(QSize(30, self.regularImageHeight))
        listwidget.setResizeMode(QListView.Adjust)
        listwidget.setViewMode(QListView.IconMode)
        listwidget.setMovement(QListView.Static)
        listwidget.setSpacing(10)

        for i in range(len(self.labels)):
            item = QListWidgetItem(self.labels[i])
            font = QFont()
            font.setPixelSize(25)
            item.setFont(font)
            listwidget.addItem(item)
        listwidget.itemClicked.connect(self.searchMovieWithTag)
        return listwidget


    def addLabelsActorWidget(self):
        listwidget = QListWidget(self.dock_labels)

        # listwidget.setItemAlignment(Qt.AlignCenter)
        # listwidget.setIconSize(QSize(30, self.regularImageHeight))
        listwidget.setResizeMode(QListView.Adjust)
        listwidget.setViewMode(QListView.IconMode)
        listwidget.setMovement(QListView.Static)
        listwidget.setSpacing(10)
        for i in range(len(self.actor_labels)):
            item = QListWidgetItem(self.actor_labels[i])
            font = QFont()
            font.setPixelSize(25)
            item.setFont(font)
            # item.setSizeHint(QSize(item.sizeHint().width(), item.sizeHint().height()))
            # listwidget.insertItem(i, item)
            listwidget.addItem(item)
            
        listwidget.itemClicked.connect(self.searchMovieWithActor)
        return listwidget
    def searchMovieWithActor(self, item):
        print(item.text())
        # widget = self.updateLabelsWidget()
        # self.dock_labels.setWidget(widget)

    def searchMovieWithTag(self, item):
        print(item.text())
        # widget = self.updateLabelsWidget()
        # self.dock_labels.setWidget(widget)


    def addMovieWidget(self):
        listWidget = MovieListWidget(self)
        listWidget.setI_mainWindow(self)
        # listWidget.setItemAlignment(Qt.AlignCenter)
        listWidget.setIconSize(QSize(self.regularImageWidth, self.regularImageHeight))
        listWidget.setResizeMode(QListView.Adjust)
        listWidget.setViewMode(QListView.IconMode)
        listWidget.setMovement(QListView.Static)
        listWidget.setSpacing(10)

        for i in self.movieList.keys():
            posterPath = self.movieList[i]['cover_path']
            if posterPath == "":
                posterPath = "./resource/no_image.jpg"
            pm = QPixmap(posterPath)

            item = QListWidgetItem(QIcon(pm.scaled(QSize(self.regularImageWidth, self.regularImageHeight))), self.movieList[i]['title'])
            # item = QListWidgetItem("test")
            font = QFont()
            font.setPixelSize(25)
            item.setFont(font)
            item.index = i
            item.setSizeHint(QSize(self.regularImageWidth, self.regularImageHeight+25))
            # listWidget.insertItem(i, item)
            listWidget.addItem(item)
        # listWidget.itemClicked.connect(listWidget.movieClicked)
        listWidget.itemDoubleClicked.connect(listWidget.movieDoubleClicked)
        listWidget.itemPressed.connect(listWidget.mousePressed)
            # item.clicked.connect(self.movieClicked)
            # listwidget.ItemClicked.connect(movieClicked)
        return listWidget
        # self.setCentralWidget(listwidget)
    

class MovieListWidget(QListWidget):
    def __init__(self, parent=None):
        super(MovieListWidget, self).__init__(parent)
        self.timer = QTimer(self)

    def setI_mainWindow(self, mainWin):
        self.I_mainWindow = mainWin
        
    def mousePressed(self, item):
        self.timer.start(500)
        self.timer.timeout.connect(lambda:self.movieClicked(item))


    def movieClicked(self, item):
        self.timer.stop()

        self.I_mainWindow.win_message = MovieMessage()
        self.I_mainWindow.win_message.setI_mainWindow(self.I_mainWindow)
        self.I_mainWindow.win_message.resize(700, 800)
        self.I_mainWindow.win_message.setMessage(self.I_mainWindow.movieList[item.index])

        self.I_mainWindow.win_message.exec_()
        self.timer.timeout.disconnect()


        # cmd = ("PotPlayerMini64.exe " + self.movieList[1]['video_path'])
        # os.popen(cmd)
    def movieDoubleClicked(self, item):
        self.timer.stop()
        self.timer.timeout.disconnect()


        videoPath = self.I_mainWindow.movieList[item.index]['video_path']
        print(item.text())

if __name__ == '__main__':
    app = QApplication(sys.argv)
    uiSystem = mainWindow()
    #test1.Test()
    sys.exit(app.exec_())
