# Plate Characters

Extracting Glyphs (Characters) of letters and numbers from `Teraffic`, `Roya Bold`, and `Khorshid` fonts which we assume are used to create license plates.

Here is an explanation on how image of glyphs are created:

# Instruction

For accessing images of each glyph used in a font, First we extract the glyphs from the font as images and we process them to have images with no background and extra paddings.

## prequisites

- Python +3
- [fontforge](https://github.com/fontforge/fontforge)
- [ImageMagick](https://github.com/ImageMagick/ImageMagick)

## Extracting glyphs

We use fontforge to extract the glyphs for each font, it has a python interpreter which can be used to work with fonts as described [here](http://fontforge.github.io/en-US/documentation/scripting/python/#Glyph).

```shell
# Linux (Debian)
sudo add-apt-repository ppa:fontforge/fontforge;
sudo apt-get update;
sudo apt-get install fontforge;

# Windows (requires chocolatey)
choco install fontforge
```

so after installing, add the `bin` folder of the program to your systems `PATH` variable so you can use `ffpython` in your terminal.

then create a python file (like `extract_glyphs.py`) with script below and address your `ttf` font and your output directory:

```python
import fontforge
F = fontforge.open("khorshid/KHORSHID.ttf")
for name in F:
    filename = name + ".png"
    # print name
    F[name].export(filename)
    # F[name].export(filename, 600)     # set height to 600 pixels
```

use the script like this get glyphs as `png` images:

```shell
ffpython extract_glyphs.py
```


## Processing images

After that, we use `ImageMagick` to remove the backgrounds and trim images:

```shell
# Linux
cd 'KHORSHID'



# Windows
cd 'KHORSHID'

for %i in (*.png) do magick convert %i -transparent white -trim -gravity center %~ni-trim.png
```