import sys

from PyQt5.QtCore import QModelIndex, Qt
from PyQt5.QtWidgets import QWidget, QTableWidget, QApplication, QTableWidgetItem, QAbstractItemView

from src.single.single import Singleton


class SongTable(Singleton, QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        tableWidget = QTableWidget(self)  # 创建一个表格

        # 标头内容
        tableHead = ["标题", "歌手", "专辑", "时长"]
        # 数据字段
        tableZd = ["title", "songer", "album", "long"]

        # 表格内容
        songList = [
            {"title": "Fallen Angel", "songer": "Mitsunori Ikeda", "album": 'Panty&Stocking', "long": "04:27"},
            {"title": "霞光", "songer": "曲锦楠", "album": '霞光', "long": "02:37", "mm": '233'},
            {"title": "New Kings", "songer": "遠藤幹雄", "album": 'K MISSING KINGS Original Sound Track', "long": "03:01"},
        ]

        # 列数
        tableWidget.setColumnCount(len(tableHead))
        # 行数
        tableWidget.setRowCount(len(songList))
        # 设置横标题
        tableWidget.setHorizontalHeaderLabels(tableHead)
        # 设置总标题，序号
        tableWidget.setVerticalHeaderLabels([str(i) for i in range(1, len(songList) + 1)])
        # 点击
        tableWidget.clicked.connect(self.playSong)
        # 双击
        tableWidget.doubleClicked.connect(self.playSong)
        # 禁止编辑
        tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)

        for songMsgDup in [
            (colIndex, rowIndex, songList[colIndex].get(tableZd[rowIndex]))  # (列数,行数,内容)
            for rowIndex in range(len(tableZd))  # 第几列
            for colIndex in range(len(songList))  # 第几行
        ]:
            print(songMsgDup)
            tableWidget.setItem(songMsgDup[0], songMsgDup[1], QTableWidgetItem(songMsgDup[2]))

        tableWidget.resize(600, 600)
        self.resize(600, 600)
        self.show()

    def playSong(self, model: QModelIndex):
        print(model.row())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = SongTable()
    sys.exit(app.exec_())
