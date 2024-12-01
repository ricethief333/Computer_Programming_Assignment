#main.py

from file_mouth_print import file_mouth_printing
from graph import graph_generator

print("열람 가능 년도: 2024")
user_input_year = int(input("열람 년도 입력: "))
print("열람 가능 과목: [국어, 수학, 생활과 윤리, 윤리와 사상, 한국지리, 세계지리, 동아시아사, 세계사, 경제, 정치와 법, 사회·문화, 물리학 I, 화학 I, 생명과학 I, 지구과학 I, 물리학 II, 화학 II, 생명과학 II, 지구과학 II, 성공적인 직업생활, 농업 기초 기술, 공업 일반, 상업 경제, 수산·해운 산업 기초, 인간 발달]")
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





