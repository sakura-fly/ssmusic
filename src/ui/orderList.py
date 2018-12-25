import os
import sys

from PyQt5.QtGui import QStandardItem, QIcon, QStandardItemModel
from PyQt5.QtWidgets import QWidget, QListView, QApplication, QMessageBox

from src.single.single import Singleton
from src.ui.playingSong import PlayingSong


class OrderList(Singleton, QListView):
    # def __init__(self):
    #     super().__init__()
    #
    #     self.initUI()

    def initUI(self):
        self.setViewMode(QListView.ListMode)
        mOrderList = [
            "列表1",
            "列表2",
            "列表3",
            "列表4",
            "列表5",
            "列表6",
            "列表7",
        ]
        model = QStandardItemModel()
        for order in mOrderList:
            item = QStandardItem(QIcon(os.path.join(os.path.abspath("../../"), "resource", "img", "rin.png")), order)
            model.appendRow(item)
        self.clicked.connect(self.clickOrder)
        self.setModel(model)

    def clickOrder(self, index):
        print("ListView", "选择项是：%d" % (index.row()))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    orderList = OrderList()
    orderList.show()
    sys.exit(app.exec_())
