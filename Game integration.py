pointTotal = 0
#Timerfunction
import time
# function to show countdown time
x = 10  # start countdown from 10 second


def timing(x):
  while x >= 0:
    # loop every second
    timer = '{:02d}'.format(x)  # formating time to two digit integer
    print('_   ', timer, end="\r")  # displaying input and time left
    time.sleep(1)  # stopping the timer every second
    x -= 1


# step down every second


class Question:

  def __init__(self, questionNumber, questionAsked, potentialAnswers,
               correctAnswer, questionBounty, reducedBounty):
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
      print(f"CORRECT! You now have {pointTotal} points!")
      return
    else:
      print(
        "That is incorrect. You can however have one more attempt for reduced points."
      )
      userAnswer2 = input("Enter your answer here: ")
      if userAnswer2.upper() in self.correctAnswer:
        pointTotal += self.reducedBounty
        print(
          f"\nWell I guess second time's the 'PyCharm!\nYou now have {pointTotal} point!"
        )
        return
      else:
        print("Sorry you FAILED! Onto the next question.")
        return


questionOne = Question("1", "How many toes does a human have?", {
  "A": "8",
  "B": "9",
  "C": "10",
  "D": "11"
}, ["C", "10"], 5, 1)

questionOne.askQuestion()
