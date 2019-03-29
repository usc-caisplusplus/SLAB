import cv2
import math
import os
from random import randint
import random
import sys
import numpy as np
from scipy.ndimage import imread
from coordinates_to_xml import write_xml

from PIL import Image, ImageDraw, ImageFilter

'''def assembled_background_photo(word, special_word, rand_word_1, rand_word_2, height, width, pic_file, xml_file, picture_dir):
    # background base
    image = np.ones((height, width)) * 255
    cv2.randn(image, 235, 10)
    back_image = Image.fromarray(image).convert('RGB')

    # word we care about
    im_1 = Image.open(special_word)
    w, h = im_1.size
    x = (randint(0, width-w))
    y = (randint(0, height-h))
    position = (x, y)
    back_image.paste(im_1, position)
    #saving relevant xml file
    write_xml(xml_file, word, x, x+w, y, y+h, width, height, pic_file)

    #random words
    im_2 = Image.open(rand_word_1)
    w, h = im_2.size
    x = (randint(0, width-w))
    y = (randint(0, height-h))
    position = (x, y)
    back_image.paste(im_2, position)

    im_3 = Image.open(rand_word_2)
    w, h = im_3.size
    x = (randint(0, width-w))
    y = (randint(0, height-h))
    position = (x, y)
    back_image.paste(im_3, position)

    back_image.save(processed_photos + pic_file)'''

def rand_back(back_dir):
    a=random.choice(os.listdir(back_dir))
    file = back_dir+a
    return Image.open(file)

def assembled_background_photo(special_word, height, width, pic_file, xml_file, picture_dir, back_dir):
    back_image = rand_back(back_dir)

    # word we care about
    im_1 = Image.open(special_word)
    w, h = im_1.size
    x = (randint(0, width-w))
    y = (randint(0, height-h))
    position = (x, y)
    back_image.paste(im_1, position)
    #saving relevant xml file
    write_xml(xml_file, 'sign' , x, x+w, y, y+h, width, height, pic_file)

    back_image.save(processed_photos + pic_file)

if __name__ == '__main__':
    languages = ['en', 'es', 'cn', 'de', 'fr']

    # sample_word = sys.argv[1]
    DATA_PATH_1 = 'data_generation/specialword/'
    # DATA_PATH_2 = 'data_generation/randomwords/'
    processed_photos = 'data_generation/pictures/'
    labels = 'data_generation/labels/'
    BACKGROUND_DIR = 'background_images/'


    '''lang = open('dicts/sp.txt','w') 
    lang.write(sample_word + '\n')
    lang.close()'''

    SAMPLES_PER_LANGUAGE = 100
    HEIGHT = 500
    WIDTH = 500

    DATAGEN_LOC = 'TextRecognitionDataGenerator/TextRecognitionDataGenerator/run.py'
    os.system('rm -rf ' + labels)
    os.system('rm -rf ' + processed_photos)
    os.system('rm -rf ' + DATA_PATH_1)
    # os.system('rm -rf ' + DATA_PATH_2)

    # iterate through languages
    for i in range(len(languages)):
        language = languages[i]
        os.system('python ' + DATAGEN_LOC + ' --output_dir data_generation/specialword -na 0 -l ' + language + ' -c ' + str(int(SAMPLES_PER_LANGUAGE/2)) + ' -w 2 -b')
        os.system('python ' + DATAGEN_LOC + ' --output_dir data_generation/specialword -na 0 -l ' + language + ' -c ' + str(int(SAMPLES_PER_LANGUAGE/2)) + ' -w 2 -bl 2 -rbl -b')
    # os.system('python ' + DATAGEN_LOC + ' --output_dir data_generation/randomwords -na 0 -l en -c ' + str(2*POSITIVE_SAMPLES) + ' -w 1')

    #image = np.ones((HEIGHT, WIDTH)) * 255
    #cv2.randn(image, 235, 10)
    #back_image = Image.fromarray(image).convert('RGB')

    special_files = os.listdir(DATA_PATH_1)
    # ran_files = os.listdir(DATA_PATH_2)
    list_of_special = []
    # list_of_ran = []    
    for _, input_file in enumerate(special_files):
        list_of_special.append(DATA_PATH_1 + input_file)

    '''for _, input_file in enumerate(ran_files):
        list_of_ran.append(DATA_PATH_2 + input_file)'''
    
    i = 0
    os.system('mkdir data_generation/pictures/')
    os.system('mkdir data_generation/labels/')
    while(i < len(list_of_special)):
        special_word = list_of_special[i]
        '''rand_word_1 = list_of_ran[2*i]
        rand_word_2 = list_of_ran[2*i + 1]'''

        assembled_background_photo(special_word, HEIGHT, WIDTH, 'positive' + str(i) + '.jpg', labels + 'positive' + str(i) + '.xml', processed_photos, BACKGROUND_DIR)
        i += 1
    
    os.system('rm -rf ' + DATA_PATH_1)
    # os.system('rm -rf ' + DATA_PATH_2)
    