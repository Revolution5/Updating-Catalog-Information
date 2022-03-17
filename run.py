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

                #converts weight string to an integer, will always be the 2nd line in the txt files
                if keycount == 1:
                    weightToInt = value.strip(" ")
                    dict[keys[keycount]] = int(weightToInt[0:3]) #only works if the weight is 3 digits, need to find something else...
                else:
                    dict[keys[keycount]] = value
                keycount+=1
                
            print(dict)
            print("\n")