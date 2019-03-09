# CV-RaceNet
Configure ClearView ground station receivers with a GUI; for drone racing organizers using a button emulator. 

This is a work in progress - announcements will be made when it works. Project focus: Box up 8 receivers for race organizers and distribute power/video to panel connectors. This software is 3rd party. 

Hardware required:
1) A Racing or Pro RX
2) A Solonoid to press the button
3) A laptop with Python 3 installed OR a Rasberry Pi 3 B+

Planned features:
1) Configure frequency, camera type, and OSD through a GUI on a different device
2) Import racer heats and other info to Python software to make race organizer's video management easier

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



