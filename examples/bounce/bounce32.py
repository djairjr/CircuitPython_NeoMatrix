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

matrix = matrix32.MatrixSetup(NEO_PIN, "vstripes", 0.1)

from bounce.point import Point

######

WIDTH = matrix._width
HEIGHT = matrix._height

COL = 0
LEN = 6

def init():
    global Start, End, COL, LEN, Lines

    Start = Point(WIDTH, HEIGHT, LEN)
    End   = Point(WIDTH, HEIGHT, LEN)
    COL   = random.randint(0, 256)
    Lines = []

def update(num):
    global Lines, COL

    #print(Start.X, Start.Y, End.X, End.Y)
    L = [(Start.X, Start.Y), (End.X, End.Y), COL]
    Lines.append(L)

    COL = (COL + random.randint(0, 10)) & 255
    Start.update()
    End.update()

    while len(Lines) >= num:
        Lines.pop(0)

def draw():
    for i in range(len(Lines)):
        S = Lines[i][0]
        E = Lines[i][1]
        C = Lines[i][2]
        #print(i, S, E, C)
        color = rainbowio.colorwheel(C)

        matrix.line(S[0], S[1], E[0], E[1], color)

def loop(cnt, num):
    for i in range(cnt):
        update(num)
        matrix.fill(0)
        draw()
        matrix.display()

######

NUM = 8
CNT = 128   # 64

while True:
    init()
    loop(CNT, NUM)
    sleep(3)

