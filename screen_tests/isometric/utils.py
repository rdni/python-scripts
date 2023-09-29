import os
import sys
import json
import pygame

from config import (
    SCREENSIZE_CENTER
)

def resource_path(relative_path: str) -> str:
    """ Get absolute path to resource, works for dev and for PyInstaller """
    base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)

def get_map(path: str) -> list[list[int]]:
    with open(path, "r") as f:
        map_data = json.load(f)
    return map_data

def is_point_within_tile(
    point: list[int, int],
    tile: list[int, int],
    tile_image: pygame.Surface
) -> bool:
    """Check if a point is within the boundaries of a tile."""
    tile_rect= tile_image.get_rect(topleft=tile)
    return tile_rect.collidepoint(point)

def cart_to_centered_iso(
    cart: list[int, int],
    camera: list[int, int],
) -> list[int, int]:
    # Convert from cartesian to isometric
    iso_x = (cart[0] - cart[1])
    iso_y = (cart[0] + cart[1]) / 2

    # Adjust based on the camera's angle
    # if camera_angle == 180:
    #     max_row = len(map_data) - 1
    #     max_col = len(map_data[0]) - 1
    #     iso_x = (max_row - cart[0] - cart[1])
    #     iso_y = (max_row - cart[0] + cart[1]) / 2
    # elif camera_angle == 90:  # to the right
    #     iso_x, iso_y = iso_y, -iso_x
    # elif camera_angle == 270:  # to the left
    #     iso_x, iso_y = -iso_y, iso_x

    centered_x = SCREENSIZE_CENTER[0] / 2 + iso_x + camera[0]
    centered_y = SCREENSIZE_CENTER[1] / 4 + iso_y + camera[1]

    return [centered_x, centered_y]

def centered_iso_to_cart(
    centered: list[int, int],
    camera: list[int, int],
) -> list[int, int]:
    # Adjust for screen center and camera offset
    iso_x = centered[0] - SCREENSIZE_CENTER[0] / 2 - camera[0]
    iso_y = centered[1] - SCREENSIZE_CENTER[1] / 4 - camera[1]

    # Convert from isometric to cartesian
    cart_x = (2 * iso_y + iso_x) / 2
    cart_y = (2 * iso_y - iso_x) / 2

    # Adjust based on the camera's angle
    # if camera_angle == 180:
        # max_row = len(map_data) - 1
        # max_col = len(map_data[0]) - 1
        # cart_x = max_row - cart_x
        # cart_y = max_col - cart_y
    # elif camera_angle == 90:  # rotated to the right
        # cart_x, cart_y = -cart_y, cart_x
    # elif camera_angle == 270:  # rotated to the left
        # cart_x, cart_y = cart_y, -cart_x
    
    print(cart_x, cart_y)
    return [cart_x, cart_y]

def reverse_rows(map_data: list[list[int]]) -> list[list[int]]:
    """Reverse the rows of the map."""
    return map_data[::-1]

def reverse_tiles(row: list[int]) -> list[int]:
    """Reverse the tiles in a row."""
    return row[::-1]

def transpose(map_data: list[list[int]]) -> list[list[int]]:
    """Transpose the map (swap rows with columns)."""
    return [list(x) for x in zip(*map_data)]

def get_map_differences(
    old_map: list[list[int]],
    new_map: list[list[int]]
) -> list[list[int]]:
    """Get the differences between two maps."""
    differences = []
    for row_nb, row in enumerate(new_map):
        for col_nb, tile in enumerate(row):
            if tile != old_map[row_nb][col_nb]:
                differences.append((row_nb, col_nb))
    return differences