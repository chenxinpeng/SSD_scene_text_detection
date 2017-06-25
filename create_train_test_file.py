#encoding=utf8
'''
生成训练图像与 XML 标签的位置文件
'''
#! /usr/bin/python

import os
# import sys
import glob

from config import TextDetectionConfig as cfg


def create_file(filename, data_dir, dataset_name, img_dir, xml_dir, suffix):
    '''生成训练图像与 XML 标签的位置文件
        filename 文件列表存放路径
        img_dir 图片存放路径
        xml_dir xml存放路径
        suffix 图片后缀名
    '''
    filelist = os.path.join(data_dir, dataset_name, filename)
    with open(filelist, 'w') as fobj:
        for imgpath in glob.glob(os.path.join(data_dir, dataset_name, img_dir) + '/*' + suffix):
            img_basename = os.path.basename(imgpath)
            img_name = os.path.splitext(img_basename)[0]
            xmlpath = os.path.join(dataset_name, xml_dir, img_name + '.xml')
            fobj.write(os.path.join(dataset_name, img_dir, img_basename) + ' ' + xmlpath + '\n')


create_file("trainval.txt",
            cfg.data_dir, cfg.dataset_name,
            cfg.train_img_dir, cfg.train_xml_dir,
            cfg.suffix)
create_file("test.txt",
            cfg.data_dir, cfg.dataset_name,
            cfg.test_img_dir, cfg.test_xml_dir,
            cfg.suffix)
