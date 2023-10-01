"""Tổng số SV tham gia môn học	Sum( cột sĩ số) / thư viện numpy
-Tổng số SV đạt điểm A,B,C… 	Sum( từng cột 3,4,..)/  numpy
-Tổng số SV đạt (điểm >=D) của môn học	Tìm tổng có điều kiện của các cột A,B.. D hoặc tổng sv – tổng SV đạt F
Tìm lớp có số SV đạt >=D nhiều nhất/ ít nhất	Hàm max/ min
Tìm lớp có điểm A,B,C…  nhiều nhất/ ít nhất	Max/ min
Tìm xem điểm nào có nhiều SV đạt nhất/ ít SV nhất
TìmTBC số sv đạt điểm A,B.. của cả 9 lớp	mean
Tìm sự chênh lệch giữa só sv đạt điêm A, B… 	Phép trừ
So sánh số SV đạt bài TX1, TX2 và cuối kỳ	Sum / phép ss
So sánh số SV đạt chuẩn L1/ L2	Sum/ phép ss
Vẽ đồ thị phổ điểm từng lớp	plot
"""
import pandas as pd
from tkinter import *
import matplotlib.pyplot as plt


data=pd.read_csv("diemPython.csv")

class SV:
    def __init__(self,data):
        self.data=data

    def SV_total( self ):
        return sum(self.data["So_SV"])
    def classfition( self,type ):
        check="type "+str(type)
        return sum(self.data[check])

sinh_vien=SV(data)
"""print(sinh_vien.SV_total())
print(sinh_vien.classfition("A"))
print(sinh_vien.classfition("B"))
print(sinh_vien.classfition("C"))
print(sinh_vien.classfition("D"))
print(sinh_vien.classfition("A+"))"""
"""def quit_gui(text):
    text.quit()"""

def total():
    gui_total=Toplevel()
    gui_total.geometry("200x100")
    label=Label(gui_total,text="Tong So Sinh Vien Tham Gia La: "+str(sinh_vien.SV_total()))
    label.pack(fill="both",expand=True)
    fin_but=Button(gui_total,text="QUIT",comman=gui_total.destroy).pack()




def classfi():
    gui_class=Toplevel()
    gui_class.geometry("350x350")
    Label(gui_class,text="Tich Vao Diem Muon Kiem Tra: ").pack()

    def check():
        selected=var.get()
        result.config(text="Tong Sinh Vien Dat "+str(selected)+" La: "+str(sinh_vien.classfition(str(selected))))

    var=StringVar()
    var.set("")
    check_Apl = Radiobutton(gui_class, text = "Check Diem A+", variable = var,value="A+",comman=check)
    check_Apl.pack(fill="y")

    check_A = Radiobutton(gui_class, text = "Check Diem A", variable = var, value = "A", comman = check)
    check_A.pack(fill="y")

    check_Bpl = Radiobutton(gui_class, text = "Check Diem B+", variable = var,value="B+",comman=check)
    check_Bpl.pack(fill="y")

    check_B = Radiobutton(gui_class, text = "Check Diem B", variable = var, value = "B", comman = check)
    check_B.pack(fill="y")

    check_Cpl = Radiobutton(gui_class, text = "Check Diem C+", variable = var, value = "C+", comman = check)
    check_Cpl.pack(fill="y")

    check_C = Radiobutton(gui_class, text = "Check Diem D", variable = var, value = "C", comman = check)
    check_C.pack(fill="y")

    check_Dpl = Radiobutton(gui_class, text = "Check Diem D+", variable = var, value = "D+", comman = check)
    check_Dpl.pack(fill="y")

    check_D = Radiobutton(gui_class, text = "Check Diem D", variable = var, value = "D", comman = check)
    check_D.pack(fill="y")

    check_D = Radiobutton(gui_class, text = "Check Diem F", variable = var, value = "F", comman = check)
    check_D.pack(fill="y")
    result=Label(gui_class,text="")
    result.pack()
    Label(gui_class,text="",width=20)
    fin_but = Button(gui_class, text = "QUIT", comman = gui_class.destroy).pack()

def graph():
    gui_graph=Toplevel()
    gui_graph.geometry("250x300")
    def show():
         print(data["Ma_lop"])

    var=
    _1 = Radiobutton(gui_graph, text = "Lop 20222FE6051001",comman=show).pack()
    _2 = Radiobutton(gui_graph, text = "Lop 20222FE6051002",comman=show).pack()
    _3 = Radiobutton(gui_graph, text = "Lop 20222FE6051003",comman=show).pack()
    _4 = Radiobutton(gui_graph, text = "Lop 20222FE6051004",comman=show).pack()
    _5 = Radiobutton(gui_graph, text = "Lop 20222FE6051005",comman=show).pack()
    _6 = Radiobutton(gui_graph, text = "Lop 20222FE6051006",comman=show).pack()
    _7 = Radiobutton(gui_graph, text = "Lop 20222FE6051007",comman=show).pack()
    _8 = Radiobutton(gui_graph, text = "Lop 20222FE6051008",comman=show).pack()
    _9 = Radiobutton(gui_graph, text = "Lop 20222FE6051009",comman=show).pack()



gui=Tk()
gui.geometry("250x450")
gui.title("Thong Ke Sinh Vien")

but_total=Button(gui,text="Tong So Sinh Vien Tham Gia",width=27,comman=total).pack()
but_classfition=Button(gui,text="Phan Loai Sinh Vien Theo Diem",width=27,comman=classfi).pack()
but_graph=Button(gui,text="Pho Diem Tung Lop",width=27,comman=graph).pack()




gui.mainloop()