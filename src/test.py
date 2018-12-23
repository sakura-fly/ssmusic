import sys

from PyQt5.QtWidgets import QWidget, QVBoxLayout, QTextEdit, QApplication


class Test(QWidget):
    def __init__(self):
        super().__init__()

        self.inintUI()

    def inintUI(self):
        qv = QVBoxLayout()

        texted1 = QTextEdit()
        texted2 = QTextEdit()

        texted1.resize(300, 300)

        qv.addWidget(texted1)
        qv.addWidget(texted2)

        self.setLayout(qv)

        self.show()


app = QApplication(sys.argv)
test = Test()
sys.exit(app.exec_())
