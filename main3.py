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

print("Нужна симметрия? (1 - да, 0 - нет): ")
sim = int(input())
if sim == 1:
    print("Введите k: ")
    k = float(input())
    print("Введите b: ")
    b = float(input())

# ось симметрии
if sim == 1:
    xt = np.arange(-10, 11)
    yt = k * xt + b
    plt.plot(xt, yt)
    if k > 0:                           # Угол
        alpha1 = complex(cmath.atan(k))
        print(alpha1)
    else:
        if k < 0:
            alpha1 = complex(cmath.pi - cmath.atan(abs(k)))
        else:
            alpha1 = 0
else:
    sim = 0

# Угол
if sim == 1:
    alpha = alpha1 * 180 / math.pi
    print(alpha)
    alpha = int(alpha.real)
    print(alpha)

# Задаём координаты точек
def triangle(abc):
    x0 = 8  # А
    y0 = 1

    x1 = 7  # B
    y1 = 3

    x2 = 6  # C
    y2 = 2

    x3 = x0
    y3 = y0

    # Задаём точку и коэффициент
    print('Введите точку (A, B или C) или точку D: ')
    point = str(input())
    if point == "D":
        print("Введите координаты: \nx: ")
        dx = float(input())
        print("\ny: ")
        dy = float(input())
    print("Введите коэффициент k: ")
    k = float(input())

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
            if point == 'C':
                m = -x2
                n = -y2
            else:
                m = -dx
                n = -dy

    # Перенос в начало координат
    q2 = np.array([[1, 0, 0],
          [0, 1, 0],
          [m, n, 1]])

    total = q1.dot(q2)

    # Масштабирование
    q3 = np.array([[k, 0, 0],
          [0, k, 0],
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
            if point == 'C':
                m = x2
                n = y2
            else:
                m = dx
                n = dy

    # Возврат в исходное положение
    q4 = np.array([[1, 0, 0],
          [0, 1, 0],
          [m, n, 1]])

    total3 = total2.dot(q4)

    if sim == 1:
        qi = np.array([[1, 0, 0],
                   [0, 1, 0],
                   [0, b, 1]])

    if sim == 1:
        if b != 0:
            qj = np.array([[1, 0, 0],
                [0, 1, 0],
                [0, -b, 1]])
            q1 = q1.dot(qj)
            print(qj)
            print(q1)
        qsim = np.array([[math.cos(math.radians(2*alpha)), math.sin(math.radians(2*alpha)), 0],
          [math.sin(math.radians(2*alpha)), -math.cos(math.radians(2*alpha)), 0],
          [0, 0, 1]])
        totalsim = q1.dot(qsim)
        print(totalsim)
        totalsim = totalsim.dot(qi)
    else:
        con = 0

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

    # Треугольник симметрии
    if sim == 1:
        xxsim0 = totalsim[0]
        xxxsim0 = round((xxsim0[0]), 2)
        print(xxxsim0)
        xxsim1 = totalsim[1]
        xxxsim1 = round((xxsim1[0]), 2)
        print(xxxsim1)
        xxsim2 = totalsim[2]
        xxxsim2 = round((xxsim2[0]), 2)
        print(xxxsim2)
        yysim0 = totalsim[0]
        yyysim0 = round((yysim0[1]), 2)
        print(yyysim0)
        yysim1 = totalsim[1]
        yyysim1 = round((yysim1[1]), 2)
        print(yyysim1)
        yysim2 = totalsim[2]
        yyysim2 = round((yysim2[1]), 2)
        print(yyysim2)
        xxxsim3 = xxxsim0
        yyysim3 = yyysim0
    else:
        con = 0

    # Рисуем изначальный и повернутый
    line = Line2D([x0, x1, x2, x3], [y0, y1, y2, y3], color="k")
    abc.add_line(line)
    line = Line2D([xxx0, xxx1, xxx2, xxx3], [yyy0, yyy1, yyy2, yyy3], color="b")
    abc.add_line(line)
    if sim == 1:
        line = Line2D([xxxsim0, xxxsim1, xxxsim2, xxxsim3], [yyysim0, yyysim1, yyysim2, yyysim3], color="b")
        abc.add_line(line)
    else:
        con = 0

plt.xlim(0, 10)
plt.ylim(0, 10)
plt.grid()

abc = plt.gca()
abc.set_aspect("equal")

triangle(abc)

plt.show()
