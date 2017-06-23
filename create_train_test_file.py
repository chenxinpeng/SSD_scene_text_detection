#encoding=utf8
'''
生成训练图像与 XML 标签的位置文件
'''
#! /usr/bin/python

import os
# import sys
import glob

from config import TextDetectionConfig as cfg


def create_file(filename, img_dir, xml_dir, suffix):
    '''生成训练图像与 XML 标签的位置文件
    '''
    with open(filename, 'w') as fobj:
        for imgpath in glob.glob(img_dir + '/*' + suffix):
            imgnum = os.path.splitext(os.path.basename(imgpath))[0]
            xmlpath = os.path.join(xml_dir, str(imgnum), '.xml')
            fobj.write(imgpath + ' ' + xmlpath + '\n')


create_file(os.path.join(cfg.data_dir, "trainval.txt"),
            cfg.train_img_dir, cfg.train_xml_dir, cfg.suffix)
create_file(os.path.join(cfg.data_dir, "test.txt"),
            cfg.test_img_dir, cfg.test_xml_dir, cfg.suffix)
