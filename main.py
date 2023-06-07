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
from tkinter import * # geeksforgeeks

#make a window 
initial = Tk()

#give it a title
initial.title("wfg working window")

# set size (wxl)
initial.geometry('640x480')

# add some text/a label
txt = Label(initial, text = "there is text here now")
txt.grid()

#button and stuff
    #define what clicked is make it easier
def clicked():
    txt.configure(text = "the button got clicked")

btn = Button(initial, text = "has this been clicked?", command = clicked)

#set grid order
btn.grid(column = 2, row = 0)

#execute
initial.mainloop()

