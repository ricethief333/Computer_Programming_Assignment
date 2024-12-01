#main.py

from file_mouth_print import file_mouth_printing

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







