import cmath
import math
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.lines import Line2D

# Рисуем оси
plt.xlabel("x")
plt.ylabel("y")
plt.grid()

plt.show()

# Задаём координаты точек
def triangle(abc):
    x0 = 4  # А
    y0 = 2

    x1 = 6  # B
    y1 = 2

    x2 = 6  # C
    y2 = 6

    x3 = x0
    y3 = y0

    # Задаём точку и коэффициент
    print('Введите точку (A, B или C): ')
    point = str(input())
    print('Введите угол: ')
    alpha = int(input())

    # Задаём матрицу
    q1 = np.array([[x0, y0, 1],
          [x1, y1, 1],
          [x2, y2, 1]])


    # Какая точка выбрана
    if point == 'A':
        m = -x0
        n = -y0
    else:
        if point == 'B':
            m = -x1
            n = -y1
        else:
                m = -x2
                n = -y2

    # Перенос в начало координат
    q2 = np.array([[1, 0, 0],
          [0, 1, 0],
          [m, n, 1]])

    total = q1.dot(q2)

    # Поворот
    q3 = np.array([[math.cos(math.radians(alpha)), math.sin(math.radians(alpha)), 0],
          [-math.sin(math.radians(alpha)), math.cos(math.radians(alpha)), 0],
          [0, 0, 1]])

    total2 = total.dot(q3)

    if point == 'A':
        m = x0
        n = y0
    else:
        if point == 'B':
            m = x1
            n = y1
        else:
            m = x2
            n = y2

    # Возврат в исходное положение
    q4 = np.array([[1, 0, 0],
          [0, 1, 0],
          [m, n, 1]])

    total3 = total2.dot(q4)

    # Задаём наш новый треугольник
    xx0 = total3[0]
    xxx0 = xx0[0]
    xx1 = total3[1]
    xxx1 = xx1[0]
    xx2 = total3[2]
    xxx2 = xx2[0]

    yy0 = total3[0]
    yyy0 = yy0[1]
    yy1 = total3[1]
    yyy1 = yy1[1]
    yy2 = total3[2]
    yyy2 = yy2[1]

    xxx3 = xxx0
    yyy3 = yyy0

    # Рисуем изначальный и повернутый
    line = Line2D([x0, x1, x2, x3], [y0, y1, y2, y3], color="k")
    abc.add_line(line)
    line = Line2D([xxx0, xxx1, xxx2, xxx3], [yyy0, yyy1, yyy2, yyy3], color="b")
    abc.add_line(line)

plt.xlim(0, 10)
plt.ylim(0, 10)
plt.grid()

abc = plt.gca()
abc.set_aspect("equal")

triangle(abc)

plt.show()
