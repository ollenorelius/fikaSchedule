import sqlite3
import os
import time
from app.UserModel import UserModel
from app.RequestModel import RequestModel
import uuid

class DatabaseModel():
    
    def open_db(self):
        if os.path.isfile("database.db"):
            conn = sqlite3.connect("database.db")
        else:
            conn = sqlite3.connect("database.db")
            with open("database_def.sql") as f:
                for line in f:
                    c = conn.cursor()
                    c.execute(line)
                    conn.commit()
        return conn


    def add_user(self, user_model: UserModel):
        conn = self.open_db()
        command = "INSERT INTO users ( name, email, slack, join_date, last_fika, times_held ) VALUES (?,?,?,?,?,?);"
        c = conn.cursor()
        c.execute(command, [user_model.name, user_model.email, user_model.slack, int(time.time()), 0, 0])
        conn.commit()
    
    def remove_user(self, email):
        conn = self.open_db()
        command = "DELETE FROM users WHERE email=?;"
        c = conn.cursor()
        c.execute(command, [email])
        conn.commit()


    def add_join_request(self, email):
        conn = self.open_db()
        command = "INSERT INTO join_requests ( email, uuid, timestamp ) VALUES(?,?,?);"
        c = conn.cursor()
        key = uuid.uuid4()
        c.execute(command, [email, str(key), time.time()])
        conn.commit()
        return key
    
    def clear_join_requests(self, email):
        conn = self.open_db()
        command = "DELETE FROM join_requests WHERE email=?;"
        c = conn.cursor()
        c.execute(command, [email])
        conn.commit()

    def add_leave_request(self, email):
        conn = self.open_db()
        command = "INSERT INTO leave_requests ( email, uuid, timestamp ) VALUES (?,?,?);"
        c = conn.cursor()
        key = uuid.uuid4()
        c.execute(command, [email, str(key), time.time()])
        conn.commit()
        return key
    
    def clear_leave_requests(self, email):
        conn = self.open_db()
        command = "DELETE FROM leave_requests WHERE email=?;"
        c = conn.cursor()
        c.execute(command, [email])
        conn.commit()
        

    def get_user_by_email(self, email):
        conn = self.open_db()
        command = "SELECT * FROM users WHERE email = ?;"
        c = conn.cursor()
        c.execute(command, [email])
        return UserModel(c.fetchone())

    def get_all_users(self):
        conn = self.open_db()
        command = "SELECT * FROM users;"
        c = conn.cursor()
        c.execute(command)
        return [UserModel(x) for x in c.fetchall()]

    def get_join_request(self, key):
        conn = self.open_db()
        command = "SELECT * FROM join_requests WHERE uuid=?;"
        c = conn.cursor()
        c.execute(command, [key])
        result = c.fetchone()
        print(result)
        return RequestModel(result)

    def get_leave_request(self, key):
        conn = self.open_db()
        command = "SELECT * FROM leave_requests WHERE uuid=?;"
        c = conn.cursor()
        c.execute(command, [key])
        return RequestModel(c.fetchone())


        