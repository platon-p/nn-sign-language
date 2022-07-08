import imp
from PIL import Image
import os
import asyncio


w, h = 40, 40

# resize all images and convert to grayscale

async def resize(image_name):
    img = Image.open('./resize_images/' + image_name)
    img = img.resize((w, h), Image.ANTIALIAS)
    img = img.convert('L')
    img.save('./converted/' + image_name)

'''
./resize_images/
    ./0/
        hand1.jpg
        hand2.jpg
        ...
    ./1/
        hand1.jpg
        hand2.jpg
        ...
    ./2/
        hand1.jpg
        hand2.jpg
        ...
    ...
'''

for digit_folder in os.listdir('./resize_images/'):
    for image_file in os.listdir('./resize_images/' + digit_folder):
        # resize in new thread
        # asyncio.run_coroutine_threadsafe(resize(digit_folder + '/' + image_file), loop)
        asyncio.run(resize(digit_folder + '/' + image_file))
        print('Resized ' + image_file)
