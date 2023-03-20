from time import sleep
from datetime import datetime
from PySide6.QtCore import QThread, Signal
import pytz
from mytime import MyTime

class Clock(QThread):
    show_time_signal = Signal(MyTime, MyTime, MyTime)

    def __init__(self):
        super().__init__()
    
    def run(self):
        while True:
            self.usa_timezone = datetime.now(pytz.timezone('America/New_York'))
            self.usa_time = MyTime(self.usa_timezone.second, self.usa_timezone.minute, self.usa_timezone.hour)
            self.germany_timezone = datetime.now(pytz.timezone('Europe/Berlin'))
            self.germany_time = MyTime(self.germany_timezone.second, self.germany_timezone.minute, self.germany_timezone.hour)
            self.iran_timezone = datetime.now(pytz.timezone('Iran'))
            self.iran_time = MyTime(self.iran_timezone.second, self.iran_timezone.minute, self.iran_timezone.hour)
            self.show_time_signal.emit(self.usa_time, self.germany_time, self.iran_time)
            sleep(1)