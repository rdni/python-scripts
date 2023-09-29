from config import (
    MAP_PATH,
    GRASS_PATH,
    WALL_PATH,
    SCREENSIZE,
)
from utils import *
from renderer import Renderer
from pygame import DOUBLEBUF

if __name__ == "__main__":
    pygame.init()

    display = pygame.display.set_mode(SCREENSIZE, DOUBLEBUF)
    pygame.display.set_caption('Map Rendering Test')
    clock = pygame.time.Clock()


    with open(MAP_PATH, "r") as f:
        map_data = json.load(f)

    wall = pygame.image.load(WALL_PATH).convert_alpha()
    grass = pygame.image.load(GRASS_PATH).convert_alpha()

    renderer = Renderer(display, map_data, wall, grass)

    while True:
        deltatime = clock.tick(60) / 1000
        renderer.handle_input(deltatime)