import argparse

parser = argparse.ArgumentParser()#parser

parser.add_argument("username", type=str, help="Input username")#arguments
parser.add_argument("password", type=str, help="Input password")
parser.add_argument("--register", "-r", type=bool, help="Register new account. True or False", default=False)
parser.add_argument("--file", "-f", type=str, help="Path of storage file. Must be .txt.", default="C:\\Users\\peque\\guiData.txt")


args = parser.parse_args()#parses args

def removeBadChar(x):#Replace bad characters
        x = x.replace(" ", "")
        x = x.replace(".", "")
        x = x.replace("\\", "")
        return x

if args.register:
    usernameTest = 0

    username = removeBadChar(args.username)
    password = removeBadChar(args.password)

    try:
        for line in open(args.file,"r").readlines():#Opens guiData.txt (read only)
            registerTry = line.split()
            if len(registerTry) == 0:
                continue#Checks if there is something there
            if username == registerTry[0]:
                usernameTest = True#Checks username match
            else:
                continue
        if usernameTest == 0:#Checks if any matching names exist
            file = open(args.file, "a")
            file.write(username + " " + password + "\n")#Writes username and password to data file
            file.close()
            print("Username " + username + " registered")
        else:
            print("Name taken")
    except FileNotFoundError:
        with open(args.file, "w") as file:#If there is no file, it will make one
            file.write(username + " " + password + "\n")#Writes username and password to data file
            file.close()
else:
    loggedIn = False
    username = args.username
    password = args.password
    try:
        for line in open(args.file, "r").readlines():#Open file guiData.txt
            login_info = line.split()
            if username == login_info[0] and password == login_info[1]:#Checks if username and passwords match
                loggedIn = True
                loggedInTo = username
        if loggedIn == True:
            print("Successfully logged in as " + username + ".")
        else:
            print("Incorrect username or password")
    except FileNotFoundError:#No file found
        print("No data file found. File should be at '" + args.file + "'.")