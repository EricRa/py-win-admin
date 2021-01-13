"""
*************FIRST DRAFT OF THIS SCRIPT**********
*************STILL TESTING/REFINING**************
*************DO NOT USE YET**********************

To Do List:

- Clean up output list before writing to file.
    - possibly dump to JSON or another format?
- Comment code to highlight customizable options
- Shorten code line lengths where possible
"""

# This script gets the SHA-256 hash for every file in the
# current directory and all subdirectories recursively
# and exports those values to a new text file

import os
import subprocess
from subprocess import PIPE

def filehash(input_list):
    for file in input_list:
        file = "\"" + file + "\""
        hash_values.append("New Record: ")
        hash_values.append(subprocess.run(["C:/Windows/system32/WindowsPowerShell/v1.0/powershell.exe", "Get-FileHash", file, "|", "Format-List"], shell=False, stdout=PIPE, stderr=PIPE))
        
file_list = []
hash_values = []

for root, dirs, files in os.walk(".", topdown=False):
    for name in files:
        file_list.append(os.path.join(root, name))
    for name in dirs:
        file_list.append(os.path.join(root, name))

filehash(file_list)

with open("filehashes.txt", "w") as hashfile:
    for item in hash_values:
        hashfile.write("%s\n" % item)
        hashfile.write("\n")




"""
******Possible code to reuse later*********
******Delete from finished script**********

subprocess.run(["C:/Windows/system32/WindowsPowerShell/v1.0/powershell.exe", "Get-FileHash", file, "|", "Format-List", "|", "Out-File " "-Append", "filehash_output.txt"], shell=False)
"""