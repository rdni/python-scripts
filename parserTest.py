from problems.atoi import atoi
import re

class ConversionError(Exception):
    def __init__(self, message="An invalid character was detected."):
        self.message = message
        super().__init__(self.message)


#cleanString, openInt = insertToList(cleanString, uncleanString, openLists, openQuote, startQuote, i, char, openInt)
def insertToList(cleanString: list, uncleanString: list, openLists: list, openQuote: bool, startQuote: int, i: int, char: str, openInt: int):
    if char == "\"":
        if uncleanString[i-1] == "\\":
            targetList = cleanString
            for i in range(len(openLists)):
                targetList: list = targetList[len(targetList)-1]
                targetList.append(char)
        elif openQuote:
            openQuote = False
            addToList = ""
            for y in range(startQuote, i, 1):
                addToList += uncleanString[y]
            targetList = cleanString
            for i in range(len(openLists)):
                targetList = targetList[len(targetList)-1]
            targetList.append(addToList)
        else:
            openQuote = True
            startQuote = i + 1
    elif openInt:
        addToList = ""
        for y in range(openInt, i, 1):
            addToList += uncleanString[y]
            print(addToList)
        targetList = cleanString
        for i in range(len(openLists)):
            targetList = targetList[len(targetList)-1]
            print(targetList)
        targetList.append(int(addToList))
        openInt = 0
        return cleanString, openInt
    
    return cleanString, openQuote, startQuote

def toList(uncleanString: str):
    cleanString = []
    openLists = []
    uncleanString = list(uncleanString)
    openQuote = False
    closingBracket = False
    startQuote = 0
    numOfLists = 0
    openInt = False
    for i, x in enumerate(uncleanString):
        print(i, x)
        try:
            if x == "[":
                if i == 0:
                    continue
                numOfLists += 1
                openLists.append(numOfLists)
                cleanString.append([])
            elif x == "]" and len(openLists) > 0:
                if openInt:
                    cleanString, openInt = insertToList(cleanString, uncleanString, openLists, openQuote, startQuote, i, x, openInt)
                closingBracket = True
                openLists.remove(openLists[len(openLists)-1])
                numOfLists - 1
            elif x == "]":
                if openInt:
                    cleanString, openInt = insertToList(cleanString, uncleanString, openLists, openQuote, startQuote, i, x, openInt)
                closingBracket = True
                if i == len(uncleanString) - 1:
                    continue
                raise ConversionError(f"Unexpected ']' found at character: {i}")
            elif x == " ":
                if openInt:
                    cleanString, openInt = insertToList(cleanString, uncleanString, openLists, openQuote, startQuote, i, x, openInt)
                continue
            elif x == "'" or x == "\"":
                cleanString, openQuote, startQuote = insertToList(cleanString, uncleanString, openLists, openQuote, startQuote, i, x, 0)
            elif x == ",":
                if openInt:
                    cleanString, openInt = insertToList(cleanString, uncleanString, openLists, openQuote, startQuote, i, x, openInt)
                    openInt = 0
                continue
            elif not openQuote:
                if re.fullmatch("\d", x):
                    if openInt:
                        pass
                    else:
                        openInt = i
                    continue
                raise ConversionError(message=f"An invalid character was detected at character: {i + 1} {x}")
        except TypeError as e:
            print(e)
            if x == "[":
                numOfLists += 1
                openLists = cleanString.append(numOfLists)
            elif x == "]":
                if openInt:
                    addToList = ""
                    for y in range(openInt, i, 1):
                        addToList += uncleanString[y]
                    cleanString.append(int(addToList))
                    openInt = 0
                closingBracket = True
                if i == len(uncleanString) - 1:
                    continue
                raise ConversionError(f"Unexpected ']' found at character: {i}")
            elif x == " ":
                if openInt:
                    cleanString, openInt = insertToList(cleanString, uncleanString, openLists, openQuote, startQuote, i, x, openInt)
                continue
            elif x == "'" or x == "\"":
                cleanString, openQuote, startQuote = insertToList(cleanString, uncleanString, openLists, openQuote, startQuote, i, x, 0)
            elif x == ",":
                if openInt:
                    cleanString, openInt = insertToList(cleanString, uncleanString, openLists, openQuote, startQuote, i, x, openInt)
                continue
            elif not openQuote:
                if re.fullmatch("\d", x):
                    if openInt:
                        pass
                    else:
                        openInt = i
                    continue
                raise ConversionError(message=f"An invalid character was detected at character: {i + 1} {x}")
    if openQuote or not closingBracket:
        print(re.fullmatch("1234567890", x))
        raise ConversionError(message="No closing bracket")
    return cleanString

class NewParser():
    def __init__(self) -> None:
        self.functions = {
            "list": self.makeList
        }
        self.specialChars = {
            "[": "list",
            "]": "endList"
        }
        
    def evaluation(self, string: str):
        if any(x in string for x in self.specialChars.keys()):
            return self.read(string)
        else:
            if string.isnumeric():
                return atoi(string)
            else:
                return string
        
    def read(self, string: str):
        try:
            func = self.specialChars[string[0]]
            if func == self.functions["list"]:
                return self.functions["list"](string)
                
        except KeyError:
            return False
    
    def makeList(self, string: str):
        newList = []
        openLists = []
        for i, x in enumerate(string):
            if x == "[":
                newList.append(self.makeList(string[i:]))
                openLists.append(openLists[0] if openLists != [] else 1)
            elif x == "]":
                if openLists != []:
                    openLists.remove(openLists[len(openLists)-1])
                return newList
            elif x == " ":
                continue
            else:
                if openLists != []:
                    target = newList
                    for i in range(len(openLists)-1):
                        target = target[len(target)-1]
                    target[len(newList)-1].append(x)
                else:
                    newList.append(x)
        return newList

parser = NewParser()
print(parser.read(input()))
print(parser.evaluation(input()))
# print(toList(input()))