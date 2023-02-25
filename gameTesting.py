"""
    The map is stored in an array of strings, that can be individually be
    edited with the editMap function. The map can be displayed with the print
    map function, but it is better to use updateScreen, so that any changes
    made will always be shown.
    
    Map generation is done by making "| " multiplied by length. After this an 
    extra "|" is added. Then the number of dashes needed is calculated, by 
    the length of line multipied it by "-".

"""


class Map():#This is the main object
    def __init__(self, map):
        self.map = map#stores data about what should be shown
        self.playerPos = [0, 0]#Starting positions of things inside of the game
        self.boxPos = [10, 7]
        self.endPos = [7, 5]
        #Finding the length/height of map and making it an integer
        self.xAmount = int((len(map[0]) - 2) / 2)
        self.yAmount = int((len(map) - 1) / 2)
        self.finished = False
        
    def printMap(self, map):#Shows map to player
        for i in map:
            print(i)

#Used to edit single characters in the map
    def editMap(self, map, changeX, changeY, charToUse):
        #Finds what line to edit
        stringToUse = map[int(len(self.map) - (changeY * 2))]
        v = ""
        for i in range(len(stringToUse)):
            if i == changeX * 2 - 1:#Checks if thing to change
                v += charToUse#changes
            else:
                v += stringToUse[i]#adds what was there before
        #sets line to output
        self.map[int(len(self.map) - (changeY * 2))] = v
    
    #Draws objects to map
    def updateScreen(self, objects, objectPos):
        for i in range(0, int(len(objectPos)), 2):
            if objectPos[i] == 0:#checks if the position is invalid
                continue
            elif objectPos[i + 1] == 0:#checks if the position is invalid
                continue
            obj = objects[int(i/2)]#Gets what should be drawn
            #Draws to map
            self.editMap(self.map, objectPos[i], objectPos[i+1], obj)
        #displays changes
        self.printMap(self.map)
    
    def move(self, objectToMove, direction):#Moves any objects
        if objectToMove == "player":#if the player is moving
            if direction == "u":#Up
                if self.playerPos[1] + 1 > self.yAmount:
                    return "You can't do that!"#Error
                elif [self.playerPos[0], self.playerPos[1] + 1] == self.boxPos:
                    if self.move("box", 'u') == "Error":
                        return "You can't do that!"#Error
                #Wipes previous position
                self.editMap(self.map, self.playerPos[0], self.playerPos[1], ' ')
                #Sets new position
                self.editMap(self.map, self.playerPos[0], self.playerPos[1] + 1, 'P')
                #Sets player position
                self.playerPos = [self.playerPos[0], self.playerPos[1] + 1]
                return "Moved!"
            elif direction == "d":#down
                if self.playerPos[1] - 1 < 1:
                    return "You can't do that!"#Error
                elif [self.playerPos[0], self.playerPos[1] - 1] == self.boxPos:
                    if self.move("box", 'd') == "Error":
                        return "You can't do that!"#Error
                #Wipes previous position
                self.editMap(self.map, self.playerPos[0], self.playerPos[1], ' ')
                #Sets new position
                self.editMap(self.map, self.playerPos[0], self.playerPos[1] - 1, 'P')
                #Sets player position
                self.playerPos = [self.playerPos[0], self.playerPos[1] - 1]
                return "Moved!"
            elif direction == "l":
                if self.playerPos[0] - 1 < 1:
                    return "You can't do that!"#Error
                elif [self.playerPos[0] - 1, self.playerPos[1]] == self.boxPos:
                    if self.move("box", 'l') == "Error":
                        return "You can't do that!"#Error
                #Wipes previous position
                self.editMap(self.map, self.playerPos[0], self.playerPos[1], ' ')
                #Sets new position
                self.editMap(self.map, self.playerPos[0] - 1, self.playerPos[1], 'P')
                #Sets player position
                self.playerPos = [self.playerPos[0] - 1, self.playerPos[1]]
                return "Moved!"
            elif direction == "r":
                if self.playerPos[0] + 1 > self.xAmount:
                    return "You can't do that!"#Error
                elif [self.playerPos[0] + 1, self.playerPos[1]] == self.boxPos:
                    if self.move("box", 'r') == "Error":
                        return "You can't do that!"#Error
                #Wipes previous position
                self.editMap(self.map, self.playerPos[0], self.playerPos[1], ' ')
                #Sets new position
                self.editMap(self.map, self.playerPos[0] + 1, self.playerPos[1], 'P')
                #Sets player position
                self.playerPos = [self.playerPos[0] + 1, self.playerPos[1]]
                return "Moved!"
        elif objectToMove == "box":
            print("box move")
            if direction == "u":
                if self.boxPos[1] + 1 > self.yAmount:
                    return "Error"
                elif [self.boxPos[0], self.boxPos[1] + 1] == self.endPos:
                    #Wipes both ending and box from map
                    self.editMap(self.map, self.boxPos[0], self.boxPos[1], ' ')
                    self.editMap(self.map, self.endPos[0], self.endPos[1], ' ')
                    #Wipes coordinates of box and end
                    self.boxPos = [0, 0]
                    self.endPos = [0, 0]
                    #Currently unused flag for level complete
                    finished = True
                    return "Moved!"
                #Wipes previous position
                self.editMap(self.map, self.boxPos[0], self.boxPos[1], ' ')
                #Sets new position
                self.editMap(self.map, self.boxPos[0], self.boxPos[1] + 1, 'X')
                self.boxPos = [self.boxPos[0], self.boxPos[1] + 1]
                return "Moved!"
            elif direction == "d":
                if self.boxPos[1] - 1 < 1:
                    print(self.boxPos[1] - 1,  " ", self.yAmount)
                    return "Error"
                elif [self.boxPos[0], self.boxPos[1] - 1] == self.endPos:
                    #Wipes both ending and box from map
                    self.editMap(self.map, self.boxPos[0], self.boxPos[1], ' ')
                    self.editMap(self.map, self.endPos[0], self.endPos[1], ' ')
                    #Wipes coordinates of box and end
                    self.boxPos = [0, 0]
                    self.endPos = [0, 0]
                    #Currently unused flag for level complete
                    finished = True
                    return "Moved!"
                #Wipes previous position
                self.editMap(self.map, self.boxPos[0], self.boxPos[1], ' ')
                #Sets new position
                self.editMap(self.map, self.boxPos[0], self.boxPos[1] - 1, 'X')
                self.boxPos = [self.boxPos[0], self.boxPos[1] - 1]
                return "Moved!"
            elif direction == "l":
                if self.boxPos[0] - 1 < 1:
                    print(self.boxPos[0] - 1,  " ")
                    return "Error"
                elif [self.boxPos[0] - 1, self.boxPos[1]] == self.endPos:
                    #Wipes both ending and box from map
                    self.editMap(self.map, self.boxPos[0], self.boxPos[1], ' ')
                    self.editMap(self.map, self.endPos[0], self.endPos[1], ' ')
                    #Wipes coordinates of box and end
                    self.boxPos = [0, 0]
                    self.endPos = [0, 0]
                    #Currently unused flag for level complete
                    finished = True
                    return "Moved!"
                #Wipes previous position
                self.editMap(self.map, self.boxPos[0], self.boxPos[1], ' ')
                #Sets new position
                self.editMap(self.map, self.boxPos[0] - 1, self.boxPos[1], 'X')
                self.boxPos = [self.boxPos[0] - 1, self.boxPos[1]]
                return "Moved!"
            elif direction == "r":
                if self.boxPos[0] + 1 > self.xAmount:
                    print(self.boxPos[0] + 1,  " ", self.xAmount)
                    return "Error"
                elif [self.boxPos[0] + 1, self.boxPos[1]] == self.endPos:
                    #Wipes both ending and box from map
                    self.editMap(self.map, self.boxPos[0], self.boxPos[1], ' ')
                    self.editMap(self.map, self.endPos[0], self.endPos[1], ' ')
                    #Wipes coordinates of box and end
                    self.boxPos = [0, 0]
                    self.endPos = [0, 0]
                    #Currently unused flag for level complete
                    finished = True
                    return "Moved!"
                #Wipes previous position
                self.editMap(self.map, self.boxPos[0], self.boxPos[1], ' ')
                #Sets new position
                self.editMap(self.map, self.boxPos[0] + 1, self.boxPos[1], 'X')
                self.boxPos = [self.boxPos[0] + 1, self.boxPos[1]]
                return "Moved!"
        

        

def makeMap(x, y):
    returnVal = []#Makes an empty list to be appended
    topPart = ""#Makes empty strings to be added to
    line = "| " * x#Make the template for where data can be changed
    line += "|"
    topPart = (len(line)) * "-"#Makes the line of dashes
    for i in range(y):#Loops making the map
        returnVal.append(topPart)
        returnVal.append(line)
    returnVal.append(topPart)#Adds the bottom part of map
    return returnVal
    
m = Map(makeMap(20, 20))#Create a map that is 10 across and 5 up
#Initially edits and display the map's starting conditions
m.updateScreen(['P', 'X', 'O'], [m.playerPos[0], m.playerPos[1], m.boxPos[0], m.boxPos[1], m.endPos[0], m.endPos[1]])
while True:#Loops until player holds ctrl + c
    #Gets and prints the result of the players input (move)
    print(m.move("player", input()))
    #Updates all objects to be displayed after move
    m.updateScreen(['P', 'X', 'O'], [m.playerPos[0], m.playerPos[1], m.boxPos[0], m.boxPos[1], m.endPos[0], m.endPos[1]])
    if m.finished:
        print("You beat the level!")
        break