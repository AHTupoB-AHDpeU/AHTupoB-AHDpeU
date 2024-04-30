import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Функция F(x, z)
def F(x, z):
    R = np.sqrt(x**2 + z**2)
    return 8 * np.cos(1.2 * R) / (R + 1)

# Генерация значений x, z в указанном диапазоне
x = np.linspace(-2*np.pi, 2*np.pi, 100)
z = np.linspace(-2*np.pi, 2*np.pi, 100)
x, z = np.meshgrid(x, z)

# Расчет значений F
f_values = F(x, z)

# Создание 3D графика
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Построение поверхности viridis coolwarm
surface = ax.plot_surface(x, z, f_values, cmap='viridis')

# Добавление меток
ax.set_xlabel('Ось X')
ax.set_ylabel('Ось Z')

# шкала fig.colorbar(surface, ax=ax, shrink=0.5, aspect=10)

plt.show()
