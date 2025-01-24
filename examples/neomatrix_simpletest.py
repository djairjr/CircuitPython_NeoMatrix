# SPDX-FileCopyrightText: 2024 Michael Doerr
# SPDX-FileCopyrightText: 2020 Melissa LeBlanc-Williams, written for Adafruit Industries
# SPDX-License-Identifier: MIT
"""
This example runs on a WaveShare ESP32-S3-Zero
"""
import board
import neopixel

import neomatrix

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

matrixType = ( neomatrix.NEO_MATRIX_BOTTOM + neomatrix.NEO_MATRIX_LEFT +
               neomatrix.NEO_MATRIX_ROWS   + neomatrix.NEO_MATRIX_ZIGZAG )

mtx = neomatrix.NeoMatrix(
    pixels,
    pixel_width, pixel_height,
    tiles_X, tiles_Y,
    matrixType,
    rotation=0,
)

mtx.fill(0x000088)
mtx.pixel(5, 1, 0xFFFF00)
mtx.line(0, 0, pixel_width - 1, pixel_height - 1, 0x00FF00)
mtx.display()

