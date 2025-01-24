# Class for 2D points that are moving
# - coords X, Y
# - delta dX, dY

import random

class Point:

    def __init__(
        self,
        width, height,
        delta,
    ):
        self._width = width
        self._height = height

        self.X = random.randint(0, width)
        self.Y = random.randint(0, height)

        self.dX = random.randint(0, delta) - delta//2
        self.dY = random.randint(0, delta) - delta//2


    def update(self):
        self.X += self.dX
        if (self.X < 0) or (self.X >= self._width):
            self.dX = -self.dX
            self.X += self.dX

        self.Y += self.dY
        if (self.Y < 0) or (self.Y >= self._height):
            self.dY = -self.dY
            self.Y += self.dY

