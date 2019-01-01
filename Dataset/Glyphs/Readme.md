# Plate Characters

Here we are **Extracting** Glyphs (Characters) of letters and numbers from `Teraffic`, `Roya Bold`, and `Khorshid` fonts which we assume are used to create license plates. then we **Process** each font to remove background and extra paddings, also we rename the glyph images to the character they are representing using `nameMap.csv` file for each font available in `Fonts` directory to have the same name for each glyph of different fonts.

## prequisites

- Python +3
- [fontforge](https://github.com/fontforge/fontforge)
- [ImageMagick](https://github.com/ImageMagick/ImageMagick) with  [PythonMagick](https://github.com/ImageMagick/PythonMagick)

Here is an explanation on how image of glyphs are created:

## Instructions

### Extracting glyphs

#### Installing `fontforge`

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

#### extracting

now **run the `extract_glyphs.py` script**. it creates a folder for each font in this directory and remove old `.png` images, then extract images for each glyph of fonts and remove the ones don't use in plates, after that renames the images using the mapping provided in in `Fonts` directory for each font.

### Processing images

After that, we use a `ImageMagick` wrapper for python called `PythonMagick` to remove the backgrounds and trim images.

#### Installing `PythonMagick`

To install PythonMagick You can go to this website, download the WHL file named `PythonMagick-0.9.12-cp37-none-win_amd64.whl`, and install it via `pip install <whl file>`.

#### processing

now **run the `process_glyphs.py` script**. it removes backgrounds and trim images to have no extra paddings for each glyph image.

> This could be done in terminal using this command:
> 
> `for %i in (*.png) do magick convert %i -transparent white -trim -gravity center -resize x65 %~ni_trim.png`