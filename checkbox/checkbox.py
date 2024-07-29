from tkinter import *
def display():
    if(x.get()=="YES"):
        print("you agree!")
    else:
        print("your don't agree")
window = Tk()
x = StringVar()
logo_photo = PhotoImage(file='checkbox/logo.png')
check_button = Checkbutton(window,
                           text="I agree to something",
                           variable=x,
                           onvalue="YES",
                           offvalue="NO",
                           command=display,
                           font=('Arial',20),
                           fg='#00ff00',
                           bg='black',
                           activebackground='black',
                           activeforeground='#00ff00',
                           padx=25,
                           pady=25,
                           image=logo_photo,
                           compound='left')
check_button.pack()
window.mainloop()