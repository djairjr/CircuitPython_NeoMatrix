# SPDX-FileCopyrightText: 2024 Mike Doerr
# SPDX-License-Identifier: MIT

#######################################

# Map 16x16 NeoPixel matrix coordinates to sequential strand indices [0..255].
# Works with one square NeoMatrix tile wired as a 16x16 display.

import neopixel
import neomatrix

#######################################

# Use matrixMode to select matrix type for 2 tile arrangements of a 16x16 matrix
#   matrixMode = "hsquare"      # 1x1 horizontally arranged 16x16 tile
#   matrixMode = "vsquare"      # 1x1 vertically arranged 16x16 tile

def MatrixSetup(pixel_pin, matrixMode, brightness = 0.1):

    if (matrixMode == "hsquare"):       # one horizontally arranged 16x16 tile
        matrixType = (
            neomatrix.NEO_MATRIX_BOTTOM + neomatrix.NEO_MATRIX_LEFT +
            neomatrix.NEO_MATRIX_ROWS + neomatrix.NEO_MATRIX_ZIGZAG
        )
        tileWidth = 16
        tileHeight = 16
        tilesX = 1
        tilesY = 1
        rotation = 0

    elif (matrixMode == "vsquare"):     # one vertically arranged 16x16 tile
        matrixType = (
            neomatrix.NEO_MATRIX_TOP + neomatrix.NEO_MATRIX_LEFT +
            neomatrix.NEO_MATRIX_COLUMNS + neomatrix.NEO_MATRIX_ZIGZAG
        )
        tileWidth = 16
        tileHeight = 16
        tilesX = 1
        tilesY = 1
        rotation = 0

    else:
        raise ValueError(matrixMode)


    # Update to match the number of NeoPixels you have connected
    #pixel_num = 256
    pixel_num = (tileWidth * tilesX) * (tileHeight * tilesY)

    # initialize the neopixels. Change out for dotstars if needed.
    pixels = neopixel.NeoPixel(pixel_pin, pixel_num, brightness=brightness, auto_write=False)

    return neomatrix.NeoMatrix(pixels,
                     tileWidth, tileHeight,
                     tilesX, tilesY,
                     matrixType, rotation)

#######################################

