import csv

def file_mouth_printing():
    with open('20231231.csv') as f:
        reader = csv.reader(f)
        header = reader.__next__()
        data = [row[1:] for row in reader]

    subject_scores = {}

    for row in data:
        subject = row[0]
        scores = row[1:]

        if subject not in subject_scores:
            subject_scores[subject] = []

        subject_scores[subject].append(scores)

    return subject_scores

