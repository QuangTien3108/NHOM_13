import pandas
import pandas as pd

#names=['STT','Ma_lop','So_SV',"A+","A","B+","B","C+","C","D+","D","F","L1","L2","TX1","TX2","CUOI KI"]
data=pandas.read_csv('diemPython.csv')
#print(data)
def kiem_tra_diem(diem):
    return diem >= 4
def TongsoSV(data):
    SV_total = data.groupby('Ma_lop')[ 'So_SV' ].sum().reset_index()

    #SV_join=data[data['So_SV']>0]
    #SV_total=len(SV_join)
    return SV_total

print(TongsoSV(data))
