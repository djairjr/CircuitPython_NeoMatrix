# SPDX-FileCopyrightText: 2025 Mike Doerr
# SPDX-License-Identifier: MIT
'''
# Bouncing lines on 32x32 neopixel matrix
'''

import board
import random
from time import sleep

import rainbowio
import matrix32

NEO_PIN = board.IO1     # for my WS ESP32-S3-Zero

BRIGHT = 0.1
#MODE = "vstripes"
MODE = "hsquares"
matrix = matrix32.MatrixSetup(NEO_PIN, MODE, BRIGHT)

from bounce.point import Point

######

WIDTH = matrix._width
HEIGHT = matrix._height

COL = 0
LEN = 3


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

CNT = 64
while True:
    loop(CNT)
    sleep(3)

