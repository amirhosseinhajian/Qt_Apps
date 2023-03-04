import sys
from functools import partial
from PySide6.QtWidgets import *
from PySide6.QtCore import *
from main_window import Ui_MainWindow
from database import Database

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.db = Database()
        self.read_from_database()
        self.ui.new_task_btn.clicked.connect(self.new_task)
        self.max_tasks_number = 10
        self.tasks_number = 0
    
    def new_task(self):
        if self.tasks_number <= self.max_tasks_number:
            new_title = self.ui.new_task_title.text()
            if len(new_title) > 0:
                new_descryption = self.ui.new_task_descryption.toPlainText()
                priority = self.ui.select.currentText()
                date = self.ui.dateTimeEdit.date().toPython()
                time = self.ui.dateTimeEdit.time().toPython()
                feedback = self.db.add_new_task(new_title, new_descryption, priority, date, time)
                if feedback:
                    self.read_from_database()
                    self.ui.new_task_title.setText("")
                    self.ui.new_task_descryption.setText("")
                else:
                    msg_box = QMessageBox()
                    msg_box.setText("An error accured!")
                    msg_box.exec()
            else:
                msg_box = QMessageBox()
                msg_box.setText("Plese enter new task title")
                msg_box.exec()
        else:
            msg_box = QMessageBox()
            msg_box.setText("You have entered the maximum number of tasks.")
            msg_box.exec()
    
    def get_color(self, priority):
        if priority == "عادی":
            return "white"
        elif priority == "متوسط":
            return "orange"
        return "salmon"

    def set_style(self, widget, priority, is_done):
        color = self.get_color(priority)
        text_decoration = "line-through" if is_done == 1 else "none"
        widget.setStyleSheet(f"color: {color}; text-decoration: {text_decoration}; font-size: 14px;")
    
    def draw_widgets(self, row, btn, label, cb):
        self.ui.tasks_gl.addWidget(cb, row, 0)
        self.ui.tasks_gl.addWidget(label, row, 1)
        self.ui.tasks_gl.addWidget(btn, row, 2)
    
    def remove_task(self, id, widgets_array):
        if self.db.remove_task(id):
            for widget in widgets_array:
                widget.deleteLater()
        else:
            msg_box = QMessageBox()
            msg_box.setText("An error accured!")
            msg_box.exec()
            
    def toggle_task_status(self, id, cb, label, btn, o):
        if cb.isChecked():
            self.db.task_done(id, 1)
        else: 
            self.db.task_done(id, 0)
        self.read_from_database()

    def sort_tasks(self, tasks):
        counter = 0
        i = 0
        while len(tasks) > 0:
            if tasks[i][3] == 1:
                tasks.append(tasks.pop(i))
                i -= 1
            i += 1
            counter += 1
            if counter == len(tasks):
                break
        return tasks

    def show_info(self, descryption, date, time, o):
        msg = QMessageBox()
        msg.setText(f"توضیحات: {descryption} \n\n تاریخ: {date} \n\n ساعت: {time}")
        msg.exec()
        
    def read_from_database(self):
        for i in reversed(range(self.ui.tasks_gl.count())): 
            self.ui.tasks_gl.itemAt(i).widget().setParent(None)
        tasks = self.db.get_tasks()
        tasks = self.sort_tasks(tasks)
        self.tasks_number = len(tasks)
        for i in range(self.tasks_number):
            new_cb = QCheckBox()
            if tasks[i][3] == 1:
                new_cb.setChecked(True)
            new_label = QLabel()
            new_btn = QPushButton()
            new_label.setText(tasks[i][1])
            new_label.mousePressEvent = partial(self.show_info, tasks[i][2], tasks[i][5], tasks[i][6])
            new_btn.setFixedWidth(20)
            new_btn.setText("❌")
            new_btn.setCursor(Qt.PointingHandCursor)
            new_label.setCursor(Qt.PointingHandCursor)
            self.set_style(new_label, tasks[i][4], tasks[i][3])
            self.draw_widgets(i, new_btn, new_label, new_cb)
            new_cb.toggled.connect(partial(self.toggle_task_status, tasks[i][0], new_cb, new_label, new_btn))
            new_btn.clicked.connect(partial(self.remove_task, tasks[i][0], [new_cb, new_label, new_btn]))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    app.exec()