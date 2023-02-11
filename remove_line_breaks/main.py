import sys
import re
from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox
from ui_mainwindow import Ui_MainWindow
import pyperclip

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.remove_btn.clicked.connect(self.remove_line_breaks)
        self.ui.reset_btn.clicked.connect(self.reset)
        self.ui.copy_btn.clicked.connect(self.copy_to_clipboard)

    def remove_line_breaks(self):
        self.ui.clear_text.setPlainText(re.sub(' +', ' ', self.ui.plain_text.toPlainText().replace("\n", " ")))

    def reset(self):
        self.ui.plain_text.setPlainText("")
        self.ui.clear_text.setPlainText("")
    
    def copy_to_clipboard(self):
        text = self.ui.clear_text.toPlainText()
        if len(text) > 0:
            pyperclip.copy(text)
            msg = QMessageBox()
            msg.setText("Successfully copied to clipboard.")
            msg.exec()

app = QApplication(sys.argv)
main_window = MainWindow()
main_window.show()
app.exec()