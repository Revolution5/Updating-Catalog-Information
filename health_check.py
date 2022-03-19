#!/usr/bin/env python3

import shutil
import psutil
import emails
import socket

sender = "automation@example.com"
#actual username is given by the lab
recipient = "student-03-c0a812fad5f8@example.com"
body = "Please check your system and resolve the issue as soon as possible"

cpu = psutil.cpu_percent(1)
disk = shutil.disk_usage("/")
memory = psutil.virtual_memory()
localhost = socket.gethostbyname(socket.gethostname())

if cpu > 80:
    error = emails.generate_error_report(sender, recipient, "Error - CPU usage is over 80%", body)
    emails.send_email(error)

if (disk.used / disk.total * 100) < 20:
    error = emails.generate_error_report(sender, recipient, "Error - Available disk space is less than 20%", body)
    emails.send_email(error)

if (memory.available / 1024 ** 2) < 500:
    error = emails.generate_error_report(sender, recipient, "Error - Available memory is less than 500MB", body)
    emails.send_email(error)

if (localhost != "127.0.0.1"):
    error = emails.generate_error_report(sender, recipient, "Error - localhost cannot be resolved to 127.0.0.1", body)
    emails.send_email(error)
