#main.py

from file_mouth_print import file_mouth_printing
from graph import graph_generator

user_input_year = int(input("열람 년도 입력: "))
user_input_subject = input("열람 과목 입력: ")

def data_processing(data):
    standarized_score = []
    male = []
    female = []
    for i in data()[user_input_subject]:
        standarized_score.append(int(i[0]))
        male.append(int(i[1]))
        female.append(int(i[2]))

    return standarized_score, male, female

x = data_processing(file_mouth_printing)[0]
male = data_processing(file_mouth_printing)[1]
female = data_processing(file_mouth_printing)[2]
graph_generator(x, male, female)





