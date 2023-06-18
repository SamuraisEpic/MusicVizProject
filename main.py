#SamuraisEpic
#Music Visualizer

#start by importing sys for cli switches, this would help if the user wants to interact through a terminal similar to qemu.
#also relevant modules from pyqt5 (obviously)

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

