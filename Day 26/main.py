# double_ist = [n + n for n in range(1,5)]
# print(double_ist)

## second task

## names = ['Alex', 'Beth', 'Caroline', 'Dave', 'Eleanor', 'Freddie']
#
# # new_name_list = [name for name in names if len(name) < 5]
# #
# # print(new_name_list)
#
# #capital_name = [name.upper() for name in names if len(name) > 5]
#
# #print(capital_name)
# import random
#
# student_score = { student: random.randint(1,100) for student in names }
#
# passed_student = {name: score for (name, score) in student_score.items() if score > 60}
#
# print(passed_student)


import pandas
#
# student_dict = {
#     "student": ["eyob","angela"],
#     "score": [80,90]
# }
# student_df = pandas.DataFrame(student_dict)


## Loop through data frame
# for (key, value) in student_df.items():
#     print(value)

## Loop through row of data frame
#
# for (index, row) in student_df.iterrows():
#     #print(row.student)
#     #print(row)
#
#     if row.student == 'eyob':
#         print(row.score)


## TODO 1:
nato = pandas.read_csv('nato_phonetic_alphabet.csv')

new_dict = {row.letter: row.code for (index, row) in nato.iterrows()}

## TODO 2: Ask user
user_input = input('Enter a word: ').upper()
output = [new_dict[char] for char in user_input]
print(output)


