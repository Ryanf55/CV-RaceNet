# CV-RaceNet
This is a work in progress - announcements will be made when it works. Project focus: Box up 8 receivers for race organizers and distribute power/video to panel connectors. Include software for testing video transmitters in pre-race check in. 

This software and hardware is 3rd party. It is not supported by Iftron and should be used at your own risk. 

Hardware required:
1. 4x or 8x Racing or Pro Video RX
1. A Solonoid to press the menu button?
1. A laptop with Python 3 installed OR a Rasberry Pi 3 B+
1. A bunch of electronics to distribute power and all the panel mount connectors
1. A 12V UPS power supply
1. A RF Explorer 6G. 

Planned software features:
1. Import racer heats and other info to Python software from RotorHazard to make race organizer's video management easier
1. Test video transmitters with the RF Explorer

Planned hardware features:
1. Active cooling for operation in direct sunlight
1. Dustproof and water resistant
1. Durable container ships everything
1. Locking connectors for video cables
1. Redundant 12V power (AC input and redundant 12V battery)

How to use:
1) Open powershell window in the repository
2) If python not installed: $ python --version          
	follow this:  https://docs.python-guide.org/starting/install3/win/
3) $ pip install --user pipenv
4) $ pipenv install pyserial

5) to run the program: $ pipenv run python cv_main.py
	It will create a virtual environment when it first runs. May take a while..
	
	
Libraries Used:
serial #For using the FPC device to communicate with the Arduino->Solonoid->CV

tkinter #For the GUI



