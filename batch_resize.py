from PIL import Image
import os, sys

path = "path to folder containing images to be resized"
dirs = os.listdir( path )
out = "path to where resized images need to be stored"
def resize():
    for item in dirs:
        if os.path.isfile(path+item):
            im = Image.open(path+item)
            f, e = os.path.splitext(path+item)
            imResize = im.resize((224,224), Image.ANTIALIAS)#Here the input image gets resized to 224x224
            imResize.save(out+item, 'JPEG', quality=90)

resize()
