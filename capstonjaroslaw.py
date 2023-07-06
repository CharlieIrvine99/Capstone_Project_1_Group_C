import time

question = [
  "What is the capital of England?", "What is the square root of 16?",
  "Which fruit is commonly associated with Isaac Newton's theory of gravity?",
  "In the game of chess, which piece can only move diagonally?",
  "Which of these trees is NOT an angiosperm?"
]
answer = [['London', 'Paris', 'Rome', 'Berlin'], ['2', '4', '8', '16'],
          ['Apple', 'Banana', 'Orange', 'Watermelon'],
          ['Rook', 'Knight', 'Bishop', 'King'],
          [
            'Common Laburnum', 'Siberian Crabapple', 'Maidenhair Tree',
            'Crack Willow'
          ]]
correct_answer = ['a', 'b', 'a', 'c', 'c']

print("Let's play the game...")
time.sleep(1)
print(
  'You get 1 point for each correct answer and lose 1 point for a wrong answer.'
)
time.sleep(1)
print('Choose the answer: a, b, c or d.')
time.sleep(1)
input("Press enter to continue")

# function to show countdown time
x = 5                                                          # start countdown from 5 scond
def timing(x):                                                  
  while x:                                                      # loop every second                          
    timer = '{:02d}'.format(x)                                  # formating time to two digit integer
    print('Your have 5 seconds to answer:', timer, end="\r")    # displaying message and time
    time.sleep(1)                                               # stopping timer every second
    x -= 1                                                      # step down every second

# function declaration to calculate score, show messages and user input

def quiz():
  score = 0                                                    # start with score = 0
  k = 0                                                         # first answer
  print('\nQuestion 1:\n')
  for i in question:                                          # loop through all the questions
    print(i)                                                  # print the question
    a = 97                                                    # ASCII value of letter 'a'                      
    for j in answer[k]:                                      # loop through answers corresponding to the question
      char = chr(a)                                          # character representation of ASCII 97
      print(char + '.', j)                                    # printing succeding letter for the questions
      a += 1                                                  # next letter number in alphabet
    print('\n')                                              # break line
    timing(x)                                                # function timing() nested into function quiz()
    your_answer = input('\nYour answer is? : ')              # user answer input 
    
    if your_answer == correct_answer[k]:                    # checking if answer is correct
      score += 1                                            # addin 1 point to the score if correct
      k += 1                                                # going to the next question in the loop
      print(f'Correct, Your score is {score}\n')            # presenting updated score
    else:
      score -= 1                                            # substracting 1 pint if answer was wrong
      print(f'Wrong, you lose 1 point. Your score is {score}\n')      # updated score
  print(f'Your final score is {score}')                     # printing final score
quiz()                                                      # calling the function

                      
