from tkinter import *
window = Tk()
window.title('Weight Converter')
def from_kg():
    gram = float(e2_value.get())*1000
    pound = float(e2_value.get())*2.20462
    ounce = float(e2_value.get())*35.274
    tonne = float(e2_value.get())*0.001
    t1.delete("1.0",END)
    t1.insert(END, gram)
    t2.delete("1.0", END)
    t2.insert(END, pound)
    t3.delete("1.0", END)
    t3.insert(END, ounce)
    t4.delete("1.0", END)
    t4.insert(END, tonne)
e1 = Label(window, text="Input the weight in KG",bg="Aqua",font="Helvetica")
e2_value = StringVar()
e2 = Entry(window, textvariable=e2_value)
e3 = Label(window, text="Gram",font="Helvetica",bg="red")
e4 = Label(window, text="Pound",font="Helvetica",bg="red")
e5 = Label(window, text="Ounce",font="Helvetica",bg="red")
e6 = Label(window, text="Tonne",font="Helvetica",bg="red")
t1 = Text(window, height=5, width=30,bg="Aqua")
t2 = Text(window, height=5, width=30, bg="Aqua")
t3 = Text(window, height=5, width=30, bg="Aqua")
t4 = Text(window, height=5, width=30,bg="Aqua")
b1 = Button(window, text="Convert", bg="Aqua",font='Helvetica,500',command=from_kg)
e1.grid(row=0, column=0)
e2.grid(row=0, column=1)
e3.grid(row=1, column=0)
e4.grid(row=1, column=1)
e5.grid(row=1, column=2)
e6.grid(row=1, column=3)
t1.grid(row=2, column=0)
t2.grid(row=2, column=1)
t3.grid(row=2, column=2)
t4.grid(row=2, column=3)
b1.grid(row=0, column=2)
window.mainloop()