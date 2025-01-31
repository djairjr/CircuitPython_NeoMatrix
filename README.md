## CircuitPython_NeoMatrix

Port of Adafruit's `Adafruit_NeoMatrix` [library](https://github.com/adafruit/Adafruit_NeoMatrix) for the Arduino to CircuitPython.  
See the [Adafruit NeoPixel Überguide](https://learn.adafruit.com/adafruit-neopixel-uberguide/neomatrix-library) for everything you need to know about NeoPixel grids.

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

## Demos

There are several demos in the examples directory that are showing how
the `neomatrix` library and the helper modules `matrix<##>.py` can be used.

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
│   ├── spiral32.py
│   └── spiral8.py
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
│   └── fire8.py
└── water               # Waterfall (Fire2012 with a blue palette)
    ├── water16_a.py
    ├── water16_b.py
    └── water8.py
```

