from datetime import datetime
from time import sleep
from sqlite3 import connect
from PySide6.QtCore import QThread, Signal
from plyer import notification

class Alarm(QThread):
    alarm_signal = Signal()

    def __init__(self):
        super().__init__()
        self.monitored_alarms = self.read_alarms()
        self.alarms_done_today = []
    
    def run(self):
        while True:
            for alarm in self.monitored_alarms:
                self.is_it_time(alarm)
            sleep(1)
    
    def read_alarms(self):
        try:
            self.con = connect('alarms.db')
        except:
            print("Failure to connect to the database.")
            return False
        else:
            self.cursor = self.con.cursor()
            alarms = self.cursor.execute("SELECT * FROM alarms").fetchall()
            return alarms
    
    def add_alarm(self, name, hour, minute, days):
        try:
            self.cursor.execute(f"""INSERT INTO alarms (name, hour, minute, days)
            VALUES ('{name}', '{hour}', '{minute}', '{days}')""")
            self.con.commit()
            self.monitored_alarms = self.read_alarms()
            return True
        except:
            return False
    
    def update_alarm(self, old_title, new_title, hour, minute, days):
        try:
            self.cursor.execute(f"""UPDATE alarms
            SET name = '{new_title}', hour = '{hour}', minute = '{minute}', days = '{days}'
            WHERE name = '{old_title}'""")
            self.con.commit()
            if old_title in self.alarms_done_today:
                self.alarms_done_today.remove(old_title)
            self.monitored_alarms = self.read_alarms()
            return True
        except:
            return False
    
    def remove_alarm(self, alarm_title):
        try:
            self.cursor.execute(f"DELETE FROM alarms WHERE name = '{alarm_title}'")
            self.con.commit()
            self.monitored_alarms = self.read_alarms()
            if alarm_title in self.alarms_done_today:
                self.alarms_done_today.remove(alarm_title)
            return True
        except:
            return False
        
    def is_it_time(self, alarm):
        self.clear_for_new_day(alarm)
        now = datetime.now()
        if alarm[0] not in self.alarms_done_today and now.strftime("%A") in alarm[3].split(','):
            if now.hour == alarm[1] and now.minute == alarm[2]:
                print("AAAAAAAAAAAAAALLLLLLLLLLLLLLAAAAAAAAAAARRRRRRRRRRRMMMMMMMMMMMMMM")
                notification.notify(
                    title = alarm[0],
                    message = f'Hey! its time for {alarm[0]}!',
                    app_icon = None,
                    timeout = 20,
                )
                self.alarms_done_today.append(alarm[0])
    
    def clear_for_new_day(self, alarm):
        now = datetime.now()
        if now.hour == 0 and now.minute == 0:
            if alarm[1] != 0 or alarm[2] != 0:
                if alarm[0] in self.alarms_done_today:
                    self.alarms_done_today.remove(alarm[0])
        elif now.hour == 0 and now.minute == 1:
            if alarm[1] == 0 and alarm[2] == 0:
                if alarm[0] in self.alarms_done_today:
                    self.alarms_done_today.remove(alarm[0])