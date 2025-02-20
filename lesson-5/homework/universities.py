def enrollment_stats(universities):
    students=[]
    tuition=[]
    for i in universities:
        students.append(i[1])
        tuition.append(i[2])
    return students,tuition

mean=lambda lst: sum(lst)/len(lst)

def median(lst):
    lst.sort()
    length=len(lst)
    return lst[length//2] if length%2 else sum(lst[length//2-1:length//2+1])/2

universities = [
    ['California Institute of Technology', 2175, 37704],
    ['Harvard', 19627, 39849],
    ['Massachusetts Institute of Technology', 10566, 40732],
    ['Princeton', 7802, 37000],
    ['Rice', 5879, 35551],
    ['Stanford', 19535, 40569],
    ['Yale', 11701, 40500]
]
students,tuition=enrollment_stats(universities)
print(f"Total students: {sum(students):,}")
print(f"Total tuition: ${sum(tuition):,}")
print()
print(f"Student mean: {mean(students):,.2f}")
print(f"Student median: {median(students):,}")
print()
print(f"Tuition mean: ${mean(tuition):,.2f}")
print(f"Tuition median: ${median(tuition):,}")