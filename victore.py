#!/usr/bin/env python3
#
# victore - Renames files for Ms. Victore's 3D Modeling Class 
#

import os
import configparser
import shutil
import string

print("Reading victore_cfg.txt for configuration...")

config = configparser.ConfigParser()
config.read(os.path.expanduser('victore_cfg.txt'))

Settings = config['Victore']
oldDocDir = Settings['newDocDir']
newDocDir1 = Settings['oldDocDir']
firstName = Settings['firstName'].capitalize()
lastName = Settings['lastName'].upper()
className = Settings['className']

newDocDir2 = newDocDir1 + firstName + "_" + lastName + "_" + className

print ("Creating directory if not already existing.")
if os.path.isdir(newDocDir2):
    print ("Directory exists already")
else:
    print ("Directory does not exist, creating")
    os.mkdir(newDocDir2)

print("First name: " + firstName)
print("Last name: " + lastName)
print("Files to be converted are in: " + oldDocDir)
print("Files after conversion are in: " + newDocDir2)
print("Preparing to fix files...")

for fileName in os.listdir(oldDocDir):
        oldName = oldDocDir + "/" + fileName
        newName = newDocDir2 + "/"  + lastName + "_" + fileName

        print(oldName + " -> " + newName)
        shutil.copyfile(oldName, newName)

		
