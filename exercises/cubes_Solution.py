import matplotlib.pyplot as plt

x_values = list(range(1, 6))  # list(range(1, 5001))
y_values = [x**3 for x in x_values]

plt.title('Кубы чисел', fontsize=24)
plt.xlabel('Значение', fontsize=14)
plt.ylabel('Кубы значений', fontsize=14)

# Назначение размера шрифта делений на осях
plt.tick_params(axis='both', labelsize=14)


plt.scatter(x_values, y_values, c='blue', s=40)  # c=y_values, cmap=plt.cm.inferno s=5
plt.axis([0, 6, 0, 130])  # [0, 5000, 0, 1300000]
plt.show()
'''
show() можно заменить на savefig('nameOfTheFile.png', bbox_inches='tight')
'''