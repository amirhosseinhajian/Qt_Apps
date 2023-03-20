import time
from PySide6.QtCore import QThread, Signal
from mytime import MyTime

class TimerThread(QThread):
    update_signal = Signal(MyTime)
    end_signal = Signal()

    def __init__(self):
        super().__init__()
        self.time = MyTime(30, 15, 0)
    
    def run(self):
        end_flag = False
        while True:
            if self.time.hour > 0 or self.time.minute > 0 or self.time.second > 0:
                self.time.minus()
                self.update_signal.emit(self.time)
                time.sleep(1)
            elif not end_flag:
                self.end_signal.emit()
                end_flag = True
    
    def reset(self):
        self.time.hour = 0
        self.time.minute = 0
        self.time.second = 0

    def set_timer(self, second, minute, hour):
        self.time.second = second
        self.time.minute = minute
        self.time.hour = hour
        self.update_signal.emit(self.time)