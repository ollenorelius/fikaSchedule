from app.DatabaseModel import DatabaseModel
import sys

db_model = DatabaseModel()
db_model.open_db()

all_users = db_model.get_all_users()

def print_users():
    print("UID\tActive\tName")
    print("________________")
    users = sorted(db_model.get_all_users(), key= lambda x: x.ordering)
    for user in users:
        print("%s\t%s\t%s" % (user.uid, [" ", "X"][user.active], user.name))

if len(sys.argv) != 2 or not sys.argv[1].isnumeric():
    print("To toggle the active state of a user, call this script with one of the following UIDs:")
    print_users()
    quit()

def get_usermodel(uid):
    filtered = list(filter(lambda x: x.uid == int(uid), all_users))
    if len(filtered) == 0:
        print("Could not find user %s" % uid)
        return None
    return filtered[0]






user = get_usermodel(sys.argv[1])
if user is not None:
    print("Setting %s's status to %s" % (user.name.strip(), ["Inactive", "Active"][not user.active]))
    if user.active:
        db_model.deactivate_user(user)
    else:
        db_model.activate_user(user)
#    print_users_ordered()
    pass
else:
    quit()

