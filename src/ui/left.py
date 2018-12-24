import sys

from PyQt5.QtWidgets import QWidget, QHBoxLayout, QApplication, QVBoxLayout

from src.ui.orderList import OrderList
from src.ui.playingSong import PlayingSong


class Left(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()
        self.orderList = OrderList()
        self.playintSong = PlayingSong()
        layout.addWidget(self.orderList)
        layout.addWidget(self.playintSong)
        self.setLayout(layout)

    def keyPressEvent(self, QKeyEvent):
        print(QKeyEvent.key())
        self.playintSong.changeSong(str(QKeyEvent.key()))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    left = Left()
    left.show()
    sys.exit(app.exec_())
