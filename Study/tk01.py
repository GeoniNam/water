import tkinter as tk

def click():
    print("버튼클릭")
    btn.config(text="클릭했음")
    print(inputText.get())
 
def func1():
    label1.config(text="일반인")
 
def func2():
    label1.config(text="노약자")
    
root = tk.Tk()

label = tk.Label(root, text='첫번째 프로그램')
label.pack()

btn = tk.Button(root, text='버튼', command=click)
btn.pack()

label1 = tk.Label(root, text='문자열 출력')
label1.pack()

rb1 = tk.Radiobutton(root, text="일반인", command=func1)
rb2 = tk.Radiobutton(root, text="노약자", command=func2)
rb1.pack()
rb2.pack()

inputText = tk.Entry(root)
inputText.pack()
root.mainloop()