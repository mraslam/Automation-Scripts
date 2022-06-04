import subprocess
import sys
import os

#use paramiko
#use try exception
def patch_debian_system():
    pass

def patch_fedora_system():
    os.system("sudo yum update kernel -y")
    os.system("sudo yum upgrade kernel -y")
    os.system("sudo yum update -y")
    os.system("sudo shutdown -r now")

def find_operating_system():
    temp = subprocess.Popen(['cat', '/etc/os-release'], stdout = subprocess.PIPE)
    output = str(temp.communicate())
    if output.find('Ubuntu'):
        print("patching debian os")
        patch_debian_system()
    elif output.find('Amazon Linux') or output.find('CentOS Linux"'):
        print("patching centos os")
        patch_fedora_system()
  


if sys.platform == 'linux':
    find_operating_system()
elif sys.platform in ['win32', 'cygwin']:
    print("Host is a Windows System, please run a powershell script to update the system.")
else:
    print("Unknown Operating System. Please check again and try again.")



