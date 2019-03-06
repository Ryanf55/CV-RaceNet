#FIXME Urgent - unasign results of pack and grid to buttons https://stackoverflow.com/questions/24911805/change-the-value-of-a-variable-with-a-button-tkinter

#tk youtube references:
#https://www.youtube.com/watch?v=qCnBkZLb-E4
#newboston: https://www.youtube.com/playlist?list=PL6gx4Cwl9DGBwibXFtPtflztSNPGuIB_d

#todo:
#1) Learn how to import data via csv or JSON for "heats"
#2) Create separate frequency picker window using https://www.youtube.com/watch?v=jBUpjijYtCk&list=PLQVvvaa0QuDclKx-QpC9wntnURXVJqLyk&index=4
    #buttons for each frequency, in a table format
    #The list of bands active is in the JSON config file
#3) Bugfix: Reducing number of pilots doesn't change gui. Maybe try disabling
#4) Learn how to make a python class to handle serial comms with clearview
#5) COM port dropdown (see https://pythonspot.com/tk-dropdown-example/
#Options
numRacers = 7
racer_frequencies = [5645,5740,5800,5880]
racer_enable_lock = []
racer_camera_options = ("NSTC","PAL","AUTO") #these are fixed
racer_polarization = ("RHCP","LCHP","Linear","MIMO")
racer_defaults = {
    "camera_type": "NTSC",
    "frequency": "5740",
    "handle": "CV Pilot",
    }



import tkinter as tk
import tkinter.messagebox
import tkinter.simpledialog
import serial  #pyserial

#Setup Serial Port
# baudRate = 9600
# ser = serial.Serial('COM1',baudRate) #open port
# serName = ser.name #print port used
# ser.write(b'hello')
# ser.close()

#set up main window
main_window = tk.Tk()
main_window.title("VM")
main_window.geometry('640x480+1300+400')

#main_window menu
menu_main = tk.Menu(main_window)
main_window.config(menu=menu_main)


#   Filemenu
def save_settings():
    print("FIXME save_settings")
filemenu = tk.Menu(menu_main,tearoff=False)
menu_main.add_cascade(label="File",menu=filemenu)
filemenu.add_command(label="Save",command=save_settings)
filemenu.add_separator()
filemenu.add_command(label="Exit",command=main_window.quit)



#   HeatMenu
def do_next_heat():
    print("FIXME do_next_heat")

def do_previous_heat():
    print("FIXME do_previous_heat")
    
def do_insert_heat():
    print("FIXME do_insert_heat")
    
def do_import_heats():
    print("FIXME do_import_heat")

def do_export_heats():
    print("FIXME do_export_heat")
    
heatmenu = tk.Menu(menu_main,tearoff=False)
menu_main.add_cascade(label = "Heats",menu=heatmenu)
heatmenu.add_command(label="Next",command=do_next_heat)
heatmenu.add_command(label="Previous",command=do_previous_heat)
heatmenu.add_command(label="Insert",command=do_insert_heat)
heatmenu.add_separator()
heatmenu.add_command(label="Import Heats",command=do_import_heats)
heatmenu.add_command(label="Export Heats",command=do_export_heats)


#   Tracker
def rotor_hazard_connect():
    print("FIXME rotor_hazard_connect")
def rotor_hazard_import_all():
    print("FIXME rotor_hazard_import_all()")
def rotor_hazard_import_racer():
    print("FIXME rotor_hazard_import_racer()")
def rotor_hazard_start_race():
    print("FIXME rotor_hazard_start_race()")
trackermenu=tk.Menu(menu_main,tearoff=False)
menu_main.add_cascade(label = "RotorHazard",menu=trackermenu)
trackermenu.add_command(label="Connect",command=rotor_hazard_connect)
trackermenu.add_command(label="Import All",command=rotor_hazard_import_all)
trackermenu.add_command(label="Import Racer",command=rotor_hazard_import_racer)
trackermenu.add_command(label="Start Race",command=rotor_hazard_start_race)

#   Setup
def get_com_ports():
    import serial.tools.list_ports
    ports =  serial.tools.list_ports.comports()

    port_message = "Here is a list of " + str(len(ports)) + " available ports:\n"
    for p in ports:
        pname = str(p).split(' ')[0]
        print (pname.split(' ')[0])
        port_message = port_message+ str(p) + '\n'
    msg = tk.messagebox.showinfo("COM Lister", port_message) #pop up message with list of ports
 
    
    if com_entry_var.get() =="":#populate com port entry box with the latest available COM port if nothing is in it when you scan
        print("Populating empty com box")
        pnameShort = str(ports[-1]).split(' ')[0]
        com_entry_var.set(pnameShort)

def change_n_racers():
    global numRacers #get this global
    print(numRacers)
    n_racers_req = tk.simpledialog.askinteger("Adjust Number of Racers", "How many ClearView's are connected?")
    if n_racers_req>0 and n_racers_req <= 8:
        
        prevRacers = numRacers
        numRacers = n_racers_req
        print("FIXME - Attempt Change of n_racers from " + str(prevRacers) + " to " + str(numRacers))
        if prevRacers == numRacers:
            tk.messagebox.showinfo("Adjust Number of Racers","Error: Already set up for " + str(n_racers_req) + " racers.\n Keeping the same value...")
        else:    
            tk.messagebox.showinfo("Adjust Number of Racers","Ok. There are now " + str(n_racers_req) + " racers.")
            drawGrid(prevRacers,numRacers-prevRacers)
    else:
        tk.messagebox.showinfo("Adjust Number of Racers","Invalid number of racers")
        
setupmenu = tk.Menu(menu_main,tearoff=False)
menu_main.add_cascade(label = "Setup",menu=setupmenu)
setupmenu.add_command(label="List Serial Ports",command=get_com_ports)
setupmenu.add_command(label="Change Number of Racers",command=change_n_racers) 





#COM port Entry - Manually type the port
com_entry_var = tk.StringVar()
com_entry = tk.Entry(main_window , textvariable=com_entry_var) #text in a single line
com_entry.grid(row=0,column=0)

#Click to open or close COM port. FIXME close COM on window close
conn_serial = False
ser = serial.Serial()


def toggle_COM():
    print("Currently connected? " , conn_serial)
    if conn_serial: #Disconnect
        print("Attempting Disconnect...")
    else:
        print("FIXME-Attempting Serial Connect on ",end='')
        print("Port:",com_entry_var.get())
        ser.baud=57600
        
        
    
    
    
but_connect = tk.Button(main_window,text="Connect",command=toggle_COM)
but_connect.grid(row=0,column=1,columnspan=2)
class seat:
    def __init__(self,*args,**kwargs):
            n = 2
    

#Row 1 = Actions
def start_race():
    print("FIXME start_race")
action_race_start=tk.Button(main_window,text="Start Race",command=start_race)
action_race_start.grid(row=1,column=0)

def abort_race():
    print("FIXME abort_race")
action_abort_start=tk.Button(main_window,text="Abort Race",command=abort_race)
action_abort_start.grid(row=1,column=1)

def custom_msg(): #display custom OSD message
    print("FIXME custom_msg")
action_msg_cstm=tk.Entry(main_window)
action_msg_cstm.grid(row=1,column=2)
#FIXME bind custom message enter to send the custom message to all pilots




#FIXME add horizontal divider line or frame pack here.

#Commands to RX
def setLockStat(lockEnable):
    print("FIXME - Change lock stat to ",lockEnable)
    



#Seats, top row applies commands to all CV's that are connected
seat_all_label = tk.Label(main_window,text="All")
seat_all_label.grid(row=2,column=0)
seat_all_cvEnableBool_var = tk.IntVar()
seat_all_cvEnableBool_var.set(True)
seat_all_cvEnable_checkButton = tk.Checkbutton(main_window,text="All",variable=seat_all_cvEnableBool_var)
seat_all_cvEnable_checkButton.grid(row=2,column=2)
seat_pilotHandleLabel = tk.Label(main_window,text="Pilot Name")
seat_pilotHandleLabel.grid(row=2,column=3)
seat_all_frequency = tk.Label(main_window,text="Frequency")
seat_all_frequency.grid(row=2,column=4)
seat_all_camera = tk.Label(main_window,text="Camera Type")
seat_all_camera.grid(row=2,column=5)

# dropVar = tk.StringVar()
# setOps = set(racer_camera_options)
# dropVar.set('NTSC') # set the default option
# popupMenu = OptionMenu(mainframe, dropVar, *setOps)
# popupMenu.grid(row=1,column=10)


seat_labels = [] #seat number GUI labels
seat_cvEnable_checkButtons = [] #enable CV lock GUI CheckButton
seat_cvEnable_variables = [] #variable that keep track of whether lock is permitted
seat_pilotHandles = [] #pilot name GUI labels
seat_pilotHandles_vars=[] #pilot name variables that go on OSD
seat_pilotFrequencies = [] #seat frequency GUI labels
seat_pilotCamTypes = [] #seat camera type GUI labels



def drawGrid(current_racers,racers_to_add):
    #calculate how many "racers_to_add". Append them. At startup, append all. 
    #if racers_to_add <0, remove some
    if racers_to_add < 0:
        if current_racers == 0:
            print("Error. Tried to remove racers when there are 0")
        else: #delete some racer rows
            for x in range(-1*racers_to_add):
                print("Destroying racer n from the end. n=",x)
                seat_labels[-1].destroy()
                seat_labels.pop()
                seat_cvEnable_checkButtons[-1].destroy()
                seat_cvEnable_checkButtons.pop()
                seat_cvEnable_variables.pop()
                seat_pilotHandles[-1].destroy()
                seat_pilotHandles.pop()
                seat_pilotHandles_vars.pop()
                seat_pilotFrequencies[-1].destroy()
                seat_pilotFrequencies.pop()
                seat_pilotCamTypes[-1].destroy()
                seat_pilotCamTypes.pop()
                
    else: #add racer seat rows         
        
        for x in range(racers_to_add):
            i=current_racers+x
            r=3+i #row of text used in the grid
            
            #Seat Number
            seat_labels.append(tk.Label(main_window,text="%s%d" % ("Racer ", i)))
            seat_cvEnable_variables.append(tk.IntVar())
            
            #Lock Status
                #check racer_enable_lock has enough elements
            if len(racer_enable_lock) == i : #add element based on the "all" value
                racer_enable_lock.append(seat_all_cvEnableBool_var.get())
            seat_cvEnable_variables[i].set(racer_enable_lock[i])
            seat_cvEnable_checkButtons.append(tk.Checkbutton(main_window,
                text="%s%d" % ("Lock", x),
                variable=seat_cvEnable_variables[i],
                command = lambda: setLockStat(i)) #end button declaration
                ) #end append
            
            #Pilot Handle
            seat_pilotHandles_vars.append(tk.StringVar())
            seat_pilotHandles_vars[i].set(racer_defaults["handle"])
            seat_pilotHandles.append(tk.Entry(textvariable = seat_pilotHandles_vars[i]))
            
            #Frequency, just a label for now
            seat_pilotFrequencies.append(tk.Label(main_window,text=racer_defaults["frequency"]))
            
            #Camera Type, just a label for now
            seat_pilotCamTypes.append(tk.Label(main_window,text=racer_defaults["camera_type"]))
            
            #Put elements in the grid
            seat_cvEnable_checkButtons[i].grid(row=r, column=2)
            seat_labels[i].grid(row=r,column=0)
            seat_pilotHandles[i].grid(row=r,column=3)
            seat_pilotCamTypes[i].grid(row=r,column=4)
            seat_pilotFrequencies[i].grid(row=r,column=5)
            
drawGrid(0,numRacers) #add numRacers to the grid
    
#Menu Bars
#main_window.add_command(label = 'File')

main_window.mainloop()
