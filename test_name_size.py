#! /usr/bin/python
'''
img_name height width
'''
import os
# import sys
import glob
from PIL import Image

from config import TextDetectionConfig as cfg


def get_name_size(img_dir, namesize_file):
    ''' get name size
        img_dir 图片路径
        namesize_file name_size文件存放路径
    '''
    with open(namesize_file, 'w') as nsfile:
        for imgpath in glob.glob(os.path.join(img_dir, '*' + cfg.suffix)):
            width, height = Image.open(imgpath).size
            img_name = os.path.splitext(os.path.basename(imgpath))[0]
            nsfile.write(img_name + ' ' + str(height) + ' ' + str(width) + '\n')


get_name_size(cfg.train_img_dir,
              os.path.join(cfg.data_dir, 'train_name_size.txt'))
get_name_size(cfg.test_img_dir,
              os.path.join(cfg.data_dir, 'test_name_size.txt'))
