# This is the editing widget

from PyQt4.QtCore import *
from PyQt4.QtGui import *

class FileEditor(QWidget):
    def __init__(self, file=None):
        super().__init__()

        self.file = file

        if file != None:
            tmp_text = "<br>".join(file.readlines())
            text = ''
            for c in tmp_text:
                if c == ' ':
                    text+='&nbsp;'
                else:
                    text += c
            print(text)
        else:
            text = ""

        self.layout = QVBoxLayout()

        self.editor = QTextEdit(text)
        self.layout.addWidget(self.editor)

        self.setLayout(self.layout)


#STOPPED WITH 25m53s remaining
#TODO: Add some kind of paragraphing so that indenting works.
