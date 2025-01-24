# SPDX-FileCopyrightText: 2025 Michael Doerr
# SPDX-FileCopyrightText: 2020 Melissa LeBlanc-Williams, written for Adafruit Industries
# SPDX-License-Identifier: MIT
"""
This example runs on a WaveShare ESP32-S3-Zero
"""

import board
import neopixel

import neomatrix

# Pin for my WaveShare ESP32-S3-Zero
pixel_pin = board.IO1
pixel_width = 16
pixel_height = 16
tiles_X = 1
tiles_Y = 1

pixels = neopixel.NeoPixel(
    pixel_pin,
    pixel_width * pixel_height,
    brightness=0.1,
    auto_write=False,
)

matrixType = (
    neomatrix.NEO_MATRIX_BOTTOM +
    neomatrix.NEO_MATRIX_LEFT +
    neomatrix.NEO_MATRIX_ROWS +
    neomatrix.NEO_MATRIX_ZIGZAG
)

matrix = neomatrix.NeoMatrix(
    pixels,
    pixel_width, pixel_height,
    tiles_X, tiles_Y,
    matrixType,
    rotation=0,
)

text = "Welcome to CircuitPython"

while True:
    for i in range(6 * len(text) + pixel_width):
        matrix.fill(0x000088)
        matrix.pixel(2, 1, 0x00FFFF)
        matrix.line(0, 0, pixel_width - 1, pixel_height - 1, 0x00FF00)
        matrix.line(0, pixel_width - 1, pixel_height - 1, 0, 0x00FF00)
        matrix.fill_rect(2, 3, 12, 10, 0x000000)
        matrix.text(text, pixel_width - i, 4, 0xFFFF00)
        matrix.rect(1, 2, 14, 12, 0xFF0000)
        matrix.line(0, 2, 0, 14, 0x000088)
        matrix.line(pixel_width - 1, 2, pixel_width - 1, 14, 0x000088)
        matrix.display()

