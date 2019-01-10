import os
import PythonMagick as PM
from tqdm import tqdm

# List of Fonts to look for extracted images of glyphs
# fonts = [font.split('.')[0] for font in os.listdir('../Fonts') if font.endswith('.ttf')]
fonts = ['roya_bold']

fontsProgBar = tqdm(total=len(fonts), desc='Fonts')
for font in fonts:
    print(font)
    # Getting list of old _trim images and delete them
    oldProcessedImages = [image for image in os.listdir(font) if image.endswith('_trim.png')]
    for image in oldProcessedImages:
        os.remove(os.path.join(font, image))
    
    # for each glyph image, remove the background and trim the image
    images = [image for image in os.listdir(font) if image.endswith('.png')]
    # Define colors
    white = PM.Color("#ffffff")
    trans = PM.Color("#00000000")

    glyphProgBar = tqdm(total=len(images), desc='Glyphs', leave=False)
    for image in images:
        # Read the image
        glyphImage = PM.Image(os.path.join(font, image))
        # Remove the backgroundf
        glyphImage.transparent(white, False)
        # Trim the image
        glyphImage.trim()
        
        # If glyph is a Number resize it to 87 pixel height(35 for zero).
        # otherwise 58 pixel height.
        if os.path.splitext(image)[0].isnumeric():
            if os.path.splitext(image)[0] == '0': glyphImage.resize('x35')
            else: glyphImage.resize('67x70')
        else:
            glyphImage.resize('90x70')
        glyphImage.write(os.path.join(font, f'{image.split(".")[0]}_trim.png'))

        glyphProgBar.update(1)
    glyphProgBar.close()
    fontsProgBar.update(1)
fontsProgBar.close()