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
    data_dir = 'data'
    dataset_name = 'scenetext'
    # train_data_dir = os.path.join(data_dir, 'train-textloc')
    # test_data_dir = os.path.join(data_dir, 'test-textloc-gt')
    suffix = '.jpg'

    train_img_dir = 'train-textloc'
    train_xml_dir = 'train-textloc'
    train_txt_dir = 'train-textloc'
    test_img_dir = 'test-textloc-gt'
    test_xml_dir = 'test-textloc-gt'
    test_txt_dir = 'test-textloc-gt'

    db_format = "lmdb"
    train_lmdb_dir = os.path.join(data_dir, dataset_name, db_format,
                                  dataset_name+'_trainval_'+db_format)
    test_lmdb_dir = os.path.join(data_dir, dataset_name, db_format,
                                 dataset_name+'_test_'+db_format)

    gt_file_prefix = 'gt_'
    labelmap_file = 'labelmap_voc_{}.prototxt'.format(dataset_name)


def create_dir(path):
    '''创建文件夹'''
    if os.path.exists(path):
        os.makedirs(path)

if __name__ == '__main__':
    cfg = TextDetectionConfig()
    print cfg.caffe_root
    print cfg.data_dir
    print cfg.dataset_name
    # print cfg.train_data_dir
    # print cfg.test_data_dir
    print cfg.suffix
    print cfg.train_img_dir
    print cfg.train_txt_dir
    print cfg.train_xml_dir
    print cfg.test_img_dir
    print cfg.test_txt_dir
    print cfg.test_xml_dir
