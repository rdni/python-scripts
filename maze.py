class mainMaze():
    def __init__(self):
        self.x = 0
        self.y = 0
        self.itemPickedUp01 = False
        self.itemPickedUp20 = False
        self.itemPickedUp31 = False
        self.itemPickedUp22 = False
        self.monstDead01 = False
        self.monstDead20 = False
        self.monstDead31 = False
        self.monstDead22 = False
        self.x0y0()

    def askDirection(self, actions, directions):
        self.actionDone = (False,)
        self.actions = actions
        self.directions = directions
        print(f"Your position is X: {self.x} Y: {self.y}")
        print(f"You can {self.makeList(self.actions)} {self.makeList(self.directions)}")
        self.action = input("What action? ")
        self.action = self.action.split()
        if len(self.action) == 1:
            for i in range(0, len(self.actions), 1):
                if self.actions[i] == self.action[0].lower():
                    self.actionDone = self.actions[i]
        elif len(self.action) == 2:
            for i in range(0, len(self.actions), 1):
                if self.action[0].lower() == self.actions[i]:
                    self.actionDone = self.action
            
        return self.actionDone

    def getPos(self):
        return self.x, self.y
    
    def up(self):
        self.y = self.y - 1

    def down(self):
        self.y = self.y + 1

    def left(self):
        self.x = self.x - 1

    def right(self):
        self.x = self.x + 1
        
    def makeList(self, listMaker):
        self.listMaker = listMaker
        if self.listMaker == []:
                return " "
        elif len(self.listMaker) == 1:
            return self.listMaker[0]
        elif len(listMaker) == 2:
            return f"{self.listMaker[0]} or {self.listMaker[1]}"
        elif len(listMaker) == 3:
            return f"{self.listMaker[0]}, {self.listMaker[1]} or {self.listMaker[2]}"

    
    def bossRoom(self, question, answer):
        self.question = question
        self.answer = answer
        self.monstDead = False
        while self.monstDead == False:
            self.actions = ["attack"]
            self.directions = []
            self.actionDone = self.askDirection(self.actions, self.directions)
            if self.actionDone == "attack":
                self.question = input(question)
                if self.question.lower() == answer:
                    print("The monster is dead.")
                    self.monstDead = True
                else:
                    print("The monster lives. Try again")
        return True


    def x0y0(self):
        self.x = 0
        self.y = 0
        print("You stand in a dark room, with only 2 exits illuminated.")
        self.actions = ["go"]
        self.directions = ["right", "down"]
        self.actionDone = self.askDirection(self.actions, self.directions)
        if self.actionDone[0] == "go":
            if self.actionDone[1] == "right":
                self.right()
                self.x1y0()
            elif self.actionDone[1] == "down":
                self.down()
                self.x0y1()
            else:
                print("Not possible")

    def x1y0(self):
        print("You find nothing")
        self.actions = ["go"]
        self.directions = ["left", "right"]
        self.actionDone = self.askDirection(self.actions, self.directions)
        if self.actionDone[0] == "go":
            if self.actionDone[1] == "right":
                self.right()
                self.x2y0()
            elif self.actionDone[1] == "left":
                self.left()
                self.x0y0()
            else:
                print("Not possible")
    
    def x2y1(self):
        print("You find nothing")
        self.actions = ["go"]
        self.directions = ["down", "right", "up"]
        self.actionDone = self.askDirection(self.actions, self.directions)
        if self.actionDone[0] == "go":
            if self.actionDone[1] == "right":
                self.right()
                self.x3y1()
            elif self.actionDone[1] == "down":
                self.down()
                print("Nothing yet")
            elif self.actionDone[1] == "up":
                self.up()
                self.x2y0()
            else:
                print("Not possible")

    def x2y0(self):
        if self.monstDead20 == True:
            pass
        else:
            self.monstDead20 = False
            print("You come to a room with a monster.")
            self.question = """What is the keyword for condition controlled
loops? """
            self.answer = "while"
            self.monstDead20 = True
            self.bossRoom(self.question, self.answer)
            self.monstDead20 = True
        if self.itemPickedUp20 == True:
            self.actions = ["go"]
        else:
            self.actions = ["pickup", "go"]
        self.directions = ["down", "left", "right"]
        self.actionDone = self.askDirection(self.actions, self.directions)
        if self.actionDone[0] == "go":
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
        elif self.actionDone == "pickup":
            print("Map picked up. It says that down is the correct way.")
            self.itemPickedUp20 = True
            self.x2y0()

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
        self.directions = ["left", "right"]
        self.actionDone = self.askDirection(self.actions, self.directions)
        if self.actionDone[0] == "go":
            if self.actionDone[1] == "left":
                self.left()
                self.x2y1()
            if self.actionDone[1] == "right":
                self.x4y1()
            else:
                print("Not possible")
        elif self.actionDone == "pickup":
            print("Map picked up. It says that left is the correct way.")
            self.itemPickedUp31 = True
            self.x3y1()

    
    def x0y1(self):
        if self.monstDead01 == True:
            pass
        else:
            self.monstDead01 = False
            print("You come to a room with a monster.")
            self.question = """What is the keyword for count controlled
loops? """
            self.answer = "for"
            self.bossRoom(self.question, self.answer)
            self.monstDead01 = True
        if self.itemPickedUp01 == True:
            self.actions = ["go"]
        else:
            self.actions = ["pickup", "go"]
        self.directions = ["down", "up"]
        self.actionDone = self.askDirection(self.actions, self.directions)
        if self.actionDone[0] == "go":
            if self.actionDone[1] == "up":
                self.up()
                self.x0y0()
            if self.actionDone[1] == "down":
                self.x0y2()
            else:
                print("Not possible")
        elif self.actionDone == "pickup":
            print("Map picked up. It says that up is the correct way.")
            self.itemPickedUp01 = True
            self.x0y1()
    
    def x0y2(self):
        print("You find a dead end. You turn around")
        self.x0y1()

    def x4y1(self):
        print("You find a dead end. You turn around.")
        self.x3y1()

    def x3y0(self):
        print("You find a dead end.You turn around.") 
        self.x2y0()


startMaze = mainMaze()