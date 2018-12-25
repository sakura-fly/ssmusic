import sys

import time
from PyQt5.QtWidgets import QWidget, QHBoxLayout, QApplication, QVBoxLayout

from src.single.single import Singleton
from src.ui.orderList import OrderList
from src.ui.playingSong import PlayingSong


class Left(Singleton, QWidget):

    def initUI(self):
        with open("../../qss/left.qss") as f:
            ss = f.read()
        self.setStyleSheet(ss)

        layout = QVBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)
        self.orderList = OrderList()
        self.playintSong = PlayingSong()
        layout.addWidget(self.orderList)
        layout.addWidget(self.playintSong)

        self.setMaximumWidth(160)
        self.setLayout(layout)

    # def keyPressEvent(self, QKeyEvent):
    #     print(QKeyEvent.key())
    #     self.playintSong.changeSong(str(QKeyEvent.key()))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    left = Left()
    left.show()
    sys.exit(app.exec_())
