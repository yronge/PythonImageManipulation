# Usage: JPGtoPNGconverter source_folder output_folder
# Takes all jpg files from source folder and save them as png files in output folder
# source_folder can ONLY contain images, and no other directory
# create output_folder at same level of source_folder

import sys
import os
from PIL import Image

# grab 1st and 2nd arguments
src_folder = sys.argv[1]
out_folder = sys.argv[2]

print(f'\nSource folder = {src_folder}, output folder = {out_folder}\n')

if not os.path.exists(out_folder):
    os.makedirs(out_folder)

print('-------------')
print(os.listdir(src_folder))   # remove directories from this list for the program to work!
print('-------------')

for filename in os.listdir(src_folder):
    print(f'Opening {filename} ... ')
    img = Image.open(f'{src_folder}{filename}')
    clean_name = os.path.splitext(filename)[0]
    img.save(f'{out_folder}{clean_name}.png', 'png')
    print(f'Image: {filename} converted to png')
