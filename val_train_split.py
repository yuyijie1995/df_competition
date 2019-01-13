# _*_ coding:utf-8 _*_
"""
-------------------------------------------
    File Name: val_train_split
    Description:
    Author: wrc
    date: 19-1-12
-------------------------------------------
    Change Activity:
            19-1-12:
-------------------------------------------
"""
import random
import os
import shutil

src_img_dir='data_aug/DataAugForObjectDetection/newimg'
src_label_dir='data_aug/DataAugForObjectDetection/newxml'
val_img_dir='data_aug/DataAugForObjectDetection/newimg_val'
val_label_dir='data_aug/DataAugForObjectDetection/newxml_val'

if not os.path.exists(val_img_dir):
    os.mkdir(val_img_dir)
if not os.path.exists(val_label_dir):
    os.mkdir(val_label_dir)

filelist=os.listdir(src_img_dir)
val_rate=0.3
val_numbers=int(len(filelist)*val_rate)
val_list=random.sample(filelist,val_numbers)
print(val_list)
for file in val_list:
    imagefile_path=os.path.join(src_img_dir,file)
    image_path=os.path.join(val_img_dir,file)

    filename,_=os.path.splitext(file)
    shutil.move(imagefile_path,image_path)
    src_label_dir1=os.path.join(src_label_dir,filename+'.xml')
    label_path=os.path.join(val_label_dir,filename+'.xml')
    shutil.move(src_label_dir1,label_path)










if __name__ == '__main__':
    pass