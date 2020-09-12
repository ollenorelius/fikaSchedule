from app import APP_FLASK as app_flask
from app import USER_CONTROLLER as user_controller
from flask import Response
from flask import render_template, redirect
from app import DATABASE_MODEL as database_model
from app import STATE_MODEL as state_model
from app.forms import AddUserForm, AddRequestForm, RemoveRequestForm
from app.UserModel import UserModel as UserModel
from app.send_email import send_email, send_html
from config import Config
import datetime

@app_flask.route('/')
def index():
    users = sorted(database_model.get_all_users(), key=lambda x: x.ordering)
    users = list(filter(lambda x: x.active, users))
    
    state_model.load_state()
    if len(users) != 0:
        index = state_model.state["index"] % len(users)
        users = users[index:] + users[:index]
        current_week = datetime.datetime.today().isocalendar()[1]
        for user, week in zip(users, range(current_week, current_week+len(users))):
            user.week = ((week-1) % 52) + 1

    return render_template("index.html", users=users)

@app_flask.route('/add/<key>', methods=["GET", "POST"])
def add_user(key):
    form = AddUserForm()
    request_model = database_model.get_join_request(key)
    if request_model.email != "":
        form.name = request_model.email.split(".")[0].title()
        if form.validate_on_submit():
            user = UserModel()
            user.name = form.username.data
            user.email = request_model.email
            user.slack = form.slack.data
            database_model.add_user(user)
            database_model.clear_join_requests(request_model.email)
            return redirect("/")
        return render_template("add_user.html", form=form)
    else:
        return Response("Invalid key", 403)


@app_flask.route('/remove/<key>', methods=["GET", "POST"])
def remove_user(key):
    form = RemoveRequestForm()
    request_model = database_model.get_leave_request(key)
    if request_model.email != "":
        print("Removing " + request_model.email)
        form.name = request_model.email.split(".")[0].title()
        database_model.remove_user(request_model.email)
        database_model.clear_leave_requests(request_model.email)
        return render_template("remove_user.html", form=form)
    else:
        return Response("Invalid key", 403)


@app_flask.route('/add_request', methods=["GET", "POST"])
def add_request():
    form = AddRequestForm()
    if form.validate_on_submit():
        if form.email.data.split("@")[1].lower() == "infotiv.se":
            key = database_model.add_join_request(form.email.data)
            with open("app/templates/email_template.html") as f:
                send_html(form.email.data, "Join FredagsFika!", ''.join(f.readlines()).format(key=key, host=Config.HOST))
        return redirect("/")
    else:
        return render_template("add_request.html", form=form)


@app_flask.route('/remove_request', methods=["GET", "POST"])
def remove_request():
    form = AddRequestForm()
    if form.validate_on_submit():
        if form.email.data.split("@")[1].lower() == "infotiv.se":
            key = database_model.add_leave_request(form.email.data)
            with open("app/templates/leave_email_template.html") as f:
                send_html(form.email.data, "Leave FredagsFika", ''.join(f.readlines()).format(key=key, host=Config.HOST))
        return redirect("/")
    else:
        return render_template("remove_request.html", form=form)

