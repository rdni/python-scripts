import argparse
import sqlite3

parser = argparse.ArgumentParser()#parser

parser.add_argument("username", type=str, help="Input username")#arguments
parser.add_argument("password", type=str, help="Input password")
parser.add_argument("--register", "-r", type=bool, help="Register new account. True or False", default=False)
parser.add_argument("--file", "-f", type=str, help="Name of storage file. Must be .db.", default="guiData.db")

args = parser.parse_args()#parses args

def removeBadChar(x):#Replace bad characters
        x = x.replace(" ", "")
        x = x.replace(".", "")
        x = x.replace("\\", "")
        x = x.replace("\"", "")
        x = x.replace("'", "")
        return x


conn = sqlite3.connect(args.file)

if args.register:
    usernameTest = 0

    username = removeBadChar(args.username)
    password = removeBadChar(args.password)

    userTaken = False
    cur = conn.execute("""SELECT username from GUIDATA""")
    rows = cur.fetchall()
    rows = ' '.join([str(x) for t in rows for x in t])
    rows = rows.split()
    for i in range(len(rows)):
        if rows[i] == username:
            userTaken = True
            break
    
    if userTaken:
        print("Username taken")
    else:
        cursor = conn.execute("""SELECT MAX(ID) from GUIDATA""")
        id = cursor.fetchone()
        id = int(id[0]) + 1
        conn.execute("""INSERT INTO GUIDATA (USERNAME, PASSWORD, ID) VALUES (?,?,?)""", (username, password, id))
        conn.commit()
        print("Username registered")

    
else:
    loggedIn = False
    username = args.username
    password = args.password
    cur = conn.execute("""SELECT username from GUIDATA""")
    rows = cur.fetchall()
    rows = ' '.join([str(x) for t in rows for x in t])
    rows = rows.split()
    for i in range(len(rows)):
        if rows[i] == username:
            print("Match")
            id = i
            break