class UserModel:
    uid = 0   
    name = ""
    email = ""
    slack = ""
    join_date = ""
    last_fika = ""
    times_hosted = 0
    ordering = 0
    active = 0
    def __init__(self, db_line=None):
        if db_line is not None:
            self.uid =  db_line[0]
            self.name =  db_line[1]
            self.email =  db_line[2]
            self.slack =  db_line[3]
            self.join_date =  db_line[4]
            self.last_fika =  db_line[5]
            self.times_hosted =  db_line[6]
            self.ordering =  db_line[7]
            self.active =  db_line[8]
            
    def to_dict(self):
        return {
            'uid': self.uid,
            'name': self.name,
            'email': self.email,
            'slack': self.slack,
            'join_date': self.join_date,
            'last_fika': self.last_fika,
            'times_hosted': self.times_hosted,
            'ordering': self.ordering,
            'active': self.active
        }
