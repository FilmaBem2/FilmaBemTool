from cgi import test
import tkinter
from tkinter import messagebox
from appJar import gui
import doctest
import os
from os.path import exists as file_exists
import subprocess
import sys
import webbrowser
import time
import ctypes

# Variables

choco = 'true'


# def window():
#     app = QApplication(sys.argv)
#     win = QMainWindow()
#     win.setGeometry(200, 200, 1200, 900)
#     win.setWindowTitle("Filma Bem Install Tool")
#     win.setWindowIcon("imgs/icon.ico")


#     win.show()
#     sys.exit(app.exec_())

# window


# Checking is chocolatey is installed

if file_exists('C:\ProgramData\Chocolatey\choco.exe'):
    choco = 'true'
else:
    choco = 'false'

# Window Properties

Installgui = gui()
Installgui.setBg("indigo")
Installgui.setFg("white")
Installgui.setSize("1200x900")
Installgui.setResizable(False)
Installgui.setTitle("Filma Bem Install Tool")
Installgui.setIcon("imgs/icon.ico")

# Functions

def press(name):
    # Browsers
    if name == "Update Apps":
        program = subprocess.Popen('sudo choco upgrade all -y', shell=True)
    elif name == "Edge":
        program = subprocess.Popen('sudo choco install microsoft-edge -y', shell=True)
    elif name == "Brave":
        program = subprocess.Popen('sudo choco install brave -y', shell=True)
    elif name == "Waterfox":
        program = subprocess.Popen('sudo choco install waterfox -y', shell=True)
    elif name == "Chrome":
        program = subprocess.Popen('sudo choco install googlechrome -y', shell=True)
    elif name == "Firefox":
        program = subprocess.Popen('sudo choco install firefox -y', shell=True)
    elif name == "Opera":
        program = subprocess.Popen('sudo choco install opera -y', shell=True)
    elif name == "Opera GX":
        program = subprocess.Popen('sudo choco install opera-gx -y', shell=True)
    elif name == "Vivaldi":
        program = subprocess.Popen('sudo choco install vivaldi -y', shell=True)
    elif name == "Librewolf":
        program = subprocess.Popen('sudo choco install librewolf -y', shell=True)
    elif name == "Pale Moon":
        program = subprocess.Popen('sudo choco install palemoon -y', shell=True)
    # Games
    elif name == "Steam":
        program = subprocess.Popen('sudo choco install steam-client -y', shell=True)
    elif name == "Origin":
        program = subprocess.Popen('sudo choco install origin -y', shell=True)
    elif name == "uPlay":
        program = subprocess.Popen('sudo choco install ubisoft-connect -y', shell=True)
    elif name == "GoG Galaxy":
        program = subprocess.Popen('sudo choco install goggalaxy -y', shell=True)
    elif name == "Minecraft":
        program = subprocess.Popen('sudo choco install minecraft-launcher -y', shell=True)
    elif name == "GDLauncher":
        program = subprocess.Popen('sudo choco install gdlauncher -y', shell=True)
    elif name == "Épic Games Store":
        program = subprocess.Popen('sudo choco install epicgameslauncher -y', shell=True)
    elif name == "Overwolf":
        program = subprocess.Popen('sudo choco install overwolf -y', shell=True)
    elif name == "Battle.net":
        program = subprocess.Popen('sudo choco install battle.net -y', shell=True)
    elif name == "Itch.io":
        program = subprocess.Popen('sudo choco install itch -y', shell=True)
    # Compression
    elif name == "Winrar":
        program = subprocess.Popen('sudo choco install winrar -y', shell=True)
    elif name == "7-Zip":
        program = subprocess.Popen('sudo choco install 7zip -y', shell=True)
    elif name == "Peazip":
        program = subprocess.Popen('sudo choco install peazip -y', shell=True)
    # Comunications
    elif name == "Guilded":
        # program = subprocess.Popen('sudo choco install guilded', shell=True)
        messagebox('Guilded not Available yet')
    elif name == "Discord":
        program = subprocess.Popen('sudo choco install discord.install -y', shell=True)
    elif name == "Skype":
        program = subprocess.Popen('sudo choco install skype -y', shell=True)
    elif name == "Teams":
        program = subprocess.Popen('sudo choco install microsoft-teams.install -y', shell=True)
    elif name == "Zoom":
        program = subprocess.Popen('sudo choco install zoom -y', shell=True)
    elif name == "Better Discord":
        program = subprocess.Popen('sudo choco install betterdiscord -y', shell=True)
    # Security
    elif name == "Authy":
        program = subprocess.Popen('sudo choco install authy-desktop -y', shell=True)
    elif name == "BitWarden":
        program = subprocess.Popen('sudo choco install bitwarden -y', shell=True)
    elif name == "ProtonVPN":
        program = subprocess.Popen('sudo choco install protonvpn -y', shell=True)
    elif name == "NordVPN":
        program = subprocess.Popen('sudo choco install nordvpn -y', shell=True)
    elif name == "ExpressVPN":
        program = subprocess.Popen('sudo choco install expressvpn -y', shell=True)
    elif name == "RadminVPN":
        program = subprocess.Popen('sudo choco install radmin-vpn -y', shell=True)
    elif name == "Hamachi":
        program = subprocess.Popen('sudo choco install hamachi -y', shell=True)
    elif name == "FortiClient":
        program = subprocess.Popen('sudo choco install forticlientvpn -y', shell=True)
    elif name == "VeraCrypt":
        program = subprocess.Popen('sudo choco install veracrypt -y', shell=True)
    elif name == "PIA":
        program = subprocess.Popen('sudo choco install pia -y', shell=True)
    # Remote Control
    elif name == "Anydesk":
        program = subprocess.Popen('sudo choco install anydesk.install -y', shell=True)
    elif name == "TeamViewer":
        program = subprocess.Popen('sudo choco install teamviewer -y', shell=True)
    # Poweruser Tools
    elif name == "Powertoys":
        program = subprocess.Popen('sudo choco install powertoys -y', shell=True)
    elif name == "Sysinternal Suite":
        program = subprocess.Popen('sudo choco install sysinternals -y', shell=True)
    elif name == "Putty":
        program = subprocess.Popen('sudo choco install putty -y', shell=True)
    elif name == "VirtualBox":
        program = subprocess.Popen('sudo choco install virtualbox -y', shell=True)
    elif name == "Vmware Workstation":
        program = subprocess.Popen('sudo choco install vmwareworkstation -y', shell=True)
    elif name == "Vmware Player":
        program = subprocess.Popen('sudo choco install vmware-workstation-player -y', shell=True)
    elif name == "TeraCopy":
        program = subprocess.Popen('sudo choco install teracopy -y', shell=True)
    elif name == "WSL":
        program = subprocess.Popen('sudo wsl --install', shell=True)
    elif name == "Partition Assistant":
        program = subprocess.Popen('sudo choco install partition-assistant-standard -y', shell=True)
    elif name == "FileZilla":
        program = subprocess.Popen('sudo choco install filezilla -y', shell=True)
    elif name == "Git":
        program = subprocess.Popen('sudo choco install git -y', shell=True)
    # Office
    elif name == "WPS Office":
        program = subprocess.Popen('sudo choco install wps-office-free -y', shell=True)
    elif name == "LibreOffice":
        program = subprocess.Popen('sudo choco install libreoffice-fresh -y', shell=True)
    elif name == "OnlyOffice":
        program = subprocess.Popen('sudo choco install onlyoffice -y', shell=True)
    elif name == "OpenOffice":
        program = subprocess.Popen('sudo choco install openoffice -y', shell=True)
    elif name == "Microsoft Office":
        program = subprocess.Popen('sudo choco install office365homepremium -y', shell=True)
    # Others
    elif name == "OBS":
        program = subprocess.Popen('sudo choco install obs-studio -y', shell=True)
    elif name == "Adobe Reader DC":
        program = subprocess.Popen('sudo choco install adobereader -y', shell=True)
    elif name == "VLC":
        program = subprocess.Popen('sudo choco install vlc -y', shell=True)
    elif name == "MPV":
        program = subprocess.Popen('sudo choco install mpv -y', shell=True)
    elif name == "Visual Studio Code":
        program = subprocess.Popen('sudo choco install vscode -y', shell=True)
    elif name == "Windows Terminal":
        program = subprocess.Popen('sudo choco install microsoft-windows-terminal -y', shell=True)
    elif name == "Etcher":
        program = subprocess.Popen('sudo choco install etcher -y', shell=True)
    elif name == "ShareX":
        program = subprocess.Popen('sudo choco install sharex -y', shell=True)
    elif name == "GIMP":
        program = subprocess.Popen('sudo choco install gimp -y', shell=True)
        program2 = subprocess.Popen('sudo choco install gimp-data-extras -y', shell=True)
    elif name == "Deluge":
        program = subprocess.Popen('sudo choco install deluge -y', shell=True)
    elif name == "Notion":
        program = subprocess.Popen('sudo choco install notion -y', shell=True)
    elif name == "EarTrumpet":
        program = subprocess.Popen('sudo choco install eartrumpet -y', shell=True)
    elif name == "Thunderbird":
        program = subprocess.Popen('sudo choco install thunderbird -y', shell=True)
    elif name == "Adblock (Systemwide)":
        program = subprocess.Popen('sudo choco install adguardhome -y', shell=True)
    elif name == "Photogimp":
        program = subprocess.Popen('sudo choco install photogimp -y', shell=True)

# Lables

Installgui.addLabel("title", "Install Apps", 0, 0, rowspan=1)
Installgui.addButton("Update Apps", press, 1, 0, 2, )

# Buttons in groups

with Installgui.labelFrame("Web Browsers", colspan=3, sticky="news", expand="both"):
    Installgui.addButton( "Edge", press, 0, 3, 3 )
    Installgui.addButton( "Brave", press, 0, 9, 3 )
    Installgui.addButton( "Waterfox", press, 0 , 0, 3 )
    Installgui.addButton( "Chrome", press, 0 , 6, 3 )
    Installgui.addButton( "Firefox", press, 0, 12, 3)
    Installgui.addButton( "Opera", press, 1, 0, 3)
    Installgui.addButton( "Opera GX", press, 1, 3, 3)
    Installgui.addButton( "Vivaldi", press, 1, 6, 3)
    Installgui.addButton( "Librewolf", press, 1, 9, 3)
    Installgui.addButton( "Pale Moon", press, 1, 12, 3)
    
with Installgui.labelFrame("Games", colspan=3, sticky="news", expand="both"):
    Installgui.addButton( "Steam", press, 0 , 0, 3 )
    Installgui.addButton( "Origin", press, 0 , 3, 3 )
    Installgui.addButton( "uPlay", press, 0 , 6, 3 )
    Installgui.addButton( "GoG Galaxy", press, 0 , 9, 3 )
    Installgui.addButton( "Minecraft", press, 1 , 0, 3 )
    Installgui.addButton( "GDLauncher", press, 1 , 3, 3 )
    Installgui.addButton( "Épic Games Store", press, 1 , 6, 3 )
    Installgui.addButton( "Overwolf", press, 1 , 9, 3 )
    Installgui.addButton( "Battle.net", press, 0 , 12, 3 )
    Installgui.addButton( "Itch.io", press, 1, 12, 3 )
    
with Installgui.labelFrame("Compression", colspan=3, sticky="news", expand="both"):
    Installgui.addButton( "Winrar", press, 0, 0, 3 )
    Installgui.addButton( "7-Zip", press, 0, 4, 3)
    Installgui.addButton( "Peazip", press, 0, 8, 3)
      
with Installgui.labelFrame("Communication", colspan=3, sticky="news", expand="both"):
    Installgui.addButton( "Guilded", press, 0, 0, 3 )
    Installgui.addButton( "Discord", press, 0 , 3, 3 )
    Installgui.addButton( "Skype", press, 0 , 6, 3 )
    Installgui.addButton( "Teams", press, 0 , 9, 3 )
    Installgui.addButton( "Zoom", press, 0 , 12, 3 )
    Installgui.addButton( "Better Discord", press, 1, 0, 3 )
    
with Installgui.labelFrame("Security", colspan=3, sticky="news", expand="both"):
    Installgui.addButton( "Authy", press, 0 , 0, 3 )
    Installgui.addButton( "BitWarden", press, 0 , 3, 3 )
    Installgui.addButton( "ProtonVPN", press, 0, 6, 3 )
    Installgui.addButton( "NordVPN", press, 0, 9, 3)
    Installgui.addButton( "ExpressVPN", press, 0, 12, 3)
    Installgui.addButton( "RadminVPN", press, 1, 0, 3)
    Installgui.addButton( "Hamachi", press, 1, 3, 3)
    Installgui.addButton( "FortiClient", press, 1, 6, 3)
    Installgui.addButton( "VeraCrypt", press, 1, 9, 3 )
    Installgui.addButton( "PIA", press, 1, 12, 3)

with Installgui.labelFrame("Remote Control", colspan=3, sticky="news", expand="both"):
    Installgui.addButton( "Anydesk", press, 0, 0, 3 )
    Installgui.addButton( "TeamViewer", press, 0, 3, 3 )

with Installgui.labelFrame("Poweruser Tools", colspan=3, sticky="news", expand="both"):
    Installgui.addButton( "Powertoys", press, 0 , 0, 3 )
    Installgui.addButton( "Sysinternal Suite", press, 0, 3, 3)
    Installgui.addButton( "Putty", press, 0, 6, 3 )
    Installgui.addButton( "VirtualBox", press, 0, 9, 3 )
    Installgui.addButton( "Vmware Workstation", press, 0, 12, 3 )
    Installgui.addButton( "Vmware Player", press, 1, 0, 3 )
    Installgui.addButton( "TeraCopy", press, 1, 3, 3)
    Installgui.addButton( "WSL", press, 1, 6, 3)
    Installgui.addButton( "Partition Assistant", press, 1, 9, 3)
    Installgui.addButton( "FileZilla", press, 1 , 12, 3 )
    Installgui.addButton( "Git", press, 2, 0, 3)

with Installgui.labelFrame("Office", colspan=3, sticky="news", expand="both"):
    Installgui.addButton( "WPS Office", press, 0, 0, 3)
    Installgui.addButton( "LibreOffice", press, 0, 3, 3)
    Installgui.addButton( "OnlyOffice", press, 0, 6, 3)
    Installgui.addButton( "OpenOffice", press, 0, 9, 3)
    Installgui.addButton( "Microsoft Office", press, 0, 12, 3)

with Installgui.labelFrame("Others", colspan=3, sticky="news", expand="both"):
    Installgui.addButton( "OBS", press, 0, 3, 3 )
    Installgui.addButton( "Adobe Reader DC", press, 0, 9, 3 )
    Installgui.addButton( "VLC", press, 0, 6, 3 )
    Installgui.addButton( "MPV", press, 0, 9, 3 )
    Installgui.addButton( "Visual Studio Code", press, 0, 12, 3 )
    Installgui.addButton( "Windows Terminal", press, 1 , 3, 3 )
    Installgui.addButton( "Etcher", press, 1 , 12, 3 )
    Installgui.addButton( "ShareX", press, 2 , 3, 3 )
    Installgui.addButton( "GIMP", press, 2, 6, 3 )
    Installgui.addButton( "Deluge", press, 2, 0, 3 )
    Installgui.addButton( "Notion", press, 1 , 0, 3 )
    Installgui.addButton( "EarTrumpet", press, 0 , 0, 3 )
    Installgui.addButton( "Thunderbird", press, 1, 6, 3 )
    Installgui.addButton( "Adblock (Systemwide)", press, 1, 9, 3 )
    Installgui.addButton( "Photogimp", press, 2, 9, 3 )

# start GUI if winget is installed
# if not this tool should install it automatically

if choco == 'true':
    Installgui.go()
else:
    def is_admin():
        try:
            return ctypes.windll.shell32.IsUserAnAdmin()
        except:
            return False
    if is_admin():
        program = subprocess.Popen("powershell.exe Set-ExecutionPolicy Bypass -Scope Process -Force; [System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072; iex ((New-Object System.Net.WebClient).DownloadString('https://community.chocolatey.org/install.ps1'))", shell=True)
        time.sleep(60)
        program2 = subprocess.Popen('choco install sudo -y')
        Installgui.stop()
    else:
        # Re-run the program with admin rights
        ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)

