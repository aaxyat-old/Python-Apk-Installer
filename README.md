# Python Apk Installer
This is a simple python script to install APK Files in given directory to your android phone.
### Requirements
* [ADB](https://developer.android.com/studio/releases/platform-tools)
* [Python](https://www.python.org) (version 3.6 or higher)
* An android phone with USB debugging enabled

### Installation:
* Download python
* Download apkinstaller.py from [Release](https://github.com/aaxyat/Python-Apk-Installer/releases) or clone this repository with `git clone https://github.com/aaxyat/Python-Apk-Installer.git`
* Download ADB and put apkinstaller.py in the directory containing ADB files.
* Open your command terminal and navigate to the folder containing apkinstaller.py
* run the command `python apkinstaller.py <Path To APK Files>` (in linux use `python3 apkinstaller.py <Path To APK Files>`)

### Limitations:
* ~~Currently, this only works on linux~~ Added a botched windows implementation.
* ~~This program uses absolute path. So, you'll need to edit the script to change the filename or username.~~ Now uses the path given by user.
* ~~Currently, it is too buggy. I haven't tested it extensively.~~ Removed as many bugs as I could find.
  
### Todo List:
- [X] Add Windows Support :heavy_check_mark:
- [X] Add an interactive interface to choose the folder containing APKs. :heavy_check_mark:
- [X] Test for bugs. :heavy_check_mark:
- [X] Remove the need for end user to touch the script at all. :heavy_check_mark:
- [X] Error Handling. :heavy_check_mark:

### Known Bug:
~~If you try installing apk with special characters and any non-English character the program will break.~~ (Fixed)

## Bug report:
 This script was only tested in Arch linux. I have no idea how this script functions in Mac or Windows.
 #### If you came across any bug, please report them as issues. Any pull request will be greatly appreciated.

