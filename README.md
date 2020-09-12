# Fika Scheduling System

This project is a quick and dirty scheduling systemm for the Friday snacks at my workplace.

The frontend is generated from Jinja templates in python, using bootstrap for CSS. The frontend data is read from a SQLite3 database, where users are stored in a table together with their order in the queue.

The whole project is deployed using docker, mounting the database and config file.

## Usage
The system uses a simple email verification for signup. When a user clicks the button "Add yourself", they're taken to a form where they submit their email. The email is checked for domain (ATM hardcoded to @infotiv.se), and if valid they'll receive an email with a unique signup link which acually sets up their user (check out app/frontend_routes.py:add_request). 

The same system is used for removing users. When a user submits their email to the 'Remove yourself' form, they receive a unique link by email allowing them to remove themselves from the database (check out app/frontend_routes.py:remove_request).

There is currently no convenient system for removing users as an admin, or swapping spots with someone (though there is a script for this, see Misc). 

## Setup

There is a simple Makefile with some useful targets, the most useful of which are:

**debug**: Deploys a local instance of the fika system in debug mode (localhost:5201), without building the docker container.

**redeploy_docker**: Takes down the running docker container, rebuilds it, and sets it back up with the latest code. 

## Misc

There is a script to swap two users order in the list, *swap_users.py*. Calling it without params will display a list of users and their UIDs, calling it with two UIDs will then swap those and display the new ordering.
