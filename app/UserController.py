from app.DatabaseModel import DatabaseModel
from app.UserModel import UserModel
from flask import Response

class UserController:
    def __init__(self, database_model: DatabaseModel):
        self.database_model = database_model

    def add_user(self, form_data):
        user= UserModel()
        user.name = "Olle"
        user.slack = "Olle"
        user.email = "olle.norelius@infotiv.se"
        self.database_model.add_user(user)
        return Response("OK", 200)

    def remove_user(self):
        return Response("NIMPL", 200)
    
    def get_user_by_email(self, email):
        user = self.database_model.get_user_by_email(email)
        return Response(user, 200)

    def get_all_users(self):
        users = self.database_model.get_all_users()
        print(users)
        return Response(str(users), 200)

