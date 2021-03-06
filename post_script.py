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
    print("")
    print("###############################################################")
    print("")
    print("Package Versions:")
    print("")
    os.system("rpm -q expat")
    os.system("rpm -q python-pillow")
    os.system("rpm -q libtiff")
    os.system("rpm -q gzip")
    os.system("rpm -q cyrus-sasl")
    os.system("rpm -q zlib")
    os.system("rpm -q vim")
    os.system("rpm -q grub2")
    os.system("rpm -q gcc10")
    os.system("rpm -q openldap")
    os.system("rpm -q openssl")
    os.system("rpm -q microcode_ctl")
    os.system("rpm -q containerd")
 

host_details()
