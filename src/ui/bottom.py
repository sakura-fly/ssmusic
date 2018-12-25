import os
import sys

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QWidget, QPushButton, QLabel, QSlider, QHBoxLayout, QApplication

from src.single.single import Singleton


class Bottom(Singleton, QWidget):

    def initUI(self):
        previousBtn = QLabel()
        playBtn = QLabel()
        nextBtn = QLabel()


        previousBtn.setMinimumSize(30, 30)
        playBtn.setMinimumSize(30, 30)
        nextBtn.setMinimumSize(30, 30)
        previousBtn.setMaximumSize(30, 30)
        playBtn.setMaximumSize(30, 30)
        nextBtn.setMaximumSize(30, 30)

        playImgPath = os.path.join(os.path.abspath("../../"), "resource", "img", "play.png")
        playPixmap = QPixmap(playImgPath).scaled(previousBtn.width(), previousBtn.height())

        nextImgPath = os.path.join(os.path.abspath("../../"), "resource", "img", "next.png")
        nextPixmap = QPixmap(nextImgPath).scaled(previousBtn.width(), previousBtn.height())

        previousImgPath = os.path.join(os.path.abspath("../../"), "resource", "img", "previous.png")
        previousPixmap = QPixmap(previousImgPath).scaled(previousBtn.width(), previousBtn.height())

        previousBtn.setPixmap(nextPixmap)
        playBtn.setPixmap(playPixmap)
        nextBtn.setPixmap(previousPixmap)

        playedTime = QLabel("00:00")
        songLong = QLabel("04:00")

        sld = QSlider(Qt.Horizontal)
        sld.valueChanged[int].connect(self.volumeChange)

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


if __name__ == "__main__":
    app = QApplication(sys.argv)
    head = Bottom()
    head.show()
    sys.exit(app.exec_())
