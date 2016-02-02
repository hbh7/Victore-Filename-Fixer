#!/usr/bin/env python3
#
# victore - Renames files for Ms. Victore's 3D Modeling Class 
#

import os, configparser, shutil, string, errno, glob

print("Reading victore_cfg.txt for configuration...")

config = configparser.ConfigParser()
config.read(os.path.expanduser('victore_cfg.txt'))

Settings = config['Victore']
<<<<<<< HEAD
newDocDir1 = Settings['newDocDir']
oldDocDir = Settings['oldDocDir']
=======
oldDocDir = Settings['newDocDir']
newDocDir1 = Settings['oldDocDir']
>>>>>>> origin/master
firstName = Settings['firstName'].capitalize()
lastName = Settings['lastName'].upper()
className = Settings['className']
classDirName = Settings['classDirName']

newDocDir2 = firstName + "_" + lastName + "_" + className

print("First name: " + firstName)
print("Last name: " + lastName)
print("Files to be converted are in: " + oldDocDir)
print("Files after conversion are in: " + newDocDir1)
print("Preparing to fix files...")

for dirpath, dirnames, files in os.walk(oldDocDir, topdown=True):
    for dir in dirnames:
        makeDir = os.path.join(dirpath, dir)
        makeDir = makeDir.replace("Harris", classDirName)
        print ("makeDir: ",makeDir)
        if not os.path.isdir(makeDir):
            os.mkdir(makeDir)
    
    for name in files:
        fileName = os.path.join(dirpath, name)
        newName = fileName.replace("Harris", newDocDir2)
        newName = newName.replace(name, (firstName.lower() + "_" + lastName.upper() + "_" + name))
        print(fileName + " -> " + newName)
        
        try:
            shutil.copytree(fileName, newName)
        except OSError as exc:
            if exc.errno == errno.ENOTDIR:
                shutil.copy(fileName, newName)
        else: raise
    print ("")
