from PIL import Image, ImageDraw
import numpy as np

# Создаём растр 32х32
width, height = 32, 32
raster = np.zeros((height, width, 3), dtype=np.uint8)

# Задаём центр окружности
center_x, center_y = 16, 16

# Радиус
radius = 10

# Создание изображения с помощью Pillow
image = Image.new("RGB", (width, height), (255, 255, 255))
draw = ImageDraw.Draw(image)

# Рисование круга
draw.ellipse(
    (center_x - radius, center_y - radius, center_x + radius, center_y + radius),
    outline=(0, 0, 0),
    width=1,
)

# Сохранение изображения
image.save("32x32.bmp")

print("Окружность с радиусом 15 сгенерирована в файле '32x32.bmp'")
