#!/usr/bin/env python3

from PIL import Image
import os

imageDirectory = "supplier-data/images/"

for image in os.listdir(imageDirectory):
        #example directory contains images with .tiff extension
        if (image.endswith(".tiff")):
            im = Image.open(imageDirectory + image)
            imSplit = image.split(".")
            imNew = imSplit[0] + ".jpeg"
            #resize image to 600x400, convert image to RGB from RGBA, save as a .JPEG
            im.resize((600,400))
            im.convert("RGB")
            im.save(imageDirectory + imNew, "JPEG")
