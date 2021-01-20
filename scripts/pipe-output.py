# DESCRIPTION:
# This script shows how to pipe the output of a powershell command
# to a text file using a python script
# 
# In the example below, we are using the Get-Alias cmdlet which shows all
# aliases for available powershell cmdlets (including user-defined ones).
#
# We then use the Out-File cmdlet to pipe the output to a text file.
# Since we are not changing the format of the output in this case, it is
# simpler to let Powershell handle the piping without having to use Python
# to interact with files.
#
# USAGE: 
# Run this script to execute a powershell cmdlet in the current directory.
# Can replace Get-Alias with any other powershell cmdlet
# Can pipe output to whatever file you want.  With some modifications, can pipe
# output to different formats such as json or csv.
# We will take a look at doing that using the python standard library in
# later scripts.
# 
# DEPENDENCIES:
# Python 3.5+
# Powershell 5.0+

import subprocess

# Reusable code block for running a powershell cmdlet and piping output
# out to a text file (letting Powershell handle the file output)
def pipe_output():
    subprocess.run(["C:/Windows/system32/WindowsPowerShell/v1.0/powershell.exe", "Get-Alias", "|", "Out-File", "output.txt"], shell=False)

pipe_output()
 
# NOTES, TROUBLESHOOTING, AND OTHER INFO
# 
