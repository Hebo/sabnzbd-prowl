sabnzbd-prowl.py
=================

Introduction
------------
sabnzbd-prowl.py is a sabnzbd post-processing script that allows you to send download notifications from Sabnzbd to the Prowl service, which can forward notifications to iOS devices.


Usage
-----

**Setup**
Set up a Prowl account at http://prowlapp.com
You can find your Prowl API key at https://www.prowlapp.com/api_settings.php (you'll need this later)
Install the Prowl app on your iOS device and log in.

**Linux / OSX**
1. Set sabnzbd "Post-Processing Scripts Folder" (located in Sabnzbd Settings > General) to the folder containing this script
2. Set the default user script (in Settings > Switches) to _sabnzbd-notifo.py_
3. In sabnzbd-notifo.py, enter in your Prowl and _API Key_

**Windows**
1. In sabnzbd-notifo.py, enter in your Notifo _username_ and _api secret_
2. Run the command `python py2exe-setup.py py2exe` to create exe
3. Set sabnzbd "Post-Processing Scripts Folder" (located in Sabnzbd Settings > General) to the folder containing the exe (/dist/)