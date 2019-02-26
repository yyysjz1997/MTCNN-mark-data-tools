
# !/usr/bin/env python3
# -*- coding: utf-8 -*-

import re

save_txt = 'C:/Users\yyy\Desktop/m11.txt'
read_txt = 'C:/Users\yyy\Desktop/mark_1218.txt'

def main(input_file, output_file):

    reader = open(input_file, 'r')

    writer = open(output_file, 'a')
    while True:
        line = reader.readline()
        if len(line) == 0:
            print("convert successfully!!")
            break

        line = line.replace('\n','')
        (dir, x1 , x2, y1 , y2 , point_leye_x , point_leye_y ,
         point_reye_x , point_reye_y , point_nose_x , point_nose_y,
         point_lmouse_x , point_lmouse_y , point_rmouse_x , point_rmouse_y) = line.split(' ')
        print('dir = ',dir,'    x1 = ',x1, '    x2 = ',x2, '    y1 = ',y1, '    y2 =',y2,
              '    point_leye_x=',point_leye_x,'    point_leye_y = ',point_leye_y, '   point_reye_x = ',point_reye_x,
              '   point_reye_y = ', point_reye_y,'    point_nose_x = ',point_nose_x,'      point_nose_y = ',point_nose_y,
              '    point_lmouse_x = ',point_lmouse_x,'       point_lmouse_y = ',point_lmouse_y,'    point_rmouse_x = ',point_rmouse_x,'point_rmouse_y = ',point_rmouse_y) # 打印出两个串，串之间加入said：作为分割。
        #print(type(point_leye_x))
        num_jpg = dir.split('/')[-1]

        line = 'D:\Pattern_recognition\MTCNN-Tensorflow\prepare_data\pic/' + num_jpg + ' ' + x1 + ' ' + y1 + ' ' + x2 + ' ' + y2 + '\n'

        #print(line.split(' '))
        #print(line)
        writer.write(line)

    reader.close()
    writer.close()


if __name__ == '__main__':
    main(read_txt, save_txt)
