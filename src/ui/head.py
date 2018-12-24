import os
import sys

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QTextLine, QPixmap
from PyQt5.QtWidgets import QWidget, QLabel, QHBoxLayout, QApplication, QLineEdit, QPushButton


class Head(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # 左边标题
        title = QLabel("music")

        # 搜索框
        search = QLineEdit()
        # 提示内容
        search.setPlaceholderText("搜索")
        search.setMaximumWidth(200)
        # 绑定回车时间
        search.returnPressed.connect(self.search)

        # 放了个图片
        uNameLabel = QLabel("sakura")
        closeLabel = QLabel()
        imgPath = os.path.join(os.path.abspath("../../"), "resource", "img", "rin.png")
        pixmap = QPixmap(imgPath).scaled(closeLabel.width(), closeLabel.height())
        closeLabel.setPixmap(pixmap)
        closeLabel.setMinimumSize(40, 40)
        closeLabel.setMaximumSize(40, 40)

        # 横布局
        headLayout = QHBoxLayout()
        headLayout.addWidget(title)
        headLayout.addWidget(search)

        headLayout.addStretch(1)

        headLayout.addWidget(uNameLabel)
        headLayout.addWidget(closeLabel)

        self.setLayout(headLayout)
        # self.setWindowFlags(Qt.FramelessWindowHint)

    # 查询方法
    def search(self):
        searchMsg = self.sender().text()
        print(searchMsg)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    head = Head()
    head.show()
    sys.exit(app.exec_())
