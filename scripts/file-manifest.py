# DESCRIPTION:
# This script gets all file and directory names in the current directory
# and all subdirectories recursively and saves them to a text file
#
# USAGE: 
# Run this script in the root directory where you want the manifest to begin
#
# DEPENDENCIES:
# Python 3.5+
# Powershell 5.0+

import os

# Reusable code block for getting a recursive file and directory listing from
# the current directory and saving the items in a python list object
file_list = []
for root, dirs, files in os.walk(".", topdown=False):
    for name in files:
        file_list.append(os.path.join(root, name))
    for name in dirs:
        file_list.append(os.path.join(root, name))
 
 
# Reusable code block for outputing a python list object to a text file 
# with a single item on each new line
with open("file_manifest.txt", "w") as output_file:
    for file in file_list:
        output_file.write(file)
        output_file.write("\n")

        
# NOTES, TROUBLESHOOTING, AND OTHER INFO
# 