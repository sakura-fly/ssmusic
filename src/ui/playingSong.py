import os
import sys

from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QApplication

from src.model.song import Song
from src.single.single import Singleton


class PlayingSong(Singleton, QWidget):
    # def __init__(self):
    #     super().__init__()
    #
    #     self.initUI()

    def initUI(self):
        layout = QVBoxLayout()
        self.songNameLabel = QLabel("songName")
        self.songerLabel = QLabel("songer")

        layout.addWidget(self.songNameLabel)
        layout.addWidget(self.songerLabel)
        self.setLayout(layout)

    def changeSong(self, song: Song):
        self.songNameLabel.setText(song.title)
        self.songerLabel.setText(song.songer)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    orderList = PlayingSong()
    orderList.show()
    sys.exit(app.exec_())
