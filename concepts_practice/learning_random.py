'''
------ Random Module ------

When to use it?
- when we want computer to randomly select a number in a given range
- pick up a random element from alist, from a deck, flip a coin, etc
- while making a password database more secure

Must include: import random
'''

## Python Random Module functions: 

'''
## [A] To generate random integers, we can use the following two functions.
1. randit() -
- used only to generate integers
- accepts two parameter, lower and higher limit of range.
'''
import random

print("random.randit() to generate random integer: ")
print(random.randint(1, 10))
print(random.randint(1, 10))
# each time the output will be different, as said, generate random numbers

print(random.random()* 100) #a random number between 0 and 100

'''
2. random.randrange(start,  stop [,  step]) -
- used to generate a random integer number within a given range.
- the step is optional, it is a difference between each number in the sequence.
- the default value of the step is 1.
'''
print("\nRandom number within given range: ")
print(random.randrange(1, 100, 10))

'''
## [B] To select a random element from a *sequence*, it can a list or string.
3. choice(list) - randomly selects an element from a list
parameter  - sequence
'''
cities = ['Austin', 'Pune', 'Nashik', 'Satara']
print("\nChoice function on list: ", random.choice(cities))