import sys

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout

from src.single.single import Singleton
from src.ui import playingSong
from src.ui.bottom import Bottom
from src.ui.head import Head
from src.ui.left import Left
from src.ui.playingSong import PlayingSong
from src.ui.songTable import SongTable


class MainView(Singleton, QWidget):
    # def __init__(self):
    #     super().__init__()
    #
    #     self.initUI()

    def initUI(self):
        mainLayout = QVBoxLayout()
        centerLayout = QHBoxLayout()

        left = Left()
        songTable = SongTable()
        head = Head()
        bottom = Bottom()

        left.setMaximumWidth(160)

        centerLayout.addWidget(left)
        centerLayout.addWidget(songTable)

        centerQWidget = QWidget()
        centerQWidget.setLayout(centerLayout)

        mainLayout.addWidget(head)
        mainLayout.addWidget(centerQWidget)
        mainLayout.addWidget(bottom)

        self.setLayout(mainLayout)
        # self.setWindowFlags(Qt.SplashScreen)
        self.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main = MainView()
    # head = Bottom()
    # head.show()
    sys.exit(app.exec_())
