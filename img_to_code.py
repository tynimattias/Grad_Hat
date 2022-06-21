import matplotlib.pyplot as plt
from PIL import Image
import numpy as np

def photo2pixelart(image, i_size, o_size):
    """
    image: path to image file
    i_size: size of the small image eg:(8,8)
    o_size: output size eg:(10000,10000)
    """
    #read file
    img=Image.open(image)

    #convert to small image
    small_img=img.resize(i_size,Image.BILINEAR)

    #resize to output size
    res=small_img.resize(img.size, Image.NEAREST)

    #Save output image
    filename=f'mario_{i_size[0]}x{i_size[1]}.png'
    res.save(filename)

    #Display images side by side
    plt.figure(figsize=(16,10))
    #original image
    plt.subplot(1,2,1)
    plt.title('Original image', size=18)
    plt.imshow(img)   #display image
    plt.axis('off')   #hide axis
    #pixel art
    plt.subplot(1,2,2)
    plt.title(f'Pixel Art {i_size[0]}x{i_size[1]}', size=18)
    plt.imshow(res)
    plt.axis('off')
    plt.show()

wizard = 'Hat/Music_note_2.png'

im = Image.open(wizard)
im = im.resize((32,32))
print(im)
plt.imshow(im)
plt.show()
im = im.convert("RGB")
pix_value = list(im.getdata())
print(pix_value)

pixel_rows = np.zeros((32,32,3))

count = 0

file_object = open("Hat/Music_note_2.txt", "w")

for i in range(32):
    for j in range(32):
        for k in range(3):
            pixel_rows[i][j][k] = pix_value[count][k]
        print(f'matrix.draw_Pixel({i},{j}, matrix.ColorHSV({pix_value[count]}),)')
        file_object.write(f'matrix.drawPixel({i},{j}, matrix.Color888({pix_value[count][0]},{pix_value[count][1]},{pix_value[count][2]},true));\n')
        count+=1

file_object.close()
#print(pixel_rows)
