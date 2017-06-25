#encoding=utf8
#! /usr/bin/python
'''
先将 ICDAR 2011 给定的 gt_**.txt 标签文件转换为 Pascal VOC XML 格式
'''

import os
# import sys
import glob
from PIL import Image

from config import TextDetectionConfig as cfg

def create_xml(img_dir, txt_dir, xml_dir, suffix):
    '''create xml'''
    for imgpath in glob.glob(img_dir + '/*' + suffix):
        img_name = os.path.splitext(os.path.basename(imgpath))[0]

        width, height = Image.open((img_dir + '/' + img_name + suffix)).size
        print imgpath, img_name, width, height

        # write in xml file
        # os.mknod(src_txt_dir + '/' + img_name + '.xml')
        xml_file = open((xml_dir + '/' + img_name + '.xml'), 'w')
        xml_file.write('<annotation>\n')
        xml_file.write('    <folder>VOC2007</folder>\n')
        xml_file.write('    <filename>' + str(img_name) + suffix + '</filename>\n')
        xml_file.write('    <size>\n')
        xml_file.write('        <width>' + str(width) + '</width>\n')
        xml_file.write('        <height>' + str(height) + '</height>\n')
        xml_file.write('        <depth>3</depth>\n')
        xml_file.write('    </size>\n')

        # open the crospronding txt file
        gt_file_name = os.path.join(txt_dir, 'gt_' + img_name + '.txt')
        # write the region of text on xml file
        for img_each_label in open(gt_file_name, 'r').read().splitlines():
            spt = img_each_label.split(',')
            xml_file.write('    <object>\n')
            xml_file.write('        <name>text</name>\n')
            xml_file.write('        <pose>Unspecified</pose>\n')
            xml_file.write('        <truncated>0</truncated>\n')
            xml_file.write('        <difficult>0</difficult>\n')
            xml_file.write('        <bndbox>\n')
            xml_file.write('            <xmin>' + str(spt[0]) + '</xmin>\n')
            xml_file.write('            <ymin>' + str(spt[1]) + '</ymin>\n')
            xml_file.write('            <xmax>' + str(spt[2]) + '</xmax>\n')
            xml_file.write('            <ymax>' + str(spt[3]) + '</ymax>\n')
            xml_file.write('        </bndbox>\n')
            xml_file.write('    </object>\n')

        xml_file.write('</annotation>')

if __name__ == '__main__':
    create_xml(cfg.train_img_dir, cfg.train_txt_dir, cfg.train_xml_dir, cfg.suffix)
    create_xml(cfg.test_img_dir, cfg.test_txt_dir, cfg.test_xml_dir, cfg.suffix)
