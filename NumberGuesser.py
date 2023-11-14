import random
import math

def start():
  game()
def game():
  lower = int(input("Enter Maximum Possible Number:- "))
  upper = int(input("Enter Smallest Possible Number:- "))
  x = random.randint(lower, upper)
  print("\n\tYou've only ", round(math.log(upper - lower + 1, 2)),
      " chances to guess the integer!\n")
  count = 0
  while count < math.log(upper - lower + 1, 2):
      count += 1
      guess = int(input("Guess a number:- "))
      if x == guess:
          if count == 1:
              print("You probably cheated so screw you")
          else:
            print("Congratulations, it took you ", count, " tries")
          break
      elif x > guess:
          print("You guessed too small!")
      elif x < guess:
          print("You Guessed too high!")
  if count >= math.log(upper - lower + 1, 2):
      print("\nThe number was %d" % x)
      print("\tSorry mate but you lost!")
      x = input(r"\n\would you like to play again? Y\N: ") 
      if x.lower() ==  "y":
        start()
      if x.lower() ==  "n":
        quit()
start()