import matplotlib.pyplot as plt

inputValues = [1, 2, 3, 4, 5]
squares = [1, 4, 9, 16, 25]
plt.plot(squares, inputValues, 'ro', linewidth=5, color='#f4a561')

# Назначение заголовка диаграммы и меток осей
plt.title('Квадраты чисел', fontsize=24)
plt.xlabel('Значение', fontsize=14)
plt.ylabel('Квадраты значений', fontsize=14)

# Назначение размера шрифта делений на осях
plt.tick_params(axis='both', labelsize=14)

plt.show()
