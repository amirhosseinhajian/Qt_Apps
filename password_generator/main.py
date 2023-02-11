import sys
from random import choice, shuffle, sample
from PySide6.QtWidgets import QApplication, QMainWindow
from ui_mainwindow import Ui_MainWindow

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.lower_case_chars = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
                                 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                                 'u', 'v', 'w', 'x', 'y', 'z']
        self.upper_case_chars = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J',
                                 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
                                 'U', 'V', 'W', 'X', 'Y', 'Z']
        self.numbers = [str(i) for i in range(0, 10)]
        self.special_chars = ["~", "!", "@", "#", "$", "%", "^", "&", "*", "(",
                               ")", "-", "_", "+", "=", "{", "}", "[", "]", "|", 
                               "/", ":", ";", "<", ">", ",", ".", "?"]
        self.all_chars = self.lower_case_chars + self.upper_case_chars + self.numbers + self.special_chars
        shuffle(self.all_chars)
        self.ui.generate_btn.clicked.connect(self.generate_password)

    def generate_password(self):
        if self.ui.strong_password_btn.isChecked():
            self.generate_standard_password()
        elif self.ui.extera_strong_password_btn.isChecked():
            self.generate_extra_strong_password()
        else:
            self.generate_super_strong_password()

    def generate_basic_password(self):
        password = choice(self.upper_case_chars)
        password += choice(self.numbers)
        password += choice(self.special_chars)
        return password

    def generate_standard_password(self):
        password = self.generate_basic_password()
        for i in range(5):
            password += choice(self.lower_case_chars)
        self.ui.password.setText(''.join(sample(password, len(password))))

    def generate_extra_strong_password(self):
        password = self.generate_basic_password()
        for i in range(9):
            password += choice(self.all_chars)
        self.ui.password.setText(''.join(sample(password, len(password))))
    
    def generate_super_strong_password(self):
        password = self.generate_basic_password()
        for i in range(17):
            password += choice(self.all_chars)
        self.ui.password.setText(''.join(sample(password, len(password))))

app = QApplication(sys.argv)
main_window = MainWindow()
main_window.show()
app.exec()