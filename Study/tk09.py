from tkinter import *

w = Tk()
f1  = Frame(w)
f2  = Frame(w)

l1 = Label(f1, text="<label1(너비)>", bg = "white", fg = "black")
e1 = Entry(f1, text="<entry1>", bg = "white", fg = "black")
l2 = Label(f1, text="<label2(높이)>", bg = "white", fg = "black")
e2 = Entry(f1, text="<entry2>", bg = "white", fg = "black")
b1 = Button(w, text="박스 #1", bg = "white", fg = "black")
b2 = Button(w, text="박스 #2", bg = "white", fg = "black")
b3 = Button(w, text="박스 #3", bg = "white", fg = "black")
l3 = Label(f2, text="<label3(image)>", bg = "white", fg = "black")

l1.grid(row = 0, column = 0)
e1.grid(row = 0, column = 1)
l2.grid(row = 1, column = 0)
e2.grid(row = 1, column = 1)
b1.grid(row = 2, column = 1)
b2.grid(row = 2, column = 2)
b3.grid(row = 2, column = 3)


f1.pack()
f2.pack()

w.mainloop() 