import sys
from math import ceil
from random import randint
from functools import partial
from PySide6.QtWidgets import *
from PySide6.QtCore import *
from main_window import Ui_MainWindow
from sudoku import Sudoku

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.light_mode_style = '''
        * {
            background-color: white;
            }
        QMenuBar { 
            background-color: #262626;
            color: white;
              }
        QMenuBar::item::selected {
            color: blue;
            background-color: white;
        }
        QMenu::item::selected {
            color: blue;
        }
        color_mood_btn{
            background-color: red;
            color: blue;
        }
        '''
        self.dark_mode_style = '''
        * {
            background-color: #262626;
            }
        QMenuBar { 
            background-color: white;
            color: black;
              }
        QMenuBar::item::selected {
            color: white;
            background-color: black;
        }   
        QMenu {
            background-color: white;
        }
        QMenu::item::selected {
            color: blue;
        } 
        '''
        self.wrong_guesses = []
        self.current_style = self.light_mode_style
        self.setStyleSheet(self.current_style)
        self.line_edits = [[None for i in range(9)] for j in range(9)]
        self.ui.menu_new.triggered.connect(self.new_board)
        self.ui.menu_open_file.triggered.connect(self.open_file)
        self.new_game(Sudoku(3, seed=randint(1, 1000)).difficulty(0.5))
        self.ui.color_mood_btn.clicked.connect(self.color_mood_toggle)
        self.set_line_edits_color()
        self.ui.menu_about.triggered.connect(self.show_about)
        self.ui.menu_exit.triggered.connect(self.exit)
        self.ui.menu_solve.triggered.connect(self.show_solve)
        self.ui.menu_help_.triggered.connect(self.help)

    def help(self):
        is_changed = False
        for i, row in enumerate(self.line_edits):
            for j, col in enumerate(row):
                if col.text() == "":
                    col.setText(str(self.solve.board[i][j]))
                    is_changed = True
                    break
            if is_changed:
                break

    def show_solve(self):
        for i, row in enumerate(self.line_edits):
            for j, col in enumerate(row):
                col.setText(str(self.solve.board[i][j]))

    def exit(self):
        sys.exit(app.exec())

    def show_about(self):
        msg = QMessageBox()
        msg.setText("""سودوکو یک بازی معمایی است که شامل جدولی ۹ در ۹ خانه‌ایاست که باید با قرار دادن اعداد از ۱ تا ۹ در آن، خانه‌های خالی را پر کنید. هر سطر، ستون و بلوک ۳ در ۳ باید شامل همه اعداد از ۱ تا ۹ باشدو هیچ عدد تکراری نباید در هر سطر، ستون و بلوک وجود داشته باشد.
        """)
        msg.exec()

    def get_line_edit_colors(self):
        if self.current_style == self.dark_mode_style: 
            return "yellow", "white"
        else:
            return "blue", "black"

    def set_line_edits_color(self):
        color_1, color_2 = self.get_line_edit_colors()
        for row in self.line_edits:
            for col in row:
                if col.isReadOnly():
                    col.setStyleSheet(f"color: {color_1};")
                else:
                    col.setStyleSheet(f"color: {color_2};")

    def set_line_edit_background_color(self):
        color_1, color_2 = self.get_line_edit_colors()
        for le in self.wrong_guesses:
                if le.isReadOnly():
                    le.setStyleSheet(f"color: {color_1}; background-color: salmon;")
                else:
                    le.setStyleSheet(f"color: {color_2}; background-color: salmon;")
    
    def set_corrected_line_edit_style(self, line_edit):
        color_1, color_2 = self.get_line_edit_colors()
        if line_edit.isReadOnly():
            line_edit.setStyleSheet(f"color: {color_1};")
        else:
            line_edit.setStyleSheet(f"color: {color_2};")

    def color_mood_toggle(self):
        if self.current_style == self.light_mode_style:
            self.current_style = self.dark_mode_style
            self.ui.color_mood_btn.setStyleSheet("color: black; background-color: white; border-radius: 6px;")
            for row in self.line_edits:
                for col in row:
                    if col.isReadOnly():
                        col.setStyleSheet("color: yellow;")
                    else:
                        col.setStyleSheet("color: white;")
        else:
            self.current_style = self.light_mode_style
            self.ui.color_mood_btn.setStyleSheet("color: white; background-color: black; border-radius: 6px;")
            for row in self.line_edits:
                for col in row:
                    if col.isReadOnly():
                        col.setStyleSheet("color: blue;")
                    else:
                        col.setStyleSheet("color: black;")
        self.setStyleSheet(self.current_style)
        self.set_line_edit_background_color()

    def new_board(self):
        self.new_game(Sudoku(3, seed=randint(1, 1000)).difficulty(0.5))
    
    def validation(self, i, j, text):
        if text not in ["1", "2", "3", '4', '5', '6', '7', '8', '9']:
            self.line_edits[i][j].setText("")
        self.check(i, j)
    
    def new_game(self, puzzle_board):
        try:
            self.solve = puzzle_board.solve(raising=True)
        except:
            msg = QMessageBox()
            msg.setText("This puzzle will not be solved.")
            msg.exec()
            self.solve = False
        puzzle_board = puzzle_board.board
        for i in range(9):
            for j in range(9):
                new_cell = QLineEdit()
                new_cell.setAlignment(Qt.AlignCenter)
                new_cell.setFixedWidth(30)
                new_cell.setFixedHeight(30)
                if puzzle_board[i][j] != None:
                    new_cell.setText(str(puzzle_board[i][j]))
                    new_cell.setReadOnly(True)
                self.ui.grid_layout.addWidget(new_cell, i, j)
                new_cell.textChanged.connect(partial(self.validation, i, j))
                self.line_edits[i][j] = new_cell
        self.set_line_edits_color()

    def open_file(self):
        try:
            file_path = QFileDialog.getOpenFileName(self, "open file")[0]
            f = open(file_path, "r")
            big_text = f.read()
            rows = big_text.split("\n")
            puzzle_board = [[None for i in range(9)] for j in range(9)]
            for i in range(len(rows)):
                cells = rows[i].split(" ")
                for j in range(len(cells)):
                    puzzle_board[i][j] = int(cells[j])
            self.new_game(Sudoku(3, 3, board=puzzle_board))
        except FileNotFoundError:
            pass
        except:
            msg = QMessageBox()
            msg.setText("""The structure of the file content is wrong. 
The numbers of each rows must be on the same line and separated by a space.""")
            msg.exec()

    def check(self, row_number, col_number):
        # Check for row and col
        for i in range(9):
            if self.line_edits[row_number][col_number].text() != "" and i != col_number and \
                self.line_edits[row_number][i].text() == self.line_edits[row_number][col_number].text() or\
                self.line_edits[row_number][col_number].text() != "" and i != row_number and\
                self.line_edits[i][col_number].text() == self.line_edits[row_number][col_number].text():
                if self.line_edits[row_number][col_number] not in self.wrong_guesses:
                    self.wrong_guesses.append(self.line_edits[row_number][col_number])
                self.set_line_edit_background_color()
                return False

        # Check for 3*3 cell
        if row_number % 3 == 0:
            lower_row_range, upper_row_range = row_number, row_number+3
        else:
            lower_row_range, upper_row_range = (row_number//3)*3, ceil(row_number/3)*3
        if col_number % 3 == 0:
            lower_col_range, upper_col_range = col_number, col_number+3
        else:
            lower_col_range, upper_col_range = (col_number//3)*3, ceil(col_number/3)*3
        for i in range(lower_row_range, upper_row_range):
            for j in range(lower_col_range, upper_col_range):
                if self.line_edits[i][j].text() != "" and\
                      self.line_edits[i][j].text() == self.line_edits[row_number][col_number].text():
                    if row_number != i or col_number != j:
                        if self.line_edits[row_number][col_number] not in self.wrong_guesses:
                            self.wrong_guesses.append(self.line_edits[row_number][col_number])
                        self.set_line_edit_background_color()
                        return False
        
        if self.line_edits[row_number][col_number] in self.wrong_guesses:
            self.wrong_guesses.remove(self.line_edits[row_number][col_number])
            self.set_corrected_line_edit_style(self.line_edits[row_number][col_number])

        is_won = True
        for row in self.line_edits:
            for le in row:
                if le.text() == "":
                    is_won = False
                    break
            if not is_won:
                break
        else:
            msg = QMessageBox()
            msg.setText("Congratulations, you won 🎉🎉🎉")
            msg.exec()
        return True
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()