import pandas as pd



# Tong so sv tham gia mon hoc
def total_students_participated(data):
    return data['So_SV'].sum()

# tong sv dat dc A, B, C, ...
def total_students_achieved_grade(data,grade):
    return data[data[f'type {grade}'] > 0]['So_SV'].sum()

# Hàm tính tổng số SV đạt điểm >=D
def total_students_achieved_D_and_above(data):
    return data[data['type D'] > 0]['So_SV'].sum()

# Hàm tìm lớp có số SV đạt >=D nhiều nhất
def class_with_most_students_achieved_D(data):
    max_students = data[data['type D'] == df['type D'].max()]
    return max_students['Ma_lop'].tolist()

# Hàm tìm lớp có điểm A, B, C... nhiều nhất
def class_with_most_students_achieved_grade(data,grade):
    max_students = data[data[f'type {grade}'] == df[f'type {grade}'].max()]
    return max_students['Ma_lop'].tolist()



#names=['STT','Ma_lop','So_SV',"A+","A","B+","B","C+","C","D+","D","F","L1","L2","TX1","TX2","CUOI KI"]
data=pd.read_csv('diemPython.csv')

print(total_students_participated(data))