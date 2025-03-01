# SPDX-FileCopyrightText: 2025 Mike Doerr
# SPDX-License-Identifier: MIT
'''
# Bouncing lines on 16x16 neopixel matrix
'''

import board
import random
from time import sleep

import rainbowio
import matrix16

NEO_PIN = board.IO1     # for my WS ESP32-S3-Zero

matrix = matrix16.MatrixSetup(NEO_PIN, "hsquare", 0.1)

from bounce.point import Point

######

WIDTH = matrix._width
HEIGHT = matrix._height

COL = 0
LEN = 2


def line(Start, End):
    global COL

    color = rainbowio.colorwheel(COL)
    matrix.line(Start.X, Start.Y, End.X, End.Y, color)

    COL = (COL + random.randint(1, 9)) & 255
    Start.update()
    End.update()

def loop(count):
    Start = Point(WIDTH, HEIGHT, LEN)
    End   = Point(WIDTH, HEIGHT, LEN)

    matrix.fill(0)
    for i in range(count):
        line(Start, End)
        matrix.display()

######

CNT = 16
while True:
    loop(CNT)
    sleep(3)

