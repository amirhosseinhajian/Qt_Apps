import time
from PySide6.QtCore import QThread, Signal
from mytime import MyTime

class StopWatchThread(QThread):
    update_signal = Signal(MyTime)

    def __init__(self):
        super().__init__()
        self.time = MyTime(0, 0, 0)
    
    def run(self):
        while True:
            self.time.plus()
            self.update_signal.emit(self.time)
            time.sleep(1)
    
    def reset(self):
        self.time.hour = 0
        self.time.minute = 0
        self.time.second = 0
        self.update_signal.emit(self.time)