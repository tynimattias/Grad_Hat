import matplotlib.pyplot as plt
from PIL import Image
import numpy as np


#Opens an image with a given directory
#Resizes that image
#Opens a text file
#Writes C++ code for Arduino into that text file

image = str(input("Image path: "))

im = Image.open(image)
im = im.resize((32,32))

plt.imshow(im)
plt.show()
im = im.convert("RGB")
pix_value = list(im.getdata())


pixel_values = np.zeros((32,32,3))

count = 0

file_object = open(image + '.txt' , "w")

for i in range(32):
    for j in range(32):
        for k in range(3):
            pixel_values[i][j][k] = pix_value[count][k]
        file_object.write(f'matrix.drawPixel({i},{j}, matrix.Color888({pix_value[count][0]},{pix_value[count][1]},{pix_value[count][2]},true));\n')
        count+=1

file_object.close()

