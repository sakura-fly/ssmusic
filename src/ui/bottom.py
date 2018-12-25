import os
import sys

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QWidget, QPushButton, QLabel, QSlider, QHBoxLayout, QApplication

from src.single.single import Singleton


class Bottom(Singleton, QWidget):

    def initUI(self):
        previousBtn = QPushButton()
        playBtn = QPushButton()
        nextBtn = QPushButton()

        previousBtn.setMinimumSize(30, 30)
        playBtn.setMinimumSize(30, 30)
        nextBtn.setMinimumSize(30, 30)
        previousBtn.setMaximumSize(30, 30)
        playBtn.setMaximumSize(30, 30)
        nextBtn.setMaximumSize(30, 30)

        playedTime = QLabel("00:00")
        songLong = QLabel("04:00")

        sld = QSlider(Qt.Horizontal)
        sld.valueChanged[int].connect(self.volumeChange)

        playBtn.setStyleSheet("QPushButton{border-image: url(../../resource/img/play.png)}")
        previousBtn.setStyleSheet("QPushButton{border-image: url(../../resource/img/previous.png)}")
        nextBtn.setStyleSheet("QPushButton{border-image: url(../../resource/img/next.png)}")

        playBtn.clicked.connect(self.playSong)
        previousBtn.clicked.connect(self.previousSong)
        nextBtn.clicked.connect(self.nextSong)

        layout = QHBoxLayout()
        layout.addWidget(previousBtn)
        layout.addWidget(playBtn)
        layout.addWidget(nextBtn)
        layout.addWidget(playedTime)
        layout.addWidget(sld)
        layout.addWidget(songLong)

        self.setLayout(layout)

    def volumeChange(self, value):
        print("音量", value)

    def playSong(self):
        print("play")

    def previousSong(self):
        print("previous")

    def nextSong(self):
        print("next")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    head = Bottom()
    head.show()
    sys.exit(app.exec_())
