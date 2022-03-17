#! /usr/bin/env python3

import os
import requests

descDirectory = "supplier-data/descriptions/"
keys = ["name", "weight", "description", "image_name"]

#loop thru the directory
for file in os.listdir(descDirectory):
    if (file.endswith("txt")):
        dict = {}
        keycount = 0
        #open the file
        with open(descDirectory + file) as f:
            #iterate thru each line in the file
            for line in f:
                value = line.strip()
                #add each line to the corresponding key in the dict,
                #should have same order in txt file as the keys list
                dict[keys[keycount]] = value
                keycount+=1