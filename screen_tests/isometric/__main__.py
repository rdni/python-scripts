import pygame
from pygame.locals import *
import sys
import json
import os
import math

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)

pygame.init()

display = pygame.display.set_mode((640, 480), DOUBLEBUF)
pygame.display.set_caption('Map Rendering Demo with Camera Movement')
clock = pygame.time.Clock()


with open(resource_path("assets\\map.json"), "r") as f:
    map_data = json.load(f)

wall = pygame.image.load(resource_path('assets\\wall.png')).convert_alpha()
grass = pygame.image.load(resource_path('assets\\grass.png')).convert_alpha()

TILEWIDTH = 64
TILEHEIGHT = 64
TILEHEIGHT_HALF = TILEHEIGHT / 2
TILEWIDTH_HALF = TILEWIDTH / 2

camera_x, camera_y = 0, 0

center_of_map = (len(map_data) * TILEWIDTH_HALF / 2, len(map_data[0]) * TILEHEIGHT_HALF / 2)
camera_distance = 200
camera_angle = 0

def is_point_within_tile(point_x, point_y, tile_x, tile_y, tile_image):
    """Check if a point is within the boundaries of a tile."""
    tile_rect: pygame.Rect = tile_image.get_rect(topleft=(tile_x, tile_y))
    return tile_rect.collidepoint(point_x, point_y)


def centered_iso_to_cart(centered_x, centered_y):
    iso_x = centered_x - display.get_rect().centerx
    iso_y = centered_y - display.get_rect().centery / 2
    cart_x = (2 * iso_y + iso_x) / 2 - camera_x
    cart_y = (2 * iso_y - iso_x) / 2 - camera_y
    return cart_x, cart_y

def cart_to_centered_iso(cart_x, cart_y):
    iso_x = (cart_x - cart_y)
    iso_y = (cart_x + cart_y) / 2
    
    # Adjust for camera rotation
    rotated_x = iso_x * math.cos(camera_angle) - iso_y * math.sin(camera_angle)
    rotated_y = iso_x * math.sin(camera_angle) + iso_y * math.cos(camera_angle)
    
    # Apply the camera's distance from the center
    rotated_x += camera_distance * math.sin(camera_angle)
    rotated_y -= camera_distance * math.cos(camera_angle)
    
    centered_x = display.get_rect().centerx + rotated_x + camera_x
    centered_y = display.get_rect().centery / 2 + rotated_y + camera_y
    return centered_x, centered_y

def render():
    for row_nb, row in enumerate(map_data):
        for col_nb, tile in enumerate(row):
            if tile == 1:
                tileImage = wall
            else:
                tileImage = grass

            cart_x = row_nb * TILEWIDTH_HALF
            cart_y = col_nb * TILEHEIGHT_HALF
            display.blit(tileImage, cart_to_centered_iso(cart_x, cart_y))
            
            
def toggle_tile():
    """Edit the map"""
    mouse_x, mouse_y = pygame.mouse.get_pos()
    
    for row_nb, row in enumerate(map_data):
        for col_nb, tile in enumerate(row):
            tile_x, tile_y = cart_to_centered_iso(row_nb * TILEWIDTH_HALF, col_nb * TILEHEIGHT_HALF)
            
            # Adjust for rotations
            # if direction == 1:  # 90-degree rotation
            #     tile_x, tile_y = cart_to_centered_iso(col_nb * TILEWIDTH_HALF, (len(row) - 1 - row_nb) * TILEHEIGHT_HALF)
            # elif direction == 2:  # 180-degree rotation
            #     tile_x, tile_y = cart_to_centered_iso((len(map_data) - 1 - row_nb) * TILEWIDTH_HALF, (len(row) - 1 - col_nb) * TILEHEIGHT_HALF)
            # elif direction == 3:  # 270-degree rotation
            #     tile_x, tile_y = cart_to_centered_iso((len(map_data) - 1 - col_nb) * TILEWIDTH_HALF, row_nb * TILEHEIGHT_HALF)
            
            tile_image = wall if tile == 1 else grass
            
            if is_point_within_tile(mouse_x, mouse_y, tile_x, tile_y, tile_image):
                map_data[row_nb][col_nb] = 1 - map_data[row_nb][col_nb]
                return

#wtf why is this here
camera_x = center_of_map[0] + camera_distance * math.sin(camera_angle)
camera_y = center_of_map[1] - camera_distance * math.cos(camera_angle)
while True:
    deltatime = clock.tick(60) / 1000.0
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == KEYUP:
            if event.key == K_SPACE:
                toggle_tile()


    pressed_keys = pygame.key.get_pressed()
    if pressed_keys[K_ESCAPE]:
        pygame.quit()
        sys.exit()
    if pressed_keys[K_RIGHT]:
        camera_x -= TILEWIDTH_HALF * deltatime * 5
    if pressed_keys[K_LEFT]:
        camera_x += TILEWIDTH_HALF * deltatime * 5
    if pressed_keys[K_DOWN]:
        camera_y -= TILEHEIGHT_HALF * deltatime * 5
    if pressed_keys[K_UP]:
        camera_y += TILEHEIGHT_HALF * deltatime * 5
    if pressed_keys[K_a]:
        camera_angle += math.pi * deltatime
    if pressed_keys[K_d]:
        camera_angle -= math.pi * deltatime

    display.fill((0, 0, 0))
    render()

    pygame.display.flip()

    print(f"FPS: {clock.get_fps()}")