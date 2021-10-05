import glob
import sys
from PyQt5 import QtCore, QtWidgets
from PyQt5 import QtGui
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QGridLayout, QWidget
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt

class Example(QWidget):

    def __init__(self):
        super().__init__()
        self.qmaps = []
        self.grid = QGridLayout()
        self.two = 1
        tempimg = QPixmap()
        tempimg = tempimg.scaled(800,600,Qt.KeepAspectRatio)
        self.qmaps.append(tempimg)

        self.test = True;
        self.label = QLabel()
        self.index = 0;
        self.label.setPixmap(self.qmaps[self.index])

        
        self.grid.addWidget(self.label,1,1)
        self.setLayout(self.grid)
        btn = QtWidgets.QPushButton("Quit", self)
        btn.clicked.connect(self.close_application)
        btn.resize(btn.minimumSizeHint())
        btn.move(0,100)
        btn = QtWidgets.QPushButton("Load", self)
        btn.clicked.connect(self.load_images)
        btn.resize(btn.minimumSizeHint())
        btn.move(0,300)
        

    #     self.keyPressed = QtCore.pyqtSignal(int)
    #     self.widget.keyPressed.connect(self.on_key)
        self.setGeometry(50,50,920,600)
        self.setWindowTitle("PyQT show image")
        self.setFocusPolicy(Qt.StrongFocus)
        self.show()

    
    
    def load_images(self):
        myfiles = glob.glob("/var/myprojects/tmpimages/new-thumbs/*.jpg")
        for f in myfiles:
            self.two+=1
            tempimg = QPixmap(f)
            # tempimg2 = tempimg.scaled(100,100,Qt.KeepAspectRatio)
            tempimg = tempimg.scaled(800,600,Qt.KeepAspectRatio)
            # tmplabel = QLabel()
            # tmplabel.setPixmap(tempimg2)
            # self.grid.addWidget(tmplabel,1,self.two)
            self.qmaps.append(tempimg)
    def keyPressEvent(self, event):
        key = event.key()
        print('key pressed: %i' % key)
        if key == QtCore.Qt.Key_Z:
            self.close_application()
        elif key == QtCore.Qt.Key_X:
            self.close_application2()
        else:
            print('key pressed: %i' % key)
    def close_application(self):
        self.index+=1
        self.label.setPixmap(self.qmaps[self.index ])
        if((self.index+1)>=len(self.qmaps)):
            self.index=0
    def close_application2(self):
        self.index-=1
        self.label.setPixmap(self.qmaps[self.index ])
        if((self.index+1)<2):
            self.index=len(self.qmaps)
        # self.test =  not self.test
        # print("whooaaaa so custom!!!")
        # if(self.test):
        #     self.label.setPixmap(self.img1)
        # else:
        #     self.label.setPixmap(self.img2)
        

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())