import cv2
import os

global img, point1, point2, start_num

file_path = '/Users/MLB/Desktop/123/'
green = (0, 255, 0)


def on_mouse(event, x, y, flags, param):
    global img, point1, point2, start_num
    img_temp = img.copy()

    if event == cv2.EVENT_LBUTTONDOWN:  # 左键点击
        point1 = (x, y)
        cv2.circle(img_temp, point1, 10, green, 3)
        cv2.imshow('img', img_temp)
    elif event == cv2.EVENT_MOUSEMOVE and (flags & cv2.EVENT_FLAG_LBUTTON):  # 按住左键拖曳
        cv2.rectangle(img_temp, point1, (x, y), (255, 0, 0), 3)
        cv2.imshow('img', img_temp)
    elif event == cv2.EVENT_LBUTTONUP:  # 左键释放
        point2 = (x, y)
        cv2.rectangle(img_temp, point1, point2, (0, 0, 255), 3)
        cv2.imshow('img', img_temp)
        cv2.imwrite(file_path + 'bbox/' + str(start_num) + '_bbox.jpg', img_temp)
    elif event == cv2.EVENT_RBUTTONDOWN:    #中间键点击保存当前框数据
        param.write(' ' + str(point1[0]) + ' ' + str(point1[1]) + ' ' + str(point2[0]) + ' ' + str(
            point2[1]))
        cv2.imshow('img', img_temp)


def main():
    global img, point1, point2, start_num
    if not os.path.exists(file_path + 'bbox'):
        os.mkdir(file_path + 'bbox')

    file = open(file_path + 'mark.txt', 'w')

    # set start number
    start_num = 47

    while True:
        pic_path = file_path + str(start_num) + '.jpg'
        img = cv2.imread(pic_path)
        if img is None:
            break
        cv2.putText(img, 'pic_' + str(start_num), (60, 40), cv2.FONT_HERSHEY_COMPLEX, 1, green)
        cv2.imshow('img', img)
        file.write(file_path + str(start_num))
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
