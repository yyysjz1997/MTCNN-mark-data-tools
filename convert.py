# coding=utf-8
# author  yyy  2018/11/28
# 彩色图片变为灰度图片
from PIL import Image
import os
import os.path

file_path = 'C:/Users/yyy/Desktop/test2/'

def main():
    global start_num
    start_num = 0

    files = os.listdir(file_path)

    print(len(files))
    if not os.path.exists(file_path + 'gray'):
        os.mkdir(file_path + 'gray')

    while (start_num < len(files)):
        pic_path = file_path+files[start_num]

        img = Image.open(pic_path)
        if img is None:
            break
        # 模式L”为灰色图像，它的每个像素用8个bit表示，0表示黑，255表示白，其他数字表示不同的灰度。
        Img = img.convert('L')
        Img.save(file_path + 'gray/' + str(start_num+1) + '.jpg')
        # Img.show()

        start_num += 1

    print(start_num)
    print("RGB TO GRAY FINISH!!")

if __name__ == '__main__':
    main()





'''
# 自定义灰度界限，大于这个值为黑色，小于这个值为白色
threshold = 200

table = []
for i in range(256):
    if i < threshold:
        table.append(0)
    else:
        table.append(1)

# 图片二值化
photo = Img.point(table, '1')
photo.save("test2.jpg")
photo.show()
'''