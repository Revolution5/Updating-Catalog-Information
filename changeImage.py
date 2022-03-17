#!/usr/bin/env python3

from PIL import Image
import os

imageDirectory = "/supplier-data/images/"

for image in os.listdir(imageDirectory):
        im = Image.open(imageDirectory + image)
