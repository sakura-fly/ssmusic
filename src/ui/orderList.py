import os
import sys

from PyQt5.QtGui import QStandardItem, QIcon, QStandardItemModel
from PyQt5.QtWidgets import QWidget, QListView, QApplication, QMessageBox

from src.ui.playingSong import PlayingSong


class OrderList(QListView):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setViewMode(QListView.ListMode)
        item_1 = QStandardItem(QIcon(os.path.join(os.path.abspath("../../"), "resource", "img", "rin.png")), "列表A");
        item_2 = QStandardItem(QIcon(os.path.join(os.path.abspath("../../"), "resource", "img", "rin.png")), "列表B");
        item_3 = QStandardItem(QIcon(os.path.join(os.path.abspath("../../"), "resource", "img", "rin.png")), "列表C");
        model = QStandardItemModel()
        model.appendRow(item_1)
        model.appendRow(item_2)
        model.appendRow(item_3)
        self.clicked.connect(self.clickOrder)
        self.setModel(model)

    def clickOrder(self, index):
        print("ListView", "选择项是：%d" % (index.row()))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    orderList = OrderList()
    orderList.show()
    sys.exit(app.exec_())
