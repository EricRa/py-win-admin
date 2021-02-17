# DESCRIPTION:
# This script shows how to execute a Powershell .ps1 script file
# from a Python script
# 
#
# USAGE: 
# Run this script to execute a powershell cmdlet in the current directory.
# In this example, the Powershell script file should be in the same
# directory as the Python script, but the script can be easily altered
# to point to the full path of the .ps1 file in another directory
#
# DEPENDENCIES:
# Python 3.5+
# Powershell 5.0+
# [Additional dependencies here]

import subprocess

# This script block can be used to run a Powershell script from inside
# a python script.

def run_ps1():
    subprocess.run(["./test_script.ps1"], shell=False)
        
        
# NOTES, TROUBLESHOOTING, AND OTHER INFO

# The full text of test_script.ps1 in this example is the following:
#
#       Get-Help Get-Help | Out-File help.txt
#       Get-Help Get-Alias | Out-File alias.txt
#       Get-Help Set-Fileshare | Out-File fileshare.txt
#
# This script just gets help listings for various Powershell cmdlets
# and dumps the output into text files.
#
# The text can be replaced with any valid Powershell script.


# old code:
# "C:/Windows/system32/WindowsPowerShell/v1.0/powershell.exe"