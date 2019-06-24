import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QHBoxLayout, QLabel, QListView, QListWidget, QListWidgetItem
from PyQt5.QtCore import QSize
from PyQt5.QtGui import QStandardItemModel, QPixmap, QIcon, QFont


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)

        listwidget = QListWidget(self)
        listwidget.setIconSize(QSize(100, 70))
        listwidget.setResizeMode(QListView.Adjust)
        listwidget.setViewMode(QListView.IconMode)
        listwidget.setMovement(QListView.Static)
        listwidget.setSpacing(10)

        for i in range(10):
            # imagepath = "./images/screen.png"
            # pm = QPixmap(imagepath)
            # item = QListWidgetItem(QIcon(pm.scaled(QSize(100, 70))), "testpng")
            item = QListWidgetItem("test")
            font = QFont()
            font.setPixelSize(30)
            item.setFont(font)
            print(item.text())

            item.setSizeHint(QSize(100, 80))
            listwidget.insertItem(i, item)

        self.setCentralWidget(listwidget)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainform = MainWindow()
    mainform.show()
    mainform.listwidget = None
    # mainform.setCentralWidget(mainform.listwidget)
    sys.exit(app.exec())

