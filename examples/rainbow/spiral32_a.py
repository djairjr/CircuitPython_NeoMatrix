# SPDX-FileCopyrightText: 2025 Pagong
# SPDX-License-Identifier: MIT
'''
# This is for WaveShare ESP32-S3-Zero with four 16x16 NeoPixel-Matrix at IO1
'''

import time
import board
import neopixel

import rainbowio
import neomatrix

import matrix32

#####################

BRIGHTNESS = 0.05     # A number between 0.0 and 1.0, where 0.0 is off, and 1.0 is max.
NEO_PIN = board.IO1   # NeoPixel pin on my ESP32-S3-Zero with 16x16 NeoPixel matrix
matrix = matrix32.MatrixSetup(NEO_PIN, "hsquares", BRIGHTNESS)

NUM_COLS = matrix._width
NUM_CELLS = matrix._height

NUM_PIXELS = (NUM_COLS * NUM_CELLS)  # Update this to match the number of LEDs.
SPEED = 0.05         # Increase to slow down the fire. Decrease to speed it up.

####################### coord mapping ###################

def spiral32(frame):
    xmin = 0; xmax = NUM_COLS-1
    ymin = 0; ymax = NUM_CELLS-1
    xsrc = 0; ysrc = 0; direction = 0

    for src in range(len(frame)):
        matrix.pixel(xsrc, ysrc, frame[src])
        #print(src, xsrc, ysrc)

        # advance X and Y along the spiral
        if direction == 0:      # go right
            xsrc += 1
            if xsrc == xmax: direction += 1
        elif direction == 1:    # go down
            ysrc += 1
            if ysrc == ymax: direction += 1
        elif direction == 2:    # go left
            xsrc -= 1
            if xsrc == xmin: direction += 1
        else:                   # go up
            ysrc -= 1
            if ysrc == ymin:
                direction = 0
                # end of box has been reached
                # start next, smaller box
                xmin += 1; xmax -= 1; xsrc = xmin
                ymin += 1; ymax -= 1; ysrc = ymin

#####################

def rainbow(frame, start):
    for i in range(NUM_PIXELS):
        hue = (start - i) % 256
        frame.append(rainbowio.colorwheel(hue))
    #print(frame[0])

########## main loop #################

while True:
    for start in range(128):
        frame = []
        rainbow(frame, start*2)
        spiral32(frame)
        matrix.display()
        time.sleep(SPEED)

