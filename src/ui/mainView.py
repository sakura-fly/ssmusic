import sys

from PyQt5.QtWidgets import QApplication

from src.ui.bottom import Bottom
from src.ui.head import Head
from src.ui.left import Left

if __name__ == "__main__":
    app = QApplication(sys.argv)
    head = Bottom()
    head.show()
    sys.exit(app.exec_())
