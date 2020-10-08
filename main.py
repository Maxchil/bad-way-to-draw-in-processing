import webbrowser
import os
try:
    from PIL import Image
except:
    print("installing pillow")
    os.system('python -m pip install pillow')

from PIL import Image

Print = False
sizex = 60
sizey = 60
pix = 0

newsize = (sizex, sizey)
file = open("code.txt", "w")
file.truncate(0)
im = Image.open(r"full path to image")# MUST CHANGE PATH
im = im.resize(newsize)#resizes to 500 by 500

file.write("void setup() {\n")
file.write("size(" + str(sizex) + ", " + str(sizey) + ");\n")
file.write("background(255);\n")
file.write("}\n")
for i in range(3):
    file.write("\n")
file.write("void draw() {\n")

rgb = im.getpixel((2, 2))


for y in range(sizey):
    for x in range(sizex):

        rgb = im.getpixel((x, y))
        file.write("stroke(" + str(rgb[0]) + ", " + str(rgb[1]) + ", " + str(rgb[2]) + ");" + "\n")
        file.write("point(" + str(x) + ", " + str(y) + ");" + "\n")
        if Print == True:
            pix = pix + 1
            print("pixel: " + str(pix))
file.write("}\n")
webbrowser.open("code.txt")
file.close()