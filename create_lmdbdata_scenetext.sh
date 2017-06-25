cur_dir=$(cd $( dirname ${BASH_SOURCE[0]} ) && pwd )
root_dir=$cur_dir
echo 'root_dir :' $root_dir

caffe_root=/data/zhangxin/github/caffe_ssd
# caffe_root=$HOME/github/caffe_ssd
echo 'caffe_root :' $caffe_root

redo=1
data_root_dir=$root_dir/data/
echo 'data_root_dir' $data_root_dir

dataset_name="scenetext"
echo 'dataset_name' $dataset_name

mapfile="$data_root_dir/$dataset_name/labelmap_voc_scenetext.prototxt"
echo 'mapfile' $mapfile

anno_type="detection"
db="lmdb"
min_dim=0
max_dim=0
width=0
height=0

extra_cmd="--encode-type=jpg --encoded"
if [ $redo ]
then
  extra_cmd="$extra_cmd --redo"
fi
for subset in test trainval
do
  python $caffe_root/scripts/create_annoset.py --anno-type=$anno_type --label-map-file=$mapfile \
  --min-dim=$min_dim --max-dim=$max_dim --resize-width=$width --resize-height=$height \
  --check-label $extra_cmd $data_root_dir $root_dir/data/$dataset_name/$subset.txt \
  $data_root_dir/$dataset_name/$db/$dataset_name"_"$subset"_"$db examples/$dataset_name
done
