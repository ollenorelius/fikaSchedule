from app.DatabaseModel import DatabaseModel
import sys

db_model = DatabaseModel()
db_model.open_db()

all_users = db_model.get_all_users()

if len(sys.argv) != 3 or not all([x.isnumeric() for x in sys.argv[1:2]]):
    print("To swap two users, call this script with two UIDs from the following list:")
    print("UID\tName")
    print("________________")
    for user in all_users:
        print("%s\t%s" % (user.uid, user.name))
    quit()

def get_usermodel(uid):
    filtered = list(filter(lambda x: x.uid == int(uid), all_users))
    if len(filtered) == 0:
        print("Could not find user %s" % uid)
        return None
    return filtered[0]

def print_users_ordered():
    print("UID\tName")
    print("________________")
    users = sorted(db_model.get_all_users(), key= lambda x: x.ordering)
    for user in users:
        print("%s\t%s" % (user.uid, user.name))





user1 = get_usermodel(sys.argv[1])
user2 = get_usermodel(sys.argv[2])
if user1 is not None and user2 is not None:
    db_model.swap_users(user1, user2)
    print_users_ordered()
else:
    quit()

