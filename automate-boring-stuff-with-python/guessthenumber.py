# This is a guess the number game, which asks the user to guess a number for 6 times. 

import random
print("Hey there! What is your good name?")
name = input()

print("Well, " + name + " I am thinking of a number between 1 and 20")
secretNumber = random.randint(1,20)

for guessesTaken in range(1,5):
    print("Could you take a guess which number is on my mind?")
    guess = int(input())
    if guess < secretNumber:
        print("No, you guess is too low.")
    elif guess > secretNumber:
        print("No, you guess is too high.")
    else:
        break  # condition for the correct guess!

if guess == secretNumber:
    print("Yo!! That\'s correct! You got it!")
    print("Good job! " + name + " you took " + str(guessesTaken) + " to guess my number.")
else:
    print("Nope, the number which I was thinking was " + str(secretNumber))

