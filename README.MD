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
This tool Depends on Chocolatey and Sudo. if you don't have them installed this tool will not work. It will tell you that every time you run the tool. If you don't know how to install this things don't worry. The tool will launch the interface anyways so you can go to the top menu, select software and the select this things and a new tab on your browser will open with the instructions

## Themes
You can choose the theme accent color from this 5 colors:
- Blue
- Cyan
- Pink
- Red
- Yellow

If you don't choose any color it will default to Blue.

To choose the color you want the theme you want the tool to launch open your command line in this the executable folder and launch the tool with the argument "-c" or "--color" followed by the color you want. Example "fbtool.exe -c red" or "fbtool.exe --color red". Always remeber to spell in lowercase

The Tool will use the light or dark variant depending on yout windows theme.

## Force Light Mode
THIS OPTION IS NOT IMPLEMENTED YET but i'm working on that i'm working on that feature

## Force Light Mode
THIS OPTION IS NOT IMPLEMENTED YET but i'm working on that i'm working on that feature


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