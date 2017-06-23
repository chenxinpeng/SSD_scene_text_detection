#encoding=utf8
'''
配置项
本例所用数据从
http://robustreading.opendfki.de/trac/wiki/SceneText
下载，下载数据解压后放入data文件夹
'''
import os

class TextDetectionConfig:
    '''经常用到的路径'''
    caffe_root = '/data/zhangxin/github/caffe_ssd'
    data_dir = './data/'
    # train_data_dir = os.path.join(data_dir, 'train-textloc')
    # test_data_dir = os.path.join(data_dir, 'test-textloc-gt')
    suffix = '.jpg'

    train_img_dir = os.path.join(data_dir, 'train-textloc')
    train_xml_dir = os.path.join(data_dir, 'train-textloc')
    train_txt_dir = os.path.join(data_dir, 'train-textloc')
    test_img_dir = os.path.join(data_dir, 'test-textloc-gt')
    test_xml_dir = os.path.join(data_dir, 'test-textloc-gt')
    test_txt_dir = os.path.join(data_dir, 'test-textloc-gt')

if __name__ == '__main__':
    cfg = TextDetectionConfig()
    print cfg.caffe_root
    print cfg.data_dir
    # print cfg.train_data_dir
    # print cfg.test_data_dir
    print cfg.suffix
    print cfg.train_img_dir
    print cfg.train_txt_dir
    print cfg.train_xml_dir
    print cfg.test_img_dir
    print cfg.test_txt_dir
    print cfg.test_xml_dir
