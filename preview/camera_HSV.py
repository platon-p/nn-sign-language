import cv2
import numpy


def read_values_from_file(filename):
    file = open(filename, 'r')
    values_split = file.read().split(',')
    for number in range(6):
        values_split[number] = int(values_split[number])
    file.close()
    return values_split


def create_window():
    cv2.namedWindow('window_HSV')
    cv2.resizeWindow('window_HSV', 400, 300)
    cv2.createTrackbar('H_up', 'window_HSV', H_up, 255, print)
    cv2.createTrackbar('H_down', 'window_HSV', H_down, 255, print)
    cv2.createTrackbar('S_up', 'window_HSV', S_up, 255, print)
    cv2.createTrackbar('S_down', 'window_HSV', S_down, 255, print)
    cv2.createTrackbar('V_up', 'window_HSV', V_up, 255, print)
    cv2.createTrackbar('V_down', 'window_HSV', V_down, 255, print)

    #cv2.namedWindow('window_grey')
    #cv2.resizeWindow('window_grey', 400, 300)
    #cv2.createTrackbar('H_up', 'window_grey', up, 255, print)
    #cv2.createTrackbar('H_down', 'window_grey', down, 255, print)


H_up, H_down, S_up, S_down, V_up, V_down = read_values_from_file('HSV.txt')

create_window()


def get_sliders():
    H_up = cv2.getTrackbarPos('H_up', 'window_HSV')
    H_down = cv2.getTrackbarPos('H_down', 'window_HSV')
    S_up = cv2.getTrackbarPos('S_up', 'window_HSV')
    S_down = cv2.getTrackbarPos('S_down', 'window_HSV')
    V_up = cv2.getTrackbarPos('V_up', 'window_HSV')
    V_down = cv2.getTrackbarPos('V_down', 'window_HSV')
    return H_up, H_down, S_up, S_down, V_up, V_down

    #H_up = cv2.getTrackbarPos('H_up', 'window_grey')
    #H_down = cv2.getTrackbarPos('H_down', 'window_grey')
    #return H_up, H_down


def write_grey_values(filename):
    file = open(filename, 'w')
    file.write(str(H_up))
    file.write(',')
    file.write(str(H_down))
    file.write(',')
    file.write(str(S_up))
    file.write(',')
    file.write(str(S_down))
    file.write(',')
    file.write(str(V_up))
    file.write(',')
    file.write(str(V_down))
    file.close()


cap = cv2.VideoCapture(0)
key = -1
while key == -1:
    imread, image = cap.read()
    image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV_FULL)
    image = image[40:440, 120:520]
    H_up, H_down, S_up, S_down, V_up, V_down =get_sliders()
    up = [H_up, S_up, V_up]
    down = [H_down, S_down, V_down]
    nu_up = numpy.array(up)
    nu_down = numpy.array(down)
    image_mask = cv2.inRange(image, nu_down, nu_up)
    image = cv2.cvtColor(cv2.cvtColor(image, cv2.COLOR_HSV2BGR), cv2.COLOR_BGR2GRAY)
    image_mask_and = cv2.bitwise_and(image, image_mask)
    write_grey_values('HSV.txt')

    image_mask_and_resize = cv2.resize(image_mask_and, (40, 40))
    cv2.imwrite('photo_HSV.jpg', image_mask_and_resize)

    cv2.imshow('win1', image_mask_and)
    key = cv2.waitKey(100)
cap.release()
