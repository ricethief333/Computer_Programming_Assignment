#main.py

from file_mouth_print import file_mouth_printing
from graph import graph_generator

print("열람 가능 년도: 2021, 2022, 2023, 2024")
user_input_year = int(input("열람 년도 입력: "))
key = list(file_mouth_printing(user_input_year).keys())
for i in key:
    print(f"{key.index(i) + 1}. {i}")
user_input_subject = int(input("열람 과목 번호 입력: "))

def data_processing(data):
    standarized_score = []
    male = []
    female = []
    for i in data()[key[user_input_subject - 1]]:
        standarized_score.append(int(i[0]))
        male.append(int(i[1]))
        female.append(int(i[2]))

    return standarized_score, male, female

x = data_processing(file_mouth_printing)[0]
male = data_processing(file_mouth_printing)[1]
female = data_processing(file_mouth_printing)[2]
graph_generator(x, male, female)





