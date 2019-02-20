import cv2
import math
import os
from random import randint
import sys
import numpy as np
from scipy.ndimage import imread

from PIL import Image, ImageDraw, ImageFilter




if __name__ == '__main__':

    sample_word = sys.argv[1]
    DATA_PATH_1 = 'data_generation/picture1/'

    lang = open('dicts/sp.txt','w') 
    lang.write(sample_word + '\n')
    lang.close()

    HEIGHT = 400
    WIDTH = 400
    image = np.ones((HEIGHT, WIDTH)) * 255
    cv2.randn(image, 235, 10)
    paste_img = Image.new('RGB', (100, 100), (228, 150, 150))
    position = (100, 100)
    back_image = Image.fromarray(image).convert('RGB')
    back_image.paste(paste_img, position)
    #back_image.show()

    DATAGEN_LOC = 'TextRecognitionDataGenerator/TextRecognitionDataGenerator/run.py'
    os.system('rm -rf ' + DATA_PATH_1)
    os.system('python ' + DATAGEN_LOC + ' --output_dir data_generation/picture1 -na 0 -l sp -c 1 -w 1')
    os.system('python ' + DATAGEN_LOC + ' --output_dir data_generation/picture1 -na 0 -l en -c 2 -w 1')

    image = np.ones((HEIGHT, WIDTH)) * 255
    cv2.randn(image, 235, 10)
    back_image = Image.fromarray(image).convert('RGB')

    files_1 = os.listdir(DATA_PATH_1)
    for _, input_file in enumerate(files_1):
        im = Image.open(DATA_PATH_1 + input_file)
        w, h = im.size
        x = (randint(0, WIDTH-w))
        y = (randint(0, HEIGHT-h))
        if(input_file == sample_word + '_0.jpg'):
            print('X-Min: ' + str(x))
            print('Y-Min: ' + str(y))
            print('X-Max: ' + str(x + w))
            print('Y-Max: ' + str(y + h))
        position = (x, y)
        back_image.paste(im, position)
    back_image.show()
    
