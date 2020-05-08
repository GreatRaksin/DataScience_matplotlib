import matplotlib.pyplot as plt
from rw import RandomWalk

# строим случайное блуждание и наносим точки на диаграмму
rw = RandomWalk()
rw.fillWalk()

pNumber = list(range(rw.numberOfPoints))

plt.title('Случайное блуждание', fontsize=24)
plt.scatter(rw.x_val, rw.y_val, c=pNumber, cmap=plt.cm.plasma, s=5)
plt.show()