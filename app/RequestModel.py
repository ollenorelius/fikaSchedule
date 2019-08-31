class RequestModel:
        
    email = ""
    key = ""
    timestamp = 0 
    def __init__(self, db_line=None):
        if db_line is not None:
            self.email =  db_line[0]
            self.key =  db_line[1]
            self.timestamp =  db_line[2]
