import sys

from PyQt5.QtWidgets import QApplication

from src.ui.bottom import Bottom
from src.ui.head import Head
from src.ui.left import Left

if __name__ == "__main__":
    app = QApplication(sys.argv)
    print(Left() is Left())
    print(Left() is Left())
    print(Left() is Left())
    print(Left() is Left())
    print("-------------")
    print(Head() is Head())
    print(Head() is Head())
    print(Head() is Head())
    print(Head() is Head())
    print("-------------")
    print(Head() is Left())
    print(Head() is Left())
    print(Head() is Left())
    print(Head() is Left())
    Bottom()
    sys.exit(app.exec_())
