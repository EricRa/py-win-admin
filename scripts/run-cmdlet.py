# DESCRIPTION:
# This script uses Python to run a Powershell cmdlet.  
# There is obviously no reason to use this in isolation instead of just
# running the cmdlet directly, but I am using this as a template to build
# up boilerplate code for more complex scripts.
# 
# In the example below, we are running the Get-Command cmdlet with an argument
# to list all available powershell cmdlets.
#
# USAGE: 
# Run this script to execute a powershell cmdlet in the current directory.
# You can replace the "Get-Command" cmdlet in the script below with any other
# and include each argument as a separate string"
# 
# DEPENDENCIES:
# Python 3.5+
# Powershell 5.0+

import subprocess

# Reusable code block for running a powershell cmdlet from a python script
def run_cmdlet():
    subprocess.run(["C:/Windows/system32/WindowsPowerShell/v1.0/powershell.exe", "Get-Command", "-CommandType", "Cmdlet"], shell=False)

run_cmdlet()
 
# NOTES, TROUBLESHOOTING, AND OTHER INFO
# 
# Be sure the path in the first argument of subprocess.run points to your
# Powershell executable.
#
# Be sure to add each argument or string as a separate python string in quotes.
# This is necessary since we are running all scripts with shell=False for
# security reasons.  To learn more about this, see the Python docs here:
# https://docs.python.org/3.9/library/subprocess.html#security-considerations