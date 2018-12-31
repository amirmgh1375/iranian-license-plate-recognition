from PIL import Image
import os
import random

numbers = [str(i) for i in range(0, 10)]
letters = ['ALEF', 'BE', 'PE', 'TE', 'SE', 'JIM', 'CHE', 'HE', 'KHE', 'DAL', 'ZAL', 'RE', 'ZE', 'ZHE', 'SIN','SHIN', 'SAD', 'ZAD', 'TA', 'ZA', 'EIN', 'GHEIN', 'FE', 'GHAF', 'KAF', 'GAF', 'LAM', 'MIM', 'NON', 'VAV', 'HA', 'YE']

# fonts = [font.split('.')[0] for font in os.listdir('../Fonts') if not font.endswith('.csv')]
fonts_ = ['traffic_bold']
# templates = [template for template in os.listdir('../templates') if template.endswith('.png') and template not in ['tashrifat.png']]
templates_ = ['template-base.png']

def getPlateName(n1, n2, l, n3, n4, n5):
    return f'{n1}{n2}_{l}_{n3}{n4}{n5}'

def getGlyphAddress(font, glyphName):
    return f'../Glyphs/{font}/{glyphName}_trim.png'

def getNewPlate ():
    return [random.choice(numbers), 
            random.choice(numbers),
            random.choice(letters), 
            random.choice(numbers), 
            random.choice(numbers),
            random.choice(numbers)]


for font in fonts_:
    # Create font directory if not exists
    if not os.path.exists(font): os.mkdir(font)

    plate = getNewPlate()
    plateName = label = getPlateName(*plate)

    glyphImages = []
    for glyph in plate:
        glyphImage = Image.open(getGlyphAddress(font, glyph)).convert("RGBA")
        # number.putalpha(255)
        glyphImages.append(glyphImage)
        

    for template in templates_:
        background = Image.open(f'../Templates/{template}', 'r')
        newPlate = Image.new('RGBA', (600,132), (0, 0, 0, 0))
        newPlate.paste(background, (0,0))
        w = 0
        for glyph in glyphImages:
            newPlate.paste(glyph, (70 + w,19), mask=glyph)
            w += glyph.size[0] + 5
        newPlate.show("out.png")
        # newPlate.save("out.png", format="png")