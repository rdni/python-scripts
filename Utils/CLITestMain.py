import time

class Main():
    def __init__(self, username, id):
        self.username = username
        self.id = id
        print("You have launched the program.")
        time.sleep(1)
        print("You are logged in as " + self.username)
        if username == "Guest":
            print("You are logged in as a guest. They can only do certain things")
            self.guest = True
            self.guestStart()

    def guestStart(self):
        time.sleep(2)
        


def startUp(username, id):
    app = Main(username, id)