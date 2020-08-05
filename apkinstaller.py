from os import listdir, chdir, rename
import subprocess
from os.path import isfile, join


def apk_path(path):
    apks = [f for f in listdir(
        path) if isfile(join(path, f))]
    return apks


path = input("please Enter the full path where your apk is located: ")
chdir(path)


for items in apk_path(path):
    old_name = items
    rename(items, "test.apk")
    subprocess.call(f"adb install {items}", shell=True)
    rename("test.apk", old_name)
