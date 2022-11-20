import logging

class Logger():
    def __init__(self):
        logging.basicConfig(filename="logfile.txt", level=logging.INFO)
        self.logger1 = logging.getLogger("my-app")
    def log(self, logValue):
        self.logger1.info(f"{__name__} returned value {logValue}")
        
logger = Logger()

class Vector():
    def __init__(self, x, y, logger):
        self.x = x
        self.y = y
        self.logger = logger
    def logged(self, functionDone):
        self.logger.log(functionDone)
    def __add__(self, other):
        returnValue = Vector(self. x + other.x, self.y + other.y, self.logger)
        self.logged(returnValue)
        return returnValue
    def __sub__(self, other):
        returnValue = Vector(self. x - other.x, self.y - other.y, self.logger)
        self.logged(returnValue)
        return returnValue
    def __mul__(self, other):
        returnValue = Vector(self. x * other.x, self.y * other.y, self.logger)
        self.logged(returnValue)
        return returnValue
    def __truediv__(self, other):
        returnValue = Vector(self. x / other.x, self.y / other.y, self.logger)
        self.logged(returnValue)
        return returnValue
    def __repr__(self):
        returnValue = f"X: {self.x}, Y: {self.y}"
        self.logged(returnValue)
        return returnValue
    def __call__(self):
        print(f"X: {self.x}, Y: {self.y}")

v1 = Vector(10, 20, logger)
v2 = Vector(40, 35, logger)
v3 = v1 + v2
print(v3)
v3 = v1 - v2
print(v3)
v3 = v1 * v2
print(v3)
v3 = v1 / v2
print(v3)

def multiply(a, b):
    logValue = f"{a} multiplied by {b} equals {a*b}."
    logger.log(logValue)
    print(logValue)

multiply(2,5)

logger.log("Program ended\n")