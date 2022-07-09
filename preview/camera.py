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
    cv2.namedWindow('window_BGR')
    cv2.resizeWindow('window_BGR', 400, 300)
    cv2.createTrackbar('B_up', 'window_BGR', B_up, 255, print)
    cv2.createTrackbar('B_down', 'window_BGR', B_down, 255, print)
    cv2.createTrackbar('G_up', 'window_BGR', G_up, 255, print)
    cv2.createTrackbar('G_down', 'window_BGR', G_down, 255, print)
    cv2.createTrackbar('R_up', 'window_BGR', R_up, 255, print)
    cv2.createTrackbar('R_down', 'window_BGR', R_down, 255, print)

    #cv2.namedWindow('window_grey')
    #cv2.resizeWindow('window_grey', 400, 300)
    #cv2.createTrackbar('H_up', 'window_grey', up, 255, print)
    #cv2.createTrackbar('H_down', 'window_grey', down, 255, print)


B_up, B_down, G_up, G_down, R_up, R_down = read_values_from_file('RGB.txt')

create_window()


def get_sliders():
    H_up = cv2.getTrackbarPos('B_up', 'window_BGR')
    H_down = cv2.getTrackbarPos('B_down', 'window_BGR')
    S_up = cv2.getTrackbarPos('G_up', 'window_BGR')
    S_down = cv2.getTrackbarPos('G_down', 'window_BGR')
    V_up = cv2.getTrackbarPos('R_up', 'window_BGR')
    V_down = cv2.getTrackbarPos('R_down', 'window_BGR')
    return H_up, H_down, S_up, S_down, V_up, V_down

    #H_up = cv2.getTrackbarPos('H_up', 'window_grey')
    #H_down = cv2.getTrackbarPos('H_down', 'window_grey')
    #return H_up, H_down


def write_grey_values(filename):
    file = open(filename, 'w')
    file.write(str(B_up))
    file.write(',')
    file.write(str(B_down))
    file.write(',')
    file.write(str(G_up))
    file.write(',')
    file.write(str(G_down))
    file.write(',')
    file.write(str(R_up))
    file.write(',')
    file.write(str(R_down))
    file.close()


cap = cv2.VideoCapture(0)
key = -1
while key == -1:
    imread, image = cap.read()
    #image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    image = image[40:440, 120:520]
    B_up, B_down, G_up, G_down, R_up, R_down =get_sliders()
    up = [B_up, G_up, R_up]
    down = [B_down, G_down, R_down]
    nu_up = numpy.array(up)
    nu_down = numpy.array(down)
    image_mask = cv2.inRange(image, nu_down, nu_up)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    image_mask_and = cv2.bitwise_and(image, image_mask)
    write_grey_values('RGB.txt')

    image_mask_and_resize = cv2.resize(image_mask_and, (40, 40))
    cv2.imwrite('photo.jpg', image_mask_and_resize)

    cv2.imshow('win1', image_mask_and)
    key = cv2.waitKey(200)
cap.release()
