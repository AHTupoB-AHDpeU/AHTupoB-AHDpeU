import numpy as np
import matplotlib.pyplot as plt

# Рисуем оси
plt.xlabel("x")
plt.ylabel("y")
plt.grid()

# 1 график синий
x1 = np.arange(-20, 20)
y1 = x1**3
plt.plot(x1, y1)

plt.show()
