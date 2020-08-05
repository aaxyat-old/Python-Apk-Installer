# Python Apk Installer
This is a simple python script to install APK Files in given directory to your android phone.
### Requirements
* ADB

### How to use?
Put all your apk files in /home/[User]/Downloads/Apks. Make sure your apk files donot contain any special charactes. And run the script.

### Limitations:
* ~~ Currently this only works on linux ~~ Added a botched windows implimentation.
* This program uses absolute path so you'll need to edit the script to change the filename or username.
* Currently it is too buggy. I haven't tested it extensively.
  
### Todo List:
- [X] Add Windows Support (a littly dodgy).
- [ ] Add an interactive interface to choose the folder containing apks.
- [ ] Test for bugs.
- [ ] Remove the need for end user to touch the script at all.

### Known Bug:
If you try installing apk with special charaters and any non English character the program will break.

## Bug report:
 #### If you came across any bug, please report them as issues. Any pull request will be greatly appriciated.
