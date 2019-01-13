# -*- coding=utf-8 -*-
import os
import shutil

source_pic_root_path = '/media/wrc/8EF06A4CF06A3A9B/kitti/training/JPEGImages'
target_pic_root_path = '/media/wrc/8EF06A4CF06A3A9B/kitti/training/data_coco/coco_train2014'
if os.path.exists(target_pic_root_path):
    shutil.rmtree(target_pic_root_path)
os.makedirs(target_pic_root_path)
for parent, _, files in os.walk(source_pic_root_path):
    for file in files:
        target_pic_path = os.path.join(target_pic_root_path, file)
        source_pic_path = os.path.join(source_pic_root_path, file)
        shutil.copyfile(source_pic_path, target_pic_path)
print('done')