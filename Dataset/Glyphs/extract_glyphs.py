import os
import glob
import csv
import subprocess

# Fonts we want to extract glyphs from
fonts = ['khorshid',
         'roya bold', 
         'traffic bold'
         ]


for font in fonts:
    print(f'\n\nExtracting fonts from {font} ...\n\n')
    # Extracting Glyphs from font using fontforge python script (ffpython)
    ffouptut = subprocess.call(['ffpython', f'extract_{font.replace(" ", "_")}.py'], cwd=font)
    # Read name mapping to rename glyph files
    # creates an object of {glyphNames: persianLetterName}
    nameMap = {}
    with open(os.path.join(font, 'namesMap.csv')) as nameMapCsv:
        reader = csv.reader(nameMapCsv)
        next(reader) # Skipping header
        nameMap = {rows[0]:rows[1] for rows in reader}
    
    # Removing unnecessary files
    # remove extras like extension and addressing of the files
    imageFiles = [os.path.basename(os.path.splitext(name)[0]) for name in glob.glob(os.path.join(font, '*.png'))]
    # Mark which files to delete
    filesToKeep = [f'{name}.png' for name in nameMap.keys()]
    filesToDelete = [f'{name}.png' for name in imageFiles if name not in nameMap.keys()]
    # Delete files
    for _file in filesToDelete:
        os.remove(os.path.join(font, _file))
    # Rename files according to namesMap.csv
    for glyphName in nameMap.keys():
        os.rename(os.path.join(font, f'{glyphName}.png'), os.path.join(font, f'{nameMap[glyphName]}.png'))