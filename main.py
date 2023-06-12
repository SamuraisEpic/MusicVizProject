#Mitam Kacha
#Music Visualizer

#start by importing sys for cli switches, this would help if the user wants to interact through a terminal similar to qemu.
#also relevant modules from pyqt5 (obviously)
'''
import sys
from PyQt5 import QApplications,QWidget

#make a qapplication called gui, since it's the gui frontend for the program

gui = QApplication(sys.argv) #sys.argv allows for cli switches

#qwidget acts as the windo
window = QWidget()

#have to show the window since all top level widgets are hidden
window.show()

#now start the event loop
gui.exec()
'''
from tkinter import * 

from tkinter.filedialog import askopenfilename #filepicker

#make a window 
mainwindow = Tk()

#give it a title
mainwindow.title("wfg working window")

# set size (wxl)
mainwindow.geometry('640x480')

# add some text/a label
txt = Label(mainwindow, text = "waveform generator")
txt.grid()

#button and stuff
    #file picker function
def filepicker():
    filename = askopenfilename()
    print(filename) #print filename to the console (this is just a standin to make sure it actually works)

btn = Button(mainwindow, text = "open file picker", command = filepicker) #button to open file picker/choose audiofile

#set grid order
btn.grid(column = 0, row = 2)

#execute
mainwindow.mainloop()

