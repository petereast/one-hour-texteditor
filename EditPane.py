# This is the editing widget

from PyQt4.QtCore import *
from PyQt4.QtGui import *

from SyntaxHighlighter import *

class FileEditor(QWidget):
    def __init__(self, file=None, master = None):
        super().__init__()

        self.file = file
        text = ''
        if file != None:
            tmp_text = "<br>".join(DocumentObj(file.read()).convert_to_html())

            for c in tmp_text:
                if c == ' ':
                    text+='&nbsp;'
                else:
                    text += c

        self.layout = QVBoxLayout()

        self.editor = QTextEdit(text)
        self.editor.keyReleaseEvent = self.syntax_update
        self.layout.addWidget(self.editor)

        self.sabutton = QPushButton("Update syntex highlight")
        self.sabutton.clicked.connect(self.syntax_update)
        self.layout.addWidget(self.sabutton)

        self.setLayout(self.layout)

    def syntax_update(self, ev=None):
        if ev.text() == " ":
            self.cursorPos = self.editor.textCursor().position()
            #self.editor.setPlainText(self.editor.toPlainText()+ev.text())
            tmp_text = "<br>".join(DocumentObj(self.editor.toPlainText()).convert_to_html())
            text = ''
            for c in tmp_text:
                if c == ' ':
                    text += '&nbsp;'
                else:
                    text += c

            self.editor.setHtml(text)
            new_cursor = QTextCursor()
            new_cursor.setPosition(self.cursorPos)
            self.editor.setTextCursor(new_cursor)


#STOPPED WITH 25m53s remaining
#TODO: Add some kind of paragraphing so that indenting works.
