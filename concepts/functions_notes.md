- Function Junction
Functions are defined with three components:

1. The header, which includes the def keyword, the name of the function, and any parameters the function requires. Here’s an example:

def hello_world(): # There are no parameters

2. An optional comment that explains what the function does.

"""Prints 'Hello World!' to the console."""

3. The body, which describes the procedures the function carries out. The body is indented, just like conditional statements.

print "Hello World!"
Here’s the full function pieced together:

def hello_world():
  """Prints 'Hello World!' to the console."""
  print "Hello World!"
----------------------------------------------------------------------
- Call and Response
After defining a function, it must be called to be implemented.

- Example
def square(n):
  """Returns the square of a number."""
  squared = n ** 2
  print "%d squared is %d." % (n, squared)
  return squared

# Call the square function on line 10! Make sure to
# include the number 10 between the parentheses.

square(10)
----------------------------------------------------------------------
- Parameters and Arguments
Let’s take another look at the definition of the function square from the previous exercise:

def square(n):
Here, n is a parameter of square. A parameter is a variable that is an input to a function. It says, “Later, when square is used, you’ll be able to input any value you want, but for now we’ll call that future value n.” A function can have any number of parameters.

The values of the parameters passed into a function are known as the arguments. Recall in the previous example, we called: py square(10)

Here, the function square was called with the parameter n set to the argument 10.

Typically, when you call a function, you should pass in the same number of arguments as there are parameters.

To summarize:

1. When defining a function, placeholder variables are called parameters.
2. When using, or calling, a function, inputs into the function are called arguments.
/----------------------------------/
- Example
def power(base, exponent):  # Add your parameters here!
  result = base ** exponent
  print "%d to the power of %d is %d." % (base, exponent, result)

power(37, 4)

- Example 2
def cube(number):
  return number * number * number

def by_three(number):
  if number % 3 == 0:
  	return cube(number)
  else:
    return False
----------------------------------------------------------------------
- Importing modules
 A module is a file that contains definitions—including variables and functions—that you can use once it is imported.
 There is a Python module named math that includes a number of useful variables and functions, and sqrt() is one of those functions. In order to access math, all you need is the import keyword. When you simply import a module this way, it’s called a generic import.
 - Eg.
 import math
 print math.sqrt(25)
/----------------------------------/
However, we only really needed the sqrt function, and it can be frustrating to have to keep typing math.sqrt().

It’s possible to import only certain variables or functions from a given module. Pulling in just a single function from a module is called a function import, and it’s done with the from keyword:

from module import function
Now you can just type sqrt() to get the square root of a number—no more math.sqrt()!
- Eg.
  from math import sqrt
/----------------------------------/
What if we still want all of the variables and functions in a module but don’t want to have to constantly type math.?

Universal import can handle this for you. The syntax for this is:

from module import *
----------------------------------------------------------------------
- max function
- eg
maximum = max(3,3.6, 0.9)
print maximum

Similarly for minu
- eg.
minimum = min(1,2,0.369)
print minimum
/----------------------------------/
- abs()
The abs() function returns the absolute value of the number it takes as an argument—that is, that number’s distance from 0 on an imagined number line. For instance, 3 and -3 both have the same absolute value: 3. The abs() function always returns a positive value, and unlike max() and min(), it only takes a single number.
/----------------------------------/
- type()
Finally, the type() function returns the type of the data it receives as an argument. If you ask Python to do the following:

print type(3)
print type(3.6)
print type('Adiket')
=> <type 'int'>
   <type 'float'>
   <type 'str'>'
/----------------------------------/
- Review: Functions
   Okay! Let’s review functions.
- eg 1;

   def speak(message):
     return message

   if happy():
     speak("I'm happy!")
   elif sad():
     speak("I'm sad.")
   else:
     speak("I don't know what I'm feeling.")

- eg 2:
def shut_down(s):
  if s == "yes":
    return "Shutting down"
  elif s == "no":
    return "Shutdown aborted"
  else:
    return "Sorry"
