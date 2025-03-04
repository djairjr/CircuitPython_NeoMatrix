## CircuitPython_NeoMatrix

Port of Adafruit's `Adafruit_NeoMatrix` [library][ada01] for the Arduino to CircuitPython.  
See the [Adafruit NeoPixel Überguide][ada02] for everything you need to know about NeoPixel grids.

- Features:
  - Single matrix: 8x8, 16x16, 8x32, 32x8 NeoPixels
  - Tiled matrices: multiple single matrices

### Single matrix
- Horizontal strips (row major)
  - 8w * 8h, 16w * 16h , 8w * 32h
  - zigzag and progressive rows
- Vertical strips (column major)
  - 8w * 8h, 16w * 16h, 32w * 8h
  - zigzag and progressive columns
- Position of first Pixel
  - Bottom, Top, Left, Right

### Tiled matrices
- Assumption: only identical matrices are used
  - tiles of size 8 * 8, or 16 * 16, or 8 * 32, or 32 * 8
- Tiles are laid out in a regular style
  - N * tiles in X direction, either Left --> Right, or reversed
  - M * tiles in Y direction, either Top --> Down, or reversed
  - tiles are wired either in progressive or zigzag mode
- Position of first Tile
  - Bottom, Top, Left, Right


## Basic Usage
1. Determine size and led aranagement of a single NeoPixel matrix.
2. Determine number and arrangement of all your matrix tiles.
3. Use these values to compute a `matrixType` variable.
4. Create a normal CircuitPython `neopixel.NeoPixel` object.
5. Use this `NeoPixel` object and `matrixType` variable to create a `neomatrix.NeoMatrix` object.
6. Finally, use the APIs of the `NeoMatrix` object to draw colorful animations using X and Y coordinates.


## Advanced Usage

### `NeoMatrix` FrameBuffer API
This drawing API is based on the [`adafruit_pixel_framebuf`][ada06] library by Melissa LeBlanc-Williams.

### `NeoGrid` PixelMap API
This drawing API is based on the [`adafruit_led_animation.grid`][ada07] library by Kattni Rembor.


## Demos

There are several demos in the `examples` directory that are showing how
the `neomatrix.py` library and the helper modules `matrix<##>.py` can be used.

Python files with an 8 in the name are intended for 8x8 or 8x32 NeoPixel matrices.
Files with a 16 in the name are meant for 16x16 NeoMatrices and 
files with a 32 in the name should be used for tiled 32x32 matrices.

``` bash
examples/
├── bounce              # bouncing lines and random walks
│   ├── bounce32.py
│   ├── lines16.py
│   ├── lines32.py
│   ├── point.py
│   ├── walk16.py
│   └── walk32.py
├── rainbow             # spiraling rainbows
│   ├── spiral16_a.py
│   ├── spiral16_b.py
│   ├── spiral16_c.py
│   ├── spiral32_a.py
│   ├── spiral32_b.py
│   ├── spiral8_a.py
│   └── spiral8_b.py
├── life                # Tim C's Game of Life animation
│   ├── animate_life.py
│   ├── life16.py
│   ├── life32.py
│   └── life8.py
├── snake               # Tim C's snake animation
│   ├── animate_snake.py
│   ├── snake16.py
│   ├── snake32.py
│   └── snake8.py
├── fire                # Mark Kriegsman's Fire2012 simulation
│   ├── fire16_a.py
│   ├── fire16_b.py
│   ├── fire16_c.py
│   ├── fire32.py
│   └── fire8.py
└── water               # Waterfall (Fire2012 with a blue palette)
│   ├── water16_a.py
│   ├── water16_b.py
│   ├── water16_c.py
│   ├── water32.py
│   └── water8.py
└── snoise              # Simplex Noise demo using Tod Kurt's library
    ├── noise16a.py
    ├── noise16b.py
    ├── noise16c.py
    ├── noise16d.py
    ├── noise32a.py
    ├── noise32b.py
    ├── noise32c.py
    ├── noise32d.py
    ├── noise32e.py
    ├── noise8a.py
    ├── noise8b.py
    └── noise8c.py
```

---

[ada01]: https://github.com/adafruit/Adafruit_NeoMatrix
[ada02]: https://learn.adafruit.com/adafruit-neopixel-uberguide/neomatrix-library

[ada03]: https://github.com/adafruit/Adafruit_CircuitPython_NeoPixel
[ada04]: https://github.com/adafruit/Adafruit_CircuitPython_framebuf
[ada05]: https://github.com/adafruit/Adafruit_CircuitPython_PixelMap

[ada06]: https://github.com/adafruit/Adafruit_CircuitPython_Pixel_Framebuf
[ada07]: https://github.com/adafruit/Adafruit_CircuitPython_LED_Animation
[ada08]: https://github.com/adafruit/Adafruit_CircuitPython_LED_Animation/blob/main/adafruit_led_animation/grid.py
[ada09]: https://github.com/adafruit/Adafruit_CircuitPython_LED_Animation/blob/main/adafruit_led_animation/helper.py

