#SamuraisEpic
#Music Visualizer

#start by importing sys for cli switches, this would help if the user wants to interact through a terminal similar to qemu.
#also relevant modules from pyqt5 (obviously)

from tkinter import * #gui

from tkinter.filedialog import askopenfilename #filepicker

import wave

#make a window 
mainwindow = Tk()

#give it a title
mainwindow.title("wfg working window")

# set size (wxl)
mainwindow.geometry('640x480')

# add some text/a label
txt = Label(mainwindow, text = "waveform generator\n instrusctions: click \"generate!\" and pick a file")
txt.grid()

#button and stuff
    #file picker function
def generate():
    filename = askopenfilename(filetypes=(("Wave files", "*.wav"),))
    print(filename)
    #okie now that we have a path we can start doing fun stuff
    soundin = wave.open("" + filename + "",'rb')
    samplerate = soundin.getframerate()
    totalsamples = soundin.getnframes()
    totalduration = totalsamples/samplerate
    totalchannels = soundin.getnchannels()
    



btn = Button(mainwindow, text = "generate!", command = generate) #button to open file picker/choose audiofile

#set grid order
btn.grid(column = 0, row = 2)

#execute
mainwindow.mainloop()

