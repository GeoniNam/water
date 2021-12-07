import pymysql
from tkinter import *
from tkinter import messagebox


##함수 선언부
def insertData():
    conn, cur = None, None
    data1, data2, data3, data4 = "", "", "", ""
    sql = ""
    conn = pymysql.connect(host = '127.0.0.1', user = 'root', password = '1234', db = 'hanbitDB', charset = 'utf8')
    cur = conn.cursor()
    
    
    data1 = edt1,get(); data2 = edt2,get(); data3 = edt3,get(); data4 = edt4,get()
    try :
        sql = "INSERT INTO userTable VALUES('" + data1 +"', '"+ data2 + "','"+ data3 +"', "+ data4+")"
        cur.execute(sql)
    except :
        messagebox.showerror('오류', '데이터 입력 오류가 발생함')
    else :
        messagebox.showinfo('성공', '데이터 입력 성공')
    conn.commit()
    conn.close()
   
def selectData():
    strData1, strData2, strData3, strData4 = [], [], [], []
    conn = pymysql.connect(host = '127.0.0.1', user = 'root', password = '1234', db = 'hanbitDB', charset = 'utf8')
    cur = conn.cursor()
    cur.execute("SELECT*FROM userTable")
    strData1.append("사용자 ID");     strData2.append("사용자 이름");    strData3.append("이메일");       strData4.append("출생년도")
    strData1.append("---------------");     strData2.append("---------------")    
    strData3.append("---------------");     strData4.append("---------------")
    
    while (True) :
        row = cur.fetchone()
        if row==None:
            break;
    strData1.append(row(0));     strData2.append(row(1))   
    strData3.append(row(2));     strData4.append(row(3))
    
    listData1.delete(0, listData1.size() -1);    listData2.delete(0, listData2.size() -1)
    listData3.delete(0, listData3.size() -1);    listData4.delete(0, listData4.size() -1)
    for item1, item2, item3, item4 in zip(strData1, strData2, strData3, strData4):
        listData1.insert(END, item1);    listData2.insert(END, item2)
        listData3.insert(END, item3);    listData4.insert(END, item4)
    conn.close()

    ##메인코드부
w = Tk()
w.geometry("600x300")
w.title("GUI 데이터 입력")

edtFrame = Frame(w);
edtFrame.pack()
listFrame = Frame(w)
listFrame.pack(side = BOTTOM, fill = BOTH, expand = 1) #fill은 다 채우는거 expand는 내부에서만 확장, expane=1은 yes

edt1 = Entry(edtFrame,width = 10); edt1.pack(side = LEFT,padx = 10, pady = 10) #pad는 내부
edt2 = Entry(edtFrame,width = 10); edt2.pack(side = LEFT,padx = 10, pady = 10)
edt3 = Entry(edtFrame,width = 10); edt3.pack(side = LEFT,padx = 10, pady = 10)
edt4 = Entry(edtFrame,width = 10); edt4.pack(side = LEFT,padx = 10, pady = 10)

btnInsert = Button(edtFrame, text = "입력", command = insertData)
btnInsert.pack(side = LEFT, padx = 10, pady = 10)
btnSelect = Button(edtFrame, text = "조회", command = selectData)
btnSelect.pack(side = LEFT, padx = 10, pady = 10)

listData1 = Listbox(listFrame, bg = 'yellow')
listData1.pack(side = LEFT, fill = BOTH, expand = 1)
listData2 = Listbox(listFrame, bg = 'yellow')
listData2.pack(side = LEFT, fill = BOTH, expand = 1)
listData3 = Listbox(listFrame, bg = 'yellow')
listData3.pack(side = LEFT, fill = BOTH, expand = 1)
listData4 = Listbox(listFrame, bg = 'yellow')
listData4.pack(side = LEFT, fill = BOTH, expand = 1)

w.mainloop() 