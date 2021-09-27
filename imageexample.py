import sys
from PyQt5 import QtCore, QtWidgets
from PyQt5 import QtGui
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QGridLayout, QWidget
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt

class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.im = QPixmap("./patrick-schneider-I4fDK4Fz_vw-unsplash.jpg")
        smaller_pixmap = self.im.scaled(700,400,Qt.KeepAspectRatio )
        self.test = True;
        self.label = QLabel()
        self.label.setPixmap(smaller_pixmap)

        self.grid = QGridLayout()
        self.grid.addWidget(self.label,1,1)
        self.setLayout(self.grid)
        btn = QtWidgets.QPushButton("Quit", self)
        btn.clicked.connect(self.close_application)
        btn.resize(btn.minimumSizeHint())
        btn.move(0,100)
        self.setGeometry(50,50,320,200)
        self.setWindowTitle("PyQT show image")
        self.show()
    def close_application(self):
        self.test =  not self.test
        print("whooaaaa so custom!!!")
        img = "./patrick-schneider-I4fDK4Fz_vw-unsplash.jpg"
        if(self.test):
            img = "./vadim-sadovski-Bu8UgMfqACs-unsplash.jpg"
            
        tm = QPixmap(img)
        smaller_pixmap = tm.scaled(700,400,Qt.KeepAspectRatio )
        self.label.setPixmap(smaller_pixmap)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())