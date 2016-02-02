# File explorer class

from PyQt4.QtCore import *
from PyQt4.QtGui import *

import os

class FileExplorerPane(QFrame):
    # This widget will display a list of files in the cwd

    def __init__(self, master):
        super().__init__()
        self.master = master

        self.layout = QVBoxLayout()

        self.files_list = QListView()
        self.files_list.clicked.connect(self.file_click)

        self.layout.addWidget(self.files_list)

        self.update_files_list()

        self.setLayout(self.layout)

    def file_click(self):
        filename = os.listdir(os.getcwd())[self.files_list.currentIndex().row()]
        self.master.open_file(filename)

    def update_files_list(self):
        files = os.listdir(os.getcwd())

        model = QStandardItemModel()

        for f in files:
            tmp = QStandardItem(f)
            tmp.setCheckable(False)
            model.appendRow(tmp)

        self.files_list.setModel(model)
