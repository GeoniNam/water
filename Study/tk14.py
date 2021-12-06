from tkinter import *

w = Tk()

def key(event):
    print(repr(event.char), "가 눌렸습니다.")
    
def callback(event):
    frame.focus_set()
    print(event.x, event.y, "에서 마우스 이벤트가 발생")
    
frame = Frame(w, width = 100, height = 100)
frame.bind("<Key>", key)
frame.bind("<Button-1>", callback)
frame.pack()

w.mainloop()