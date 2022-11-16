#Required dependency for pythonCLITest
#Requires sqlite3

import sqlite3

def createFile(loc, endswithdb):
    if endswithdb:
        pass
    else:
        loc = loc + ".db"
    conn = sqlite3.connect(loc)
    conn.execute("""CREATE TABLE "GUIDATA" (
	"ID"	INT NOT NULL,
	"USERNAME"	TEXT NOT NULL,
	"PASSWORD"	TEXT NOT NULL,
	PRIMARY KEY("ID")
    )""")
    conn.commit()