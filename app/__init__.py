from flask import Flask
from app import UserController
from app import DatabaseModel
from config import Config

app_flask = Flask(__name__)
app_flask.config.from_object(Config)

database_model = DatabaseModel.DatabaseModel()
user_controller =  UserController.UserController(database_model)


from app import backend_routes
from app import frontend_routes