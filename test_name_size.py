#! /usr/bin/python

import os, sys
import glob
from PIL import Image

img_dir = "/home/chenxp/data/VOCdevkit/scenetext/JPEGImages"

img_lists = glob.glob(img_dir + '/*.jpg')

test_name_size = open('/home/chenxp/caffe/data/scenetext/test_name_size.txt', 'w')

for item in img_lists:
    img = Image.open(item)
    width, height = img.size
    temp1, temp2 = os.path.splitext(os.path.basename(item))
    test_name_size.write(temp1 + ' ' + str(height) + ' ' + str(width) + '\n')

