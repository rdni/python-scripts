import re

filePath = "D:\\Code\\python-scripts\\test.sk"
filePathRead = "D:\\Code\\python-scripts\\CompilerTest.txt"

def writeToFile(information, filePath):
    f = open(filePath, "a")
    f.write(information + "\n")
    f.close()
    print(f"Wrote {information} to file {filePath}.")

def constructIfStatement(variables, variable1, condition, variable2="", \
compareTo=""):
    if variables == 1:
        ifStatement = "if {" + variable1 + "} is " + condition + " " + \
compareTo + ":"
        return ifStatement
    else:
        ifStatement = "if {" + variable1 + "} is " + condition + " {" + \
variable2 + "}:"
        return ifStatement

for line in open(filePathRead, "r"):
    read = line.split()
    if read[0] == "Literal":
        text = []
        for i in range((int(len(read))-1)):
            text.append(read[i+1])
        writeToFile(" ".join(text), filePath)
    elif read[0] == "create":
        if read[1] == "if":
            variable1 = read[2]
            condition = read[3]
            variable2type = read[4]
            variable2 = read[5]
            if variable2type == "literal":
                sendToFile = constructIfStatement(1, variable1, condition, \
compareTo=variable2)
            else:
                sendToFile = constructIfStatement(2, variable1, condition, \
variable2=variable2)
            writeToFile(sendToFile, filePath)
