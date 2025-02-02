# double_ist = [n + n for n in range(1,5)]
# print(double_ist)

## second task

names = ['Alex', 'Beth', 'Caroline', 'Dave', 'Eleanor', 'Freddie']

# new_name_list = [name for name in names if len(name) < 5]
#
# print(new_name_list)

#capital_name = [name.upper() for name in names if len(name) > 5]

#print(capital_name)
import random

student_score = { student: random.randint(1,100) for student in names }

passed_student = {name: score for (name, score) in student_score.items() if score > 60}

print(passed_student)

