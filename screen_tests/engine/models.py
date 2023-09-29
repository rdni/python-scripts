class PositionalObject(object):
    def __init__(self, position: tuple[float, float, float]):
        self.x, self.y, self.z = position
        self.homogenous_position = position + (1,)

class Colour(object):
    def __init__(self, r: int, g: int, b: int):
        self.r = r
        self.g = g
        self.b = b

    @staticmethod
    def from_hex(hex: str):
        return Colour(int(hex[0:2], 16), int(hex[2:4], 16), int(hex[4:6], 16))

    def __repr__(self):
        return "Colour(r=%s, g=%s, b=%s)" % (self.r, self.g, self.b)

class Triangle(PositionalObject):
    def __init__(self, vertices: list[tuple[float, float, float]], color: Colour):
        # Assuming the position of the triangle is the average of its vertices
        avg_position = tuple(sum(coords) / 3 for coords in zip(*vertices))
        super(Triangle, self).__init__(avg_position)
        self.vertices = vertices
        self.color = color

    def project(self, camera: "Camera"):
        projected_vertices = [camera.project(*vertex) for vertex in self.vertices]
        return projected_vertices

    def __repr__(self):
        return "Triangle(vertices=%s, color=%s)" % (self.vertices, self.color)

class Mesh(PositionalObject):
    def __init__(self, position: tuple[float, float, float], triangles: list[Triangle]):
        super(Mesh, self).__init__(position)
        self.triangles = triangles

    def project(self, camera: "Camera"):
        projected_triangles = [triangle.project(camera) for triangle in self.triangles]
        return projected_triangles