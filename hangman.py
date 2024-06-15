import random
import os
import sys

hangman_stages = [
'''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\\  |
      |
      |
=========
''',
'''
  +---+
  |   |
  O   |
 /|\\  |
 /    |
      |
=========
''',
'''
  +---+
  |   |
  O   |
 /|\\  |
 / \\  |
      |
=========
''']


words = ['apple', 'ball', 'cat', 'dog', 'elephant', 'fish', 'giraffe', 'house', 'ice', 'juice',
    'kite', 'lion', 'monkey', 'nest', 'orange', 'pencil', 'queen', 'rabbit', 'snake', 'tree',
    'umbrella', 'vase', 'watch', 'xray', 'yak', 'zebra', 'banana', 'carrot', 'drum', 'egg']
random_word=random.choice(words)
display=["_"] * len(random_word)
print("[ ", ' '.join(display), " ]")

lives = 6
repeat_tries = 0
print(hangman_stages[0]) # Preparing the firt stage in the death

while "_" in display and lives > 0 :
    try:
      guess=input("Enter your guess letter\n").lower()
      if guess in display: # if the user choosed the same letter more than onnce
          if repeat_tries == 3:
            os.system('cls')
            print("You lost")
            print(hangman_stages[6])
            break
          else:
            repeat_tries+=1
            print(f"You have repeated the same letter for {repeat_tries} times and you have {3-repeat_tries}")
          continue

      if guess not in random_word:
          lives -=1
          os.system('cls')
          print(hangman_stages[6-lives])
          print(f"You still have {lives} more tries")
          print("[ ", ' '.join(display), " ]")
      
      else:  
        for position in range(len(random_word)):
            if random_word[position] == guess:
                display[position] = guess
                
            elif random_word == guess:
                display = guess
        os.system("cls")
        print(hangman_stages[6-lives])
        print("Wow, you guessed it correctly!")
        print("[ ", ' '.join(display), " ]")
    except KeyboardInterrupt:
       sys.exit()        



if lives == 0 or repeat_tries == 3:
    print("You Lost!")
else:
    print("You Win!")