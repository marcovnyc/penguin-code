import math
import time
import os

# Cube vertices in 3D space
vertices = [
    [-1, -1, -1],
    [-1, -1,  1],
    [-1,  1, -1],
    [-1,  1,  1],
    [ 1, -1, -1],
    [ 1, -1,  1],
    [ 1,  1, -1],
    [ 1,  1,  1]
]

# Edges of the cube defined by the indices of the vertices
edges = [
    (0, 1), (0, 2), (1, 3), (2, 3),
    (4, 5), (4, 6), (5, 7), (6, 7),
    (0, 4), (1, 5), (2, 6), (3, 7)
]

# Rotate a point around the Y axis
def rotateY(point, angle):
    x, y, z = point
    cosA = math.cos(angle)
    sinA = math.sin(angle)
    return [cosA * x + sinA * z, y, -sinA * x + cosA * z]

# Project a 3D point to 2D
def project(point, width, height, fov, distance):
    x, y, z = point
    factor = fov / (z + distance)
    x = x * factor + width / 2
    y = -y * factor + height / 2
    return [int(x), int(y)]

# Clear terminal
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

# Draw the cube in terminal
def draw_cube(angle):
    projected_points = []
    width, height = os.get_terminal_size()

    for vertex in vertices:
        # Rotate around Y axis
        rotated = rotateY(vertex, angle)
        # Project to 2D
        projected = project(rotated, width, height, 400, 5)
        projected_points.append(projected)

    # Clear the terminal
    clear()

    for edge in edges:
        x1, y1 = projected_points[edge[0]]
        x2, y2 = projected_points[edge[1]]
        print(f"\x1b[{y1};{x1}H#")
        print(f"\x1b[{y2};{x2}H#")

angle = 0
try:
    while True:
        draw_cube(angle)
        time.sleep(0.03)
        angle += 0.02
except KeyboardInterrupt:
    clear()
    pass
