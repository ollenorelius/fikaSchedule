#Fika Scheduling System

This project is a quick and dirty scheduling systemm for the Friday snacks at my workplace.

The frontend is generated from Jinja templates in python, using bootstrap for CSS. The frontend data is read from a SQLite3 database, where users are stored in a table together with their order in the queue.

The whole project is deployed using docker, mounting the database and config file.

## Setup

There is a simple Makefile with some useful targets, the most useful of which are:

*debug*: Deploys a local instance of the fika system in debug mode (localhost:5201), without building the docker container.

*redeploy_docker*: Takes down the running docker container, rebuilds it, and sets it back up with the latest code. 

## Misc

There is a script to swap two users order in the list, *swap_users.py*. Calling it without params will display a list of users and their UIDs, calling it with two UIDs will then swap those and display the new ordering.
