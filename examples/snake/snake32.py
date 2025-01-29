# SPDX-FileCopyrightText: 2024 Tim Cocks for Adafruit Industries
# SPDX-FileCopyrightText: 2024 Michael Doerr
#
# SPDX-License-Identifier: MIT
import board
import neopixel

import neomatrix

from snake.animate_snake import SnakeAnimation

# Update to match the pin connected to your NeoPixels
pixel_pin = board.IO1
# Update to match the number of NeoPixels you have connected
pixel_num = 1024

# initialize the neopixels. Change out for dotstars if needed.
pixels = neopixel.NeoPixel(pixel_pin, pixel_num, brightness=0.02, auto_write=False)

####

# Use mode to select matrix type for 4 common tile arrangements of a 32x32 matrix
mode = "hsquares"       # horizontally arranged 16x16 tiles
#mode = "vsquares"      # vertically arranged 16x16 tiles
#mode = "hstripes"      # horizontally arranged 32x8 tiles
#mode = "vstripes"      # vertically arranged 8x32 tiles

if (mode == "hsquares"):
    matrixType = (
        neomatrix.NEO_MATRIX_BOTTOM + neomatrix.NEO_MATRIX_LEFT +
        neomatrix.NEO_MATRIX_ROWS + neomatrix.NEO_MATRIX_ZIGZAG +
        neomatrix.NEO_TILE_BOTTOM + neomatrix.NEO_TILE_LEFT +
        neomatrix.NEO_TILE_ROWS + neomatrix.NEO_TILE_PROGRESSIVE
    )
    tileWidth = 16
    tileHeight = 16
    tilesX = 2
    tilesY = 2
    color = 0x0000ff

elif (mode == "vsquares"):
    matrixType = (
        neomatrix.NEO_MATRIX_TOP + neomatrix.NEO_MATRIX_LEFT +
        neomatrix.NEO_MATRIX_COLUMNS + neomatrix.NEO_MATRIX_ZIGZAG +
        neomatrix.NEO_TILE_TOP + neomatrix.NEO_TILE_LEFT +
        neomatrix.NEO_TILE_COLUMNS + neomatrix.NEO_TILE_PROGRESSIVE
    )
    tileWidth = 16
    tileHeight = 16
    tilesX = 2
    tilesY = 2
    color = 0xff0000

elif (mode == "vstripes"):
    matrixType = (
        neomatrix.NEO_MATRIX_BOTTOM + neomatrix.NEO_MATRIX_LEFT +
        neomatrix.NEO_MATRIX_ROWS + neomatrix.NEO_MATRIX_ZIGZAG +
        neomatrix.NEO_TILE_BOTTOM + neomatrix.NEO_TILE_LEFT +
        neomatrix.NEO_TILE_COLUMNS + neomatrix.NEO_TILE_ZIGZAG
    )
    tileWidth = 8
    tileHeight = 32
    tilesX = 4
    tilesY = 1
    color = 0x00ffff

elif (mode == "hstripes"):
    matrixType = (
        neomatrix.NEO_MATRIX_TOP + neomatrix.NEO_MATRIX_LEFT +
        neomatrix.NEO_MATRIX_COLUMNS + neomatrix.NEO_MATRIX_ZIGZAG +
        neomatrix.NEO_TILE_TOP + neomatrix.NEO_TILE_LEFT +
        neomatrix.NEO_TILE_ROWS + neomatrix.NEO_TILE_ZIGZAG
    )
    tileWidth = 32
    tileHeight = 8
    tilesX = 1
    tilesY = 4
    color = 0xffff00

else:
    raise ValueError(mode)

####

matrix = neomatrix.NeoMatrix(pixels, tileWidth, tileHeight, tilesX, tilesY, matrixType)

# initialize the animation
snake = SnakeAnimation(matrix, speed=0.1, color=color, snake_length=7)

while True:
    # call animation to show the next animation frame
    snake.animate()

