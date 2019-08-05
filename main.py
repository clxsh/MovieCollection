# coding:utf-8
from PyQt5.QtWidgets import (QMainWindow, QStatusBar, QAction, QFileDialog, QApplication, QDockWidget, QWidget,
                             QVBoxLayout, QLabel, QAbstractItemView, QListWidget, QListWidgetItem, QListView)
from PyQt5.QtGui import (QIcon, QPixmap, QFont)
from PyQt5.QtCore import Qt, QEventLoop, QSize, QTimer
import sys
import os
import time

from dbcontroller import query_movie, query_tag, query_actress, create_db, addtodb
from MovieMessage import MovieMessage
from dirwallthrough import parse_nfo, create_nfo


video_ext = [".mkv", ".mp4", ".wmv", ".avi"]


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

        self.statusBar = QStatusBar(self)
        self.setStatusBar(self.statusBar)

        bar = self.menuBar()
        file = bar.addMenu("文件")
        adddir = QAction("添加文件夹", self)
        file.addAction(adddir)
        initdb = QAction("初始化", self)
        file.addAction(initdb)
        act_quit = QAction("退出", self)
        file.addAction(act_quit)
        others = bar.addMenu("其他")
        allv = QAction("所有影片", self)
        others.addAction(allv)

        adddir.triggered.connect(self.addDir)
        initdb.triggered.connect(self.initdb)
        act_quit.triggered.connect(self.process_quit)
        allv.triggered.connect(self.allVideo)
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

    def delListWidgetItems(self, listWidget):
        for i in reversed(range(listWidget.count())):
            listWidget.takeItem(0)


    def allVideo(self):
        self.delListWidgetItems(self.movieListWidget)
        del self.movieList

        self.movieList = query_movie()
        self.updateMovieListWidget()
        aftertime = time.time()


    def process_quit(self):
        quit()

    def initdb(self):
        create_db()
        self.updateLabelsWidget()

        self.delListWidgetItems(self.movieListWidget)
        del self.movieList
        self.movieList = query_movie()
        self.updateMovieListWidget()

    def addDir(self):
        
        dlg = QFileDialog()
        dlg.setFileMode(QFileDialog.Directory)

        directory = dlg.getExistingDirectory()

        self.statusBar.clearMessage()
        self.statusBar.showMessage("正在扫描请稍后........", 20000)
        if directory != "":
            for dirpath, dirname, files in os.walk(directory):
                self.statusBar.showMessage(dirpath, 20000)
                for file_name in files:
                    QApplication.processEvents(QEventLoop.ExcludeUserInputEvents)
                    split_name = os.path.splitext(file_name)
                    if split_name[1] in video_ext:
                        movie_detail = {}

                        nfo_path = os.path.join(dirpath, split_name[0]+".nfo")
                        if os.path.isfile(nfo_path):
                            movie_detail = parse_nfo(nfo_path)
                        else:
                            create_nfo(nfo_path)
                            movie_detail["actress"] = ""
                            movie_detail["tags"] = []

                        cover_path = os.path.join(dirpath, split_name[0]+".png")
                        if os.path.isfile(cover_path):
                            with open(cover_path, "rb") as f:
                                movie_detail["cover"] = f.read()
                        else:
                            movie_detail["cover"] = None

                        movie_detail["title"] = split_name[0]
                        movie_detail["video_path"] = os.path.join(dirpath, file_name)

                        # print(movie_detail)
                        addtodb(movie_detail)

            self.updateLabelsWidget()

            self.delListWidgetItems(self.movieListWidget)
            del self.movieList
            self.movieList = query_movie()
            self.updateMovieListWidget()

            self.statusBar.showMessage("扫描结束", 3000)

        else:
            self.statusBar.showMessage("未选择任何文件夹", 3000)


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

        self.updateLabelsWidget()

    def updateLabelsWidget(self):
        self.tags = query_tag()
        self.actor_labels = query_actress()

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
        self.dock_labels.setWidget(widget)



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
        # movieListLayout = QVBoxLayout()
        # movieListLayout.setAlignment(Qt.AlignmentFlag.AlignCenter)


        # movieListWidget.setLayout(movieListLayout)
        # # movieListWidget.setFixedWidth(1000)
        # movieListWidget.adjustSize()
        
        # movieListLayout.addWidget(movieListWidget)

        # self.movieListWidget = self.addMovieWidget()
        # self.dock_movieList.setWidget(self.movieListWidget)
        self.updateMovieListWidget()


    def updateMovieListWidget(self):
        
        self.movieListWidget = self.addMovieWidget()

        # TODO: 使滑动更加平滑 NOT WORKING
        self.movieListWidget.setVerticalScrollMode(QAbstractItemView.ScrollPerPixel)
        self.movieListWidget.setVerticalScrollBarPolicy


        self.dock_movieList.setWidget(self.movieListWidget)
        # self.dock_movieList.setWidget(self.scrollBar)

        # print("after set: " + str(time.time()))

    # def process_thread(self, listWidget):
    #     self.movieListWidget = listWidget
    #     self.dock_movieList.setWidget(self.movieListWidget)


    def init(self):
        self.setWindowTitle('Movie Collection')
        width = QApplication.desktop().width()
        height = QApplication.desktop().height()
        # self.move(int(width * 0.05), int(height * 0.01) )
        # self.resize(int(width ), int(height ) )

        self.penWidth = 25
        self.regularImageWidth = 210
        self.regularImageHeight = int(210 * 1.4) 
        self.fontStyle = "{ font-family:'Microsoft YaHei';" + "font-size:25px;color:#666666;}"

        self.CreateLayout()

        # self.show()

    def addLabelsTagWidget(self):
        listwidget = QListWidget(self.dock_labels)

        # listwidget.setItemAlignment(Qt.AlignCenter)
        # listwidget.setIconSize(QSize(30, self.regularImageHeight))
        listwidget.setResizeMode(QListView.Adjust)
        listwidget.setViewMode(QListView.IconMode)
        listwidget.setMovement(QListView.Static)
        listwidget.setSpacing(10)

        for i in range(len(self.tags)):
            item = QListWidgetItem(self.tags[i])
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
        text = item.text()
        if text == "未知姓名":
            searchtext = ""
        else:
            searchtext = text

        self.delListWidgetItems(self.movieListWidget)
        del self.movieList
        self.movieList = query_movie(actress=searchtext)
        self.updateMovieListWidget()

    def searchMovieWithTag(self, item):
        self.delListWidgetItems(self.movieListWidget)
        self.movieListWidget.deleteLater()
        del self.movieList
        self.movieList = query_movie(tag=item.text())
        self.updateMovieListWidget()


    def addMovieWidget(self):
        listWidget = MovieListWidget(self)
        listWidget.setI_mainWindow(self)
        # listWidget.setItemAlignment(Qt.AlignCenter)
        listWidget.setIconSize(QSize(self.regularImageWidth, self.regularImageHeight))
        listWidget.setResizeMode(QListView.Adjust)
        listWidget.setViewMode(QListView.IconMode)
        listWidget.setMovement(QListView.Static)
        listWidget.setSpacing(30)

        with open("./resource/no_image.png", "rb") as f:
            null_poster = f.read()

        for i in self.movieList.keys():
            QApplication.processEvents(QEventLoop.ExcludeUserInputEvents)
            poster = self.movieList[i]['cover']
            if poster is None:
                poster = null_poster
            pm = QPixmap()
            pm.loadFromData(poster, "png")

            item = QListWidgetItem(QIcon(pm.scaled(QSize(self.regularImageWidth, self.regularImageHeight))), self.movieList[i]['title'])
            # item = QListWidgetItem("test")
            font = QFont()
            font.setPixelSize(25)
            item.setFont(font)
            item.index = i
            item.setSizeHint(QSize(self.regularImageWidth, self.regularImageHeight+30))
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
        self.I_mainWindow.win_message.setIndex(item.index)
        self.I_mainWindow.win_message.setMessage(self.I_mainWindow.movieList[item.index])


        self.I_mainWindow.win_message.exec_()
        self.timer.timeout.disconnect()


        # cmd = ("PotPlayerMini64.exe " + self.movieList[1]['video_path'])
        # os.popen(cmd)
    def movieDoubleClicked(self, item):
        self.timer.stop()
        self.timer.timeout.disconnect()

        videoPath = self.I_mainWindow.movieList[item.index]['video_path']
        cmd = ("PotPlayerMini64.exe " + videoPath)
        os.popen(cmd)

    
# class LoadMovieListWidget(QThread):
#     trigger = pyqtSignal()
#     movieList = dict()
#     def __init__(self, movieList):
#         super(LoadMovieListWidget, self).__init__()
#         self.movieList = movieList

#     def run(self):
#         listWidget = MovieListWidget(self)
#         listWidget.setI_mainWindow(self)
#         # listWidget.setItemAlignment(Qt.AlignCenter)
#         listWidget.setIconSize(QSize(self.regularImageWidth, self.regularImageHeight))
#         listWidget.setResizeMode(QListView.Adjust)
#         listWidget.setViewMode(QListView.IconMode)
#         listWidget.setMovement(QListView.Static)
#         listWidget.setSpacing(30)

#         for i in self.movieList.keys():
#             posterPath = self.movieList[i]['cover_path']
#             if posterPath == "":
#                 posterPath = "./resource/no_image.jpg"
#             pm = QPixmap(posterPath)

#             item = QListWidgetItem(QIcon(pm.scaled(QSize(self.regularImageWidth, self.regularImageHeight))), self.movieList[i]['title'])
#             # item = QListWidgetItem("test")
#             font = QFont()
#             font.setPixelSize(25)
#             item.setFont(font)
#             item.index = i
#             item.setSizeHint(QSize(self.regularImageWidth, self.regularImageHeight+30))
#             # listWidget.insertItem(i, item)
#             listWidget.addItem(item)
#         # listWidget.itemClicked.connect(listWidget.movieClicked)
#         listWidget.itemDoubleClicked.connect(listWidget.movieDoubleClicked)
#         listWidget.itemPressed.connect(listWidget.mousePressed)
#             # item.clicked.connect(self.movieClicked)
#             # listwidget.ItemClicked.connect(movieClicked)
#         self.trigger.emit(listWidget)

if __name__ == '__main__':

    app = QApplication(sys.argv)
    uiSystem = mainWindow()
    #test1.Test()
    uiSystem.showMaximized()
    sys.exit(app.exec_())
    # except:
    #     while True:
    #         pass
