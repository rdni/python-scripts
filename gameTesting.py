class Map():
    def __init__(self, map):
        self.map = map
        self.playerPos = [1, 1]
        self.boxPos = [3, 2]
        self.xAmount = int((len(map[0]) - 2) / 2)
        self.yAmount = int((len(map) - 1) / 2)
        self.objects = ['P', 'X']
        self.objectPos = [1, 1,
                          3, 2]
        
    def printMap(self, map):
        for i in map:
            print(i)
    
    def editMap(self, map, changeX, changeY, charToUse):
        stringToUse = map[int(len(self.map) - (changeY * 2))]
        v = ""
        for i in range(len(stringToUse)):
            if i == changeX * 2 - 1:
                v += charToUse
            else:
                v += stringToUse[i]
        stringToUse = v
        self.map[int(len(self.map) - (changeY * 2))] = stringToUse
    
    def updateScreen(self, objects, objectPos):
        for i in range(0, int(len(objectPos)), 2):
            self.editMap(self.map, objectPos[i], objectPos[i+1], objects[int(i/2)])
        self.printMap(m.map)
    
    def move(self, objectToMove, direction):
        if objectToMove == "player":
            if direction == "u":
                if self.playerPos[1] + 1 > self.yAmount:
                    return "You can't do that!"
                elif [self.playerPos[0], self.playerPos[1] + 1] == self.boxPos:
                    if self.move("box", 'u') == "Error":
                        return "You can't do that!"
                self.editMap(self.map, self.playerPos[0], self.playerPos[1], ' ')
                self.editMap(self.map, self.playerPos[0], self.playerPos[1] + 1, 'P')
                self.playerPos = [self.playerPos[0], self.playerPos[1] + 1]
                return "Moved!"
            elif direction == "d":
                if self.playerPos[1] - 1 < 1:
                    return "You can't do that!"
                elif [self.playerPos[0], self.playerPos[1] - 1] == self.boxPos:
                    if self.move("box", 'd') == "Error":
                        return "You can't do that!"
                self.editMap(self.map, self.playerPos[0], self.playerPos[1], ' ')
                self.editMap(self.map, self.playerPos[0], self.playerPos[1] - 1, 'P')
                self.playerPos = [self.playerPos[0], self.playerPos[1] - 1]
                return "Moved!"
            elif direction == "l":
                if self.playerPos[0] - 1 < 1:
                    return "You can't do that!"
                elif [self.playerPos[0] - 1, self.playerPos[1]] == self.boxPos:
                    if self.move("box", 'l') == "Error":
                        return "You can't do that!"
                self.editMap(self.map, self.playerPos[0], self.playerPos[1], ' ')
                self.editMap(self.map, self.playerPos[0] - 1, self.playerPos[1], 'P')
                self.playerPos = [self.playerPos[0] - 1, self.playerPos[1]]
                return "Moved!"
            elif direction == "r":
                if self.playerPos[0] + 1 > self.xAmount:
                    return "You can't do that!"
                elif [self.playerPos[0] + 1, self.playerPos[1]] == self.boxPos:
                    if self.move("box", 'r') == "Error":
                        return "You can't do that!"
                self.editMap(self.map, self.playerPos[0], self.playerPos[1], ' ')
                self.editMap(self.map, self.playerPos[0] + 1, self.playerPos[1], 'P')
                self.playerPos = [self.playerPos[0] + 1, self.playerPos[1]]
                return "Moved!"
        elif objectToMove == "box":
            print("box move")
            if direction == "u":
                if self.boxPos[1] + 1 > self.yAmount:
                    return "Error"
                self.editMap(self.map, self.boxPos[0], self.boxPos[1], ' ')
                self.editMap(self.map, self.boxPos[0], self.boxPos[1] + 1, 'X')
                self.boxPos = [self.boxPos[0], self.boxPos[1] + 1]
                return "Moved!"
            elif direction == "d":
                if self.boxPos[1] - 1 > self.yAmount:
                    print(self.boxPos[1] - 1,  " ", self.yAmount)
                    return "Error"
                self.editMap(self.map, self.boxPos[0], self.boxPos[1], ' ')
                self.editMap(self.map, self.boxPos[0], self.boxPos[1] - 1, 'X')
                self.boxPos = [self.boxPos[0], self.boxPos[1] - 1]
                return "Moved!"
            elif direction == "l":
                if self.boxPos[0] - 1 > 1:
                    print(self.boxPos[0] - 1,  " ", self.xAmount)
                    return "Error"
                self.editMap(self.map, self.boxPos[0], self.boxPos[1], ' ')
                self.editMap(self.map, self.boxPos[0] - 1, self.boxPos[1], 'X')
                self.boxPos = [self.boxPos[0] - 1, self.boxPos[1]]
                return "Moved!"
            elif direction == "r":
                if self.boxPos[0] + 1 > self.xAmount:
                    print(self.boxPos[0] + 1,  " ", self.xAmount)
                    return "Error"
                self.editMap(self.map, self.boxPos[0], self.boxPos[1], ' ')
                self.editMap(self.map, self.boxPos[0] + 1, self.boxPos[1], 'X')
                self.boxPos = [self.boxPos[0] + 1, self.boxPos[1]]
                return "Moved!"
        

        

def makeMap(x, y):
    returnVal = []
    topPart = ""
    line = ""
    for v in range(x):
        line += "| "
    line += "|"
    topPart = (len(line) + 1) * "-"
    for i in range(y):
        returnVal.append(topPart)
        returnVal.append(line)
    returnVal.append(topPart)
    print(returnVal)
    return returnVal
    
m = Map(makeMap(5, 3))
m.updateScreen(m.objects, m.objectPos)
while True:
    print(m.move("player", input()))
    m.printMap(m.map)