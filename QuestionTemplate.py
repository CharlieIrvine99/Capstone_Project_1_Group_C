import time


class Question:
    def __init__(self, questionNumber, questionAsked, potentialAnswers, correctAnswer, questionBounty, reducedBounty):
        self.questionNumber = questionNumber
        self.questionAsked = questionAsked
        self.potentialAnswers = potentialAnswers
        self.correctAnswer = correctAnswer
        self.questionBounty = questionBounty
        self.reducedBounty = reducedBounty

    def askQuestion(self):
        global pointTotal
        print(f"Question Number {self.questionNumber}\n{self.questionAsked}")
        for answerLetter, answer in self.potentialAnswers.items():
            print(f"{answerLetter}: {answer}")
        print(f"This question is worth {self.questionBounty} points")
        userAnswer = input("Enter your answer here: ")
        if userAnswer.upper() in self.correctAnswer:
            pointTotal += self.questionBounty
            print(f"CORRECT! You now have {pointTotal} points!\n")
            return
        else:
            print(f"That is incorrect. You can however have one more attempt, you're still playing for {self.reducedBounty} point.")
            userAnswer2 = input("Enter your answer here: ")
            if userAnswer2.upper() in self.correctAnswer:
                pointTotal += self.reducedBounty
                print(f"\nWell I guess second time's the 'PyCharm'!\n\nYou now have {pointTotal} points!\n")
                return
            else:
                correct_answer_formatted = ': '.join(self.correctAnswer)
                print(
                    f"Sorry, you FAILED! The correct answer was {correct_answer_formatted}\nOnto the next question.\n\nYour point total is currently {pointTotal} points.\n")
                return


pointTotal = 0
timeToWait = 2 # While testing code change this to 0, so you can test without waiting for text to load
print("Welcome to the greatest quiz know to mankind!")
time.sleep(timeToWait)
print("The rules are simple, you will get 2 attempts to answer a question correctly.")
time.sleep(timeToWait)
print("If you get the correct answer first try you will get more points.")
time.sleep(timeToWait)
print("If you fail to answer correctly the second time, you will score no points.")
time.sleep(timeToWait)
print("Let the games begin!\n")
time.sleep(timeToWait)

questionOne = Question("1", # Here put question number
                       "How many toes does a human have?", # Here put the question you are asking
                       {"A": "8", "B": "9", "C": "10", "D": "11"}, # Here put the potential answers, obvs leaving the letters the same
                       ["C", "10"], # Change this to the correct answer
                       5, # If it is a v hard question maybe increase this
                       1) # By default, I put 0 but not set on this

time.sleep(timeToWait) # Maybe change how much time between questions?

questionTwo = Question("2", # This is obvs just a joke question for now :)
                       "How many test questions do we have?",
                       {"A": "3", "B": "4", "C": "7", "D": "10"},
                       ["D", "10"],
                       5,
                       1)

questionOne.askQuestion()
questionTwo.askQuestion()