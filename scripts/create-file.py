# DESCRIPTION:
# This script creates new files in the current directory using Powershell
# 
#
# USAGE: 
# Run the script in the directory where you want the new files to exist
#
# DEPENDENCIES:
# Python 3.5+
# Powershell 5.0+
# 

import subprocess

# Script block to create new files using Powershell cmdlets
        
def create_files():
    data = subprocess.run(["C:/Windows/system32/WindowsPowerShell/v1.0/powershell.exe", "New-Item", "'testfile A.txt',", "'testfile B.txt',", "'testfile C.txt'"], shell=False)

create_files()
print("Operation complete.  New files have been created.")

# NOTES, TROUBLESHOOTING, AND OTHER INFO
#
# Again, this is a pretty trivial example of running Powershell cmdlets
# within a Python script, but we are slowly building up short, useful code
# blocks to extend into more useful tasks.
# 
# We could also replace the hard-coded cmdlets with variables to generalize
# the function.  This introduces some problems, though, so we will address
# those in another script.
#
# Note that single quotes were added inside of the double quotes for each new
# file added.  This allows us to use spaces within the new file filenames 
# without breaking the script.  If no spaces are used within filenames, the 
# single quotes can be omitted.  Ensure that the trailing comma at the end of
# each filename is inside of the double quotes but outside of the single
# quotes.