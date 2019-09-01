CREATE TABLE users(id INTEGER PRIMARY KEY, name, email, slack, join_date, last_fika, times_held);
CREATE TABLE join_requests(email, uuid, timestamp);
CREATE TABLE leave_requests(email, uuid, timestamp);
