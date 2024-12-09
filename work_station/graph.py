#graph.py

import matplotlib.pyplot as plt

def graph_generator(x, male, female):
    fig = plt.figure()
    grade = fig.add_subplot(1, 1, 1)

    # x = main.data_processing(file_mouth_printing)[0]
    # male = main.data_processing(file_mouth_printing)[1]
    # female = main.data_processing(file_mouth_printing)[2]
    grade.plot(x, male, 'b-', label = 'Male')
    grade.plot(x, female, 'r-', label = 'Female')
    grade.legend(loc='best')

    grade.set_title('Standard Score Distribution Graph')
    grade.set_ylabel('Students')
    grade.set_xlabel('Standard Score')
    
    plt.show()