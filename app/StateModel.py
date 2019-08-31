import json
from config import Config
import datetime

class StateModel():
    state = None
    def __init__(self):
        try:
            self.load_state()
        except FileNotFoundError:
            self.init_state()
            self.save_state()

    def load_state(self):
        with open(Config.STATE_FILE, 'r') as f:
            self.state = json.load(f)

    def save_state(self):
        with open(Config.STATE_FILE, 'w') as f:
            json.dump(self.state, f)

    def init_state(self):
        self.state = {"index": 0,
                      "start_week": datetime.datetime.today().isocalendar()[1]
        }

    