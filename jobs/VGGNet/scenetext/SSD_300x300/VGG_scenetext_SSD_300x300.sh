/data/dmcvcache/zhangxin/caffe_ssd/build/tools/caffe train \
--solver="models/VGGNet/scenetext/SSD_300x300/solver.prototxt" \
--weights="/data/dmcvcache/zhangxin/caffe_ssd/models/VGGNet/VGG_ILSVRC_16_layers_fc_reduced.caffemodel" \
--gpu 4,5,6,7 2>&1 | tee jobs/VGGNet/scenetext/SSD_300x300/VGG_scenetext_SSD_300x300.log
