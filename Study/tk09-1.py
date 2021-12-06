from tkinter import *

w = Tk()
f1  = Frame(w)
f2  = Frame(w)

l1 = Label(f1, text="<label1(너비)>")
e1 = Entry(f1)
l2 = Label(f1, text="<label2(높이)>")
e2 = Entry(f1)
l1.grid(row = 0, column = 0)
e1.grid(row = 0, column = 1)
l2.grid(row = 1, column = 0)
e2.grid(row = 1, column = 1)
f1.grid(row = 0, column = 0)

l3 = Label(w, text = "이미지")
l3.grid(row = 0, column = 1)        
          

b1 = Button(w, text="박스 #1(이미지 저장)")
b1.grid(row = 1, column = 0)
b2 = Button(f2, text="박스 #2(확대)")
b3 = Button(f2, text="박스 #3(축소)")
b2.pack(side = LEFT)
b3.pack(side = LEFT)
f2.grid(row = 1, column = 1)

w.mainloop() 