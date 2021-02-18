# DESCRIPTION:
# This script shows how get output from a Powershell cmdlet or
# script and save that output as a python object.
# 
#
# USAGE: 
# Run the python script from the command line, ensuring that whatever
# data you want to manipulate using Powershell is included in the same
# directory (or use full paths in your script)
#
# DEPENDENCIES:
# Python 3.5+
# Powershell 5.0+
# 

import subprocess

output_list = []

# Script block used to run a Powershell cmdlet or script and save the 
# Powershell output to a Python object.
def run_powershell():
    data = subprocess.run(["C:/Windows/system32/WindowsPowerShell/v1.0/powershell.exe", "Get-Help", "Get-Command"], shell=False, capture_output=True)
    
    return(data)
    
output_list.append(run_powershell())
print(output_list)

        
# NOTES, TROUBLESHOOTING, AND OTHER INFO
# 
# For the purposes of this script, we are not worrying about formatting
# the output.  As you can see from the printed list, the output is 
# mostly ugly and unusable in the current format, but we have managed
# to easily capture it into a Python list.