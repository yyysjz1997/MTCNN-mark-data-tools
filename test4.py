#mark1(don't have landmarks) convert to wider_face_train_bbx_gt_new.txt

# !/usr/bin/env python3
# -*- coding: utf-8 -*-

import re

save_txt = 'C:/Users\yyy\Desktop/wider_face_train_bbx_gt_new.txt'
read_txt = 'C:/Users\yyy\Desktop/mark_num1 .txt'

def main(input_file, output_file):

    reader = open(input_file, 'r')

    writer = open(output_file, 'a')
    while True:
        line = reader.readline()
        if len(line) == 0:
            print("convert successfully!!")
            break

        line = line.replace('\n','')
        (dir, x1 , y1, x2 , y2 ) = line.split(' ')
        print('dir = ',dir,'    x1 = ',x1, '    y1 = ',y1, '    x2 = ',x2, '    y2 =',y2,)# 打印出两个串，串之间加入said：作为分割。

        num_jpg= dir.split('/')[-1]
        #print(num_jpg)
        x1_num = int(x1)
        y1_num = int(y1)
        x2_num = int(x2)
        y2_num = int(y2)
        height = str(y2_num - y1_num)
        weight = str(x2_num - x1_num)
        print(height,weight)
        line = num_jpg + '.jpg'+ '\n' + '1\n' + x1 + ' ' + y1 + ' ' + weight + ' ' + height + ' 2 0 0 0 0 0 \n'

        #print(line.split(' '))
        #print(line)
        writer.write(line)

    reader.close()
    writer.close()


if __name__ == '__main__':
    main(read_txt, save_txt)
