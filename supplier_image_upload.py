#!/usr/bin/env python3
import requests
import os

imageDirectory = "supplier-data/images/"
url = "http://localhost/upload/" #ip address is given by the lab

#loops thru directory and uploads jpegs to test server
for image in os.listdir(imageDirectory):
    if (image.endswith("jpeg")):
        with open(imageDirectory + image, "rb") as opened:
            r = requests.post(url, files={"file": opened})

