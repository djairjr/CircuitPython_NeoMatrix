# SPDX-FileCopyrightText: 2025 Mike Doerr
# SPDX-License-Identifier: MIT

'''
# Class for 2D points that are moving
# - coords X, Y
# - delta dX, dY
'''

import random

class Point:

    def __init__(
        self,
        width, height,
        delta,
    ):
        self._width = width
        self._height = height

        self.X = random.randint(0, width-1)
        self.Y = random.randint(0, height-1)

        self.dX = random.randint(-delta, delta)
        self.dY = random.randint(-delta, delta)


    def update(self):
        self.X += self.dX
        if (self.X < 0) or (self.X >= self._width):
            self.dX = -self.dX
            self.X += self.dX

        self.Y += self.dY
        if (self.Y < 0) or (self.Y >= self._height):
            self.dY = -self.dY
            self.Y += self.dY

