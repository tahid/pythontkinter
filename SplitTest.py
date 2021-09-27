import sys
import myappwindow.MainWindow as mw

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


app = QApplication(sys.argv)
# app.setStyle('Fusion')
window = mw.MainWindow()
#window.setGeometry(300, 100, 1200, 900)
window.show()

app.exec()
