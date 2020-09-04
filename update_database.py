import sqlite3
import os
import sys

if len(sys.argv) != 2:
    print("Call this script with the database file as the only argument.")
    quit()

database_file = sys.argv[1]

def open_db(db_file):
    if os.path.isfile(db_file):
        conn = sqlite3.connect(db_file)
        return conn
    else:
        print("Database file %s does not exist." % db_file)
        return False

def execute_command(conn, command, *args):
    c = conn.cursor()
    c.execute(command, args)
    conn.commit()

conn = open_db(sys.argv[1])

if conn is False:
    quit()


add_ordering_command = "ALTER TABLE users ADD ordering INTEGER;"
add_active_command = "ALTER TABLE users ADD active INTEGER;"
set_ordering_command = "UPDATE users SET ordering = id, active = 1;"

execute_command(conn, add_ordering_command)
execute_command(conn, add_active_command)
execute_command(conn, set_ordering_command)
