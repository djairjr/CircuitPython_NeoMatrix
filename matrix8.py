# SPDX-FileCopyrightText: 2025 Mike Doerr
# SPDX-License-Identifier: MIT

#######################################

# Map 8x32 NeoPixel matrix coordinates to sequential strand indices [0..255].
# Works with one NeoMatrix tile wired as a 8x32 display.

import neopixel
import neomatrix

#######################################

# Use matrixMode to select matrix type for 2 tile arrangements of a 8x32 matrix
#   matrixMode = "hstripe"      # 1x1 horizontally arranged 32x8 tile
#   matrixMode = "vstripe"      # 1x1 vertically arranged 8x32 tile

def MatrixSetup(pixel_pin, matrixMode, brightness = 0.1):

    if (matrixMode == "hstripe"):       # one horizontally arranged 32x8 tile
        matrixType = (
            neomatrix.NEO_MATRIX_TOP + neomatrix.NEO_MATRIX_LEFT +
            neomatrix.NEO_MATRIX_COLUMN + neomatrix.NEO_MATRIX_ZIGZAG
        )
        tileWidth = 32
        tileHeight = 8
        tilesX = 1
        tilesY = 1
        rotation = 0

    elif (matrixMode == "vstripe"):     # one vertically arranged 8x32 tile
        matrixType = (
            neomatrix.NEO_MATRIX_BOTTOM + neomatrix.NEO_MATRIX_LEFT +
            neomatrix.NEO_MATRIX_ROWS + neomatrix.NEO_MATRIX_ZIGZAG
        )
        tileWidth = 8
        tileHeight = 32
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

