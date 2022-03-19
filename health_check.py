#!/usr/bin/env python3

import shutil
import psutil
import emails

cpu = psutil.cpu_percent(1)

if cpu > 80:
    emails.generate_error_report("automation@example.com", "username@example.com", "Error = CPU usage is over 80%", 
    "Please check your system and resolve the issue as soon as possible")