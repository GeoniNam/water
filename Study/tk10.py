from tkinter import *

w = Tk()

counter = 0
def clicked():
    global counter
    counter += 1
    l["Text"] = '버튼 클릭 횟수:' + str(counter)
    
l = Label(w, text = "아직 눌려지지 않음")
l.pack()
b = Button(w, text = "증가", command = clicked).pack()

w.mainloop