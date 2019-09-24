###################### BASIC OPERATIONS ON STRINGS ####################
greeting = 'Hello'
name = 'Aditi'
message = 'Hi, Welcome to Python'

# to find the length of the string
print(len(greeting))

# position of each character in string using index
print(greeting[2])
print(greeting[1:])
print(greeting[:4])

# upper case and lower case function to make all characters upper and lower
print(greeting.upper())
print(greeting.lower())

# counting the number of occurance in string
print("The number of occurance of letter 'i' in name 'Aditi' : ", name.count('i'))
print("The number of occuance of letter 'l' in word 'Hello' : ", greeting.count('l'))
# if no letter or word is found it will return 0
print("Number of occurance of character 'c' in name 'Aditi' : ", name.count('c'))

# find() - returns the index of the element or word to be found in a string
print(greeting.find('l')) #the index of 'l' in 'Hello' = 2
print(message.find('to')) #the index of the word 'Python' begins at index 12, if not found returns -1.

# replace() - used to replace a string in a string
#NOTE - a new variable is required to replace a string
new_message = message.replace('Python', 'YOUniverse!')
print("Replacing word 'Python' with word 'YOUniverse': ", new_message)

# formatting strings using placeholders
print ("Method I: using placeholders.")
message = '{}, {}. Welcome. I am YOUniverse.'.format(greeting, name)
print(message)

## formatting strings using fstring (3.6+ version)
print ("")
print('Method II: Using fstrings')
message = f'{greeting}, {name}. Welcome. I am YOUniverse.'
print(message)

#TIP: can use upper()/lower() in the fstring formatting
message = f"{greeting}, {name.upper()}. Welcome to the learnings."
print(message)

# Tip: print(dir(name))
# Using this will give out all the attributes and methods that we have access to with that mentioned variable.

# Tip: print(help(str))
# Gives out the help information about the passed attribute

#################### ADVANCED OPERATIONS ON STRINGS, LISTS AND DICTIONARIES ####################
# [A] Accessing values from Dictionaries and Lists:-

# Using string concatenation
person = {'name': 'Aditi', 'age': 27}
sentence = 'Hello! My name is ' + person['name'] + ' and I am ' + str(person['age']) + ' years young.'
print(sentence)     

# Drawbacks of string concatenation:
# 1. Not useful for longer strings
# 2. Not readable, we have to open/close strings in different places.
# 3. Many + signs
# 4. Whenever there is an integer we have to catch them str.
# 5. Have to remember to add spaces.

# Using string formatting
sentence1 = "Hello! My name is {} and I am {} years young.".format(person['name'], person['age'])
print("Using formatting of string : ", sentence1)

# We can also pass the index of the value passed in the format like:
sentence1 = "Hello! My name is {0} and I am {1} years young.".format(person['name'], person['age'])
sentence2 = "Hello! My name is {0[name]}, and I am {1[age]} years young.".format(person, person)
sentence3 = "My name is {0[name]} and I am {0[age]}".format(person)

# Using lists too
listy = ['Me. Abhang', '27']
sentence3 = "My name is {0[0]} and I am {0[1]}".format(listy)

# This is very useful when we want the values to be repeated.
tag = "h1"
headline = "This is a headline"
sentence4 = "<{0}>{1}<{0}>".format(tag, headline)
print(sentence4)

#  Access attributes in similar way (Class):-

class Person():
    def __init__(self, myname, myage):
        self.myname = myname
        self.myage = myage
    
person1 = Person('Aditi Abhang', '27')
person2 = Person('Aditi L', '26')
intro = "Good Morning! My name is {1.myname} and my age is {0.myage}".format(person1, person2)
print(intro)

# using keyword arguments in the format
intro1 = "Good Morning! My name is {myname} and my age is {myage}".format(myname= 'Sanket', myage= '29')
print(intro1)

# unpacking dictionaries
sentence5 = "Hello! I am unpacking dictionaries with name as {name} and age as {age}.".format(**person)
print(sentence5)

#[B] Format and print out Numbers:-
for i in range(1,11):
    num_sentence = "The value is: {:02}".format(i)  #for two digits
    print(num_sentence)
    # We can do the padding by simply putting {:02} for two digits

# padding for decimal numbers
pi = 3.14151965
pi_val = "Value of Pi is {:2f}".format(pi)
print(pi_val)

# printing large numbers using comma separators
mb_val = "1 MB is equal to {:,}".format(1000 ** 2) 
print(mb_val) # ->  1,000,000
# {:,.2f} -> 1,000,000.00

# [C] Date Time

import datetime
my_date = datetime.datetime(2019, 9, 23, 4, 21, 36)
print(my_date)  # -> 2019-09-23 04:21:36
# We want the format of Month DD, YYYY
# We use %B - Month, %d - day, %Y - year
my_date1 = '{:%B %d, %Y}'.format(my_date) # -> September 23, 2019
my_date_sentence = '{0:%B %d, %Y} fell on a {0:%A} and was the {0:%j} day of the year.'.format(my_date)
print("Other format: ", my_date1)
print("Another format: ", my_date_sentence)