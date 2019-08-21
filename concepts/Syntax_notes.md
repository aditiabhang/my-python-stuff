- Print
There are two different Python versions.
Both Python 2 and Python 3 are used throughout the globe.
The most significant difference between the two is how you write a print statement. In Python 3, print has parentheses.
Example:
Python 2:
      print "Hello YOUniverse!"
Python 3:
      print ("Hello YOUniverse!")

We can combine multiple strings using +, like so:
    print "Hello " + " Aditi"
---------------------------------------------------------------------
- Error Handling
If the quotes are mismatched Python will notice this and inform you that your code has an error in its syntax because the line ended (called an EOL) before the double-quote that was supposed to close the string appeared. The program will abruptly stop running with the following message:

SyntaxError: EOL while scanning a string literal

This means that a string wasn’t closed, or wasn’t closed with the same quote-character that started it.

Another issue you might run into is attempting to create a string without quotes at all. Python treats words not in quotes as commands, like the print statement. If it fails to recognize these words as defined (in Python or by your program elsewhere) Python will complain the code has a NameError. This means that Python found what it thinks is a command, but doesn’t know what it means because it’s not defined anywhere.
-----------------------------------------------------------------------
- Variables
Python uses variables to define things that are subject to change.

greeting_message = "Welcome to Codecademy!"
current_excercise = 5

In the above example, we defined a variable called greeting_message and set it equal to the string “Welcome to Codecademy!”. It also defined a variable called current_exercise and set it equal to the number 5.
-------------------------------------------------------------------------
- Comments
A line of text preceded by a # is called a comment.
---------------------------------------------------
- Multi-line Strings
We have seen how to define a string with single quotes and with double quotes. If we want a string to span multiple lines, we can also use triple quotes:

address_string = """136 Whowho Rd
Apt 7
Whosville, WZ 44494"""
This address spans multiple lines, and is still contained in one variable, address_string.

When a string like this is not assigned to a variable, it works as a multi-line comment. This can be helpful as your code gets more complex:

"""The following piece of code does the following steps:
takes in some input
does An Important Calculation
returns the modified input and a string that says "Success!" or "Failure..."
"""
... a complicated piece of code here...
============================================
? Why are there two kinds of comments?
============================================
=> In Python, comments begin with a # symbol and continue to the end of the line. Text that is delimited by three double quotes at its beginning and end actually forms a multi-line string rather than a comment. In fact, a multi-line string is really just a string. Both comments and multi-line strings come in handy in different ways!

Single-line comments are great when you need to:
1. Write a comment on the same line (inline), perhaps to explain a variable or value.
2. Comment out a single line of code so that it doesn’t run.

Multi-line strings are useful when you need to:
1. Remove large blocks of code from a process without deleting them.
2. Write documentation for a program or function. If a string is positioned as the first line within a function, it serves as a docstring that can be accessed programmatically. For docstrings, it is conventional to use multi-line strings.
-------------------------------------------------------------------------
- Two Types of Division
In Python 2, when we divide two integers, we get an integer as a result. When the quotient is a whole number, this works fine:

quotient = 6/2
# the value of quotient is now 3, which makes sense

However, if the numbers do not divide evenly, the result of the division is truncated into an integer. In other words, the quotient is rounded down to a whole number. This can be surprising when you expect to receive a decimal and you receive a rounded-down integer:

quotient = 7/2
# the value of quotient is 3, even though the result of the division here is 3.5

To yield a float as the result instead, programmers often change either the numerator or the denominator (or both) to be a float:

quotient1 = 7./2
# the value of quotient1 is 3.5

quotient2 = 7/2.
# the value of quotient2 is 3.5

quotient3 = 7./2.
# the value of quotient3 is 3.5

An alternative way is to use the float() method:

quotient1 = float(7)/2
# the value of quotient1 is 3.5
--------------------------------------------------------------------------
- Boolean
In Python, we define booleans using the keywords True and False:

a = True
b = False

A boolean is actually a special case of an integer. A value of True corresponds to an integer value of 1, and will behave the same. A value of False corresponds to an integer value of 0.
===============================
? common uses for booleans?
=> The use of booleans might not be as immediately obvious. There are lots of times we want to control how our program behaves with boolean conditions. For example, if we want to continue asking a question until the user provides valid input, we might use a boolean variable that is set to False and only becomes True when their input is checked and is valid.
---------------------------------------------------------------------------
- ValueError

Sometimes we will want to convert variables to different datatypes. For example, if we wanted to print out an integer as part of a string, we would want to convert that integer to a string first. We can do that using str():

age = 13
print "I am " + str(age) + " years old!"
This would print:

>> "I am 13 years old!"

 Similarly, if we have a string like "7" and we want to perform arithmetic operations on it, we must convert it to a numeric datatype. We can do this using int():

number1 = "100"
number2 = "10"

string_addition = number1 + number2
#string_addition now has a value of "10010"

int_addition = int(number1) + int(number2)
#int_addition has a value of 110
If you use int() on a floating point number, it will round the number down. To preserve the decimal, you can use float():

string_num = "7.5"
print int(string_num)
print float(string_num)
>>> 7
>>> 7.5
