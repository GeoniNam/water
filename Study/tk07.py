from tkinter import *

w = Tk()
f  = Frame(w)

b1 = Button(f, text="박스 #1", bg = "red", fg = "white")
b2 = Button(f, text="박스 #2", bg = "green", fg = "white")
b3 = Button(f, text="박스 #3", bg = "orange", fg = "white")
b1.pack(side = LEFT)
b2.pack(side = LEFT)
b3.pack(side = LEFT)

l = Label(w, text = "이 레이블은 버튼들 위에 배치된다.") #쉼표임

l.pack()
f.pack()

w.mainloop() 