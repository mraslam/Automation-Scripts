#!/usr/bin/python3 -u

import os

def host_details():
    print("###############################################################")
    print("")
    print("Current Date:")
    os.system("date")
    print("")
    print("###############################################################")
    print("")
    print("Uptime:")
    os.system("uptime")
    print("")
    print("###############################################################")
    print("")
    print("Kernel Version:")
    os.system("uname -r")
    print("")
    print("###############################################################")
    print("")
    print("Network Configuration:")
    print("")
    os.system("ifconfig")

host_details()
