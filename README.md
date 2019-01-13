# Iranian License Plate Recognition

Using **YOLO** object detection for Detecting plates and a combination of **CNN and LSTM with CTC Loss** for OCR.

## Dataset

### Fonts

Fonts used to create license plate are most likely on of `Traffic Bold`, `Khorshid`, or `Roya Bold` fonts.

![](Assets/license_plate_fonts1.png)
![](Assets/license_plate_fonts2.png)

here is what you can find in `Dataset/Fonts` directory

#### Font files

Fonts are available in `.tff` format. they are used to extract glyphs (characters) of font for creating custom virtual license plates.

#### Name-Maps

A mapping from the glyph name to the number or pronunciation of letter the glyph is representing in available in `<FontName>_namesMap.csv`. it is used to have the same id for same glyphs of each font. later extracted glyphs are renamed using this mapping.

##### e.g.

letter `ج` in `traffic_bold` font is named as `u062C`, the name mapping provides would be `JIM`, also number `۲` which is named `two` will be `2`.

> if you want to use another font, name it in snake_case then create the `namesMap.csv` file with the same structure as others and name it `<FontName>_namesMap.csv`.

## Glyphs

![](Assets/extracting_and_processing_glyphs.png)

we **Extract** Glyphs (Characters) of letters and numbers from `Teraffic`, `Roya Bold`, and `Khorshid` fonts which we assume are used to create license plates. then we **Process** each font to remove background and extra paddings, also rename the glyph images to the character they are representing using `nameMap.csv` file for each font available in `Fonts` directory to have the same name for each glyph of different fonts.

### prequisites

- Python +3
- [fontforge](https://github.com/fontforge/fontforge)
- [ImageMagick](https://github.com/ImageMagick/ImageMagick) with  [PythonMagick](https://github.com/ImageMagick/PythonMagick)

Here is an explanation on how image of glyphs are created:

### Extracting glyphs

We use fontforge to extract the glyphs for each font, it has a python interpreter which can be used to work with fonts as described [here](http://fontforge.github.io/en-US/documentation/scripting/python/#Glyph).

#### Installing `fontforge`

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

##### Linux

```shell
sudo apt install python3-pythonmagick
```

##### Windows

To install PythonMagick on windows You can go to [this website](https://www.lfd.uci.edu/~gohlke/pythonlibs/), download the WHL file named `PythonMagick-0.9.12-cp37-none-win_amd64.whl`, and install it via `pip install <whl file>`.

#### processing

now **run the `process_glyphs.py` script**. it removes backgrounds and trim images to have no extra paddings for each glyph image.

> This could be done in terminal using this command:
> 
> `for %i in (*.png) do magick convert %i -transparent white -trim -gravity center -resize x65 %~ni_trim.png`


## Templates

![](Assets/plate_templates.png)

Different plate templates are used to represent the functionality and origin of the vehicle. you can find the images of these templates with numbers and letters removed, and a `psd` file containing all of these images in the `Templates` directory.

## Generated plates

> Still on process...
