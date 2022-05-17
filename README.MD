# Filma Bem Tool
This tool was made to install software after a fresh windows install. It uses Chocolatey as backend. if you don’t have chocolatey installed it will install Chocolatey and sudo to install the software you want. Filma Bem Tool uses qt for the gui.

## Light Mode
![Filma Bem Tool Blue Theme!](/imgs/lightblue.png)
![Filma Bem Tool Cyan Theme!](/imgs/lightcyan.png)
![Filma Bem Tool Pink Theme!](/imgs/lightpink.png)
![Filma Bem Tool Red Theme!](/imgs/lightred.png)
![Filma Bem Tool Yellow Theme!](/imgs/lightyellow.png)

## Dark Mode
![Filma Bem Tool Blue Theme!](/imgs/darkblue.png)
![Filma Bem Tool Cyan Theme!](/imgs/darkcyan.png)
![Filma Bem Tool Pink Theme!](/imgs/darkpink.png)
![Filma Bem Tool Red Theme!](/imgs/darkred.png)
![Filma Bem Tool Yellow Theme!](/imgs/darkyellow.png)

# First Run
## Depends
if it’s the first run or chocolatey is not installed this tool will relaunch as root to install it and then install sudo to elevate privileges to install programs. I recommend you to close the tool and re-open it after chocolatey is installed. To avoid some issues this tool will only run as admin if it needs to install chocolatey. All other software instalations will use sudo to elevate privileges.

## Configurations
If it's the first run this tool will download the default configuration file (i clould make it create one, but downloading it is easier) and will start with the default configurations

# Configure the tool
You can configure this tool by editing the config file located on your appdata folder. It will download the config file to a subfolder called filmabem.

## Themes
You can choose the theme accent color from this 5 colors:
- Blue
- Cyan
- Pink
- Red
- Yellow

The Tool will use the light or dark variant depending on yout windows theme.

## Force Light Mode
THIS OPTION IS NOT IMPLEMENTED YET but if this option is set to 'True' this tool will use only light mode.

## Advanced Mode
THIS OPTION IS NOT IMPLEMENTED YET and it's not planned to be implemented soon. It will take a lot of time to implement if i don't just remove this option

# Top Menu
In the top menu you have the ‘Software’ tab with 2 options to troubleshoot and an option to upgrade all software installed by this tool or directlly by chocolatey. In the same menu you have the ‘Help’ tab with 2 options. One of them is some information about the tool and the other option is to donate to my paypal.

# Why did i made this tool?
I made this tool because i could not find a tool to install the software i want and without malware included. So i decided to make my own install tool so i can install the software i want with less work.

# Why in python?
Because python is easy.

# Why using sudo?
Because i think it's better to call a process with sudo instead of running the main process with elevated privilegs.

# Why it asks for administrator anywhay?
It only asks for administrator if chocolatey is not installed and it's just to install ir and the install sudo. If you want you can restart the tool after it installs this 2 softwares and it will not ask for admin anymore. The only administrator prompts you will see will be subprocess to install the software you selected. All Subprocess will run in a command line so you can see whats happening during the installation.

# Used tools
I used this tools to help to make the code easier and make sure the software will act as it should

## PyQt5
PyQt is a Python binding of the cross-platform GUI toolkit Qt, implemented as a Python plug-in. PyQt is free software developed by the British firm Riverbank Computing

## Chocolatey
Chocolatey is a software management solution that allows you to manage 100% of your software, anywhere you have Windows, with any endpoint management tool. No other solution (including newly announced solutions) reach this level of management - most only can manage to software in Programs and Features.

## Sudo
sudo is a program that enables users to run programs with the elevated privileges of another user.