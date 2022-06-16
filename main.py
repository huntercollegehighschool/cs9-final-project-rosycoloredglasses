"""
Name(s): Jisu
Name of Project: Hangman :)
"""
import random
import page1
word = random.choice(page1.lis)
list(word)

print("Welcome to Hangman, except there is no hangman. I know, I was disappointed as well. If you haven't got the word after all the guesses, type in a random character to see the answer. Here is your word.")

spaces = "*"*(len(word))
print(spaces)
print("There are four letters in this word.")

firstletter = ["h", "p", "f", "b", "t", "w", "g", "y", "s", "d"]
guesses = 6

lettersguessed = []

def subtract():
  subtraction = guesses
  print("You started with 6 guesses. I'm sure you've already figured out the word. Here are the amount of guesses you have remaining:")
  return subtraction
  
listspaces = ["*","*","*","*"]

letter = str(input("Enter a new letter: "))

while guesses != 0:
  if letter in firstletter:
    if letter in list(word):
      list(listspaces)
      listspaces.insert(0, letter)
      listspaces.pop(1)
      ' '.join(listspaces)
      guesses = guesses - 1
      print(' '.join(listspaces))
      print(subtract())
      list(listspaces)
      letter = str(input("Enter a new letter: "))
    else:
      print("That input is not present in the word. Please try again.")
      guesses = guesses - 1
      print(subtract())
      letter = str(input("Enter a new letter: "))
  elif letter == "e":
      list(listspaces)
      listspaces.insert(1, "e")
      listspaces.pop(2)
      ' '.join(listspaces)
      guesses = guesses - 1
      print(' '.join(listspaces))
      print(subtract())
      list(listspaces)
      letter = str(input("Enter a new letter: "))
  elif letter == "a":
      list(listspaces)
      listspaces.insert(2, "a")
      listspaces.pop(3)
      ' '.join(listspaces)
      guesses = guesses - 1
      print(' '.join(listspaces))
      print(subtract())
      list(listspaces)
      letter = str(input("Enter a new letter: "))
  elif letter == "r":
      list(listspaces)
      listspaces.insert(3, "r")
      listspaces.pop(4)
      ' '.join(listspaces)
      guesses = guesses - 1
      print(' '.join(listspaces))
      print(subtract())
      list(listspaces)
      letter = str(input("Enter a new letter: "))
  else:
      print("That letter is not present in the word. Please try again.")
      guesses = guesses -1
      print(subtract())
      letter = str(input("Enter a new letter: "))
if guesses == 0:
  print("Here is the answer: ")
  print(word)