import pygame
from pygame.locals import *
from OpenGL.GLU import *
from OpenGL.GL import *
import numpy as np

# Заданными вручную координаты вершины куба
vertices = [
    (-1, -1, -1),
    (-1, -1, 1),
    (-1, 1, -1),
    (-1, 1, 1),
    (1, -1, -1),
    (1, -1, 1),
    (1, 1, -1),
    (1, 1, 1)
]

# Задаём рёбра куба
edges = [
    (0, 1), (1, 3), (3, 2), (2, 0),
    (4, 5), (5, 7), (7, 6), (6, 4),
    (0, 4), (1, 5), (2, 6), (3, 7)
]

# используем Pygame
pygame.init()
display = (800, 600)
pygame.display.set_mode(display, DOUBLEBUF | OPENGL)

# Настравиваем перспективу
gluPerspective(45, (display[0] / display[1]), 0.1, 50.0)
glTranslatef(0, 0, -5)

# Инициализируем матрицу вращения и вектор вращения
rotation_matrix = np.identity(4)
rotation_vector = np.array([1, 1, 1], dtype=float)
rotation_vector /= np.linalg.norm(rotation_vector)  # Normalize the initial rotation vector

# Задаём функцию для поворота
def set_rotation_matrix(rotation_vector):
    global rotation_matrix
    angle = np.linalg.norm(rotation_vector)
    if angle != 0:
        axis = rotation_vector / angle
        c = np.cos(angle)
        s = np.sin(angle)
        t = 1 - c
        x, y, z = axis
        rotation_matrix = np.array([
            [t*x*x+c, t*x*y-s*z, t*x*z+s*y, 0],
            [t*x*y+s*z, t*y*y+c, t*y*z-s*x, 0],
            [t*x*z-s*y, t*y*z+s*x, t*z*z+c, 0],
            [0, 0, 0, 1]
        ])
    else:
        rotation_matrix = np.identity(4)

# Скорость и направление вращения
rotation_speed = 5
rotation_direction = np.array([0, 0, 10], dtype=float)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    # Непрерывное вращение
    rotation_vector += rotation_speed * rotation_direction
    set_rotation_matrix(rotation_vector)  #glMultMatrixf(rotation_matrix)
    glMultMatrixf(rotation_matrix)

    # Рисуем оси и сам куб
    glBegin(GL_LINES)
    glColor3fv((1, 0, 0))  # X красный
    glVertex3fv((0, 0, 0))
    glVertex3fv((2, 0, 0))

    glColor3fv((0, 1, 0))  # Y зелёный
    glVertex3fv((0, 0, 0))
    glVertex3fv((0, 2, 0))

    glColor3fv((0, 0, 1))  # Z синий
    glVertex3fv((0, 0, 0))
    glVertex3fv((0, 0, 2))

    glColor3fv((1, 1, 1))
    for edge in edges:
        for vertex in edge:
            glVertex3fv(vertices[vertex])

    glEnd()
    pygame.display.flip()
    pygame.time.wait(150)
