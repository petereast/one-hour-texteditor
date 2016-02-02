from PyQt4 import QtCore, QtGui
import os
from EditPane import *

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.central_widget = QWidget()

        #Minimalist design?

        self.setWindowTitle("PEdit")

        # Define the actions for the menubar

        self.exitAction = QAction("&Exit", self)
        self.exitAction.setShortcut("Ctrl+Q")

        self.openAction = QAction("&Open File...", self)
        self.openAction.setShortcut("Ctrl+O")
        self.openAction.triggered.connect(self._openAction)

        self.saveAction = QAction("&Save", self)
        self.saveAction.setShortcut("Ctrl+S")
        self.saveAction.triggered.connect(self._save_action)

        self.newAction = QAction("&New File", self)
        self.newAction.setShortcut("Ctrl+N")
        self.newAction.triggered.connect(self._new_file_action)


        # Define the menubar

        self.menubar = self.menuBar()
        filemenu = self.menubar.addMenu("&file")
        filemenu.addAction(self.exitAction)
        filemenu.addAction(self.openAction)
        filemenu.addAction(self.newAction)
        filemenu.addAction(self.saveAction)

        self.layout = QVBoxLayout()
        self.tab_switcher = QTabWidget()

        edit = FileEditor()
        self.tab_switcher.addTab(edit, "file0")
        self.layout.addWidget(self.tab_switcher)
        self.tab_switcher.setTabsClosable(True)


        self.central_widget.setLayout(self.layout)
        self.setCentralWidget(self.central_widget)

        self.setGeometry(400, 400, 400, 400)

        self.news = 1

    def _openAction(self):
        cwd = os.getcwd()
        filename = QFileDialog.getOpenFileName(self, "Open File", cwd, "")

        # Get the last part of the filename
        filename_end = filename.rsplit("/")[-1]

        self.tab_switcher.addTab(FileEditor(open(filename)), filename_end)
        self.tab_switcher.setCurrentIndex(len(self.tab_switcher)+1)

    def _new_file_action(self):
        self.tab_switcher.addTab(FileEditor(None), "new{0}".format(self.news-1))
        self.news+=1

    def _save_action(self):
        ci = self.tab_switcher.currentIndex()
        current = self.tab_switcher.widget(ci)
        if current.file == None:
            # No filename defined - show the open dialog box...
            cwd = os.getcwd()
            filename = QFileDialog.getSaveFileName(self, "Save File", cwd, "")
        else:
            filename = current.file.name

        with open(filename, "w") as f:
            f.write(current.editor.toPlainText())
        print("Saved")
