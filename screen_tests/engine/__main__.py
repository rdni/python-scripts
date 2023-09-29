import pygame
from state import RendererState
import numpy as np

def main():
    # Initialize pygame
    pygame.init()

    # Create a window
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("3D Renderer")

    # Initialize the renderer state
    state = RendererState(screen)
    
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        keys = pygame.key.get_pressed()
        
        # Camera movement
        if keys[pygame.K_w]:
            state.update_camera(position=(state.camera.x, state.camera.y + 1, state.camera.z))
        if keys[pygame.K_s]:
            state.update_camera(position=(state.camera.x, state.camera.y - 1, state.camera.z))
        if keys[pygame.K_a]:
            state.update_camera(position=(state.camera.x - 1, state.camera.y, state.camera.z))
        if keys[pygame.K_d]:
            state.update_camera(position=(state.camera.x + 1, state.camera.y, state.camera.z))
        if keys[pygame.K_q]:
            state.update_camera(position=(state.camera.x, state.camera.y, state.camera.z - 1))
        if keys[pygame.K_e]:
            state.update_camera(position=(state.camera.x, state.camera.y, state.camera.z + 1))
        if keys[pygame.K_UP]:
            state.update_camera(theta=state.camera.theta + 0.1)
        if keys[pygame.K_DOWN]:
            state.update_camera(theta=state.camera.theta - 0.1)
        if keys[pygame.K_LEFT]:
            state.update_camera(phi=state.camera.phi + 0.1)
        if keys[pygame.K_RIGHT]:
            state.update_camera(phi=state.camera.phi - 0.1)
        
        state.draw_scene()

        # Limit the frame rate to 30 FPS
        pygame.time.Clock().tick(30)

    pygame.quit()

if __name__ == "__main__":
    main()