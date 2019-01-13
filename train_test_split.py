# _*_ coding:utf-8 _*_
"""
-------------------------------------------
    File Name: train_test_split
    Description:
    Author: wrc
    date: 19-1-11
-------------------------------------------
    Change Activity:
            19-1-11:
-------------------------------------------
"""
import os

if __name__ == '__main__':


    train_file = open('/media/wrc/8EF06A4CF06A3A9B/钢筋计数/VOC/ImageSets/Main/trainval.txt', 'w')
    test_file = open('/media/wrc/8EF06A4CF06A3A9B/钢筋计数/VOC/ImageSets/Main/test.txt', 'w')
    for _, _, train_files in os.walk('/media/wrc/8EF06A4CF06A3A9B/钢筋计数/VOC/JPEGImages'):
        continue
    for _, _, test_files in os.walk('/media/wrc/8EF06A4CF06A3A9B/钢筋计数/test_dataset'):
        continue
    for file in train_files:
        train_file.write(file.split('.')[0] + '\n')

    for file in test_files:
        test_file.write(file.split('.')[0] + '\n')
