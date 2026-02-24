score = []
student_name = []

students = int(input('Enter the number of students :'))
for student in range(students):
    name = input(f'Enter the student name{student+1}:')
    grade = float(input(f'Enter the grade for {name}:'))
    student_name.append(name)
    score.append(grade)

max_score = max(score)
min_score = min(score)
avg = sum(score) / len(score)

print('\n___result___')
print("students :", student_name)
print('average :', avg)
print('min score :', min_score)
print('max score :', max_score)