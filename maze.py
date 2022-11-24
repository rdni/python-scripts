"""If a function is called "x0y1" it means that it is in the 
position x = 0 and y = 1
"""

import logging  #allows logging to logfile.txt

from datetime import datetime  #Used for logging more accuratly

class Logger():
    def __init__(self):#Runs on start
        logging.basicConfig(filename="logfile.txt", level=logging.INFO)
        #Prints to logfile.txt as level info
        self.logger1 = logging.getLogger("maze-game")#Gets the logger
    def log(self, logValue):#Called when you want to log anything
        self.getTime = datetime.now()
        self.cT = self.getTime.strftime("%H:%M:%S")
        self.logger1.info(f"{self.cT}: {__name__} returned value {logValue}")
    def newline(self):#Used when restarting the program
        self.getTime = datetime.now()
        self.currentTime = self.getTime.strftime("%H:%M:%S")
        #Fetch time and assign it to variable
        self.logger1.info(f"\nNew program at '{self.currentTime}'.")
        
logger = Logger()

class mainMaze():
    def __init__(self, logger):
        self.logger = logger  #Creates logger
        self.logger.newline() #Sets up logger
        self.x = 0
        self.y = 0 #Assigns values to x and y
        self.itemPickedUp01 = False
        self.itemPickedUp20 = False
        self.itemPickedUp31 = False
        self.itemPickedUp22 = False #Sets item picked up to false
        self.monstDead01 = False
        self.monstDead20 = False
        self.monstDead31 = False
        self.monstDead22 = False #Sets boss killed up to false
        self.logger.log("Init completed")#Message in log that log is complete
        self.x0y0()#Begins maze

    def askDirection(self, actions, directions):
        self.actionDone = (False,)
        self.actions = actions
        self.directions = directions
        print(f"Your position is X: {self.x} Y: {self.y}")#says x,y + options
        print(f"You can {self.makeList(self.actions)} \
{self.makeList(self.directions)}")
        self.action = input("What action? ") #Gets user input
        self.action = self.action.split() #Makes input into a list
        if len(self.action) == 1: #Checks length of list
            for i in range(0, len(self.actions), 1): #Check if action matches
                if self.actions[i] == self.action[0].lower():
                    self.actionDone = self.actions[i]
        elif len(self.action) == 2: #Checks length of list
            for i in range(0, len(self.actions), 1):
                if self.action[0].lower() == self.actions[i]:
                    self.actionDone = self.action
        else: #Checks if it is none of them
            self.logger.log(f"Error: askDirection. {self.action} isn't valid")
            print("Error")
            
        return self.actionDone #Returns value when finished

    def getPos(self): #Checks position
        self.logger.log(self.x, self.y)
        return self.x, self.y
    
    def up(self):
        self.y = self.y - 1 #Updates position
        self.logger.log(f"Player went up to X: {self.x} Y: {self.y}")

    def down(self):
        self.y = self.y + 1 #Updates position
        self.logger.log(f"Player went down to X: {self.x} Y: {self.y}")

    def left(self):
        self.x = self.x - 1 #Updates position
        self.logger.log(f"Player went left to X: {self.x} Y: {self.y}")

    def right(self):
        self.x = self.x + 1 #Updates position
        self.logger.log(f"Player went right to X: {self.x} Y: {self.y}")
        
    def makeList(self, lm): #Creates a string list
        self.lm = lm
        if self.lm == []: #Checks for blank list
                self.logger.log("")
                return ""
        elif len(self.lm) == 1: #Checks for 1 long list
            return self.lm[0]
        elif len(self.lm) == 2: #Checks for 2 long list
            self.logger.log(f"{self.lm[0]} or {self.lm[1]}")
            return f"{self.lm[0]} or {self.lm[1]}"
        elif len(self.lm) == 3: #Checks for 3 long list
            self.logger.log(f"{self.lm[0]}, {self.lm[1]} or {self.lm[2]}")
            return f"{self.lm[0]}, {self.lm[1]} or {self.lm[2]}"
        else: #Checks for invalid lists
            self.logger.log(f"Error: makeList. {self.lm} isn't valid")
            print("Error")

    
    def bossRoom(self, question, answer): #Boss room definition
        self.question = question
        self.answer = answer #Gets values
        self.monstDead = False
        while self.monstDead == False:  #Conditional loop
            self.actions = ["attack"]
            self.directions = []
            self.actionDone = self.askDirection(self.actions, self.directions)
            if self.actionDone == "attack":  #Checks for input
                self.question = input(question)
                if self.question.lower() == answer: #Checks for correct answer
                    print("The monster is dead.")
                    self.logger.log("The monster is dead.")
                    self.monstDead = True
                else:
                    print("The monster lives. Try again")
                    self.logger.log("The monster lives. Try again")
        return True


#Rooms section


    def x0y0(self): #Beginning room
        print("You stand in a dark room, with only 2 exits illuminated.")
        self.actions = ["go"]
        self.directions = ["right", "down"] #Actions and directions
        self.actionDone = self.askDirection(self.actions, self.directions)
        if self.actionDone[0] == "go": #Checks for action
            if self.actionDone[1] == "right":
                self.right()
                self.x1y0()
            elif self.actionDone[1] == "down":
                self.down()
                self.x0y1()
            else:
                print("Not possible")
                self.logger.log(f"Error: x0y0. {self.actionDone} isn't valid")
                print("Error")
                self.x0y0()
        else:
            self.logger.log(f"Error: x0y0. {self.actionDone} isn't valid")
            print("Error")
            self.x0y0()

    def x3y3(self):
        print("You win! Well done.")

#Find nothing section

    def x1y0(self):
        print("You find nothing")
        self.actions = ["go"]
        self.directions = ["left", "right"] #Actions and directions
        self.actionDone = self.askDirection(self.actions, self.directions)
        if self.actionDone[0] == "go": #Checks for action
            if self.actionDone[1] == "right":
                self.right()
                self.x2y0()
            elif self.actionDone[1] == "left":
                self.left()
                self.x0y0()
            else:
                print("Not possible")
                self.logger.log(f"Error: x1y0. {self.actionDone} isn't valid")
                print("Error")
                self.x1y0()
        else:
            self.logger.log(f"Error: x1y0. {self.actionDone} isn't valid")
            print("Error")
            self.x1y0()
    
    def x2y1(self):
        print("You find nothing")
        self.actions = ["go"]
        self.directions = ["down", "right", "up"] #Actions and directions
        self.actionDone = self.askDirection(self.actions, self.directions)
        if self.actionDone[0] == "go": #Checks for action
            if self.actionDone[1] == "right":
                self.right()
                self.x3y1()
            elif self.actionDone[1] == "down":
                self.down()
                self.x2y2()
            elif self.actionDone[1] == "up":
                self.up()
                self.x2y0()
            else:
                print("Not possible")
                self.logger.log(f"Error: x2y1. {self.actionDone} isn't valid")
                print("Error")
                self.x2y1()
        else:
            self.logger.log(f"Error: x2y1. {self.actionDone} isn't valid")
            print("Error")
            self.x2y1()

    def x3y2(self):
        print("You find nothing")
        self.actions = ["go"]
        self.directions = ["down", "right", "up"] #Actions and directions
        self.actionDone = self.askDirection(self.actions, self.directions)
        if self.actionDone[0] == "go": #Checks for action
            if self.actionDone[1] == "left":
                self.left()
                self.x2y2()
            elif self.actionDone[1] == "down":
                self.down()
                self.x3y3()
            else:
                print("Not possible")
                self.logger.log(f"Error: x3y2. {self.actionDone} isn't valid")
                print("Error")
                self.x3y2()
        else:
            self.logger.log(f"Error: x3y2. {self.actionDone} isn't valid")
            print("Error")
            self.x3y2()

#Monster section

    def x2y0(self):
        if self.monstDead20 == True:
            pass
        else:
            self.monstDead20 = False
            print("You come to a room with a monster.")
            self.question = """What is the keyword for condition controlled \
loops? """
            self.answer = "while"
            self.monstDead20 = True
            self.bossRoom(self.question, self.answer)
            self.monstDead20 = True
        if self.itemPickedUp20 == True:
            self.actions = ["go"]
        else:
            self.actions = ["pickup", "go"]
        self.directions = ["down", "left", "right"] #Actions and directions
        self.actionDone = self.askDirection(self.actions, self.directions)
        if self.actionDone[0] == "go": #Checks for action
            if self.actionDone[1] == "left":
                self.left()
                self.x1y0()
            elif self.actionDone[1] == "down":
                self.down()
                self.x2y1()
            elif self.actionDone[1] == "right":
                self.x3y0()
            else:
                print("Not possible")
                self.logger.log(f"Error: x2y0. {self.actionDone} isn't valid")
                print("Error")
                self.x2y0()
        elif self.actionDone == "pickup": #Checks for action
            print("Map picked up. It says that down is the correct way.")
            self.itemPickedUp20 = True
            self.x2y0()
        else:
            self.logger.log(f"Error: x2y0. {self.actionDone} isn't valid")
            print("Error")
            self.x2y0()

    def x2y2(self):
        if self.monstDead22 == True:
            pass
        else:
            self.monstDead22 = False
            print("You come to a room with a monster.")
            self.question = """How many types of iteration are there? """
            self.answer = "2"
            self.monstDead22 = True
            self.bossRoom(self.question, self.answer)
            self.monstDead20 = True
        if self.itemPickedUp22 == True:
            self.actions = ["go"]
        else:
            self.actions = ["pickup", "go"]
        self.directions = ["down", "left", "right"] #Actions and directions
        self.actionDone = self.askDirection(self.actions, self.directions)
        if self.actionDone[0] == "go": #Checks for action
            if self.actionDone[1] == "left":
                self.x1y2()
            elif self.actionDone[1] == "up":
                self.up()
                self.x2y1()
            elif self.actionDone[1] == "right":
                self.x3y2()
            else:
                print("Not possible")
                self.logger.log(f"Error: x2y2. {self.actionDone} isn't valid")
                print("Error")
                self.x2y2()
        elif self.actionDone == "pickup": #Checks for action
            print("Map picked up. It says that down is the correct way.")
            self.itemPickedUp20 = True
            self.x2y2()
        else:
            self.logger.log(f"Error: x2y02. {self.actionDone} isn't valid")
            print("Error")
            self.x2y2()

    def x3y1(self):
        if self.monstDead31 == True:
            pass
        else:
            self.monstDead31 = False
            print("You come to a room with a monster.")
            self.question = """What is if the keyword for? """
            self.answer = "selection"
            self.bossRoom(self.question, self.answer)
            self.monstDead31 = True
        if self.itemPickedUp31 == True:
            self.actions = ["go"]
        else:
            self.actions = ["pickup", "go"]
        self.directions = ["left", "right"] #Actions and directions
        self.actionDone = self.askDirection(self.actions, self.directions)
        if self.actionDone[0] == "go": #Checks for action
            if self.actionDone[1] == "left":
                self.left()
                self.x2y1()
            if self.actionDone[1] == "right":
                self.x4y1()
            else:
                self.logger.log(f"Error: x3y1. {self.actionDone} isn't valid")
                print("Error")
                self.x3y1()
        elif self.actionDone == "pickup": #Checks for action
            print("Map picked up. It says that left is the correct way.")
            self.itemPickedUp31 = True
            self.x3y1()
        else:
            self.logger.log(f"Error: x3y1. {self.actionDone} isn't valid")
            print("Error")
            self.x3y1()

    
    def x0y1(self):
        if self.monstDead01 == True:
            pass
        else:
            self.monstDead01 = False
            print("You come to a room with a monster.")
            self.question = """What is the keyword for count controlled \
loops? """
            self.answer = "for"
            self.bossRoom(self.question, self.answer)
            self.monstDead01 = True
        if self.itemPickedUp01 == True:
            self.actions = ["go"]
        else:
            self.actions = ["pickup", "go"]
        self.directions = ["down", "up"] #Actions and directions
        self.actionDone = self.askDirection(self.actions, self.directions)
        if self.actionDone[0] == "go": #Checks for action
            if self.actionDone[1] == "up":
                self.up()
                self.x0y0()
            if self.actionDone[1] == "down":
                self.x0y2()
            else:
                print("Not possible")
                self.logger.log(f"Error: x0y1. {self.actionDone} isn't valid")
                print("Error")
                self.x0y1()
        elif self.actionDone == "pickup": #Checks for action
            print("Map picked up. It says that up is the correct way.")
            self.itemPickedUp01 = True
            self.x0y1()
        else:
            self.logger.log(f"Error: x0y1. {self.actionDone} isn't valid")
            print("Error")
            self.x0y1()

#Dead end section. These just send you back to where you were
    
    def x0y2(self):
        print("You find a dead end. You turn around")
        self.x0y1()

    def x4y1(self):
        print("You find a dead end. You turn around.")
        self.x3y1()

    def x3y0(self):
        print("You find a dead end.You turn around.") 
        self.x2y0()

    def x1y2(self):
        print("You find a dead end.You turn around.") 
        self.x2y2()


startMaze = mainMaze(logger)