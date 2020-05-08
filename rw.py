from random import choice


class RandomWalk:
    """Класс генерации случаного блуждания"""

    def __init__(self, np=5000):
        """Инициализация атрибутов блуждания"""
        self.numberOfPoints = np

        # Все блуждания будут начинаться с точки (0, 0)
        self.x_val = [0]
        self.y_val = [0]

    def fillWalk(self):
        """Вычисление всех точек блуждания"""

        # Шаги генерятся до достижения необходимой длины
        while len(self.x_val) < self.numberOfPoints:
            # Определние направления и длины перемещения
            xDirection = choice([1, -1])
            xDistance = choice(list(range(5)))
            xStep = xDirection * xDistance

            yDirection = choice([1, -1])
            yDistance = choice(list(range(5)))
            yStep = yDirection * yDistance

            # Отклоняем нулевые перемещения
            if xStep == 0 and yStep == 0:
                continue

            # Вычисляем следующие значения х и у
            nextX = self.x_val[-1] + xStep
            nextY = self.y_val[-1] + yStep

            self.x_val.append(nextX)
            self.y_val.append(nextY)
