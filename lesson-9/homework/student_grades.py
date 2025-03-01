import csv

grades_data = [
    {"Name": "Alice", "Subject": "Math", "Grade": 85},
    {"Name": "Bob", "Subject": "Science", "Grade": 78},
    {"Name": "Carol", "Subject": "Math", "Grade": 92},
    {"Name": "Dave", "Subject": "History", "Grade": 74}
]

with open('grades.csv',mode='w',newline='') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=['Name', 'Subject', 'Grade'])
    
    writer.writeheader()
    writer.writerows(grades_data)
    # for data in grades_data:
    #     writer.writerow(data)

with open("grades.csv",mode="rt") as file:
    reader = csv.DictReader(file)
    students = list(reader)

grades={}
for student in students:
    subj=student["Subject"]
    grade=student["Grade"]
    if subj in grades:
        grades[subj].append(int(grade))
    else:
        grades[subj]=[int(grade)]

data=[]
fieldnames=["Subject","Average Grade"]
for subj,grade in grades.items():
    data.append({fieldnames[0]:subj,fieldnames[1]:sum(grade)/len(grade)})
writer=csv.DictWriter(open("average_grades.csv",mode="w",newline=''),fieldnames=fieldnames)
writer.writeheader()
writer.writerows(data)