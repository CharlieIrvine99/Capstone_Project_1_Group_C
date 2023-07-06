cashPot = 0


def questionOne():
  global cashPot
  questionOneAnswerList = {"A": 3, "B": 4, "C": 5, "D": 6}
  questionOneBounty = 100
  print("\nQuestion 1:\n")

  answer = input(
    f"What is 2+2?\n\n{questionOneAnswerList}\n\nEnter your answer here: ")
  correctAnswer = "B" if answer.upper() in questionOneAnswerList \
      else "4"

  if answer.upper() != correctAnswer.upper():
    print(
      f"\nAnswer not correct, no money added. Your final cash pot is £{cashPot}"
      f"\n\nThanks for playing 'Charlie's' Who Wants To Be A Millionaire")
    exit()
  else:

    cashPot += questionOneBounty
    print(f"\nAnswer correct! £{questionOneBounty} added to the cash pot!")
    print(f"Your cash pot is now: £{cashPot}")


def questionTwo():
  global cashPot
  questionTwoAnswerList = {
    "A": "Liverpool",
    "B": "Manchester",
    "C": "London",
    "D": "Cardiff"
  }
  questionTwoBounty = 100
  print("\nQuestion 2:\n")

  answer = input(
    f"What is the capital of England?\n\n{questionTwoAnswerList}\n\nEnter your answer here: "
  )
  correctAnswer = "C" if answer.upper() in questionTwoAnswerList \
      else "London"

  if answer.upper() != correctAnswer.upper():
    print(
      f"\nAnswer not correct, no money added. Your final cash pot is £{cashPot}"
      f"\n\nThanks for playing 'Charlie's' Who Wants To Be A Millionaire")
    exit()
  else:

    cashPot += questionTwoBounty
    print(f"\nAnswer correct! £{questionTwoBounty} added to the cash pot!")
    print(f"Your cash pot is now: £{cashPot}")


def questionThree():
  global cashPot
  questionThreeAnswerList = {
    "A": "Avatar: The Way of Water",
    "B": "Top Gun: Maverick",
    "C": "Jurassic World: Dominion",
    "D": "Doctor Strange in the Multiverse of madness"
  }
  questionThreeBounty = 100
  print("\nQuestion 3:\n")

  answer = input(
    f"What was the highest grossing movie of 2022?\n\n{questionThreeAnswerList}\n\nEnter your answer here: "
  )
  correctAnswer = "A" if answer.upper() in questionThreeAnswerList \
      else "Avatar: The Way of Water"

  if answer.upper() != correctAnswer.upper():
    print(
      f"\nAnswer not correct, no money added. Your final cash pot is £{cashPot}"
      f"\n\nThanks for playing 'Charlie's' Who Wants To Be A Millionaire")
    exit()
  else:

    cashPot += questionThreeBounty
    print(f"\nAnswer correct! £{questionThreeBounty} added to the cash pot!")
    print(f"Your cash pot is now: £{cashPot}")


def questionFour():
  global cashPot
  questionFourAnswerList = {"A": "1", "B": "2", "C": "3", "D": "4"}
  questionFourBounty = 200
  print("\nQuestion 4:\n")

  answer = input(
    f"How many of Henry VIII's wives were called Catherine?\n\n{questionFourAnswerList}\n\nEnter your answer here: "
  )
  correctAnswer = "C" if answer.upper() in questionFourAnswerList \
      else "3"

  if answer.upper() != correctAnswer.upper():
    print(
      f"\nAnswer not correct, no money added. Your final cash pot is £{cashPot}"
      f"\n\nThanks for playing 'Charlie's' Who Wants To Be A Millionaire")
    exit()
  else:
    cashPot += questionFourBounty
    print(f"\nAnswer correct! £{questionFourBounty} added to the cash pot!")
    print(f"Your cash pot is now: £{cashPot}")


def questionFive():
  global cashPot
  questionFiveAnswerList = {
    "A": "NuttyBar",
    "B": "Feast",
    "C": "Chomper",
    "D": "Marathon"
  }
  questionFiveBounty = 500
  print("\nQuestion 5:\n")

  answer = input(
    f"Very good for getting this far!\n"
    f"What was the old name for a Snickers bar before it changed in 1990?\n\n{questionFiveAnswerList}\n\nEnter your answer here: "
  )
  correctAnswer = "D" if answer.upper() in questionFiveAnswerList \
      else "Marathon"

  if answer.upper() != correctAnswer.upper():
    print(
      f"\nAnswer not correct, no money added. Your final cash pot is £{cashPot}"
      f"\n\nThanks for playing 'Charlie's' Who Wants To Be A Millionaire")
    exit()
  else:
    cashPot += questionFiveBounty
    print(f"\nAnswer correct! £{questionFiveBounty} added to the cash pot!")
    print(f"Your cash pot is now: £{cashPot}")


def questionSix():
  global cashPot
  questionSixAnswerList = {
    "A": "Christian Bale",
    "B": "Robert Pattinson",
    "C": "Matt Damon",
    "D": "Ben Affleck"
  }
  questionSixBounty = 1000
  print("\nQuestion 6:\n")

  answer = input(
    f"\nWow! I cannot believe you got that right, you're so smart!\n"
    f"Which British actor played Batman in 2022's reboot directed by Matt Reeves?\n\n{questionSixAnswerList}\n\nEnter your answer here: "
  )
  correctAnswer = "B" if answer.upper() in questionSixAnswerList \
      else "Robert Pattinson"

  if answer.upper() != correctAnswer.upper():
    print(
      f"\nAnswer not correct, no money added. Your final cash pot is £{cashPot}"
      f"\n\nThanks for playing 'Charlie's' Who Wants To Be A Millionaire")
    exit()
  else:
    cashPot += questionSixBounty
    print(f"\nAnswer correct! £{questionSixBounty} added to the cash pot!")
    print(f"Your cash pot is now: £{cashPot}")


def questionSeven():
  global cashPot
  questionSevenAnswerList = {
    "A": "Pepsi",
    "B": "Irn-Bru",
    "C": "Tango",
    "D": "7UP"
  }
  questionSevenBounty = 2000
  print("\nQuestion 7:\n")

  answer = input(
    f"\nYou're doing very goooooood. Keep it up my friend!\n"
    f"Which soft drink is commonly associated with Scotland?\n\n{questionSevenAnswerList}\n\nEnter your answer here: "
  )
  correctAnswer = "B" if answer.upper() in questionSevenAnswerList \
      else "Irn-Bru"

  if answer.upper() != correctAnswer.upper():
    print(
      f"\nAnswer not correct, no money added. Your final cash pot is £{cashPot}"
      f"\n\nThanks for playing 'Charlie's' Who Wants To Be A Millionaire")
    exit()
  else:
    cashPot += questionSevenBounty
    print(f"\nAnswer correct! £{questionSevenBounty} added to the cash pot!")
    print(f"Your cash pot is now: £{cashPot}")


def questionEight():
  global cashPot
  questionEightAnswerList = {
    "A": "Istanbul",
    "B": "Kabul",
    "C": "Karachi",
    "D": "Islamabad"
  }
  questionEightBounty = 4000
  print("\nQuestion 8:\n")

  answer = input(
    f"\nI'm gonna be telling all the people down at the pub about how well you've done!\n"
    f"What is the Capital of Pakistan?\n\n{questionEightAnswerList}\n\nEnter your answer here: "
  )
  correctAnswer = "D" if answer.upper() in questionEightAnswerList \
      else "Islamabad"

  if answer.upper() != correctAnswer.upper():
    print(
      f"\nAnswer not correct, no money added. Your final cash pot is £{cashPot}"
      f"\n\nThanks for playing 'Charlie's' Who Wants To Be A Millionaire")
    exit()
  else:
    cashPot += questionEightBounty
    print(f"\nAnswer correct! £{questionEightBounty} added to the cash pot!")
    print(f"Your cash pot is now: £{cashPot}")


def questionNine():
  global cashPot
  questionNineAnswerList = {
    "A": "A wild Homer Simpson",
    "B": "An elephant's dung",
    "C": "A tree over 6 meters wide",
    "D": "A female deer"
  }
  questionNineBounty = 8000
  print("\nQuestion 9:\n")

  answer = input(
    f"\nRight if you get this one you're like a 9/10 smart!\n"
    f"In the animal kingdom what is a Doe?\n\n{questionNineAnswerList}\n\nEnter your answer here: "
  )
  correctAnswer = "D" if answer.upper() in questionNineAnswerList \
      else "A female deer"

  if answer.upper() != correctAnswer.upper():
    print(
      f"\nAnswer not correct, no money added. Your final cash pot is £{cashPot}"
      f"\n\nThanks for playing 'Charlie's' Who Wants To Be A Millionaire")
    exit()
  else:
    cashPot += questionNineBounty
    print(f"\nAnswer correct! £{questionNineBounty} added to the cash pot!")
    print(f"Your cash pot is now: £{cashPot}")


def questionTen():
  global cashPot
  questionTenAnswerList = {
    "A": "Bazinga",
    "B": "Bandwidth",
    "C": "Beluga",
    "D": "Benadryl"
  }
  questionTenBounty = 16000
  print("\nQuestion 10:\n")

  answer = input(
    f"\nVery good... perhaps too good...\n"
    f"What is Sheldon from The Big Bang Theory catchphrase?\n\n{questionTenAnswerList}\n\nEnter your answer here: "
  )
  correctAnswer = "A" if answer.upper() in questionTenAnswerList \
      else "Bazinga"

  if answer.upper() != correctAnswer.upper():
    print(
      f"\nAnswer not correct, no money added. Your final cash pot is £{cashPot}"
      f"\n\nThanks for playing 'Charlie's' Who Wants To Be A Millionaire")
    exit()
  else:
    cashPot += questionTenBounty
    print(f"\nAnswer correct! £{questionTenBounty} added to the cash pot!")
    print(f"Your cash pot is now: £{cashPot}")


def questionEleven():
  global cashPot
  questionElevenAnswerList = {
    "A": "IT",
    "B": "Pet Sematary",
    "C": "The Shining",
    "D": "Misery"
  }
  questionElevenBounty = 32000
  print("\nQuestion 11:\n")

  answer = input(
    f"\nStay where you are. Someone has been... dispatched...\n"
    f"Which Stephen King novel takes place mostly in the fictional Overlook Hotel?\n\n{questionElevenAnswerList}\n\nEnter your answer here: "
  )
  correctAnswer = "C" if answer.upper() in questionElevenAnswerList \
      else "The Shining"

  if answer.upper() != correctAnswer.upper():
    print(
      f"\nAnswer not correct, no money added. Your final cash pot is £{cashPot}"
      f"\n\nThanks for playing 'Charlie's' Who Wants To Be A Millionaire")
    exit()
  else:
    cashPot += questionElevenBounty
    print(f"\nAnswer correct! £{questionElevenBounty} added to the cash pot!")
    print(f"Your cash pot is now: £{cashPot}")


def questionTwelve():
  global cashPot
  questionTwelveAnswerList = {
    "A": "Venus",
    "B": "Jupiter",
    "C": "Earth",
    "D": "Saturn"
  }
  questionTwelveBounty = 61000
  print("\nQuestion 12:\n")

  answer = input(
    f"\n*Radio silence*\n"
    f"Which planet in our solar system has the most moons?\n\n{questionTwelveAnswerList}\n\nEnter your answer here: "
  )
  correctAnswer = "D" if answer.upper() in questionTwelveAnswerList \
      else "Saturn"

  if answer.upper() != correctAnswer.upper():
    print(
      f"\nAnswer not correct, no money added. Your final cash pot is £{cashPot}"
      f"\n\nThanks for playing 'Charlie's' Who Wants To Be A Millionaire")
    exit()
  else:
    cashPot += questionTwelveBounty
    print(f"\nAnswer correct! £{questionTwelveBounty} added to the cash pot!")
    print(f"Your cash pot is now: £{cashPot}")


def questionThirteen():
  global cashPot
  questionThirteenAnswerList = {
    "A": "Captain Marvel",
    "B": "Black Widow",
    "C": "The Wasp",
    "D": "Scarlet Witch"
  }
  questionThirteenBounty = 125000
  print("\nQuestion 13:\n")

  answer = input(
    f"\n*Muffled Whispering* They're on their way. They'll be ready to strike in 2 more questions\n"
    f"In the Marvel Cinematic Universe, what is Natasha Romanoff's superhero name?\n\n{questionThirteenAnswerList}\n\nEnter your answer here: "
  )
  correctAnswer = "B" if answer.upper() in questionThirteenAnswerList \
      else "Black Widow"

  if answer.upper() != correctAnswer.upper():
    print(
      f"\nAnswer not correct, no money added. Your final cash pot is £{cashPot}"
      f"\n\nThanks for playing 'Charlie's' Who Wants To Be A Millionaire")
    exit()
  else:
    cashPot += questionThirteenBounty
    print(
      f"\nAnswer correct! £{questionThirteenBounty} added to the cash pot!")
    print(f"Your cash pot is now: £{cashPot}")


def questionFourteen():
  global cashPot
  questionFourteenAnswerList = {
    "A": "T00S00N",
    "B": "BACK4U",
    "C": "OUTATIME",
    "D": "TURNB4CK"
  }
  questionFourteenBounty = 250000
  print("\nQuestion 14:\n")

  answer = input(
    f"\nIf there's one thing I can say... I'm lucky to have met you, you goddamn smart son of a gun\n"
    f"What does the licence plate on the DeLorean say in Back To The Future?\n\n{questionFourteenAnswerList}\n\nEnter your answer here: "
  )
  correctAnswer = "C" if answer.upper() in questionFourteenAnswerList \
      else "OUTATIME"

  if answer.upper() != correctAnswer.upper():
    print(
      f"\nAnswer not correct, no money added. Your final cash pot is £{cashPot}"
      f"\n\nThanks for playing 'Charlie's' Who Wants To Be A Millionaire")
    exit()
  else:
    cashPot += questionFourteenBounty
    print(
      f"\nAnswer correct! £{questionFourteenBounty} added to the cash pot!")
    print(f"Your cash pot is now: £{cashPot}")


def questionFifteen():
  global cashPot
  questionFifteenAnswerList = {
    "A": "French-Swiss",
    "B": "French-Canadian",
    "C": "French-American",
    "D": "French-Italian"
  }
  questionFifteenBounty = 500000
  print("\nQuestion 15:\n")

  answer = input(
    f"\n*choked on tears* Take the shot, if he answers right...\n"
    f"What dual-nationality is Celine Dion?\n\n{questionFifteenAnswerList}\n\nEnter your answer here: "
  )
  correctAnswer = "B" if answer.upper() in questionFifteenAnswerList \
      else "French-Canadian"

  if answer.upper() != correctAnswer.upper():
    print(
      f"\nAnswer not correct, no money added. Your final cash pot is £{cashPot}\n You were too close :'("
      f"\n\nThanks for playing 'Charlie's' Who Wants To Be A Millionaire")
    exit()
  else:
    cashPot += questionFifteenBounty
    print(
      f"\n*BANG* QUICK! I got the guy we sent in the back, I couldn't let him take you out!\n"
      f"Take your winnings and run, see you again... friend!\n"
      f"£{questionFifteenBounty} added to the cash pot!")
    print(f"Your final cash pot is: £{cashPot}\n\n"
          "Thanks for playing Who Wants To Be A Millionaire!\n\n"
          "fin")
    exit()


questionOne()
questionTwo()
questionThree()
questionFour()
questionFive()
questionSix()
questionSeven()
questionEight()
questionNine()
questionTen()
questionEleven()
questionTwelve()
questionThirteen()
questionFourteen()
questionFifteen()
