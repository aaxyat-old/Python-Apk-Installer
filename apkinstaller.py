from os import listdir, chdir
import subprocess
from os.path import isfile, join


def apk_path(path):
    apks = [f for f in listdir(
        path) if isfile(join(path, f))]
    return apks


path = input("please Enter the full path where your apk is located: ")
chdir(path)


for items in apk_path(path):
    subprocess.call(f"adb install {items}", shell=True)
