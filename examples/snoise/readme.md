# Simplex Noise by @todbot

[Simplex Noise][wkpd1] is an algorithm by [Ken Perlin][wkpd3], which can be used to generate smoothly looking random terrains.
This source [noise_square_code.py][tod02] was created by Tod Kurt and uses his library [noise.py][tod01].

## ESP32-S3-Matrix with integrated 8x8 NeoPixel matrix
- 64 NeoPixels

| Name | Type | Frames / second |
| --- | --- | --- |
| noise8a.py | NeoPixel | 80 fps |
| noise8b.py | NeoGrid | 70 fps |
| noise8c.py | NeoGrid + custom palette | 71 fps |


## ESP32-S3-Zero with addon 16x16 NeoPixel matrix
- 256 NeoPixels

| Name | Type | Frames / second |
| --- | --- | --- |
| noise16a.py | NeoPixel | 20.1 fps |
| noise16b.py | NeoMatrix | 6.1 fps |
| noise16c.py | NeoGrid | 19.1 fps |
| noise16d.py | NeoGrid + custom palette | 18.5 fps |


## ESP32-S3-Zero with addon 32x32 NeoPixel matrix (made from four 16x16 tiles)
- 1024 NeoPixels

```
noise32a.py
noise32b.py
noise32c.py
noise32d.py
noise32e.py
```

[wkpd1]: https://en.wikipedia.org/wiki/Simplex_noise
[wkpd2]: https://en.wikipedia.org/wiki/Perlin_noise
[wkpd3]: https://en.wikipedia.org/wiki/Ken_Perlin

[tod01]: https://github.com/todbot/CircuitPython_Noise
[tod02]: https://gist.github.com/todbot/58bcf7ea3a85aede3f951f8176e3aad5

