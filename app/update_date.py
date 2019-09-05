import time
import datetime
from app import state_model

def set_date_in_file():
    state_model.state["last_update"] = int(time.time())
    state_model.save_state()


def get_date_from_file():
    return state_model.state["last_update"]

def is_new_week():
    current_week = datetime.datetime.today().isocalendar()[1]
    last_update_week = datetime.date.fromtimestamp(get_date_from_file()).isocalendar()[1]
    return (current_week > last_update_week) \
        or (current_week == 1 and last_update_week == 52)

def check_week():
    if is_new_week():
        print(state_model.state['index'])
        state_model.state['index'] += 1
        state_model.save_state()
    set_date_in_file()

def run():
    while True:
        check_week()
        time.sleep(3600)        
