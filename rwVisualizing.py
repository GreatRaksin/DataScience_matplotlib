import matplotlib.pyplot as plt
from myPart.randWalk import RandomWalk

# строим случайное блуждание и наносим точки на диаграмму
rw = RandomWalk()
rw.fillWalk()


plt.title('Случайное блуждание', fontsize=24)
plt.scatter(rw.x_val, rw.y_val, c=rw.x_val, cmap=plt.cm.inferno, s=5)
plt.show()