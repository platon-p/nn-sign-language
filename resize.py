from PIL import Image
from os import listdir

w, h = 40, 40


def resize(image_name):
    # resizing all images and convert to grayscale
    img = Image.open('./resize_images/' + image_name)
    img = img.resize((w, h), Image.ANTIALIAS)
    img = img.convert('L')
    img.save('./converted/' + image_name)


if __name__ == '__main__':
    for digit_folder in listdir('./resize_images/'):
        for image_file in listdir('./resize_images/' + digit_folder):
            resize(digit_folder + '/' + image_file)
            print('Resized ' + image_file)
