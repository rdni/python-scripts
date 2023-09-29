from functools import lru_cache
import pygame
import numpy as np
import math as m
import time
from pygame_widgets.textbox import TextBox
import pygame_widgets as pw

# Constants
WALL_COLOR = (161, 246, 255)
WIN_DOOR_COLOR = (255, 255, 0)
FLOOR_COLOR = (150, 150, 150)
BACKGROUND_COLOR = (186, 84, 84)
TILE_SIZE = 590
SPEED = 10
TURN_SPEED = np.radians(100)
FOV = np.radians(80)  # Field of View
MAX_DISTANCE = 20

# Sample map (0 = empty, 1 = wall)
MAP = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
]

class Camera:
    def __init__(self, x, y, angle):
        self.x = x
        self.y = y
        self.angle = angle

    def move_forward(self, deltaTime):
        new_x = (self.x + SPEED * np.cos(self.angle) * deltaTime)
        new_y = (self.y + SPEED * np.sin(self.angle) * deltaTime)
        if 0 <= new_x < len(MAP[0]) and 0 <= new_y < len(MAP) and MAP[int(new_y)][int(new_x)] == 0:
            self.x = new_x
            self.y = new_y

    def move_backward(self, deltaTime):
        new_x = (self.x - SPEED * np.cos(self.angle) * deltaTime)
        new_y = (self.y - SPEED * np.sin(self.angle) * deltaTime)
        if 0 <= int(new_x) < len(MAP[0]) and 0 <= int(new_y) < len(MAP) and MAP[int(new_y)][int(new_x)] == 0:
            self.x = new_x
            self.y = new_y

    def turn_left(self, deltaTime):
        self.angle -= TURN_SPEED * deltaTime

    def turn_right(self, deltaTime):
        self.angle += TURN_SPEED * deltaTime

@lru_cache(maxsize=None)
def cast_ray(x, y, angle):
    distance = 0
    while distance < MAX_DISTANCE:
        x += np.cos(angle)
        y += np.sin(angle)
        distance += 1

        # Boundary checks
        if 0 <= int(y) < len(MAP) and 0 <= int(x) < len(MAP[0]):
            # Check if the ray has hit a wall
            if MAP[int(y)][int(x)] != 0:
                return distance, MAP[int(y)][int(x)]
        else:
            return MAX_DISTANCE, 1

    return MAX_DISTANCE, 1

def main():
    pygame.init()
    pygame.font.init()
    display_info = pygame.display.Info()
    screen_width = display_info.current_w
    screen_height = display_info.current_h
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("Raycasting Renderer")
    # wall_texture = pygame.image.load(os.path.join("assets", "wall.jpg"))
    clock = pygame.time.Clock()
    
    fpsOutput = TextBox(
        screen, 0, 0, 100, 100, fontSize=20, borderColour=(255, 255, 255), textColour=(255, 255, 255), radius=0, text="FPS: 0"
    )

    camera = Camera(2.5, 2.5, 0)  # Starting in the center of the map
    
    getTicksLastFrame = pygame.time.get_ticks()
    
    running = True
    while running:
        t = pygame.time.get_ticks()
        deltaTime = (t - getTicksLastFrame) / 1000.0
        getTicksLastFrame = t
        
        screen.fill(BACKGROUND_COLOR)
        
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                running = False

        start = time.time()
        keys = pygame.key.get_pressed()
        if keys[pygame.K_ESCAPE]:
            running = False
        if keys[pygame.K_UP] or keys[pygame.K_w]:
            camera.move_forward(deltaTime)
        if keys[pygame.K_DOWN] or keys[pygame.K_s]:
            camera.move_backward(deltaTime)
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            camera.turn_left(deltaTime)
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            camera.turn_right(deltaTime)
        lastKeyRegistering = time.time() - start

        start = time.time()
        totalDrawTime = 0
        # Raycasting and drawing
        for x in range(screen_width):
            # Calculate the angle of the ray for this slice
            ray_angle = camera.angle + (x - screen_width // 2) / (screen_width // 2) * FOV / 2

            # Cast the ray and get the distance to the wall
            distance = cast_ray(camera.x, camera.y, ray_angle)

            # Calculate the height of the slice based on the distance
            slice_height = screen_height / distance[0]

            start = time.time()
            # Draw the floor below the slice
            pygame.draw.rect(screen, FLOOR_COLOR, (x, screen_height // 2 + slice_height // 2, 1, screen_height - (screen_height // 2 + slice_height // 2)))
            
            """ # Calculate the texture X coordinate (based on where the ray hits the wall)
            texture_x = int((x / screen_width) * wall_texture.get_width())
            
            # Draw the textured slice
            texture_step = wall_texture.get_height() / slice_height
            texture_pos = 0
        
            for y in range(int(screen_height // 2 - slice_height // 2), int(screen_height // 2 + slice_height // 2)):
                texture_y = int(texture_pos) % wall_texture.get_height()
                screen.set_at((x, y), wall_texture.get_at((texture_x, texture_y)))
                texture_pos += texture_step"""
            
            # Draw the slice
            match distance[1]:
                case 0:
                    pass
                case 1:
                    pygame.draw.rect(screen, WALL_COLOR, (x, screen_height // 2 - slice_height // 2, 1, slice_height))
                case 2:
                    pygame.draw.rect(screen, WIN_DOOR_COLOR, (x, screen_height // 2 - slice_height // 2, 1, slice_height))
            totalDrawTime += time.time() - start
        lastDrawTime = totalDrawTime
        lastRaycasting = time.time() - start
        
        fpsOutput.setText("FPS: %s" % round(1 / (deltaTime + 1e-9), 2))

        pw.update(events)
        pygame.display.flip()
        
    print("Last key registering: %s" % lastKeyRegistering)
    print("Last raycasting: %s" % lastRaycasting)
    print("Last drawing: %s" % lastDrawTime)
    
    pygame.quit()

if __name__ == "__main__":
    main()