# Import of essential Modules
from importlib.resources import path
import os
import subprocess
import sys

# Get the path from the user


# function to clear the terminal screen: Works cross-platform
def cls():
    os.system('cls' if os.name == 'nt' else 'clear')


# Function to get the array of names of all files in the user directory
def apk_path(path):
    apk = [f for f in os.listdir(
        path) if os.path.isfile(os.path.join(path, f))]
    return apk


# Gets the path of the folder containing all teh Apks To be installed
cls()
if len(sys.argv) != 2:
    path = input("Please Enter the path of APK files")
else:
    path = sys.argv[1]
os.chdir(path)


# This loop checks if the file in folder is really an apk. apk_list variable contains only the array of .apk files
apk_list = []
for i in apk_path(path):
    if ".apk" in i:
        apk_list.append(i)

# get the total number of APK and initialize the counter
no_of_apk = len(apk_list)
counter = 1


for items in apk_list:
    # cls()
    old_name = items
    # This renames the current apk to test.apk as to make the installation easier
    # Makeshift progress bar
    print(f'Installing {old_name}.apk: {counter} of {no_of_apk}')
    os.rename(items, "test.apk")
    # This installs the created test.apk to android
    subprocess.call("adb install test.apk", shell=True)
    # This renames test.apk back to the original name
    os.rename("test.apk", old_name)
    counter += 1
