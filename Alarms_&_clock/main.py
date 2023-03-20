import sys
from functools import partial
from PySide6.QtWidgets import QMainWindow, QApplication, QMessageBox,\
      QLineEdit, QPushButton, QCheckBox,QSpinBox
from PySide6.QtGui import QFont, QFontDatabase, QCursor
from PySide6.QtCore import Qt
from stopwatch import StopWatchThread
from timer import TimerThread
from main_window import Ui_AlarmsClock
from clock import Clock
from alarm import Alarm

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_AlarmsClock()
        self.ui.setupUi(self)
        id = QFontDatabase.addApplicationFont("./font/Seven Segment.ttf")
        self.digits_font_family = QFontDatabase.applicationFontFamilies(id)

        # ------ initialize stopwatch ------ #
        self.thread_stopwatch = StopWatchThread()
        self.ui.stopwatch_start_btn.clicked.connect(self.start_stopwatch)
        self.thread_stopwatch.update_signal.connect(self.show_stopwatch_number)
        self.ui.stopwatch_stop_btn.clicked.connect(self.stop_stopwatch)
        self.ui.stopwatch_reset_btn.clicked.connect(self.reset_stopwatch)
        self.ui.stopwatch_label.setFont(QFont(self.digits_font_family[0], 42))

        # ------ initialize timer ------ #
        self.thread_timer = TimerThread()
        self.ui.timer_start_btn.clicked.connect(self.start_timer)
        self.thread_timer.update_signal.connect(self.show_time_timer)
        self.ui.timer_stop_btn.clicked.connect(self.stop_timer)
        self.ui.timer_reset_btn.clicked.connect(self.reset_timer)
        self.thread_timer.end_signal.connect(self.end_of_timer)
        self.ui.timer_hour_tb.setFont(QFont(self.digits_font_family[0], 32))
        self.ui.timer_minute_tb.setFont(QFont(self.digits_font_family[0], 32))
        self.ui.timer_second_tb.setFont(QFont(self.digits_font_family[0], 32))


        # ------ initialize clock ------ #
        self.thread_clock = Clock()
        self.thread_clock.show_time_signal.connect(self.update_clock)
        self.thread_clock.start()
        self.ui.usa_time_label.setFont(QFont(self.digits_font_family[0], 24))
        self.ui.germany_time_label.setFont(QFont(self.digits_font_family[0], 24))
        self.ui.iran_time_label.setFont(QFont(self.digits_font_family[0], 24))

        # ------ initialize alarm ------ #
        self.thread_alarm = Alarm()
        self.alarms = self.thread_alarm.read_alarms()
        self.alarms_titles = []
        self.alarms_cbs = {}
        self.ui.add_alarm_btn.clicked.connect(self.add_alarm)
        for i, alarm in enumerate(self.alarms):
            self.alarms_titles.append(alarm[0])
            self.draw_new_alarm(alarm, i)
        self.thread_alarm.start()

    def closeEvent(self, event):
        self.thread_alarm.terminate()
        self.thread_clock.terminate()
        self.thread_stopwatch.terminate()
        self.thread_timer.terminate()
        event.accept()

    def add_alarm(self):
        msg = QMessageBox()
        if len(self.alarms_titles) > 9:
            msg.setText("You have created the maximum alarms number!")
            msg.exec()
            return
        alarm_title = self.ui.new_alarm_le.text()
        if not alarm_title:
            msg.setText("Enetr new alarm title.")
            msg.exec()
            return
        elif alarm_title in self.alarms_titles:
            msg.setText("This title already exists.")
            msg.exec()
            return
        new_alarm_days = []
        if self.ui.sun_cb.isChecked():
            new_alarm_days.append("Sunday")
        if self.ui.mon_cb.isChecked():
            new_alarm_days.append("Monday")
        if self.ui.tue_cb.isChecked():
            new_alarm_days.append("Tuesday")
        if self.ui.wed_cb.isChecked():
            new_alarm_days.append("Wednesday")
        if self.ui.thu_cb.isChecked():
            new_alarm_days.append("Thursday")
        if self.ui.fri_cb.isChecked():
            new_alarm_days.append("Friday")
        if self.ui.sat_cb.isChecked():
            new_alarm_days.append("Saturday")
        if len(new_alarm_days)  == 0 :
            msg.setText("please select days for new alarm.")
            msg.exec()
            return
        alarm_hour = self.ui.new_alarm_hour.value()
        alarm_minute = self.ui.new_alarm_minute.value()
        alarm_days = ",".join(new_alarm_days)
        if not self.thread_alarm.add_alarm(alarm_title, alarm_hour, alarm_minute, alarm_days):
            msg.setText("can not connect to database.")
            msg.exec()
        else:
            self.alarms_titles.append(alarm_title)
            self.draw_new_alarm([alarm_title, alarm_hour, alarm_minute, alarm_days], self.ui.alarms_gl.rowCount())
            self.clear_alarm_inputs()

    def clear_alarm_inputs(self):
        self.ui.new_alarm_le.setText("")
        self.ui.new_alarm_hour.setValue(0)
        self.ui.new_alarm_minute.setValue(0)
        self.ui.sun_cb.setChecked(False)
        self.ui.mon_cb.setChecked(False)
        self.ui.tue_cb.setChecked(False)
        self.ui.wed_cb.setChecked(False)
        self.ui.thu_cb.setChecked(False)
        self.ui.fri_cb.setChecked(False)
        self.ui.sat_cb.setChecked(False)

    def update_alarm(self, name, title_le, hour_sb, minute_sb, current_btn, delete_btn):
        msg = QMessageBox()
        days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
        alarm_days = ""
        for i, cb in enumerate(self.alarms_cbs[name]):
            if cb.isChecked():
                alarm_days += f"{days[i]},"
        if len(alarm_days) == 0:
            msg.setText("You have not selected any day for this alarm. plese select a day first.")
            msg.exec()
            return
        if self.thread_alarm.update_alarm(name, title_le.text(), hour_sb.value(), minute_sb.value(), alarm_days[:-1]):
            if name != title_le.text():
                self.alarms_titles.remove(name)
                self.alarms_titles.append(title_le.text())
                self.alarms_cbs.update({title_le.text(): self.alarms_cbs[name]})
                del self.alarms_cbs[name]
                current_btn.clicked.disconnect()
                current_btn.clicked.connect(partial(self.update_alarm, title_le.text(), title_le, hour_sb, minute_sb, current_btn, delete_btn))
                delete_btn.clicked.disconnect()
                delete_btn.clicked.connect(partial(self.remove_alarm, title_le.text(), [title_le, hour_sb, minute_sb, current_btn, delete_btn]))
            msg.setText("This alarm updated successfully!")
            msg.exec()
        else:
            msg.setText("Can not connect to database!")
            msg.exec()

    def draw_new_alarm(self, alarm, row):
        new_le = QLineEdit()
        new_remove_btn = QPushButton()
        edit_btn = QPushButton()
        hour = QSpinBox()
        minute = QSpinBox()
        hour.setMaximum(23)
        minute.setMaximum(59)
        hour.setObjectName(f'{alarm[0]}_hour')
        minute.setObjectName(f'{alarm[0]}_minute')
        hour.setValue(int(alarm[1]))
        minute.setValue(int(alarm[2]))
        new_le.setText(alarm[0])
        new_remove_btn.setStyleSheet("border-radius: 6px;background-color: #383838;")
        edit_btn.setStyleSheet("border-radius: 6px;background-color: #383838;")
        new_remove_btn.setFixedWidth(35)
        new_remove_btn.setFixedHeight(25)
        edit_btn.setFixedWidth(35)
        edit_btn.setFixedHeight(25)
        new_remove_btn.setCursor(QCursor(Qt.PointingHandCursor))
        edit_btn.setCursor(QCursor(Qt.PointingHandCursor))
        new_remove_btn.setText("❌")
        edit_btn.setText("📝")    
        edit_btn.clicked.connect(partial(self.update_alarm, alarm[0], new_le, hour, minute, edit_btn, new_remove_btn))
        new_remove_btn.clicked.connect(partial(self.remove_alarm, alarm[0], [new_le, hour, minute, new_remove_btn, edit_btn]))
        alarm_days = alarm[3].split(",")
        days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
        self.alarms_cbs[alarm[0]] = []
        for j, day in enumerate(days):
            new_cb = QCheckBox()
            new_cb.setText(day[0:3])
            if day in alarm_days:
                new_cb.setChecked(True)
            self.alarms_cbs[alarm[0]].append(new_cb)
            self.ui.alarms_gl.addWidget(new_cb, row, j+3)
        self.ui.alarms_gl.addWidget(new_le, row, 0)
        self.ui.alarms_gl.addWidget(hour, row, 1)
        self.ui.alarms_gl.addWidget(minute, row, 2)
        self.ui.alarms_gl.addWidget(edit_btn, row, 10)
        self.ui.alarms_gl.addWidget(new_remove_btn, row, 11)

    def remove_alarm(self, alarm_title, widgets):
        if self.thread_alarm.remove_alarm(alarm_title):
            for widget in widgets:
                widget.deleteLater()
            for cb in self.alarms_cbs[alarm_title]:
                cb.deleteLater()
            self.alarms_titles.remove(alarm_title)
            del self.alarms_cbs[alarm_title]
        else:
            msg = QMessageBox()
            msg.setText("Can not connect to database.")
            msg.exec()

    def update_clock(self, usa_time, germany_time, iran_time):
        self.ui.usa_time_label.setText(f'{usa_time.hour}:{usa_time.minute}:{usa_time.second}')
        self.ui.germany_time_label.setText(f'{germany_time.hour}:{germany_time.minute}:{germany_time.second}')
        self.ui.iran_time_label.setText(f'{iran_time.hour}:{iran_time.minute}:{iran_time.second}')

    def end_of_timer(self):
        self.thread_timer.terminate()
        msg = QMessageBox()
        msg.setText("End of timer!")
        msg.exec()

    def reset_timer(self):
        self.thread_timer.set_timer(30, 15, 0)

    def stop_timer(self):
        self.thread_timer.terminate()

    def show_time_timer(self, time):
        self.ui.timer_hour_tb.setText(str(time.hour))
        self.ui.timer_minute_tb.setText(str(time.minute))
        self.ui.timer_second_tb.setText(str(time.second))

    def start_timer(self):
        try:
            self.thread_timer.set_timer(int(self.ui.timer_second_tb.text()), int(self.ui.timer_minute_tb.text()), int(self.ui.timer_hour_tb.text()))
            self.thread_timer.start()
        except:
            msg = QMessageBox()
            msg.setText("Please enter number!")
            msg.exec()

    def show_stopwatch_number(self, time):
        self.ui.stopwatch_label.setText(str(f"{time.hour}:{time.minute}:{time.second}"))

    def stop_stopwatch(self):
        self.thread_stopwatch.terminate()
        
    def start_stopwatch(self):
        self.thread_stopwatch.start()

    def reset_stopwatch(self):
        self.thread_stopwatch.reset()
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    app.exec()