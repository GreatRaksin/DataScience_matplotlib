import matplotlib.pyplot as plt

x_values = list(range(1, 1001))
y_values = [x**2 for x in x_values]

plt.title('Квадраты чисел', fontsize=24)
plt.xlabel('Значение', fontsize=14)
plt.ylabel('Квадраты значений', fontsize=14)

# Назначение размера шрифта делений на осях
plt.tick_params(axis='both', labelsize=14)


plt.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Paired, s=40)
plt.axis([0, 1100, 0, 1100000])
plt.show()
'''
show() можно заменить на savefig('nameOfTheFile.png', bbox_inches='tight')
'''