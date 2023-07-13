import time

pointTotal = 0
timeInbetweenText = 3  # change this back to 3
timeToWait = 3
x = 3  # change this back to 3


def readyForNextQuestion():
  userReady = input("\nPlease press Enter to start")
  if userReady == "":
    print("Your next question is in...")
    timing(x)
    return
  else:
    print("Input not recognised")
    readyForNextQuestion()


def readyForFirstQuestion():
  userReady = input("\nPlease press Enter to start")
  if userReady == "":
    print("Your first question is in...")
    timing(x)
    return
  else:
    print("Input not recognised")
    readyForFirstQuestion()


def timing(x):
  while x >= 0:
    # loop every second
    timer = '{:02d}'.format(x)  # formating time to two digit integer
    print('_   ', timer, end="\r")  # displaying input and time left
    time.sleep(1)  # stopping the timer every second
    x -= 1


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
    print(
      f"\nQuestion {self.questionNumber} is worth {self.questionBounty} points"
    )
    print(f"Question Number {self.questionNumber}\n{self.questionAsked}")
    for answerLetter, answer in self.potentialAnswers.items():
      print(f"{answerLetter}: {answer}")
    userAnswer = input("Enter your answer here: ")
    if userAnswer.upper() in self.correctAnswer:
      pointTotal += self.questionBounty
      print(f"CORRECT! You now have {pointTotal} points!\n")
      print("Are you ready for your next question?")
      readyForNextQuestion()
      return
    else:
      print(f"That is incorrect. You can however have one more attempt, "
            f"you're still playing for {self.reducedBounty} points.")
      userAnswer2 = input("Enter your answer here: ")
      if userAnswer2.upper() in self.correctAnswer:
        pointTotal += self.reducedBounty
        print(f"\nWell I guess second time's the 'PyCharm'!\n\n"
              f"You now have {pointTotal} points!\n")
        print("Are you ready for your next question?")
        readyForNextQuestion()
        return
      else:
        correct_answer_formatted = ': '.join(self.correctAnswer)
        print(
          f"Sorry, you FAILED! The correct answer was {correct_answer_formatted}\n"
          f"Onto the next question.\n\nYour point total is currently {pointTotal} points.\n"
        )
        print("Are you ready for your next question?")
        readyForNextQuestion()
        return

  def askFinalQuestion(self):
    global pointTotal
    print(
      f"\nQuestion {self.questionNumber} is worth {self.questionBounty} points"
    )
    print(f"Question Number {self.questionNumber}\n{self.questionAsked}")
    for answerLetter, answer in self.potentialAnswers.items():
      print(f"{answerLetter}: {answer}")
    userAnswer = input("Enter your answer here: ")
    if userAnswer.upper() in self.correctAnswer:
      pointTotal += self.questionBounty
      print(f"CORRECT! You now have {pointTotal} points!\n")
      return
    else:
      print(
        f"That is incorrect. You can however have one more attempt, you're still playing for {self.reducedBounty} points."
      )
      userAnswer2 = input("Enter your answer here: ")
      if userAnswer2.upper() in self.correctAnswer:
        pointTotal += self.reducedBounty
        print(
          f"\nWell I guess second time's the 'PyCharm'!\n\nYou now have {pointTotal} points!\n"
        )
        return
      else:
        correct_answer_formatted = ': '.join(self.correctAnswer)
        print(
          f"Sorry, you FAILED! The correct answer was {correct_answer_formatted}\nOnto the next question.\n\nYour point total is currently {pointTotal} points.\n"
        )
        return


def userPickName():
  name = input("Enter your name coward: ")
  nameCorrect = input(
    f"Okay, so {name.capitalize()} is your name?\nPlease re-enter your name to confirm and continue: "
  )
  if nameCorrect.lower() == name.lower():
    return name
  else:
    return userPickName()


name = userPickName().capitalize()
print(f"\nHello & Welcome to the greatest quiz known to mankind, {name}.")
time.sleep(timeInbetweenText)
print(
  "\nThe rules are simple, you will get 2 attempts to answer a question correctly."
)
time.sleep(timeInbetweenText)
print("\nThere is an easy quiz and a hard quiz...")
time.sleep(timeInbetweenText)
print(
  "\nIf you choose the Easy quiz, you will get 5 points for each correct answer, otherwise, you're scraping the barrel for a consolation point.\n"
)
time.sleep(timeInbetweenText)
print(
  "If you choose the Hard quiz, you will get 10 points, and only 5 if you need to try again.\n"
  "\nAt the end, we will see if you have accumulated enough to be crowned a Champion. Let the games begin!\n"
)
time.sleep(timeInbetweenText)

easyQuestionOne = Question("1", "How many toes does a human have?", {
  "A": "8",
  "B": "9",
  "C": "10",
  "D": "11"
}, ["C", "10"], 5, 2)

easyQuestionTwo = Question("2", "What is the capital of France?", {
  "A": "London",
  "B": "Madrid",
  "C": "Berlin",
  "D": "Paris"
}, ["D", "PARIS"], 5, 2)

easyQuestionThree = Question("3", "Which fruit shares its name with a colour?",
                             {
                               "A": "Orange",
                               "B": "Starfruit",
                               "C": "Banana",
                               "D": "Apple"
                             }, ["A", "ORANGE"], 5, 2)

easyQuestionFour = Question(
  "4", "Who won the most gold medals in history?", {
    "A": "Michael Phelps",
    "B": "Usain Bolt",
    "C": "Larisa Latynina",
    "D": "Christ Hoy"
  }, ["A", "MICHAEL PHELPS"], 5, 2)

easyQuestionFive = Question(
  "5", "In the game of chess, which piece can only move diagonally?", {
    "A": "Rook",
    "B": "Knight",
    "C": "Bishop",
    "D": "King"
  }, ["C", "ROOK"], 5, 2)

hardQuestionOne = Question(
  "1", "What is it called when a function is defined in a class?", {
    "A": "Module",
    "B": "Class",
    "C": "Function",
    "D": "Method"
  }, ["D", "METHOD"], 10, 5)

hardQuestionTwo = Question(
  "2", "Who developed the Python language?", {
    "A": "Albert Einstein",
    "B": "Bill Gates",
    "C": "Wick Von Rossum",
    "D": "Gregor Mendel"
  }, ["C", "WICK VON ROSSUM"], 10, 5)

hardQuestionThree = Question(
  "3", "Which of the following is the correct extension of the Python file?", {
    "A": ".python",
    "B": ".py",
    "C": ".p",
    "D": "None of these"
  }, ["B", ".PY"], 10, 5)

hardQuestionFour = Question(
  "4", "What do we use to define a block of code in Python?", {
    "A": "Indentation",
    "B": "Key",
    "C": "Curly Brackets",
    "D": "Square Brackets"
  }, ["A", "INDENTATION"], 10, 5)

hardQuestionFive = Question("5", "Who has the most PyCharm?", {
  "A": "Harbi",
  "B": "Delawar",
  "C": "Charlie",
  "D": "Merbaan"
}, ["C", "CHARLIE"], 10, 5)


def easyQuiz():
  readyForFirstQuestion()
  easyQuestionOne.askQuestion()
  easyQuestionTwo.askQuestion()
  easyQuestionThree.askQuestion()
  easyQuestionFour.askQuestion()
  easyQuestionFive.askFinalQuestion()
  print(
    "Congratulations on completing the quiz! Your final score is...\n*Drumroll*"
  )
  timing(5)
  print(
    f"{pointTotal} out of 25 on the easy quiz!\nThank you very much for playing {name}!"
  )


def hardQuiz():
  readyForFirstQuestion()
  hardQuestionOne.askQuestion()
  hardQuestionTwo.askQuestion()
  hardQuestionThree.askQuestion()
  hardQuestionFour.askQuestion()
  hardQuestionFive.askFinalQuestion()
  print(
    "Congratulations on completing the quiz! Your final score is...\n*Drumroll*"
  )
  timing(5)
  print(
    f"{pointTotal} out of 50 on the hard quiz!\nThank you very much for playing {name}!"
  )


def chooseDifficulty():
  difficulty = input(f"Well, {name}. What difficulty would you like?\n"
                     f"Please enter: Easy - or - Hard?\n")
  if difficulty.upper() == "EASY":
    print("\nYou have selected the Easy quiz.")
    easyQuiz()
    return

  if difficulty.upper() == "HARD":
    print("\nYou have selected the Hard quiz.")
    hardQuiz()
    return

  else:
    print("Sorry input unrecognized, please enter: Easy or Hard")
    chooseDifficulty(
    )  # Here it restarts the loop if the user entered it wrong.


chooseDifficulty()
score = str(pointTotal)

import csv


def saveHighScore(name, score):
  with open('highScores.csv', 'a', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow([name, score])

saveHighScore(name, score)

print("Here are the scores of everyone who has played this game!")
with open('highScores.csv') as file:
  scores = csv.reader(file)
  for row in scores:
    print(row)



