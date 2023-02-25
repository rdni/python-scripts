import pygame
from random import randint
from time import sleep
from buttonMaker import SpecialButton

def printer():
    print("Pressed!")

pygame.init()

screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)

pygame.display.set_caption("Testing Pygame")

icon = pygame.image.load("icon.png")
pygame.display.set_icon(icon)

gameRunning = True
frameCounter = 0
buttonPressed = False
score = 0

size = (screen.get_size()[0]/2, screen.get_size()[1]/10)
location = (screen.get_size()[0]/4, screen.get_size()[1] - (screen.get_size()[1]/8))
exitRectangle = pygame.surface.Surface(size)
exitButton = SpecialButton(size=size, location=location, func=exit)

size = (randint(screen.get_size()[0]/20, screen.get_size()[0]), randint(screen.get_size()[1]/20, screen.get_size()[1]))
rectangle = pygame.surface.Surface(size)
location = (randint(0, (screen.get_size()[0]-rectangle.get_width())), randint(0, (screen.get_size()[1]-rectangle.get_height())))
button = SpecialButton(size=size, location=location, func=exit)

while gameRunning:
    screen.fill((164, 236, 245))
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameRunning = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if button.on_click(pygame.mouse.get_pos()):
                buttonPressed = True
            elif exitButton.on_click(pygame.mouse.get_pos()):
                pass
            else:
                pass
    
    if not frameCounter % 30 or buttonPressed:
        if buttonPressed:
            buttonPressed = False
            frameCounter = frameCounter + 30 - (frameCounter % 30)
            score += 1
        else:
            print("You missed it!")
        size = (randint(screen.get_size()[0]/20, screen.get_size()[0]), randint(screen.get_size()[1]/20, screen.get_size()[1]))
        rectangle = pygame.surface.Surface(size)
        location = (randint(0, (screen.get_size()[0]-rectangle.get_width())), randint(0, (screen.get_size()[1]-rectangle.get_height())))
        screen.blit(rectangle, dest=location)
        button = SpecialButton(size=size, location=location, func=printer)
    else:
        screen.blit(rectangle, location)
    screen.blit(exitRectangle, exitButton.location)
        
    if not frameCounter % 600:
        print(f"You got an average of {float(score)/10.0} per second.")
        score = 0
    
    pygame.display.update()
    
    frameCounter += 1
    sleep(0.01667)