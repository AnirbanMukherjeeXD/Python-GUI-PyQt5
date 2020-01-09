import sys
from PyQt5.QtWidgets import QApplication, QWidget
if __name__ == "__main__":
    app = QApplication([])
    w = QWidget()
    w.resize(300,300)
    w.setWindowTitle('HelloWorld !')
    w.show()
    sys.exit(app.exec_())