import time  # imported this for use in the timer and the timeInbetweenText

pointTotal = 0  # declare this here and then use the global keyword to bring it into functions later
timeInbetweenText = 3  # change this back to 3
timeToWait = 3  # Time to wait inbetween text pops up to give the user time to read
x = 3  # change this back to 3


# Allows the user time to breath before the next question is shown.

def readyForNextQuestion():
    userReady = input("\nPlease press Enter to start")
    if userReady == "":
        print("Your next question is in...")
        timing(x)
        return
    else:  # Error control, loops back to original function to confirm user to press enter.
        print("Input not recognised")
        readyForNextQuestion()


# The same as the original function but with different wording, so it's relevant for the next question
def readyForFirstQuestion():
    userReady = input("\nPlease press Enter to start")
    if userReady == "":
        print("Your first question is in...")
        timing(x)
        return
    else:
        print("Input not recognised")
        readyForFirstQuestion()


# Timer to play inbetween each question
def timing(x):
    while x >= 0:
        # loop every second
        timer = '{:02d}'.format(x)  # formatting time to two digit integer
        print('_   ', timer, end="\r")  # displaying input and time left
        time.sleep(1)  # stopping the timer every second
        x -= 1


# Defined the object of question as a class, so we can give the values to each question. Makes it easy to add future questions
class Question:

    def __init__(self, questionNumber, questionAsked, potentialAnswers,
                 correctAnswer, questionBounty, reducedBounty):
        self.questionNumber = questionNumber
        self.questionAsked = questionAsked
        self.potentialAnswers = potentialAnswers
        self.correctAnswer = correctAnswer
        self.questionBounty = questionBounty  # we changed the value of these for the harder questions to reward more points
        self.reducedBounty = reducedBounty  # "                                                                            "

    # wording for asking a question allows a question to be asked for only having to provide the questionNumber,
    # questionAsked, potentialAnswers, correctAnswer, questionBounty, reducedBounty
    def askQuestion(self):
        global pointTotal  # brings the point total into each question so a total score at the end can be calculated
        print(
            f"\nQuestion {self.questionNumber} is worth {self.questionBounty} points"
        )
        print(f"Question Number {self.questionNumber}\n{self.questionAsked}")
        for answerLetter, answer in self.potentialAnswers.items():  # for loop to display the potential answers vertical in the console
            print(f"{answerLetter}: {answer}")
        userAnswer = input("Enter your answer here: ")
        if userAnswer.upper() in self.correctAnswer:  # .upper() to make it match correct answer which is in CAPITALS unless a number which the .upper() does not effect
            pointTotal += self.questionBounty
            print(f"CORRECT! You now have {pointTotal} points!\n")
            print("Are you ready for your next question?")
            readyForNextQuestion()  # function called here, but NOT in final question function
            return  # return to break out of function so the code can continue
        else:
            print(f"That is incorrect. You can however have one more attempt, "
                  f"you're still playing for {self.reducedBounty} points.")  # call the reducedBounty value that each question is supplied with
            userAnswer2 = input("Enter your answer here: ")
            if userAnswer2.upper() in self.correctAnswer:
                pointTotal += self.reducedBounty
                print(f"\nWell I guess second time's the 'PyCharm'!\n\n"
                      f"You now have {pointTotal} points!\n")  # changed wording to acknowledge user failed the question but has a second chance
                print("Are you ready for your next question?")
                readyForNextQuestion()
                return
            else:
                correct_answer_formatted = ': '.join(
                    self.correctAnswer)  # this displays the correct answer so the user can see it in the format e.g. D: Paris rather than {D, Paris} as it looks nicer
                print(
                    f"Sorry, you FAILED! The correct answer was {correct_answer_formatted}\n"  # changed wording to acknowledge user failed the question
                    f"Onto the next question.\n\nYour point total is currently {pointTotal} points.\n"
                )
                print("Are you ready for your next question?")
                readyForNextQuestion()
                return

    # This function is the same as the askQuestion except for the wording asking if the user is ready for the next question
    # as it wouldnt make sense as this is the final question
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
                    f"Sorry, you FAILED! The correct answer was {correct_answer_formatted}\n\nYour point total is currently {pointTotal} points.\n"
                )
                return


# Error control, makes sure the user's name is correct, and we cannot be blamed for a typo or miss-click confirming their name
def userPickName():
    name = input("Enter your name coward: ")  # A bit mean, but we're having fun with it ;)
    nameCorrect = input(
        f"Okay, so {name.capitalize()} is your name?\nPlease re-enter your name to confirm and continue: "
    )
    if nameCorrect.lower() == name.lower():
        return name
    else:
        return userPickName()  # break out of function and run it again if the user wants to enter their name again.


name = userPickName().capitalize()  # capitalizes the name so it looks a bit more pretty
print(f"\nHello & Welcome to the greatest quiz known to mankind, {name}.")
time.sleep(
    timeInbetweenText)  # call this variable so that it allows the user some time to read before next text pops up.
print(
    "\nThe rules are simple, you will get 2 attempts to answer a question correctly."
)
time.sleep(timeInbetweenText)
print("\nThere is an easy quiz and a hard quiz...")
time.sleep(timeInbetweenText)
print(
    "\nIf you choose the Easy quiz, you will get 5 points for each correct answer, otherwise, you're scraping the barrel for some consolation point.\n"
)  # explaining rules.
time.sleep(timeInbetweenText)
print(
    "If you choose the Hard quiz, you will get 10 points, and only 5 if you need to try again.\n"
    "\nAt the end, we will see if you have accumulated enough to be crowned a Champion. Let the games begin!\n"
)
time.sleep(timeInbetweenText)

# So here we have the easyQuestionOne being assigned the value of the class of Question. This makes it easy to make other
# questions if we wanted to in the future.

easyQuestionOne = Question("1", "How many toes does a human have?", {
    "A": "8",
    "B": "9",
    "C": "10",
    "D": "11"
}, ["C", "10"], 5, 2)  # Use a list function here so when we check for correct answer input from user we can use 'in'
# keyword to see if it's in this list

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

# Same as the previous questions definitions except we obviously made the questions harder and increased the score values.

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


# defined a function to run easy quiz so we can ask later if user want's to play easy or hard questions
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
    )  # displays the final score out of 25 and thanks the user for playing


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
    timing(5)  # call the timer again for more suspense
    print(
        f"{pointTotal} out of 50 on the hard quiz!\nThank you very much for playing {name}!"
    )  # here it displays the score out of 50 and thanks the user for playing


# function to allow the user to decide easy or hard, with error control to loop back to start of function if user misspells/inputs
def chooseDifficulty():
    difficulty = input(f"Well, {name}. What difficulty would you like?\n"
                       f"Please enter: Easy - or - Hard?\n")
    if difficulty.upper() == "EASY":  # .upper() so that capitalization does matter
        print("\nYou have selected the Easy quiz.")
        easyQuiz()
        return  # return statement to break out of function

    if difficulty.upper() == "HARD":  # .upper() so that capitalization does matter
        print("\nYou have selected the Hard quiz.")
        hardQuiz()
        return

    else:
        print("Sorry input unrecognized, please enter: Easy or Hard")
        chooseDifficulty(
        )  # Here it restarts the loop if the user entered it wrong. error control


chooseDifficulty()
score = str(pointTotal)  # here we make the pointTotal a str so that it gets recorded properly into the .csv as we were having trouble with that

import csv

# function to save the userScore and name on a csv file to record potential highscores from all that play.
def saveHighScore(name, score):
    with open('highScores.csv', 'a', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow([name, score])


saveHighScore(name, score)

# this displays the highScore.csv after it has recorded the users score so they can see where they rank vs previous players.
print("Here are the scores of everyone who has played this game!")
with open('highScores.csv') as file:
    scores = csv.reader(file)
    for row in scores:
        print(row) # prints the rows vertically for better visuals.
