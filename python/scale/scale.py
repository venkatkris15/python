from tkinter import *

def submit():
    temperature = temperature_scale.get()
    print(f"Temperature is: {temperature} degrees C")

window = Tk()

# Define file paths with raw string literals for Windows
hot_image_path = r'F:\studeys\python\project\scale\flame.png'
cold_image_path = r'F:\studeys\python\project\scale\sh.png'

# Load images
hot_image = PhotoImage(file=hot_image_path)
cold_image = PhotoImage(file=cold_image_path)

# Display hot image
hot_label = Label(window, image=hot_image)
hot_label.pack()

# Create temperature scale (from 100 to 0)
temperature_scale = Scale(window,
                          from_=100,
                          to=0,
                          length=600,
                          orient=VERTICAL,
                          font=('Consolas', 20),
                          tickinterval=10,
                          resolution=5,
                          troughcolor='#69eaff',
                          fg='#ff1c00',
                          bg='#111111')
temperature_scale.pack()

# Display cold image
cold_label = Label(window, image=cold_image)
cold_label.pack()

# Submit button
button = Button(window, text='Submit', command=submit)
button.pack()

window.mainloop()
