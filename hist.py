#https://stackoverflow.com/questions/7546050/switch-between-two-frames-in-tkinter
#update bar plot: https://www.reddit.com/r/learnpython/comments/55w2ec/updating_the_height_of_bar_graph_in_matplotlib/

#This is a multi-frame tkinter app for CV-racenet. 

import numpy as np
import tkinter as tk
import matplotlib.pyplot as plt; plt.rcdefaults()
from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg, NavigationToolbar2Tk)
# Implement the default Matplotlib key bindings.
from matplotlib.backend_bases import key_press_handler



band_name = ('Fatshark','Race','E-Band','A-Band')
amplitude = [[1,1,2,2,0,0,28,2],[1,2,1,2,26,0,28,22]]


num_channels = 8
x_0_7 = np.arange(num_channels)

width=0.35
fig, ax = plt.subplots()
rects = [0,0]
rects[0] = ax.bar(x_0_7-width/3, amplitude[0], width/2, alpha=0.75,label='Old',color='LightGray')
rects[1] = ax.bar(x_0_7+width/2, amplitude[1], width, alpha=0.75,label='New',color='SkyBlue')

ax.set_xticks(x_0_7) #x tick positions
ax.set_xticklabels(x_0_7+1) #x tick labels
ax.set_ylabel('Signal Strength (mW)') #y axis label
ax.set_title('Spectrum Analyzer') #title
ax.set_xlabel('Band: ' + band_name[1]) #x axis label is the band name
ax.legend() #legend


def autolabel(rects, xpos='center'): #add data labels
    """
    Attach a text label above each bar in *rects*, displaying its height.

    *xpos* indicates which side to place the text w.r.t. the center of
    the bar. It can be one of the following {'center', 'right', 'left'}.
    """

    xpos = xpos.lower()  # normalize the case of the parameter
   
    ha = {'center': 'center', 'right': 'left', 'left': 'right'}
    offset = {'center': 0.5, 'right': 0.57, 'left': 0.43}  # x_txt = x + w*off

    for rect in rects:
        height = int(round(rect.get_height())) #get height of rectangle as an int
        
        ax.text(rect.get_x() + rect.get_width()*offset[xpos], 1.01*height,
                '{}'.format(height), ha=ha[xpos], va='bottom')

#autolabel(rects[0])
#autolabel(rects[1])

fig.show()
plt.close()


class SampleApp(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self._frame = None
        self.switch_frame(PageSpectrum)

    def switch_frame(self, frame_class):
        """Destroys current frame and replaces it with a new one."""
        new_frame = frame_class(self)
        if self._frame is not None:
            self._frame.destroy()
        self._frame = new_frame
        self._frame.pack()

class StartPage(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Label(self, text="This is the start page").pack(side="top", fill="x", pady=10)
        tk.Button(self, text="Open main page",
                  command=lambda: master.switch_frame(PageMain)).pack()
        tk.Button(self, text="Open page options",
                  command=lambda: master.switch_frame(PageOptions)).pack()

class PageMain(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Label(self, text="This is main page").pack(side="top", fill="x", pady=10)
        tk.Button(self, text="Return to start page",
                  command=lambda: master.switch_frame(StartPage)).pack()
        tk.Button(self, text="View Spectrum Analyzer",
                  command=lambda: master.switch_frame(PageSpectrum)).pack()


class PageOptions(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Label(self, text="This is options page").pack(side="top", fill="x", pady=10)
        tk.Button(self, text="Return to start page",
                  command=lambda: master.switch_frame(StartPage)).pack()
                  
class PageSpectrum(tk.Frame):
    def __init__(self,master):
        tk.Frame.__init__(self,master)
        #Row 0: Label
        tk.Label(self,text="Spectrum Analyzer").grid(row=0,column=0)
        
        #Row 1: Navigation Buttons
            #Button: Return to Main
        tk.Button(self,text="Return to main",
                command=lambda: master.switch_frame(PageMain)).grid(row=1,column=0)
            #Button: New Scan -> Conducts a new scan. Latest scan showed against 2nd latest
        tk.Button(self,text="Conduct new scan",
                command= lambda: self.spec_new_scan()).grid(row=1,column=0)
        #Row 2: Spectrum Analyzer
        self.canvas = FigureCanvasTkAgg(fig, master=self)  # A tk.DrawingArea.
        self.canvas.draw()
        self.canvas.get_tk_widget().grid(row=2, column=0)
     
        
    def spec_new_scan(self):
        print(amplitude[-1])     
        #print(rects[-1].get_data())
        for rect_old,rect_new in zip(rects[-2],rects[-1]): 
            #set older rects to the new rects
            rect_old.set_height(rect_new.get_height())
            rect_new.set_height(5)
            
        self.canvas.draw() #redraw the canvas of PageSpectrum. 
            
       
       
        

if __name__ == "__main__":
    app = SampleApp()
    app.mainloop()
