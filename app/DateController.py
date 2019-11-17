import threading
import datetime
from app.StateModel import StateModel

class DateController():
    def __init__(self, state_model: StateModel):
        self.state_model = state_model
        current_week = datetime.datetime.today().isocalendar()[1]
        self.last_week_checked = current_week
        threading.Thread(target=self.date_checker_thread, daemon=True).start()
    def date_checker_thread(self):
        while True:
            check_date()
            time.sleep(600) # Only check every ten minutes!

    def check_date(self):
        current_week = datetime.datetime.today().isocalendar()[1]
        if self.last_week_checked != current_week:
            self.state_model.load_state()
            self.state_model.state["index"] += 1
            self.state_model.save_state()
            self.last_week_checked = current_week

