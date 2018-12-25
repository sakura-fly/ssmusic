import os
import sys

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QWidget, QPushButton, QLabel, QSlider, QHBoxLayout, QApplication

from src.single.single import Singleton


class Bottom(Singleton, QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        previousBtn = QLabel()
        playBtn = QLabel()
        nextBtn = QLabel()

        imgPath = os.path.join(os.path.abspath("../../"), "resource", "img", "rin.png")
        pixmap = QPixmap(imgPath).scaled(previousBtn.width(), previousBtn.height())

        previousBtn.setPixmap(pixmap)
        playBtn.setPixmap(pixmap)
        nextBtn.setPixmap(pixmap)

        previousBtn.setMinimumSize(20, 20)
        playBtn.setMinimumSize(20, 20)
        nextBtn.setMinimumSize(20, 20)
        previousBtn.setMaximumSize(20, 20)
        playBtn.setMaximumSize(20, 20)
        nextBtn.setMaximumSize(20, 20)

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
