- Go With the Flow
Example CODE:

def clinic():
    print "You've just entered the clinic!"
    print "Do you take the door on the left or the right?"
    answer = raw_input("Type left or right and hit 'Enter'.").lower()
    if answer == "left" or answer == "l":
        print "This is the Verbal Abuse Room, you heap of parrot droppings!"
    elif answer == "right" or answer == "r":
        print "Of course this is the Argument Room, I've told you that already!"
    else:
        print "You didn't pick left or right! Try again."
        clinic()

clinic()
/---------------------------/
- Conditional Statement Syntax
if is a conditional statement that executes some specified code after checking if its expression is True.

Here’s an example of if statement syntax:

if 8 < 9:
  print "Eight is less than nine!"
In this example, 8 < 9 is the checked expression and print "Eight is less than nine!" is the specified code.

Pay attention to the indentation before the print statement. This space, called white space, is how Python knows we are entering a new block of code. Python accepts many different kinds of indentation to indicate blocks. In this lesson, we use four spaces but elsewhere you might encounter two-space indentation or tabs (which Python will see as different from spaces).

If the indentation from one line to the next is different and there is no command (like if) that indicates an incoming block then Python will raise an IndentationError. These errors could mean, for example, that one line had two spaces but the next one had three. Python tries to indicate where this error happened by printing the line of code it couldn’t parse and using a ^ to point to where the indentation was different from what it expected.
----------------------------------------------------------------------
- I Got 99 Problems, But a Switch Ain't One

elif is short for “else if.” It means exactly what it sounds like: “otherwise, if the following expression is true, do this!”

if 8 > 9:
  print "I don't get printed!"
elif 8 < 9:
  print "I get printed!"
else:
  print "I also don't get printed!"
In the example above, the elif statement is only checked if the original if statement is False.
----------------------------------------------------------------------
- Really great work! Here’s what you’ve learned in this unit:

Comparators:
3 < 4
5 >= 5
10 == 10
12 != 13

Boolean operators:
True or False
(3 < 4) and (5 >= 5)
this() and not that()

Conditional statements:
if this_might_be_true():
  print "This really is true."
elif that_might_be_true():
  print "That is true."
else:
  print "None of the above."
/----------------------------------/
- Example:

# Complete the if and elif statements!
def grade_converter(grade):
    if grade >= 90:
        return "A"
    elif grade >= 80 and grade <= 89:
        return "B"
    elif grade >= 70 and grade <= 79:
        return "C"
    elif grade >= 65 and grade <= 69:
        return "D"
    else:
        return "F"

# This should print an "A"      
print grade_converter(92)

# This should print a "C"
print grade_converter(70)

# This should print an "F"
print grade_converter(61)
