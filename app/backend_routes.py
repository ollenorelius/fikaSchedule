from app import app_flask
from app import user_controller
from app import database_model, state_model
from flask import Response
from flask import request

@app_flask.route('/add_user', methods=['GET','POST'])
def add_user_backend():
    response = user_controller.add_user()
    return response

@app_flask.route('/remove_user', methods=['POST'])
def remove_user_backend():
    response = user_controller.remove_user()
    return response

@app_flask.route('/get_user/<email>')
def get_user(email):
    print(email)
    response = user_controller.get_user_by_email(email)
    return response

@app_flask.route("/get_users")
def get_all_users():
    response = str([x.to_dict() for x in database_model.get_all_users()])
    return response