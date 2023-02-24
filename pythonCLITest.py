#Required dependencies:
#argparse, sqlite3 and sqlite3CreateFile (see Utils)

import argparse
import sqlite3
from Utils import sqlite3CreateFile as c
from Utils import CLITestMain as a

parser = argparse.ArgumentParser()#Parser

parser.add_argument("--login", "-l", type=str, nargs=2, help="Login to account. Include username and password.", default=None)
parser.add_argument("--register", "-r", type=str, nargs=2, help="Register new account. Include username and password.", default=None)
parser.add_argument("--file", "-f", type=str, help="Name of storage file. Must be .db.", default="guiData.db")
parser.add_argument("--guest", "-g", type=bool, help="Log into a guest account", default=False)

args = parser.parse_args()#Parses args

def removeBadChar(x):#Sanitises inputs
        x = x.replace(" ", "")
        x = x.replace(".", "")
        x = x.replace("\\", "")
        x = x.replace("\"", "")
        x = x.replace("'", "")
        x = x.replace("(", "")
        x = x.replace(")", "")
        return x

if args.file.endswith(".db"):
    pass
else:
    args.file = args.file + ".db"

try:
    conn = sqlite3.connect(args.file)#Makes a connection to db file
    if args.register is not None and args.login is None: #Checks if someone is making an account
        usernameTest = 0

        username = removeBadChar(args.register[0])
        password = removeBadChar(args.register[1])#Sanitises inputs


        userTaken = False
        cur = conn.execute("""SELECT username from GUIDATA""")#Gets usernames
        rows = cur.fetchall()
        for i in range(len(rows)):
            if rows[i][0] == username:#Checks if username is taken
                userTaken = True
                break
        if userTaken:
            print("Username taken")
        else:
            cursor = conn.execute("""SELECT MAX(ID) from GUIDATA""")
            id = cursor.fetchone()
            if id[0] is None:
                id = 1
                conn.execute("""INSERT INTO GUIDATA (USERNAME, PASSWORD, ID) VALUES (?,?,?)""", (username, password, id))
                conn.commit()
                print("Username registered")
                a.startUp(username, id)
            else:
                id = int(id[0]) + 1
                conn.execute("""INSERT INTO GUIDATA (USERNAME, PASSWORD, ID) VALUES (?,?,?)""", (username, password, id))
                conn.commit()
                print("Username registered")
                a.startUp(username, id)

    
    elif args.login is not None:
        id = None
        loggedIn = False
        username = args.login[0]
        password = args.login[1]
        cur = conn.execute("""SELECT username from GUIDATA""")
        rows = cur.fetchall()
        for i in range(len(rows)):
            if str(rows[i][0]) == str(username):
                id = i
                break
        if id is not None:
            print("Match")
            cur = conn.execute("""SELECT password from GUIDATA""")
            rows = cur.fetchall()
            if str(rows[id][0]) == username:
                id = i
                print("Correct username and password")
                a.startUp(username, id)
            else:
                print("Incorrect password")
        else:
            print("No match")
    elif args.guest:
        print("Logging in as a guest")
        a.startUp("Guest", None)
    else:
        print("Argument required: --login, --guest or --register.\nUse -h for help.")
except Exception as e:
    print(e)
    createdbFile = input("Would you like to make a DB file at '" + args.file + "'? (Y/n): ")
    if createdbFile == "Y":
        c.createFile(args.file)