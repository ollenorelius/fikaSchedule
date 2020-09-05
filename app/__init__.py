import threading

from flask import Flask
from app import UserController
from app import DatabaseModel
from app import StateModel
from app import DateController
from config import Config

APP_FLASK = Flask(__name__)
APP_FLASK.config.from_object(Config)

app_flask = APP_FLASK

DATABASE_MODEL = DatabaseModel.DatabaseModel()
STATE_MODEL = StateModel.StateModel(Config.STATE_FILE)
USER_CONTROLLER = UserController.UserController(DATABASE_MODEL)
DATE_CONTROLLER = DateController.DateController(STATE_MODEL, DATABASE_MODEL)


#from app import update_date
#threading.Thread(target=update_date.run,daemon=True).start()

from app import backend_routes
from app import frontend_routes
