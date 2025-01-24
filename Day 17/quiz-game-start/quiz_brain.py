class QuizBrain:
    def __init__(self, question_list):
        self.question_number = 0
        self.question_list = question_list
        self.score = 0

    def still_has_question(self):
        return self.question_number < len(self.question_list)

    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(f'Q.{self.question_number}: {current_question.text}. (True/False)?: ')
        self.check_answer(current_question.answer, user_answer)


    def check_answer(self, correct_answer, user_answer):
        if correct_answer.lower() == user_answer.lower():
            print('You got it right!')
            self.score += 1
            print(f'Your current score is {self.score}/{self.question_number}')
        else:
            print(f'Incorrect Answer: {user_answer}')
        print(f'The correct answer is: {correct_answer}')