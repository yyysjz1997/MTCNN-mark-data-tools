import cv2
import os

global img, point1, point2, start_num, point_eye1, point_eye2, point_nose, point_mouth1, point_mouth2, flag

file_path = 'C:/Users/yyy/Desktop/pic2/'
green = (0, 255, 0)
#global flag

def on_mouse(event, x, y, flags, param):
    global img, point1, point2, start_num, point_eye1, point_eye2, point_nose, point_mouth1, point_mouth2, flag
    #flag = 0
    img_temp = img.copy()

    if ((event == cv2.EVENT_LBUTTONDOWN)&(flag == 0)):  # 左键点击
        point1 = (x, y)
        cv2.circle(img_temp, point1, 10, green, 3)
        cv2.imshow('img', img_temp)
        print(flag)
    elif event == cv2.EVENT_MOUSEMOVE and (flags & cv2.EVENT_FLAG_LBUTTON):  # 按住左键拖曳
        cv2.rectangle(img_temp, point1, (x, y), (255, 0, 0), 3)
        cv2.imshow('img', img_temp)
        flag = 1
        print(flag)
    elif (event == cv2.EVENT_LBUTTONUP)&(flag == 1):  # 左键释放
        point2 = (x, y)
        cv2.rectangle(img_temp, point1, point2, (0, 0, 255), 3)
        cv2.imshow('img', img_temp)
        #cv2.imwrite(file_path + 'bbox/' + str(start_num) + '_bbox.jpg', img_temp)
        flag = 2
        print(flag)
    elif (event == cv2.EVENT_LBUTTONDOWN)&(flag == 2) :
        point_eye1 = (x, y)
        cv2.circle(img_temp, point_eye1, 2, green, 0)
        #cv2.drawKeypoints(img_temp, point_eye1, 10, green, 3)
        cv2.imshow('img', img_temp)
        print(flag)
        flag = 3
        print(flag)
        #cv2.imwrite(file_path + 'bbox/' + str(start_num) + '_bbox.jpg', img_temp)
    elif (event == cv2.EVENT_LBUTTONDOWN) & (flag == 3):
        point_eye2 = (x, y)
        #cv2.drawKeypoints(img_temp, point_eye2, 10, green, 3)
        cv2.circle(img_temp, point_eye2, 2, green, 0)
        cv2.imshow('img', img_temp)
        flag = 4
        print(flag)
    elif (event == cv2.EVENT_LBUTTONDOWN) & (flag == 4):
        point_nose = (x, y)
        #cv2.drawKeypoints(img_temp, point_nose, 10, green, 3)
        cv2.circle(img_temp, point_nose, 2, green, 0)
        cv2.imshow('img', img_temp)
        flag = 5
        print(flag)
    elif (event == cv2.EVENT_LBUTTONDOWN) & (flag == 5):
        point_mouth1 = (x, y)
        #cv2.drawKeypoints(img_temp, point_mouth1, 10, green, 3)
        cv2.circle(img_temp, point_mouth1, 2, green, 0)
        cv2.imshow('img', img_temp)
        flag = 6
        print(flag)
    elif (event == cv2.EVENT_LBUTTONDOWN) & (flag == 6):
        point_mouth2 = (x, y)
        #cv2.drawKeypoints(img_temp, point_mouth2, 10, green, 3)
        cv2.circle(img_temp, point_mouth2, 2, green, 0)
        cv2.imshow('img', img_temp)
        flag = 0
        print(flag)
    elif ((event == cv2.EVENT_RBUTTONDOWN)):    #右键点击保存当前框数据
        param.write(' ' + str(point1[0]) + ' ' + str(point2[0]) + ' ' + str(point1[1]) + ' ' + str(point2[1]) + ' ' + str(point_eye1[0]) + ' '
                    + str(point_eye1[1]) + ' ' + str(point_eye2[0]) + ' ' + str(point_eye2[1]) + ' ' + str(point_nose[0]) + ' ' + str(point_nose[1]) +
                    ' ' + str(point_mouth1[0]) + ' ' + str(point_mouth1[1]) + ' ' + str(point_mouth2[0]) + ' ' + str(point_mouth2[1]))
        cv2.imshow('img', img_temp)
        flag = 0

def main():
    global img, point1, point2, start_num,point_eye1, point_eye2, point_nose, point_mouth1, point_mouth2, flag
    if not os.path.exists(file_path + 'bbox'):
        os.mkdir(file_path + 'bbox')

    file = open(file_path + 'mark.txt', 'w')

    # set start number
    start_num = 1


    while True:

        pic_path = file_path + str(start_num) + '.jpg'
        img = cv2.imread(pic_path)
        if img is None:
            break
        cv2.putText(img, 'pic_' + str(start_num), (60, 40), cv2.FONT_HERSHEY_COMPLEX, 1, green)
        cv2.imshow('img', img)
        flag = 0
        file.write(file_path + str(start_num) + '.jpg')
        cv2.setMouseCallback('img', on_mouse, file)

        start_num += 1

        # q to exit
        if cv2.waitKey(0) & 0xFF == ord('q'):
            break
        else:
            cv2.waitKey(0)
            file.write('\n')

    file.close()


if __name__ == '__main__':
    main()
