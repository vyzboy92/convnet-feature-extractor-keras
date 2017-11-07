from PIL import Image
import os, sys

path = "/home/vysakh/My Files/Mini Project/AlexNet-Experiments-Keras-master/DATA/Test/Vehicle/"
dirs = os.listdir( path )
out = "/home/vysakh/Documents/DATA/Test/Vehicle/"
def resize():
    for item in dirs:
        if os.path.isfile(path+item):
            im = Image.open(path+item)
            f, e = os.path.splitext(path+item)
            imResize = im.resize((224,224), Image.ANTIALIAS)
            imResize.save(out+item, 'JPEG', quality=90)

resize()
