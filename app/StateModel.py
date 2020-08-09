import json
from config import Config
import datetime

class StateModel():
    state = None
    def __init__(self, state_file):
        self.state_file_name = state_file
        try:
            self.load_state()
        except FileNotFoundError:
            print("State file not found! Creating empty state.")
            self.init_state()
            self.save_state()

    def load_state(self):
        with open(self.state_file_name, 'r') as f:
            self.state = json.load(f)

    def save_state(self):
        with open(self.state_file_name, 'w') as f:
            json.dump(self.state, f)

    def init_state(self):
        self.state = {"index": 0,
                      "start_week": datetime.datetime.today().isocalendar()[1]
        }

