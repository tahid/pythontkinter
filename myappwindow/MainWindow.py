import sys
from PyQt5 import QtGui
from PyQt5 import QtWidgets

from PyQt5.QtCore import QSize, Qt
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import (
    QAction,
    QApplication,
    QCheckBox,
    QLabel,
    QMainWindow,
    QStatusBar,
    QToolBar,
)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("House Auction Software")
        self.resize(1200, 800)
        label = QLabel("Hello!")
        label.setAlignment(Qt.AlignCenter)
        self.setCentralWidget(label)
        toolbar = QToolBar("My main toolbar")
        toolbar.setMovable(False)
        toolbar.setIconSize(QSize(24, 24))
        self.addToolBar(toolbar)
        button_action = QAction(QIcon("logo.png"), "&Your button", self)
        button_action.setStatusTip("This is your button")
        button_action.triggered.connect(self.onMyToolBarButtonClick)
        # button_action.setCheckable(True)
        toolbar.addAction(button_action)
        button_action2 = QAction(QIcon("logo.png"), "Your &button2", self)
        button_action2.setStatusTip("This is your button2")
        button_action2.triggered.connect(self.onMyToolBarButtonClick)
        button_action2.setCheckable(True)
        toolbar.addAction(button_action2)
        toolbar.addWidget(QLabel("Hello"))
        toolbar.addWidget(QCheckBox())

        extractAction = QtWidgets.QAction("&GET TO THE CHOPPAH!!!", self)
        extractAction.setShortcut("Ctrl+Q")
        extractAction.setStatusTip('Leave The App')
        extractAction.triggered.connect(self.close_application)
        
        mainMenu = self.menuBar()
        fileMenu = mainMenu.addMenu('&File')
        fileMenu.addAction(extractAction)
        self.home()

    def home(self):
        btn = QtWidgets.QPushButton("Quit", self)
        btn.clicked.connect(self.close_application)
        btn.resize(btn.minimumSizeHint())
        btn.move(0,100)
    def onMyToolBarButtonClick(self, s):
        print("click", s)
    def close_application(self):
        print("whooaaaa so custom!!!")
        sys.exit()

