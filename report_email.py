#!/usr/bin/env python3

import os
from datetime import date
import reports

descDirectory = "supplier-data/descriptions/"
today = date.today()
pdfBody = ""

for file in os.listdir(descDirectory):
    if(file.endswith("txt")):
        with open(descDirectory + file) as f:
            readlines = f.readlines()
            name = readlines[0].strip()
            weight = readlines[1].strip()
            pdfBody += "name: " + name + "<br/>" + "weight: " + weight + "<br/><br/>"
            
if __name__ == "__main__":
    title = "Processed Update on " + today
    reports.generate_report("/tmp/processed.pdf", title, pdfBody)

