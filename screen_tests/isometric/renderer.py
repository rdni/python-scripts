from config import (
    MISSING,
    MAP_PATH,
    GRASS_PATH,
    WALL_PATH,
    TILEHEIGHT_HALF,
    TILEWIDTH_HALF,
)
from utils import *
from pygame import (
    image,
    Surface,
    QUIT
)

class Renderer(object):
    def __init__(
        self,
        display: Surface,
        map: list[list[int]] | object = MISSING,
        wall: Surface | object = MISSING,
        grass: Surface| object = MISSING,
        camera_position: list[int, int] = [0, 0],
        camera_distance: int = 200,
        camera_angle: int = 0
    ) -> None:
        self.display = display
        
        self.map = map if not map is MISSING else get_map(resource_path(MAP_PATH))
        self.map_center = (len(self.map) * TILEWIDTH_HALF / 2, len(self.map[0]) * TILEHEIGHT_HALF / 2)
        
        self.wall = wall if not wall is MISSING else image.load(resource_path(WALL_PATH)).convert_alpha()
        self.grass = grass if not grass is MISSING else image.load(resource_path(GRASS_PATH)).convert_alpha()
        
        self.camera_position = camera_position
        self.camera_distance = camera_distance
        self.camera_angle = camera_angle
        
    def render(self) -> None:
        if self.camera_angle == 180:
            rendered_map = reverse_rows(self.map)
        elif self.camera_angle == 90:  # to the right
            rendered_map = transpose(self.map)
            rendered_map = [reverse_tiles(row) for row in rendered_map]
        elif self.camera_angle == 270:  # to the left
            rendered_map = transpose(self.map)
            rendered_map = reverse_rows(rendered_map)
        else:
            rendered_map = self.map

        self.display.fill((0, 0, 0))
        for row_nb, row in enumerate(rendered_map):
            for col_nb, tile in enumerate(row):
                if tile == 1:
                    tileImage = self.wall
                else:
                    tileImage = self.grass

                cart_x = row_nb * TILEWIDTH_HALF
                cart_y = col_nb * TILEHEIGHT_HALF
                self.display.blit(tileImage, cart_to_centered_iso((cart_x, cart_y), self.camera_position))
        pygame.display.flip()
        
    def handle_input(self, deltatime: float) -> None:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    self.toggle_tile()
                elif event.key == pygame.K_a:
                    self.camera_angle = (self.camera_angle + 90) % 360
                elif event.key == pygame.K_d:
                    self.camera_angle = (self.camera_angle - 90) % 360 if self.camera_angle > 0 else 270
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.camera_position[0] += 100 * deltatime
        elif keys[pygame.K_RIGHT]:
            self.camera_position[0] -= 100 * deltatime
        elif keys[pygame.K_UP]:
            self.camera_position[1] += 100 * deltatime
        elif keys[pygame.K_DOWN]:
            self.camera_position[1] -= 100 * deltatime
        self.render()
                    
    def toggle_tile(self) -> None:
        """Edit the map"""
        mouse = pygame.mouse.get_pos()
        
        if self.camera_angle == 180:
            rendered_map = reverse_rows(self.map)
            rendered_map = [reverse_tiles(row) for row in rendered_map]
        elif self.camera_angle == 90:  # to the right
            rendered_map = transpose(self.map)
            rendered_map = [reverse_tiles(row) for row in rendered_map]
        elif self.camera_angle == 270:  # to the left
            rendered_map = transpose(self.map)
            rendered_map = reverse_rows(rendered_map)
        else:
            rendered_map = self.map
                    
        print(get_map_differences(self.map, rendered_map))
            
        for row_nb, row in enumerate(self.map):
            for col_nb, tile in enumerate(row):
                tile_pos = cart_to_centered_iso((row_nb * TILEWIDTH_HALF, col_nb * TILEHEIGHT_HALF), self.camera_position)
                tile_image = self.wall if tile == 1 else self.grass
                
                if is_point_within_tile(mouse, tile_pos, tile_image):
                    rendered_map[row_nb][col_nb] = 0 if tile == 1 else 1
                    if self.camera_angle == 180:
                        rendered_map = [reverse_tiles(row) for row in rendered_map]
                        self.map = reverse_rows(rendered_map)
                    elif self.camera_angle == 90:  # to the right
                        rendered_map = [reverse_tiles(row) for row in rendered_map]
                        self.map = transpose(rendered_map)
                    elif self.camera_angle == 270:  # to the left
                        rendered_map = reverse_rows(rendered_map)
                        self.map = transpose(rendered_map)
                    else:
                        self.map = rendered_map
                    return