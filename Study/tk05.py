from tkinter import *
w = Tk()

b1 = Button(w, text="박스 #1", bg = "red", fg = "white")
b2 = Button(w, text="박스 #2", bg = "green", fg = "white")
b3 = Button(w, text="박스 #3", bg = "orange", fg = "white")
b4 = Button(w, text="박스 #4", bg = "pink", fg = "white")

b1.grid(row = 0, column = 0)
b2.grid(row = 0, column = 1)
b3.grid(row = 1, column = 0)
b4.grid(row = 1, column = 1)

w.mainloop()