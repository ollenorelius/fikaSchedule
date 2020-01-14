import threading

from flask import Flask
from app import UserController
from app import DatabaseModel
from app import StateModel
from app import DateController
from config import Config

app_flask = Flask(__name__)
app_flask.config.from_object(Config)

database_model = DatabaseModel.DatabaseModel()
state_model = StateModel.StateModel(Config.STATE_FILE)
user_controller =  UserController.UserController(database_model)
date_controller = DateController.DateController(state_model)


#from app import update_date
#threading.Thread(target=update_date.run,daemon=True).start()

from app import backend_routes
from app import frontend_routes
