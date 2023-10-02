from tkinter import *
try:
    a = int(input('hay nhap a:'))
    b= int(input('hay nhap b:'))
    print('tong = ', a+b)
    print('hieu =',a-b)
    print('tich =',a*b)
    print('thuong = ',a/b)
except:
    print(' du lieu nhap khong dung')
    print("abc")
finally:
    print('ket thuc chuong trinh!')
    print("aaaaaaaaaaaaaaaaaaaaaaaaa")

w=Tk()
w.geometry('350x350')
w.title("may tinh")
w.show()