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

        # t1 = self.dock_labels.titleBarWidget()
        # t2 = QWidget(self.dock_labels)
        # 删除dock窗口标题
        self.dock_labels.setTitleBarWidget(QWidget())
        self.labelsLayout = QVBoxLayout()

        # 滑动条区域
        # scrollArea = QScrollArea(self.dock_labels)
        # labelsWidget = QWidget(self.dock_labels)
        # 布局
        # labelsLayout = QGridLayout()
        # labelsLayout.setAlignment(Qt.AlignmentFlag.AlignTop)

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

        label_actor = QLabel(self.dock_labels)
        label_actor.setText('演员:')
        label_actor.setFixedSize(100, 40)
        actorWidget = self.addLabelsActorWidget()

        label_tag = QLabel(self.dock_labels)
        label_tag.setText('标签：')
        label_tag.setFixedSize(100, 40)

        tagWidget = self.addLabelsTagWidget()

        self.labelsLayout.addWidget(label_actor)
        self.labelsLayout.addWidget(actorWidget)
        self.labelsLayout.addWidget(label_tag)
        self.labelsLayout.addWidget(tagWidget)


        widget = QWidget(self.dock_labels)
        widget.setLayout(self.labelsLayout)
        self.dock_labels.setWidget(widget)
        # self.dock_labels.setLayout(self.labelsLayout)
#         it_i = 0
#         it_j = 0
#         i = 0

#         label_white = QLabel(' ')
#         labelsLayout.addWidget(label_white, it_i, it_j, 1, 1)
#         it_i += 1
#         labelsLayout.addWidget(label_white, it_i, it_j, 1, 1)
#         it_i += 1

#         labelsLayout.addWidget(label_actor, it_i, it_j, 1, 1)
#         it_i+=1

#         actorButton = []
#         for actorName in self.actor_labels:
#             actorButton.append(QPushButton(actorName, self))

#             actorButton[i].setStyleSheet("QPushButton{ font-family:'Microsoft YaHei';" +
#             "font-size:25px;color:#666666;}");
#             actorButton[i].resize(actorButton[i].sizeHint().width(), actorButton[i].sizeHint().height());

#             # actorButton[i].setFixedSize(100, 40)
#             actorButton[i].setFlat(True)

#             labelsLayout.addWidget(actorButton[i], it_i, it_j, 1, 1)
#             i += 1; it_j += 1
#             if(it_j > 2):
#                 it_i += 1
#                 it_j = 0
#         # 到下一行
#         if(it_j != 0):
#             it_j = 0
#             it_i += 1
#         label_label = QLabel('标签：')
#         labelsLayout.addWidget(label_label, it_i, it_j, 1, 1)
#         it_i += 1

#         i = 0
#         labelsButton = []
#         for labelName in self.labels:
#             labelsButton.append(QPushButton(labelName, self))
#             labelsButton[i].setStyleSheet("QPushButton{ font-family:'Microsoft YaHei';" +
#             "font-size:25px;color:#666666;}");
#             labelsButton[i].resize(labelsButton[i].sizeHint().width(), labelsButton[i].sizeHint().height());

# # button->setStyleSheet( "QPushButton{border-image: url(navigation_more_normal.png);}"
# #"QPushButton:hover{border-image: url(navigation_more_hover.png);}"
# # "QPushButton:pressed{border-image: url(on_more_pressed.png);}"）；
#             # labelsButton[i].setFixedSize(100, 40)
#             labelsButton[i].setFlat(True)

#             labelsLayout.addWidget(labelsButton[i], it_i, it_j, 1, 1)
#             i += 1; it_j += 1
#             if(it_j > 2):
#                 it_i += 1
#                 it_j = 0




#         labelsWidget.setLayout(labelsLayout)
#         # labelsWidget.setFixedWidth(300)
#         self.dock_labels.setWidget(labelsWidget)

#         scrollArea.setWidget(labelsWidget)
#         self.dock_labels.setWidget(scrollArea)



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

        # 滑动条区域
        # scrollArea = QScrollArea(self.dock_movieList)
        # movieListWidget = QWidget(self.dock_movieList)


        # 布局
        # movieListLayout = QGridLayout()
        # movieListLayout = QVBoxLayout(self.dock_movieList)
        movieListLayout = QVBoxLayout()
        movieListLayout.setAlignment(Qt.AlignmentFlag.AlignCenter)

        # movieListLayout.setContentsMargins(30,30,30,0)

        # a = QLabel(movieListWidget)
        # a.setText("<p style='color: red; margin-left: 20px'><b>hell world</b></p>")
        #
        #
        # videoName1 = 'videoName1'
        # movie1 = QImage(300, 300, QImage.Format_RGB888)
        # movie1.load(self.movieList[videoName1]['movieImagePath'])
        #
        # label1 = QLabel(movieListWidget)
        # label1.setScaledContents(True)
        #
        # label1.setPixmap(QPixmap.fromImage(movie1))
        # label1.resize(300, 300)
        # label1_name = QLabel(movieListWidget)
        # label1_name.setText(videoName1)
        # label1_name.setAlignment(Qt.AlignCenter)
        #
        # movieListLayout.addWidget(label1, 0, 0, 1, 1)
        # movieListLayout.addWidget(label1_name, 1, 0, 1, 1)



        # 参数是 movieList
        # movieImage = []
        # label_movieLabels = []
        # label_movieNames = []
        # # self.movieLabelGroup = QButtonGroup()
        # # movieName = []
        # i = 0
        # it_i = 0
        # it_j = 0

        # for movieId in self.movieList.keys():
        #     # movieImg = QImage(300, 300, QImage.Format_RGB888)
        #     # movieImg.load(self.movieList[movieName]['movieImagePath'])
        #     a = QImage(500, 500, QImage.Format_RGB888)
        #     movieImage.append (a)

        #     posterPath = self.movieList[movieId]["cover_path"]
        #     if posterPath == "":
        #         posterPath = "./source/no_image.jpg"

        #     movieImage[i].load(posterPath)
        #     # movieImage[i].scaled((int)(movieImage[i].width() * 0.3),
        #     # (int)(movieImage[i].height() * 0.3))
        #     labelMovie = ImageLabel(movieListWidget)
        #     labelMovie.setI_mainWindow(self)
        #     # labelMovie.resize((int)(movieImage[i].width() * 0.3),
        #     # (int)(movieImage[i].height() * 0.3))


        #     labelMovie.setPixmap(QPixmap.fromImage(movieImage[i]))
        #     labelMovie.setVideoPath(self.movieList[movieId]['video_path'])

        #     label_movieLabels.append(labelMovie)
        #     label_movieLabels[i].setAlignment(Qt.AlignmentFlag.AlignCenter)

        #     label_movieLabels[i].setScaledContents(True)
        #     label_movieLabels[i].setPixmap(QPixmap.fromImage(movieImage[i]))
        #     # label_movieLabels[i].resize(movieImage[i].width(), movieImage[i].height());
        #     # labelMovie.setFixedSize((int)(movieImage[i].width() * 0.6),
        #     # (int)(movieImage[i].height() * 0.6))
        #     labelMovie.setFixedSize(self.regularImageWidth, self.regularImageHeight)



        #     # label_movieName = QLabel(movieListWidget)
        #     # label_movieName.setText(movieName)
        #     # label_movieName.setAlignment(Qt.AlignCenter)
        #     label_movieNames.append (TitleLabel(movieListWidget))
        #     label_movieNames[i].setI_mainWindow(self)
        #     label_movieNames[i].setIndex(i)
            
        #     # label_movieNames[i].setMessage

        #     label_movieNames[i].setText(self.movieList[movieId]["title"])
        #     label_movieNames[i].setFixedWidth(self.regularImageWidth)

            
        #     # 设置影片名的样式，字体大小，长短
        #     font = QFont()
        #     font.setPixelSize(self.penWidth)
        #     label_movieNames[i].setFont(font)


        #     # 获取字符串占像素大小
        #     fontMetrics = QFontMetrics(font)
        #     titleNameSize = fontMetrics.boundingRect(self.movieList[movieId]["title"]).width()
    
        #     if titleNameSize > label_movieNames[i].width():
        #         label_movieNames[i].setText (fontMetrics.elidedText(self.movieList[movieId]["title"], 
        #         Qt.ElideRight, label_movieNames[i].width()))
            
        #     # label_movieNames[i].setAlignment(Qt.AlignCenter)
            
        #     # a = QLabel()
        #     # label_movieLabels[i]
        #     movieListLayout.addWidget(label_movieLabels[i], 2 * it_i, it_j, 1, 1)
        #     movieListLayout.addWidget(label_movieNames[i], 2 * it_i + 1, it_j, 1, 1)
        #     i += 1; it_j += 1
        #     if it_j > 2 :
        #         it_i += 1
        #         it_j = 0



        # movieListWidget.setLayout(movieListLayout)
        # # movieListWidget.setFixedWidth(1000)
        # movieListWidget.adjustSize()
        movieListWidget = self.addMovieWidget()
        movieListLayout.addWidget(movieListWidget)
        self.dock_movieList.setWidget(movieListWidget)


        # self.movieList.pop(1)        
        # self.movieList.pop(3)        
        # self.movieList.pop(2)        
        # movieListWidget = self.addMovieWidget()
        # self.dock_movieList.setWidget(movieListWidget)


        # scrollArea.setWidget(movieListWidget)
        # self.dock_movieList.setWidget(scrollArea)
        # self.repaint()

    def init(self):
        self.setWindowTitle('video play')
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

        return listwidget

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
                posterPath = "./source/no_image.jpg"
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
