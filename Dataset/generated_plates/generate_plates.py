from PIL import Image
import os
import random
import numpy as np
import cv2
import imutils
import time

# Characters of Letters and Numbers in Plates
numbers = [str(i) for i in range(0, 10)]
letters = ['ALEF', 'BE', 'PE', 'TE', 'SE', 'JIM', 'CHE', 'HE', 'KHE', 'DAL', 'ZAL', 'RE', 'ZE', 'ZHE', 'SIN','SHIN', 'SAD', 'ZAD', 'TA', 'ZA', 'EIN', 'GHEIN', 'FE', 'GHAF', 'KAF', 'GAF', 'LAM', 'MIM', 'NON', 'VAV', 'HA', 'YE']

# Fonts and Templates
# fonts = [font.split('.')[0] for font in os.listdir('../Fonts') if not font.endswith('.csv')]
fonts = ['roya_bold']
templates = [os.path.basename(os.path.splitext(template)[0]) for template in os.listdir('../templates') if template.endswith('.png') and template not in ['tashrifat.png', 'template-sepah.png', 'template-police.png']]
# templates = ['template-base']

# Noises
noises = os.listdir('../Noises')
# transformations 
transformations = ['rotate_right', 'rotate_left', 'zoom_in', 'zoom_out', 'prespective_transform']

# Count of permutations
permutations = 2

# Generateplate array from string 
# (37GAF853 -> ['3', '7', 'GAF', '8', '5', '3'])
def plateFromName (nameStr):
    numbers = []
    letters = []
    
    for char in nameStr:
        if char.isnumeric(): numbers.append(char)
        else: letters.append(char)

    return [*numbers[:2], ''.join(letters), *numbers[2:]]

# Returns a plate as a string
def getPlateName(n1, n2, l, n3, n4, n5):
    return f'{n1}{n2}_{l}_{n3}{n4}{n5}'

# Returns Address of a glyph image given font, and glyph name
def getGlyphAddress(font, glyphName):
    return f'../Glyphs/{font}/{glyphName}_trim.png'

# Returns an array containing a plate's letter and numbers:
# [number1, number2 , letter, number3, number4, number5]
def getNewPlate ():
    return [random.choice(numbers), 
            random.choice(numbers),
            random.choice(letters), 
            random.choice(numbers), 
            random.choice(numbers),
            random.choice(numbers)]
    # return plateFromName('37GAF853')

# Genrate Noise
def applyNoise (plate):
    background = plate.convert("RGBA")
    noisyTemplates = []
    for noise in noises:
        newPlate = Image.new('RGBA', (600,132), (0, 0, 0, 0))
        newPlate.paste(background, (0,0))
        noise = Image.open(os.path.join('../Noises/', noise)).convert("RGBA")
        newPlate.paste(noise, (0, 0), mask=noise)
        noisyTemplates.append(newPlate)
    return noisyTemplates

# Generate Transformations of plates
def applyTransforms (plate):
    transformedTemplates = []
    plate = np.array(plate)
    
    # Rotating to clockwise
    for _ in range(3):
        result = imutils.rotate_bound(plate, random.randint(2,15))
        result = Image.fromarray(result)
        transformedTemplates.append(result)

    # Rotating to anticlockwise
    for _ in range(3):
        result = imutils.rotate_bound(plate, random.randint(-15,-2))
        result = Image.fromarray(result)
        transformedTemplates.append(result)
    
    # Scaling up
    for _ in range(3):
        height, width, _ = plate.shape
        randScale = random.uniform(1.1, 1.3)
        result = cv2.resize(plate, None, fx=randScale, fy=randScale, interpolation = cv2.INTER_CUBIC)
        result = Image.fromarray(result)
        transformedTemplates.append(result)
    
    # Scaling down
    for _ in range(3):
        height, width, _ = plate.shape
        randScale = random.uniform(0.2, 0.6)
        result = cv2.resize(plate, None, fx=randScale, fy=randScale, interpolation = cv2.INTER_CUBIC)
        result = Image.fromarray(result)
        transformedTemplates.append(result)

    # # Adding perspective transformations
    # for _ in range(3):
    #     rows,cols,ch = plate.shape
    #     background = Image.fromarray(np.zeros(cols + 100, rows + 100, 3))
    #     pts1 = np.float32([[50,50],[200,50],[50,200]])
    #     pts2 = np.float32([[10,100],[200,50],[100,250]])
    #     M = cv2.getAffineTransform(pts1,pts2)
    #     result = cv2.warpAffine(plate,M,(cols,rows))
    #     result = Image.fromarray(result)
    #     transformedTemplates.append(result)
    
    return transformedTemplates

for font in fonts:
    # Create font directory if not exists
    if not os.path.exists(font): os.mkdir(font)
    # time.sleep(0.1)

    for template in templates:
        for i in range(permutations):
            # Generate a plate as an array
            # e.g. ['3', '7', 'GAF', '8', '5', '3']
            plate = getNewPlate()
            # Get the plate name as string
            # e.g. 37_GAF_853
            plateName = label = getPlateName(*plate)

            # Get Glyph images of plate characters
            glyphImages = []
            for glyph in plate:
                glyphImage = Image.open(getGlyphAddress(font, glyph)).convert("RGBA")
                # number.putalpha(255)
                glyphImages.append(glyphImage)

            # Create a blank image with size of templates 
            # and add the background and glyph images
            newPlate = Image.new('RGBA', (600,132), (0, 0, 0, 0))
            background = Image.open(f'../Templates/{template}.png').convert("RGBA")
            newPlate.paste(background, (0,0))
            # adding glyph images with 11 pixel margin
            w = 0
            for i, glyph in enumerate(glyphImages):
                if i == 2:
                    newPlate.paste(glyph, (70 + w,30), mask=glyph)
                else: newPlate.paste(glyph, (70 + w,25), mask=glyph)
                w += glyph.size[0] + 11
            
            # Save Simple Plate
            newPlate.save(f"{font}/{plateName}_{template.split('-')[1]}.png")
            # newPlate.show(f"{font}/{plateName}_{template.split('-')[1]}.png")
            
            noisyTemplates = applyNoise(newPlate)
            for noisyTemplate in noisyTemplates:
                transformedTemplates = applyTransforms(noisyTemplate)
                for transformedTemplate in transformedTemplates:
                    transformedTemplate.save(f"{font}/{plateName}_{template.split('-')[1]}_{random.randint(0,20)}.png")