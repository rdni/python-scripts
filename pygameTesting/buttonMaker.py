class SpecialButton:
    def __init__(self, size, location, func=exit):
        self.size = size
        self.location = location
        self.func = func
        
    def isOnButton(self, mousePos):
        inBoxX = mousePos[0] <= self.location[0]+self.size[0] and \
        mousePos[0] >= self.location[0]
        inBoxY = mousePos[1] <= self.location[1]+self.size[1] and \
        mousePos[1] >= self.location[1]
        return inBoxX and inBoxY

    def on_click(self, mousePos):
        if self.isOnButton(mousePos):
            self.func()
            return True
        else:
            return False