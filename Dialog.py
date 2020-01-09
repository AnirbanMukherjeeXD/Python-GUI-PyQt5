import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QMessageBox

def dialog():
    mbox = QMessageBox()

    mbox.setText("This is a sample text")
    mbox.setDetailedText("This is detailed sample text")
    mbox.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
            
    mbox.exec_()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = QWidget()
    w.resize(300,300)
    w.setWindowTitle('Welcome')
    
    label = QLabel(w)
    label.setText("This is PyQt5, Python")
    label.move(100,100)
    label.show()

    btn = QPushButton(w)
    btn.setText('Check this out')
    btn.move(110,150)
    btn.show()
    btn.clicked.connect(dialog)

    
    w.show()
    sys.exit(app.exec_())