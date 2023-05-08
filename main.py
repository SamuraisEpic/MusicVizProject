#Mitam Kacha
#Music Visualizer

#start by importing sys for cli switches, this would help if the user wants to interact through a terminal similar to qemu.
#also relevant modules from pyqt5 (obviously)

import sys
from PyQt5 import QApplication, QWidget

#make a qapplication called gui, since it's the gui frontend for the program

gui = QApplication(sys.argv) #sys.argv allows for cli switches

#qwidget acts as the windo
window = QWidget()

#have to show the window since all top level widgets are hidden
window.show()

#now start the event loop
gui.exec()

