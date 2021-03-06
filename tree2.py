import sys
from collections import deque
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
class view(QWidget):
    def __init__(self, data):
        super(view, self).__init__()
        self.tree = QTreeView(self)
        layout = QVBoxLayout(self)
        layout.addWidget(self.tree)
        self.model = QStandardItemModel()
        self.model.setHorizontalHeaderLabels(['Name', 'Height', 'Weight'])
        self.tree.header().setDefaultSectionSize(180)
        self.tree.header().setStretchLastSection(False)
        #
        self.tree.setModel(self.model)
        self.tree.header().resizeSection(1, 400)
        self.tree.header().setMinimumSectionSize(100)
        self.tree.header().resizeSection(0, 100)
        self.tree.header().setSectionResizeMode(0,QHeaderView.ResizeMode.Stretch); 
        #self.tree.resizeColumnToContents(0)
        self.importData(data)
        self.tree.expandAll()
    def importData(self, data, root=None):
        self.model.setRowCount(0)
        if root is None:
            root = self.model.invisibleRootItem()
        seen = {}   # List of  QStandardItem
        values = deque(data)
        while values:
            value = values.popleft()
            if value['unique_id'] == 1:
                parent = root
            else:
                pid = value['parent_id']
                if pid not in seen:
                    values.append(value)
                    continue
                parent = seen[pid]
            unique_id = value['unique_id']
            parent.appendRow([
                QStandardItem(value['short_name']),
                QStandardItem(value['height']),
                QStandardItem(value['weight'])
            ])
            seen[unique_id] = parent.child(parent.rowCount() - 1)
if __name__ == '__main__':
    data = [
        {'unique_id': 1, 'parent_id': 0, 'short_name': 'Tahid', 'height': ' ', 'weight': ' '},
        {'unique_id': 1, 'parent_id': 0, 'short_name': 'Class 1', 'height': ' ', 'weight': ' '},
        {'unique_id': 1, 'parent_id': 0, 'short_name': 'Lucy', 'height': '162', 'weight': '50'},
        {'unique_id': 1, 'parent_id': 0, 'short_name': 'Joe', 'height': '175', 'weight': '65'},
        {'unique_id': 1, 'parent_id': 0, 'short_name': 'Class 2', 'height': ' ', 'weight': ' '},
        {'unique_id': 2, 'parent_id': 1, 'short_name': 'Lily', 'height': '170', 'weight': '55'},
        {'unique_id': 1, 'parent_id': 0, 'short_name': 'Tom', 'height': '180', 'weight': '75'},
        {'unique_id': 1, 'parent_id': 0, 'short_name': 'Class 3', 'height': ' ', 'weight': ' '},
        {'unique_id': 3, 'parent_id': 1, 'short_name': 'Jack', 'height': '178', 'weight': '80'},
        {'unique_id': 4, 'parent_id': 1, 'short_name': 'Tim', 'height': '172', 'weight': '60'}
    ]
    app = QApplication(sys.argv)
    app.setStyle('Fusion')  
    view = view(data)
    view.setGeometry(300, 100, 600, 300)
    view.setWindowTitle('QTreeview Example')
    view.show()
    sys.exit(app.exec_())