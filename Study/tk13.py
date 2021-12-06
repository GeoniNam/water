from tkinter import *

w = Tk()
w.geometry("600x200")

def callback(event):
    print(event.x, event.y, "에서 마우스 이벤트 발생")
    
w.bind("<Button-1>", callback)
w.mainloop()