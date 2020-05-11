# print("What is you name my child?")
# myName = input()
# print("My name is " + myName)
# print("Welcome to the world, " + myName + ". How old are you?")
# myAge = input()
# print("Oh that's sweet!! Next year you will be " + str(int(myAge)+1) +" years old.")

total = 0
for num in range(101):
    total = total + num
print(total)

# 1 + 99, 2 + 98, 3 + 97 ...
# 49 + 51 ..
# 50 * 100 > 5000 + 50 > 5050

## Built-in functions

#1. randint 
import random
random.randint(1,10) #random int between 1 to 10

#2. sys and os and math
# import random, sys, os, math

# 3. import all from module
# from random import *

#4. sys
import sys
print("Hello sys, dont go..")
sys.exit()
print("okay bye.")

# pyperclip (third-party module) has copy and paste task: pyperclip.copy() and pyperclip.paste()
# We have to install it first using: pip3 install pyperclip
