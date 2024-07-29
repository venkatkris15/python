from tkinter import *

count = 0

def click():
    global count
    count += 1
    print(f"{count} Hi venkat")

window = Tk()
window.title("Button Example")

photo = PhotoImage(file='F:/studeys/python/project/button/bu.png')

button = Button(window,
                text="Click me!",
                command=click,
                font=("Comic Sans MS", 30),
                fg="#00ff00",
                bg="black",
                activeforeground="#00ff00",
                activebackground="black",
                state=ACTIVE,
                image=photo,
                compound='bottom')
button.pack(padx=20, pady=20)

window.mainloop()
