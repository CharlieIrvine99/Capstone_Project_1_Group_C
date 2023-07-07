pointTotal = 0 # Declaring point total outside of function so multiple fucntions can refer back to it

def questionOne():
    questionBounty = 3 # This can obvs be changed for harder or easier questions
    global pointTotal #global keyword to bring pointTotal into this function so it can be used later
    correctAnswer = ["B", "7"] # Made this a variable so it will be easier to change for future questions

    askQuestion = "Question 1!\n\nHow many continents are there in the world?\n"
    print(askQuestion) # Same with this tbf

    questionAnswers = {"A": "6", "B": "7", "C": "8", "D": "9"}
    for answerLetter, answer in questionAnswers.items():
        print(answerLetter + ": " + answer) # This prints the dict(questionAnswers) vertically
    userAnswer = input("\nEnter your answer here: ")
    if userAnswer.upper() in correctAnswer: 
        print("Very good, you got it correct!")
        pointTotal += questionBounty
        print(f"Your new point total is {pointTotal}!")
        return # Used return to break out before questionOneRepeat gets run, within this function
    else:
        print("\nSorry, that is not correct. You may try again, for reduced points.\n")

    questionOneRepeat()

def questionOneRepeat():
    questionBounty = 1  # Reduced points for retry, could maybe even give two retrys?
    global pointTotal
    correctAnswer = ["B", "7"] # Couldn't use global keyword, had to bring this into the function

    questionAnswers = {"A": "6", "B": "7", "C": "8", "D": "9"}
    print("\nAsking the question again:") # Maybe change the wording on this line???
    for answerLetter, answer in questionAnswers.items():
        print(answerLetter + ": " + answer)
    userAnswer = input("\nEnter your answer here: ")
    if userAnswer.upper() in correctAnswer: 
        print("Second time's the 'PyCharm' I suppose!")
        pointTotal += questionBounty
        print(f"Your new point total is {pointTotal}!")
        return
    else:
        print("\nSorry, that is not correct. No points awarded for this question.")

questionOne()