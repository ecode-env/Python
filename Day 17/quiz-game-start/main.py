from question_model import Question
from data import question_data
from quiz_brain import QuizBrain



question_bank = []

for question in question_data:
    question_object = Question(question["text"], question["answer"])
    question_bank.append(question_object)


user_1 = QuizBrain(question_bank)
while user_1.still_has_question():
    user_1.next_question()
print('You have completed the quiz.')
print(f'Your final score was: {user_1.score}/{user_1.question_number}')