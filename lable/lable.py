from tkinter import *
window = Tk() # instantiate an instance of a window
window.title("venkat")
icon = PhotoImage(file='F:\studeys\python\project\lable\ggv.png')
window.iconphoto(True,icon)
photo = PhotoImage(file='F:\studeys\python\project\lable\ph.png')
label = Label(window,text="Hi venkat",
              font=('Arial',40,'bold'),
              fg='#00ff00',
              bg='black',
              relief=RAISED,
              bd=10,
              padx=20,
              pady=20,
              image=photo,
              compound='bottom')
label.pack()
#label.place(x=250,y=250)
window.mainloop()# place windows on computer scree, listing for events