"""
Singleton Design Pattern restricts the instantiation of a class to one object.
It is a type of creational pattern and involves only one class to create methods and specified objects.
"""

import os
from tools import get_path
from applicationdb import ApplicationDb

ROOT = os.path.dirname(os.path.abspath(__file__))
db_path = get_path(os.path.join(ROOT, 'config.yaml'))


# first instance of the ApplicationDB class
test_db = ApplicationDb()
test_db.open_conn(db_path)
test_db.open_cursor()
data = test_db.query_db("SELECT * FROM [MediaType]")
print(data) # [(1, 'MPEG audio file'), (2, 'Protected AAC audio file'), (3, 'Protected MPEG-4 video file'),
                # (4, 'Purchased AAC audio file'), (5, 'AAC audio file')]

print(test_db)  # <applicationdb.ApplicationDb object at 0x0000027672B7DF10>


# second instance of the ApplicationDB class
new_test_db = ApplicationDb()
new_test_db.open_conn(db_path)

print(new_test_db)  # <applicationdb.ApplicationDb object at 0x0000027672B7DF10>


# verify
print(new_test_db is test_db) # TRUE;  same object id in memory;