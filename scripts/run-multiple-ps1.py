# DESCRIPTION:
# This script shows how to execute multiple Powershell .ps1 script files
# from a single Python script.
# 
#
# USAGE: 
# Run this script to execute multiple (.ps1) powershell scripts which are both
# located in the same directory as this python script.
# In this example, the Powershell script files should be in the same
# directory as the Python script, but the script can be altered
# to point to the full path of the .ps1 files in another directory
#
# DEPENDENCIES:
# Python 3.5+
# Powershell 5.0+
# [Additional dependencies here]

import subprocess

# This script block can be used to run multiple Powershell scripts from inside
# a python script.

def run_ps_script(filename):
    subprocess.run(["C:/Windows/system32/WindowsPowerShell/v1.0/powershell.exe", 
    filename], shell=False)
    
run_ps_script("./test_script1.ps1")
run_ps_script("./test_script2.ps1")
run_ps_script("./test_script3.ps1")

# NOTES, TROUBLESHOOTING, AND OTHER INFO

# Example text from a .ps1 script called in this example:
#
#       Get-Help Get-Help | Out-File help.txt
#       Get-Help Get-Alias | Out-File alias.txt
#       Get-Help Set-Fileshare | Out-File fileshare.txt
#
# This script just gets help listings for various Powershell cmdlets
# and dumps the output into text files.
#
# The text can be replaced with any valid Powershell script.