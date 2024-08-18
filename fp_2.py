import matplotlib.pyplot as plt
import numpy as np

def draw_branch(x, y, angle, length, depth):
    if depth == 0:
        return

    # Визначаємо кінцеві координати для гілки
    x_end = x + length * np.cos(angle)
    y_end = y + length * np.sin(angle)

    # Малюємо лінію (гілку) між точками (x, y) та (x_end, y_end)
    plt.plot([x, x_end], [y, y_end], color='brown', lw=2)

    # Зменшуємо довжину гілки для наступного рівня
    new_length = length * 0.7

    # Кут для нахилу правої та лівої гілки
    angle_left = angle + np.pi / 6  # 30 градусів вліво
    angle_right = angle - np.pi / 6  # 30 градусів вправо

    # Рекурсивно малюємо ліву та праву гілку
    draw_branch(x_end, y_end, angle_left, new_length, depth - 1)
    draw_branch(x_end, y_end, angle_right, new_length, depth - 1)

# Налаштування вікна для малювання
plt.figure(figsize=(8, 8))
plt.axis('off')

# Запитуємо глибину фракталу у користувача
depth = int(input("Введіть глибину фракталу (рівень рекурсії): "))

# Початкові координати та параметри для стовбура дерева
x_start, y_start = 0.5, 0  # Початкова точка на нижній середній частині
initial_length = 0.3  # Довжина стовбура
initial_angle = np.pi / 2  # Вертикальний стовбур (кут 90 градусів)

# Малюємо дерево
draw_branch(x_start, y_start, initial_angle, initial_length, depth)

# Показуємо малюнок
plt.show()