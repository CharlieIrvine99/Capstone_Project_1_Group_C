import time

question = [
  "What is the capital of England?", "What is the square root of 16?",
  "Which fruit is commonly associated with Isaac Newton's theory of gravity?",
  "In the game of chess, which piece can only move diagonally?",
  "Which of these trees is NOT an angiosperm?"
]
answer = [['London', 'Paris', 'Rome', 'Berlin'], 
          ['2', '4', '8', '16'],
          ['Apple', 'Banana', 'Orange', 'Watermelon'],
          ['Rook', 'Knight', 'Bishop', 'King'],
          [
            'Common Laburnum', 'Siberian Crabapple', 'Maidenhair Tree',
            'Crack Willow'
          ]]
correct_answer = ['a', 'b', 'a', 'c', 'c']

player = input('What is your name?')
print("Let's play the game...", player)
time.sleep(3)
print(
  'You get 1 point for each correct answer and lose 1 point for a wrong answer.'
)
time.sleep(3)
print('You have 10 second to answer.')
time.sleep(3)
print('Choose the answer: a, b, c or d and press "Enter".')
time.sleep(3)
input("Press enter to continue")

# function to show countdown time
x = 10                                                                # start countdown from 10 second
def timing(x):
  while x >= 0:                                                        # loop every second
    timer = '{:02d}'.format(x)                                          # formating time to two digit integer
    print('_   ', timer, end="\r")                                      # displaying input and time left
    time.sleep(1)                                                      # stopping the timer every second
    x -= 1                                                              # step down every second

# function declaration to calculate score, show messages and user input
def quiz():
  score = 0                                                                  # start with the score = 0
  k = 0                                                                      # the first answer
  print('\nQuestion 1:\n')
  for i in question:                                                          # loop through all the questions
    print(i)                                                                  # print the question
    a = 97                                                                    # ASCII value of letter 'a'
    for j in answer[k]:                                                      # loop through the answers corresponding to the question
      char = chr(a)                                                          # character representation of ASCII 97
      print(char + '.', j)                                                    # printing succeding letter for the questions
      a += 1                                                                  # next letter number in alphabet
    print('\n')                                                                # break line
    timing(x)                                                                  # function timing() nested into function quiz()
    your_answer = input('\n')                                                  # user answer input
    if your_answer == correct_answer[k]:                                      # checking if the answer is correct
      score += 1                                                              # add 1 point to the score if correct
      print(f'Good! Correct answer is {correct_answer[k]}')                    # displaying the correct answer
      print(f'Correct, Your score is {score}\n')                              # presenting updated score
      k += 1                                                                  # going to the next question in the loop
      time.sleep(3)
    else:
      score -= 1                                                              # substracting 1 point if the answer was wrong
      print(f'Wrong! Correct answer is {correct_answer[k]}')
      print(
        f'You lose 1 point. Your score is {score}\n')                          # updated the score
      k += 1                                                                  # going to the next question in the loop
      time.sleep(3)
  print(f'Your final score is {score}')                                        # printing the final score

quiz()                                                                          # calling the function
