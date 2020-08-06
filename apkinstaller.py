# Import of essential Modules
import os
import subprocess
from os.path import isfile, join

# function to clear the terminal screen: Works cross platform


def cls():
    os.system('cls' if os.name == 'nt' else 'clear')

# Function to get the array of names of all files in the user directory


def apk_path(path):
    apk = [f for f in os.listdir(
        path) if isfile(join(path, f))]
    return apk


# Gets the path of the folder containing all teh Apks To be installed
cls()
path = input("please Enter the full path where your apk is located: ")
os.chdir(path)


# This loop checks if the file in folder is really an apk. apk_list variable contains only the array of .apk files
apk_list = []
for i in apk_path(path):
    if ".apk" in i:
        apk_list.append(i)

# get the total number of APK and the initialize the counter
no_of_apk = len(apk_list)
counter = 1


for items in apk_list:
    cls()
    print(f'Installing APK {counter} of {no_of_apk}')  # Makeshift progress bar
    old_name = items
    # This renames the current apk to test.apk as to make the installation easier
    os.rename(items, "test.apk")
    # This installs the created test.apk to android
    subprocess.call("adb install test.apk", shell=True)
    # This renames test.apk back to the original name
    os.rename("test.apk", old_name)
    counter += 1
