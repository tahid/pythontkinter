import sys
from PyQt5 import QtGui
from PyQt5 import QtWidgets

from PyQt5.QtCore import QSize, Qt
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import (
    QAction,
    QApplication,
    QBoxLayout,
    QCheckBox,
    QFormLayout,
    QGridLayout,
    QHBoxLayout,
    QLabel,
    QLineEdit,
    QMainWindow,
    QPushButton,
    QStatusBar,
    QTextEdit,
    QToolBar,
    QVBoxLayout,
    QWidget,
)
class SimpleLayout(QWidget):
    def __init__(self):
        super().__init__()
        layout = QGridLayout()
        label1 = QLabel("Hello!")
        button1 = QPushButton("Test")
        button2 = QPushButton("Test2")
        layoutmain = QHBoxLayout(self)
        layout = QFormLayout()
        layout.setFieldGrowthPolicy(QFormLayout.AllNonFixedFieldsGrow)
        # Add widgets to the layout
        layout.addRow("                      big line of text:", QLineEdit())
        layout.addRow( QLineEdit())
        layout.addRow("Name:", QLineEdit())
        layout.addRow("Job:", QLineEdit())
        emailLabel = QLabel("Email:")
        layout.addRow(emailLabel, QLineEdit())
        layoutmain.addLayout(layout,1)
        layoutmain.addWidget(QTextEdit(),3)
        self.setLayout(layoutmain)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("House Auction Software")
        self.setAcceptDrops(True)
        self.resize(1200, 800)
        self.setCentralWidget(SimpleLayout())
           
        toolbar = QToolBar("My main toolbar")
        toolbar.setMovable(False)
        toolbar.setIconSize(QSize(18, 18))
        self.addToolBar(toolbar)
        button_action = QAction(QIcon("toolbar/icons8-auction-50.png"), "&Your button", self)
        button_action.setStatusTip("This is your button")
        button_action.triggered.connect(self.onMyToolBarButtonClick)
        # button_action.setCheckable(True)
        toolbar.addAction(button_action)
        button_action2 = QAction(QIcon("toolbar/icons8-homer-simpson-50.png"), "Your &button2", self)
        button_action2.setStatusTip("This is your button2")
        button_action2.triggered.connect(self.onMyToolBarButtonClick)
        button_action2.setCheckable(True)
        toolbar.addAction(button_action2)
        button_action3 = QAction(QIcon("toolbar/icons8-copybook-50.png"), "Your &button2", self)
        button_action3.setStatusTip("This is your button2")
        button_action3.triggered.connect(self.onMyToolBarButtonClick)
        button_action3.setCheckable(True)
        toolbar.addAction(button_action3)
    def dragEnterEvent(self, event):
        print('drag-enter')
        if event.mimeData().hasUrls():
            print('has urls')
            event.accept()
        else:
            event.ignore()
    def dropEvent(self, event):
        files = [u.toLocalFile() for u in event.mimeData().urls()]
        for f in files:
            print(f)
    def onMyToolBarButtonClick(self, s):
        print("click", s)




if __name__ == "__main__":
    app = QApplication(sys.argv)
    #app.setStyle('Windows')
    window = MainWindow()
    window.show()
    sys.exit(app.exec())