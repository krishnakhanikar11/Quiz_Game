class QuizBrain:

    # Attribute: Attributes are variables of a class that are shared between all of its instances.
    def __init__(self,q_list):
        self.question_number = 0
        self.question_list = q_list
        self.user_score = 0

    # Method: A method is a function that “belongs to” an object.
    def still_question_left(self):
        if self.question_number < len(self.question_list):
            return True
        else:
            return False

    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        user_ans = input(f"Q.{self.question_number}: {current_question.text}.(True/False): ")
        self.check_answer(user_ans,current_question.answers)

    def check_answer(self, user_ans, correct_answer):
        if user_ans.lower() == correct_answer.lower():
            print("You got it right")
            self.user_score += 1

        else:
            print("That's wrong")

        print(f"The correct answer was : {correct_answer}.")
        print(f"Your current score is {self.user_score}/{self.question_number})")
        print("\n")