from random import randint

import cv2
import numpy

from predict import predict_image


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
    cv2.createTrackbar('FPS', 'window_HSV', 0, 10, print)


H_up, H_down, S_up, S_down, V_up, V_down = read_values_from_file('.HSV')

create_window()


def get_sliders():
    H_up = cv2.getTrackbarPos('H_up', 'window_HSV')
    H_down = cv2.getTrackbarPos('H_down', 'window_HSV')
    S_up = cv2.getTrackbarPos('S_up', 'window_HSV')
    S_down = cv2.getTrackbarPos('S_down', 'window_HSV')
    V_up = cv2.getTrackbarPos('V_up', 'window_HSV')
    V_down = cv2.getTrackbarPos('V_down', 'window_HSV')
    FPS = cv2.getTrackbarPos('FPS', 'window_HSV')
    return H_up, H_down, S_up, S_down, V_up, V_down, FPS


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
    image = image[40:440, 120:520]
    image = cv2.flip(image, 1)
    image_original = image
    image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV_FULL)
    H_up, H_down, S_up, S_down, V_up, V_down, FPS = get_sliders()
    up = [H_up, S_up, V_up]
    down = [H_down, S_down, V_down]
    nu_up = numpy.array(up)
    nu_down = numpy.array(down)
    image_mask = cv2.inRange(image, nu_down, nu_up)
    image_gray = cv2.cvtColor(cv2.cvtColor(image, cv2.COLOR_HSV2BGR), cv2.COLOR_BGR2GRAY)
    image_mask_and = cv2.bitwise_and(image_gray, image_mask)
    write_grey_values('.HSV')

    image_mask_and_resize = cv2.resize(image_mask_and, (40, 40))

    cv2.imwrite('photo_HSV.jpg', cv2.flip(image_mask_and_resize, 1))

    number = str(predict_image('photo_HSV.jpg'))
    cv2.rectangle(image_original, (0, 0), (40, 40), (127, 127, 127), -1)
    cv2.putText(image_original, number, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 5)
    cv2.imshow('win1', image_original)
    cv2.imshow('win2', image_mask_and)
    key = cv2.waitKey(20 + FPS * 20)
cap.release()
