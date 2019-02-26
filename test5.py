#mark_txt_not_landmark(don't have landmarks) convert to mark_num1

# !/usr/bin/env python3
# -*- coding: utf-8 -*-

import re

save_txt = 'C:/Users\yyy\Desktop/m11.txt'
read_txt = 'C:/Users\yyy\Desktop\mark_1218.txt'

def main(input_file, output_file):

    reader = open(input_file, 'r')

    writer = open(output_file, 'a')
    while True:

        line = reader.readline()
        if len(line) == 0:
            print("convert successfully!!")
            break

        line = line.replace('\n','')
        (dir, x1 , x2, y1 , y2 ) = line.split(' ')
        print('dir = ',dir,'    x1 = ',x1, '    y1 = ',y1, '    x2 = ',x2, '    y2 =',y2,)# 打印出两个串，串之间加入said：作为分割。

        num_jpg= dir.split('/')[-1]

        print(num_jpg)

        line = 'D:\Pattern_recognition\MTCNN-Tensorflow\prepare_data\pic/' + num_jpg + ' ' + x1 + ' ' + y1 + ' ' +x2 + ' ' + y2 +'\n'

        #print(line.split(' '))
        #print(line)
        writer.write(line)

    reader.close()
    writer.close()


if __name__ == '__main__':
    main(read_txt, save_txt)
