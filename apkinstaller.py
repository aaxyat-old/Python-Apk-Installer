import os
import subprocess
from os.path import isfile, join


def cls():
    os.system('cls' if os.name == 'nt' else 'clear')


def apk_path(path):
    apk = [f for f in os.listdir(
        path) if isfile(join(path, f))]
    return apk


cls()
path = input("please Enter the full path where your apk is located: ")
os.chdir(path)

apk_list = []
for i in apk_path(path):
    if ".apk" in i:
        apk_list.append(i)


no_of_apk = len(apk_list)
counter = 1


for items in apk_list:
    cls()
    print(f'Installing APK {counter} of {no_of_apk}')
    old_name = items
    os.rename(items, "test.apk")
    subprocess.call(f"adb install test.apk", shell=True)
    os.rename("test.apk", old_name)
    counter += 1
