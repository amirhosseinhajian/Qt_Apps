import sqlite3

class Database:
    def __init__(self) -> None:
        self.con = sqlite3.connect("todolist.db")
        self.cursor = self.con.cursor()

    def get_tasks(self):
        query = "SELECT * FROM tasks"
        result = self.cursor.execute(query)
        tasks = result.fetchall()
        return tasks
    
    def add_new_task(self, new_title, new_descryption, priority, date, time):
        try:
            query = f"INSERT INTO tasks(title, description, priority, date, time) VALUES('{new_title}', '{new_descryption}', '{priority}', '{date}', '{time}')"
            self.cursor.execute(query)
            self.con.commit()
            return True
        except:
            return False
    
    def remove_task(self, id):
        try:
            query = f"DELETE FROM tasks WHERE id = '{id}'"
            self.cursor.execute(query)
            self.con.commit()
            return True
        except:
            return False
    
    def task_done(self, id, status):
        try:
            query = f"UPDATE tasks SET is_done = '{status}' WHERE id = '{id}'"
            self.cursor.execute(query)
            self.con.commit()
            return True
        except:
            return False