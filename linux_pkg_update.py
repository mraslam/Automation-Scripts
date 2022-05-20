import os

def host_details():
    print("###############################################################")
    print("")
    print("Current Date:")
    os.system("date")
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


def list_packages(status, *args):
    print("###############################################################")
    print("")
    print(f"Package Versions {status} Update:")
    print("")

    for arg in args:
        os.system(f"rpm -qa | grep -i {arg}")

    print("")
    print("###############################################################")
    print("")

def update_packages(*args):
    for arg in args:
        os.system(f"sudo yum update -y {arg}")
    print("")

host_details()
list_packages("Before", "vim")
print("Update in Progress.....")
print("")
update_packages("vim")
list_packages("After", "vim")
