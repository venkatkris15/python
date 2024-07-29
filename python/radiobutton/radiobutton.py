import tkinter as tk

food = ["pizza", "hamburger", "hotdog"]

def order():
    if x.get() == 0:
        print("You ordered pizza!")
    elif x.get() == 1:
        print("You ordered hamburger!")
    elif x.get() == 2:
        print("You ordered hotdog!")
    else:
        print("Hum!")

window = tk.Tk()

pizzaImage = tk.PhotoImage(file=r'F:\studeys\python\project\radiobutton\pz.png')
hamburgerImage = tk.PhotoImage(file=r'F:\studeys\python\project\radiobutton\hm.png')
hotdogImage = tk.PhotoImage(file=r'F:\studeys\python\project\radiobutton\ht.png')

foodImages = [pizzaImage, hamburgerImage, hotdogImage]

x = tk.IntVar()

for index in range(len(food)):
    radiobutton = tk.Radiobutton(window,
                                  text=food[index],
                                  variable=x,
                                  value=index,
                                  padx=25,
                                  font=("Impact", 50),
                                  image=foodImages[index],
                                  indicatoron=0,
                                  width=375,
                                  command=order)
    radiobutton.pack(anchor=tk.W)

window.mainloop()
