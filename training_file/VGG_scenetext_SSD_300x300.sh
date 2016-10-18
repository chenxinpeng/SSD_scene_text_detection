cd /home/chenxp/caffe
./build/tools/caffe train \
--solver="models/VGGNet/scenetext/SSD_300x300/solver.prototxt" \
--weights="models/VGGNet/VGG_ILSVRC_16_layers_fc_reduced.caffemodel" \
--gpu 0 | tee jobs/VGGNet/scenetext/SSD_300x300/VGG_scenetext_SSD_300x300.log
