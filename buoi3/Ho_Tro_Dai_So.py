import sympy as syp
import numpy as np
import matplotlib.pyplot as plt
from tkinter import *


def matrix():
    def cal():
        A=[]
        cal=Toplevel()
        count1=int(row.get())
        count2=int(col.get())
        for i in range(count1):
            for j in range(count2):
                A[i][j]=Entry(cal,width=5).place(x=25*j,y=20)
    gui_plus=Toplevel()
    gui_plus.geometry("300x300")
    Label(gui_plus,text="Ma tran co kich thuoc: ").place(x=20,y=20)
    row=Entry(gui_plus,width=5)
    row.place(x=150,y=20)
    Label(gui_plus,text="X").place(x=175,y=20)
    col=Entry(gui_plus,width=5)
    col.place(x=200,y=20)

    Button(gui_plus,text="Tinh",comman=cal).place(x=150,y=150)







gui=Tk()
gui.geometry("300x350")
gui.title("May Tinh Dai So")
Button(gui,text="Cong ma tran",width=25,comman=matrix).pack()
Button(gui,text="Tru ma tran",width=25).pack()
Button(gui,text="Nhan ma tran",width=25).pack()
gui.mainloop()

