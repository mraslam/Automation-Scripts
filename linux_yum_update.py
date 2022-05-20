#!/usr/bin/python3 -u

import os

os.system("sudo yum update kernel -y")
os.system("sudo yum upgrade kernel -y")
os.system("sudo yum update -y")
os.system("shutdown -r now")
