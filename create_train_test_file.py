#! /usr/bin/python

import os, sys
import glob

trainval_dir = "/home/chenxp/data/VOCdevkit/scenetext/trainval"
test_dir = "/home/chenxp/data/VOCdevkit/scenetext/test"

trainval_img_lists = glob.glob(trainval_dir + '/*.jpg')
trainval_img_names = []
for item in trainval_img_lists:
    temp1, temp2 = os.path.splitext(os.path.basename(item))
    trainval_img_names.append(temp1)

test_img_lists = glob.glob(test_dir + '/*.jpg')
test_img_names = []
for item in test_img_lists:
    temp1, temp2 = os.path.splitext(os.path.basename(item))
    test_img_names.append(temp1)

dist_img_dir = "scenetext/JPEGImages"
dist_anno_dir = "scenetext/Annotations"

trainval_fd = open("/home/chenxp/caffe/data/scenetext/trainval.txt", 'w')
test_fd = open("/home/chenxp/caffe/data/scenetext/test.txt", 'w')

for item in trainval_img_names:
    trainval_fd.write(dist_img_dir + '/' + str(item) + '.jpg' + ' ' + dist_anno_dir + '/' + str(item) + '.xml\n')

for item in test_img_names:
    test_fd.write(dist_img_dir + '/' + str(item) + '.jpg' + ' ' + dist_anno_dir + '/' + str(item) + '.xml\n')
