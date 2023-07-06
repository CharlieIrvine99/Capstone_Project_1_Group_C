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
#time.sleep(1)
print('You will win 200,000 of... something for each correct answer.')
#time.sleep(1)
print('If you answer correctly 5 questions you will be a millionaire!')
#time.sleep(1)
print('Choose the answer: a, b, c or d.')
#time.sleep(1)


def timing(x):
  while x:
    mins, secs = divmod(x, 60)
    timer = '{:02d}:{:02d}'.format(mins, secs)
    print('Your ansewr:', timer, end="\r")
    time.sleep(1)
    x -= 1
  print('Correct, your score is:')

x = 10

def quiz():
  money = 0
  k = 0
  print('\nQuestion 1:\n')
  for i in question:
    print(i)
    a = 97  #letter 'a'
    for j in answer[k]:
      char = chr(a)
      print(char + '.', j)
      a += 1
    print('\n')
    timing(x)
    your_answer = input('\nYour answer is? : ')
    if your_answer == correct_answer[k]:
      money += 200000
      k += 1
      print(f'You have earned {money}!!!\n')
    else:
      money = 0
      print("Sorry, you have lost everything!")
      break


quiz()
