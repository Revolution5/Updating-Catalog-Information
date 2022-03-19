#!/usr/bin/env python3

import os
from datetime import date
import reports
import emails

descDirectory = "supplier-data/descriptions/"
today = date.today().strftime('%Y-%m-%d')
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
    #actual username is given by the lab
    message = emails.generate_email("automation@example.com", "username@example.com", "Upload Completed - Online Fruit Store", 
    "All fruits are uploaded to our website successfully. A detailed list is attached to this email.", "/tmp/processed.pdf")
    emails.send_email(message)


