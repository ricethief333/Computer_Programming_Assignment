import csv

def file_mouth_printing(year):
    file = f'{year - 1}1231.csv'

    with open(file) as f:
        reader = csv.reader(f)
        reader.__next__()
        data = [row[1:] for row in reader]

    subject_scores = {}

    for row in data:
        subject = row[0]
        scores = row[1:]

        scores = [number.strip() for number in scores]

        if subject not in subject_scores:
            subject_scores[subject] = []

        subject_scores[subject].append(scores)

    return subject_scores