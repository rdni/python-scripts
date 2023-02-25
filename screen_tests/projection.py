"""Makes a projection of a cube on a screen using an edge table and a set of vertices and it is a wireframe."""
from pygame_widgets.slider import Slider
from pygame_widgets.textbox import TextBox
import pygame_widgets
import pygame
import time
import numpy

class State(object):
    """This contains the state of the program, as well as the rendering of the program."""
    def __init__(self, shapes):
        pygame.font.init()
        self.screen = pygame.display.set_mode((1000, 1000))
        self.screen.fill((0, 0, 0))
        self.screenCenter = [500, 500]
        
        self.shapes = shapes
         
        self.camera = Camera(self.shapes, self.screen)
        self.camera.draw()
        
        self.positionOutput = TextBox(self.screen, 50, 800, 250, 50, fontSize=30)
        
        self.xOutput = TextBox(self.screen, 675, 900, 90, 50, fontSize=30)
        self.xSlider = Slider(self.screen, 550, 900, 100, 40, min=-1000, max=1000, step=10, defaultValue=0)
        
        self.yOutput = TextBox(self.screen, 675, 950, 90, 50, fontSize=30)
        self.ySlider = Slider(self.screen, 550, 950, 100, 40, min=-1000, max=1000, step=10, defaultValue=0)
        
        self.zOutput = TextBox(self.screen, 425, 900, 90, 50, fontSize=30)
        self.zSlider = Slider(self.screen, 300, 900, 100, 40, min=200, max=2000, step=10, defaultValue=1000)
        
        self.phiOutput = TextBox(self.screen, 425, 950, 90, 50, fontSize=30)
        self.phiSlider = Slider(self.screen, 300, 950, 100, 40, min=0, max=360, step=1, defaultValue=0)
        
        self.thetaOutput = TextBox(self.screen, 175, 900, 90, 50, fontSize=30)
        self.thetaSlider = Slider(self.screen, 50, 900, 100, 40, min=1, max=10, step=1, defaultValue=0)
        
        self.xRotateOutput = TextBox(self.screen, 675, 800, 90, 50, fontSize=30)
        self.xRotateSlider = Slider(self.screen, 550, 800, 100, 40, min=0, max=360, step=1, defaultValue=0)
        
        self.positionOutput.setText(f"Position: {self.camera.position}")
        self.xOutput.setText(str(self.camera.position[0]))
        self.yOutput.setText(str(self.camera.position[1]))
        self.zOutput.setText(str(self.camera.position[2]))
        self.phiOutput.setText(str(self.camera.phi))
        self.thetaOutput.setText(str(self.camera.theta))
        self.xRotateOutput.setText(str(0))
        
        self.positionOutput.disable()
        self.xOutput.disable()
        self.yOutput.disable()
        self.zOutput.disable()
        self.phiOutput.disable()
        self.thetaOutput.disable()
        self.xRotateOutput.disable()

class Camera(object):
    def __init__(self, shapes, screen) -> None:
        self.screen = screen
        self.shapes = shapes
        self.focalLength = 250
        self.screenCenter = [500, 500]
        self.screenSize = [1000, 1000]
        self.position = [0, 1000, 2000]
        self.phi = 0 # Rotation around the y-axis
        self.theta = 0  # Rotation around the x-axis
    
    def draw(self):
        self.screen.fill((0, 0, 0))
        for shape in self.shapes:
            shape.cameraPosition = [self.position[0], self.position[1], self.position[2]]
            shape.cameraPhi = self.phi
            shape.cameraTheta = self.theta
            shape.focalLength = self.focalLength
            shape.screenCenter = self.screenCenter
            for edge in shape.edgeTable:
                if not (a:=shape.vertices[edge[0]].project(self)) == (b:=shape.vertices[edge[1]].project(self)):
                    if a[0] < 0 and b[0] < 0:
                        continue
                    elif a[0] > self.screenSize[0] and b[0] > self.screenSize[0]:
                        continue
                    elif a[1] < 0 and b[1] < 0:
                        continue
                    elif a[1] > self.screenSize[1] and b[1] > self.screenSize[1]:
                        continue
                    else:
                        if a[0] < 0:
                            a[0] = 0
                        elif a[0] > self.screenSize[0]:
                            a[0] = self.screenSize[0]
                        if a[1] < 0:
                            a[1] = 0
                        elif a[1] > self.screenSize[1]:
                            a[1] = self.screenSize[1]
                        if b[0] < 0:
                            b[0] = 0
                        elif b[0] > self.screenSize[0]:
                            b[0] = self.screenSize[0]
                        if b[1] < 0:
                            b[1] = 0
                        elif b[1] > self.screenSize[1]:
                            b[1] = self.screenSize[1]
                        try:
                            pygame.draw.line(self.screen, (255, 255, 255), a[0:2], b[0:2])
                        except Exception as e:
                            pass
                # else:
                #     print(f"Line between {a} and {b} is too small to draw.")

class Vertex(object):
    def __init__(self, x, y, z, shapePosition=[0, 0, 0, 1]):
        self.relativePosition = [x, y, z, 1]
        self.shapePosition = shapePosition
        self.originalPosition = [x, y, z, 1]
        self.cameraPosition = [0, 0, 0]
        self.cameraPhi = 0
        self.cameraTheta = 0
        self.focalLength = 1000
        self.zOffset = 0
        self.screenCenter = [500, 500]
        
    def project(self, camera):
        """Makes a projection of where it would be on a screen."""
        # Adjust relative position to real position
        self.position = numpy.add(self.relativePosition, self.shapePosition)
        
        # Step 1: Viewing transformation
        # Translate the world to the camera position
        T = numpy.array([
            [1, 0, 0, -camera.position[0]],
            [0, 1, 0, -camera.position[1]],
            [0, 0, 1, -camera.position[2]],
            [0, 0, 0, 1]
        ])
        
        # Rotate the world around the y-axis by phi
        R = numpy.array([
            [numpy.cos(camera.phi), 0, numpy.sin(camera.phi), 0],
            [0, 1, 0, 0],
            [-numpy.sin(camera.phi), 0, numpy.cos(camera.phi), 0],
            [0, 0, 0, 1]
        ])
        
        # Rotate the world around the x-axis by theta
        R = numpy.dot(numpy.array([
            [1, 0, 0, 0],
            [0, numpy.cos(camera.theta), -numpy.sin(camera.theta), 0],
            [0, numpy.sin(camera.theta), numpy.cos(camera.theta), 0],
            [0, 0, 0, 1]
        ]), R)
        
        # Combine the translation and rotation into one matrix
        V = numpy.dot(R, T)
        
        # Apply the viewing transformation
        position_camera = numpy.dot(V, self.position)
        # print(position_camera)
        
        # Step 2: Perspective transformation
        d = camera.focalLength  # focal length
        P = numpy.array([
            [d, 0, 0, 0],
            [0, d, 0, 0],
            [0, 0, 1, 0]
        ])
        # Apply the perspective transformation
        position_image = numpy.dot(P, position_camera)

        # Convert from homogeneous coordinates to Cartesian coordinates
        epsilon = 1e-6 # a small number
        x_projected = position_image[0] / (position_image[2] + epsilon)
        y_projected = position_image[1] / (position_image[2] + epsilon)

        return [round(x_projected + camera.screenCenter[0]), round(y_projected + camera.screenCenter[1]), self.position[2]]
        
    
    def xRotate(self, rotationMatrix):
        """Can use 2d rotation matrix, then add x back in later"""
        self.position[1], self.position[2] = numpy.matmul(rotationMatrix, [self.originalPosition[1], self.originalPosition[2]])
    
    def yRotate(self, rotationMatrix):
        """Can use 2d rotation matrix, then add y back in later"""
        self.position[0], self.position[2] = numpy.matmul(rotationMatrix, [self.originalPosition[0], self.originalPosition[2]])
        
    def zRotate(self, rotationMatrix):
        """Can use 2d rotation matrix, then add z back in later"""
        self.position[0], self.position[1] = numpy.matmul(rotationMatrix, [self.originalPosition[0], self.originalPosition[1]])
        
class Shape(object):
    def __init__(self, vertices, edgeTable):
        self.vertices = vertices
        self.edgeTable = edgeTable
        self.position = [0, 0, 0]

vertices = [
    Vertex(-100, -100, -100),
    Vertex(-100, -100, 100),
    Vertex(-100, 100, -100),
    Vertex(-100, 100, 100),
    Vertex(100, -100, -100),
    Vertex(100, -100, 100),
    Vertex(100, 100, -100),
    Vertex(100, 100, 100),
]

edgeTable = [
    [0, 1],
    [0, 2],
    [0, 4],
    [1, 3],
    [1, 5],
    [2, 3],
    [2, 6],
    [3, 7],
    [4, 5],
    [4, 6],
    [5, 7],
    [6, 7],
]

# yAxisLineVertices = [
#     Vertex(0, 0, 0),
#     Vertex(0, 1000, 0)
# ]

# yAxisLineEdgeTable = [
#     [0, 1]
# ]

state = State([
    Shape(vertices, edgeTable),
    # Shape(yAxisLineVertices, yAxisLineEdgeTable)
])
camera = state.camera
clock = pygame.time.Clock()

ticks = 0
prevXSliderVal = 0
prevYSliderVal = 0
prevZSliderVal = 0
prevPhiSliderVal = 0
prevThetaSliderVal = 0
prevXRotateSliderVal = 0
getTicksLastFrame = pygame.time.get_ticks()
while True:
    start = time.time()
    t = pygame.time.get_ticks()
# deltaTime in seconds.
    deltaTime = (t - getTicksLastFrame) / 1000.0
    getTicksLastFrame = t
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        # elif event.type == pygame.KEYDOWN:
        #     match event.key:
        #         case pygame.K_w:
        #             camera.position[1] -= 10
        #         case pygame.K_s:
        #             camera.position[1] += 10
        #         case pygame.K_a:
        #             camera.position[0] -= 10
        #         case pygame.K_d:
        #             camera.position[0] += 10
        #         case pygame.K_q:
        #             camera.position[2] -= 10
        #         case pygame.K_e:
        #             camera.position[2] += 10
        #         case pygame.K_UP:
        #             camera.theta -= 0.1
        #         case pygame.K_DOWN:
        #             camera.theta += 0.1
        #         case pygame.K_LEFT:
        #             camera.phi += 0.1
        #         case pygame.K_RIGHT:
        #             camera.phi -= 0.1
        #         case pygame.K_SPACE:
        #             camera.position = [0, 1000, 2000]
                    
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        camera.position[1] -= 1000 * deltaTime
    if keys[pygame.K_s]:
        camera.position[1] += 1000 * deltaTime
    if keys[pygame.K_a]:
        camera.position[0] += 1000 * deltaTime
    if keys[pygame.K_d]:
        camera.position[0] -= 1000 * deltaTime
    if keys[pygame.K_q]:
        camera.position[2] -= 1000 * deltaTime
    if keys[pygame.K_e]:
        camera.position[2] += 1000 * deltaTime
    if keys[pygame.K_UP]:
        camera.theta -= 1 * deltaTime
    if keys[pygame.K_DOWN]:
        camera.theta += 1 * deltaTime
    if keys[pygame.K_LEFT]:
        camera.phi += 1 * deltaTime
    if keys[pygame.K_RIGHT]:
        camera.phi -= 1 * deltaTime
    if keys[pygame.K_SPACE]:
        camera.position = [0, 1000, 2000]
        
    if prevXSliderVal != state.xSlider.getValue():
        camera.position[0] = state.xSlider.getValue()
        prevXSliderVal = state.xSlider.getValue()
        state.xOutput.setText(f"X: {str(camera.position[0])}")
        for shape in state.shapes:
            for vertex in shape.vertices:
                vertex.cameraPosition[0] = camera.position[0]
        
    if prevYSliderVal != state.ySlider.getValue():
        camera.position[1] = state.ySlider.getValue()
        prevYSliderVal = state.ySlider.getValue()
        state.yOutput.setText(f"Y: {str(camera.position[1])}")
        for shape in state.shapes:
            for vertex in shape.vertices:
                vertex.cameraPosition[1] = camera.position[1]
    
    if prevZSliderVal != state.zSlider.getValue():
        camera.position[2] = state.zSlider.getValue()
        prevZSliderVal = state.zSlider.getValue()
        state.zOutput.setText(f"Z: {str(camera.position[2])}")
        for shape in state.shapes:
            for vertex in shape.vertices:
                vertex.cameraPosition[2] = camera.position[2]
    
    if prevPhiSliderVal != state.phiSlider.getValue():
        camera.phi = state.phiSlider.getValue()
        prevPhiSliderVal = state.phiSlider.getValue()
        state.phiOutput.setText(f"P: {str(camera.phi)}")
        for shape in state.shapes:
            for vertex in shape.vertices:
                vertex.cameraPhi = camera.phi
    
    if prevThetaSliderVal != state.thetaSlider.getValue():
        camera.theta = state.thetaSlider.getValue()
        prevThetaSliderVal = state.thetaSlider.getValue()
        state.thetaOutput.setText(f"T: {str(camera.theta)}")
        for shape in state.shapes:
            for vertex in shape.vertices:
                vertex.cameraTheta = camera.theta
    
    if prevXRotateSliderVal != state.xRotateSlider.getValue():
        xRotate = state.xRotateSlider.getValue()
        prevXRotateSliderVal = state.xRotateSlider.getValue()
        state.xRotateOutput.setText(f"XR: {str(xRotate)}")
        for shape in state.shapes:
            for vertex in shape.vertices:
                vertex.xRotate(numpy.array([
                    [numpy.cos(xRotate), -numpy.sin(xRotate)],
                    [numpy.sin(xRotate), numpy.cos(xRotate)]
                ]))
    
    roundedPosition = [round(camera.position[0]), round(camera.position[1]), round(camera.position[2])]
    state.positionOutput.setText(f"Position: {roundedPosition}")
    
    camera.draw()
    
    pygame_widgets.update(events)
    pygame.display.update()
    
    print(f"next frame: {ticks} took {(time.time() - start) * 1000} ms.")
    ticks += 1
    clock.tick(30)