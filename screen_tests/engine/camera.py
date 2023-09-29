import numpy as np
from models import PositionalObject

class Camera(PositionalObject):
    def __init__(
        self, 
        position: tuple[float, float, float], 
        rotation: tuple[float, float, float],
        focal_length: float,
        phi: float = 0.0,
        theta: float = 0.0
    ):
        super(Camera, self).__init__(position)
        self.rotation = rotation
        self.focal_length = focal_length
        self.phi = phi
        self.theta = theta
        
    def project(self, x: float, y: float, z: float) -> tuple[float, float]:
        # Apply rotations using phi and theta
        # Rotation around the y-axis (azimuthal)
        x_rot_y = x * np.cos(self.phi) - z * np.sin(self.phi)
        z_rot_y = x * np.sin(self.phi) + z * np.cos(self.phi)
        
        # Rotation around the x-axis (polar)
        y_rot_x = y * np.cos(self.theta) - z_rot_y * np.sin(self.theta)
        z_rot_x = y * np.sin(self.theta) + z_rot_y * np.cos(self.theta)
        
        if x_rot_y == 0:
            x_rot_y = 1.000000000
        if y_rot_x == 0:
            y_rot_x = 1.000000000
        if z_rot_x == 0:
            z_rot_x = 1.000000000
        
        # Perspective projection
        print(x_rot_y, y_rot_x, z_rot_x)
        x_proj = (x_rot_y * self.focal_length) / z_rot_x
        y_proj = (y_rot_x * self.focal_length) / z_rot_x
        return (x_proj, y_proj)

    def __repr__(self):
        return "Camera(x=%s, y=%s, z=%s, rotation=%s, phi=%s, theta=%s)" % (self.x, self.y, self.z, self.rotation, self.phi, self.theta)