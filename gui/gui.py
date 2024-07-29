# widgets = GUi elements: buttons,textboxes,lables,images
# windows = serves as a container to hold or contain these widgets
from tkinter import *
window = Tk() # instantiate an instance of a window
window.geometry("420x420")
window.title("venkat")
icon = PhotoImage(file='F:\studeys\python\project\gui\ggv.png')
window.iconphoto(True,icon)
window.config(background="#5cfcff")
window.mainloop()# place windows on computer scree, listing for events