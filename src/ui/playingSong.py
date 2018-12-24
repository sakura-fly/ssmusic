import os
import sys

from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QApplication

from src.single.single import Singleton


class PlayingSong(Singleton, QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()
        self.songNameLabel = QLabel("songName")
        self.songerLabel = QLabel("songer")

        layout.addWidget(self.songerLabel)
        layout.addWidget(self.songNameLabel)
        self.setLayout(layout)

    def changeSong(self, index):
        self.songNameLabel.setText(index)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    orderList = PlayingSong()
    orderList.show()
    sys.exit(app.exec_())
