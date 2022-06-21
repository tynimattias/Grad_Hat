import matplotlib.pyplot as plt
from PIL import Image
import numpy as np


wizard = 'Hat/Music_note_2.png'

#Open image and store to im
im = Image.open(wizard)
#Resize image for 32x32 image
im = im.resize((32,32))

#Show image to make sure it looks somewhat okay
plt.imshow(im)
plt.show()

#Convert image data to RGB data for each pixel
im = im.convert("RGB")
pix_value = list(im.getdata())


pixel_rows = np.zeros((32,32,3))

count = 0

#Open a text file that we're going to write all of the C code to so you can copy paste to the Arduino program
file_object = open("Hat/Music_note_2.txt", "w")

#These loops create C code in the form: matrix.drawPixel(x, y, color); where color is matrix.Color888(R, G, B)
#For each pixel, there is an RGB component associated with it so we have to write one line of code for each pixel.
for i in range(32):
    for j in range(32):
        for k in range(3):
            pixel_rows[i][j][k] = pix_value[count][k]
        print(f'matrix.draw_Pixel({i},{j}, matrix.ColorHSV({pix_value[count]}),)')
        file_object.write(f'matrix.drawPixel({i},{j}, matrix.Color888({pix_value[count][0]},{pix_value[count][1]},{pix_value[count][2]},true));\n')
        count+=1

file_object.close()

