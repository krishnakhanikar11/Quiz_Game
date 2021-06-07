from question_model import  Question
from data import question_data
from quiz_brain import QuizBrain

# creating the list from of questions object from the Data
question_bank = []
for question in question_data:
    question_text = question["text"]
    question_answer = question["answer"]
    new_question = Question(question_text,question_answer)
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)

while quiz.still_question_left():

    quiz.next_question()
