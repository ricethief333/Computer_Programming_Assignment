#graph.py

import matplotlib.pyplot as plt

def graph_generator(x, male, female):
    fig = plt.figure()
    male_graph = fig.add_subplot(2, 1, 1)
    female_graph = fig.add_subplot(2, 1, 2)

    # x = main.data_processing(file_mouth_printing)[0]
    # male = main.data_processing(file_mouth_printing)[1]
    # female = main.data_processing(file_mouth_printing)[2]
    male_graph.bar(x, male, color='skyblue')
    female_graph.bar(x, female, color='orange')
    
    fig.suptitle('Standard Score Distribution Graph', fontsize=20)

    male_graph.set_title('Male')
    male_graph.set_ylabel('Students')
    male_graph.set_xlabel('Standard Score')

    female_graph.set_title('Female')
    female_graph.set_ylabel('Students')
    female_graph.set_xlabel('Standard Score')
    
    plt.show()