## LED Matrix Graduation Hat

This repository contains the all the code and images that I used for my graduation hat.

The main objectives with this hat was to:

1. Figure out how to interface the LED Matrix with an Arduino.
2. Being able to load any image you can find onto the hat and have it display the image.
3. Determine how to mount the led matrix onto the graduation cap.


### 1. Interfacing the LED Matrix with an Arduino
I basically just followed this guide from Adafruit when wiring up the Arduino to the LED matrix found [here](https://learn.adafruit.com/32x16-32x32-rgb-led-matrix).

For power, I just used an Anker rechargable battery bank since the LED matrix only needed a 5v connection. Ripped part an old phone charger and soldered positve to the two pins on the LED matrix as well as the Vin on the Arduino. Then I soldered the gnd to the two pins on the LED Matrix and to gnd on the Arduino as well. 

### 2. Loading images onto the LED Matrix

There are a number of methods as a part of the RGBMatrixPanel class for controlling the dispaly on the LED Matrix.

drawPixel(x, y, color)
fillScreen(color)

There are also a number of drawing functions with the Adafruit GFX library, but they aren't used in this project.

I just entirly used drawPixel. This meant that I had to write one line of code for each individual pixel. With a 32x32 matrix, this could be up to 1024 lines of code for each image.

So I created a Python script to automate to process image data and write the Arduino code for me for each image. 
[img_to_code.py](https://github.com/tynimattias/Grad_Hat/blob/main/img_to_code.py)
When prompted for a directory, you just input the directory of the image that you want to turn into Arduino Code. The output will be a text file which will contain the code to output the image onto the LED matrix. 

### 3. Mounting the LED Matrix

The graduation hat was just a piece of black cloth using a piece of cardboard to shape it. I just ripped off the black cloth so that I could place the LED matrix in bwetween the cloth and the cardboard, cutting out squares so that I could run the wires through the cardboard. 

![PXL_20220621_183935922](https://user-images.githubusercontent.com/72426180/174879206-59fd999e-c040-4ba6-8fbb-ecffd3b23483.jpg)
![PXL_20220621_183944598](https://user-images.githubusercontent.com/72426180/174879211-8bd0f718-3543-46bf-afed-20fa9fa452a0.jpg)

Next, I placed the black cloth back over the led matrix and hot glued the cloth back onto the cardboard. I had the cable I used for power run out of the back of the hat and the Arduino connections run out of the bottem of the hat. The Arduino itself was then hot glued onto the bottem of the hat. 
![289427505_581200873370308_3187398874359171170_n](https://user-images.githubusercontent.com/72426180/174871270-4ec561ef-1345-45b4-9ef8-ef5f6d8f602d.jpg)
![288299116_562940185211322_8627938340762050442_n](https://user-images.githubusercontent.com/72426180/174871277-fbfb332a-9db8-4068-b3cf-f09dfe72f364.jpg)




![IMG_1790](https://user-images.githubusercontent.com/72426180/174871050-f041e3fa-410e-4e5e-ac14-a3336185264c.jpg)
![IMG_1789](https://user-images.githubusercontent.com/72426180/174871075-a62dbe8d-1580-4108-8e48-304804f8a4a9.jpg)
![IMG_1792](https://user-images.githubusercontent.com/72426180/174871084-67f9e57d-4923-4d13-9ee7-d3465dfad496.jpg)
