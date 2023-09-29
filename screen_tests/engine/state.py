import pygame
from camera import Camera
from models import Mesh, Triangle, Colour

class RendererState:
    def __init__(self, screen):
        # Initialize the camera with default position, rotation, focal length, and angles
        self.camera = Camera((0, 0, 100), (0, 0, 0), 120, 0.0, 0.0)
        self.screen = screen

        # Sample Mesh and Triangle for testing purposes
        cube = (
                [
                Triangle([(0, 0, 0), (0, 1, 0), (1, 1, 0)], Colour.from_hex("FF0000")),
                Triangle([(0, 0, 0), (1, 1, 0), (1, 0, 0)], Colour.from_hex("FF0000")),
                Triangle([(0, 0, 0), (0, 0, 1), (0, 1, 1)], Colour.from_hex("00FF00")),
                Triangle([(0, 0, 0), (0, 1, 1), (0, 1, 0)], Colour.from_hex("00FF00")),
                Triangle([(0, 0, 0), (1, 0, 0), (1, 0, 1)], Colour.from_hex("0000FF")),
                Triangle([(0, 0, 0), (1, 0, 1), (0, 0, 1)], Colour.from_hex("0000FF")),
                Triangle([(1, 1, 1), (1, 0, 1), (0, 0, 1)], Colour.from_hex("FFFFFF")),
                Triangle([(1, 1, 1), (0, 0, 1), (0, 1, 1)], Colour.from_hex("FFFFFF")),
                Triangle([(1, 1, 1), (0, 1, 1), (0, 1, 0)], Colour.from_hex("FFFFFF")),
                Triangle([(1, 1, 1), (0, 1, 0), (1, 1, 0)], Colour.from_hex("FFFFFF")),
                Triangle([(1, 1, 1), (1, 1, 0), (1, 0, 0)], Colour.from_hex("FFFFFF")),
                Triangle([(1, 1, 1), (1, 0, 0), (1, 0, 1)], Colour.from_hex("FFFFFF"))
            ],
        )

        self.meshes = [
            Mesh((0, 0, 0), cube[0]),
        ]

    def update_camera(self, position=None, rotation=None, phi=None, theta=None):
        if position:
            self.camera.x, self.camera.y, self.camera.z = position
        if rotation:
            self.camera.rotation = rotation
        if phi is not None:
            self.camera.phi = phi
        if theta is not None:
            self.camera.theta = theta

    def draw_scene(self):
        # Clear the screen with white color
        self.screen.fill((255, 255, 255))

        # Project and draw the triangles using Pygame
        for mesh in self.meshes:
            projected_triangles = mesh.project(self.camera)
            for triangle in projected_triangles:
                pygame.draw.polygon(self.screen, (255, 0, 0), triangle)

        # Refresh the display
        pygame.display.flip()