sabnzbd-prowl.py
=================

Introduction
------------
sabnzbd-prowl.py is a sabnzbd post-processing script that allows you to send download notifications from Sabnzbd to the Prowl service, which can forward notifications to iOS devices.


Usage
-----

### Setup ###
Set up a Prowl account at [prowlapp.com](http://prowlapp.com)
You can find your Prowl API key [here](https://www.prowlapp.com/api_settings.php) (you'll need this later)
Install the Prowl app on your iOS device and log in.

### Linux / OSX ###
1.  Set sabnzbd "Post-Processing Scripts Folder" (located in Sabnzbd Settings > Folders) to the folder containing this script
2.  Set the default user script (in Settings > Switches) to _sabnzbd-notifo.py_
3.  In sabnzbd-prowl.py, enter in your Prowl API Key

### Windows ###
1.  Install [Python 2.7](http://www.python.org/download/releases/2.7.1/) and [py2exe](http://www.py2exe.org/) for python 2.7
2.  In sabnzbd-prowl.py, enter in your Prowl API Key
3.  Run the command `python py2exe-setup.py py2exe` to create an exe
4.  Set Sabnzbd "Post-Processing Scripts Folder" (located in Sabnzbd Settings > Folders) to the folder containing the exe (/dist/)
5.  In Sabnzbd Settings > Switches, set "Default User Script" to sabnzbd-prowl.exe