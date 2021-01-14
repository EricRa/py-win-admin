# py-win-admin

## Useful system admin scripts for Windows written in Python and utilizing Powershell cmdlets

### Why use Python instead of Powershell directly for system administration tasks?

In many cases, directly invoking Powershell will be a faster and more direct method of getting a task done.  In general, the simpler the task, the more likely it is that you should directly use Powershell instead.

I have been experimenting using Python when tasks start to get more complex.  For example, you might want to take advantage of:

- Python's control flow tools as a cleaner or more familiar structure than using Powershell script syntax.
- Python's re (regular expressions) module for string matching
- Python's standard library packages to read and write to specific data formats such as csv and json (both of which have their own packages in the Python standard library)
- The ability to incorporate Powershell cmdlets into Python programs to achieve something that would not be possible using Powershell directly  

### Goals for this repo

I would like to eventually build up a small library of scripts starting with very basic tasks and then eventually move on to more complex ones.  The purpose of starting with tasks trival to achieve with Powershell alone is to start accumulating some boilerplate Python code for incorporating Powershell into Python scripts.  

Once we have a standard way of invoking Powershell through Python for various tasks, it will be easier to build up to more complex tasks using this boilerplate code. 

### Script list and info

A list of scripts available in this repo along with descriptions will be kept the script_descriptions.md file in the root repo directory.

### Usage

Each script file will contain a comment section at the top listing:
- Description and purpose
- Usage info
- Additional dependencies needed(if any)



### Dependencies needed for all scripts:

- Python 3.5+ 
    - (Tested with python 3.9, but these should be backward compatible at least this far back)
    - These will generally only use packages from the Python Standard Library.  If any additional python packages are needed, they will be listed in the comments at the top of the script file.
- Powershell 5.0+
    - This version or above comes by default with Windows 10, so this should already be installed.
    - To check your version, open powershell and type:
    > $PSVersionTable.PSVersion
    

    

