from os import listdir, chdir
import subprocess
from os.path import isfile, join
onlyfiles = [f for f in listdir(
    "/home/aaxyat/Downloads/Apks") if isfile(join("/home/aaxyat/Downloads/Apks", f))]
chdir("/home/aaxyat/Downloads/Apks")
for i in onlyfiles:
    subprocess.call(f"adb install {i}", shell=True)
