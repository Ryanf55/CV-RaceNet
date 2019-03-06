# CV-RaceNet
Configure ClearView ground station receivers with a GUI; for drone racing organizers.

This is a work in progress - announcements will be made when it works. This python-based code is intended to communicate with a ClearView. This software is 3rd party and unsupported by Iftron/ClearViewFPV. 

Hardware required:
1) A ClearView Racing or ClearView Pro Receiver
2) A FPC cable or similar FTDI cable
3) A laptop with Python 3 installed OR a Rasberry Pi 3 B+

Planned features:
1) Configure frequency, camera type, and OSD through a GUI on a different device
2) Import racer heats and other info to make race organizer's video management easier

How to use:
1) Open powershell window in the repository
2) If python not installed: $ python --version          
	follow this:  https://docs.python-guide.org/starting/install3/win/
3) $ pip install --user pipenv
4) $ pipenv install pyserial

5) to run the program: $ pipenv run python cv_main.py
	It will create a virtual environment when it first runs. May take a while..
	
	
Libraries Used:
serial #For using the FPC device to communicate with the ClearView

tkinter #For the GUI



