- Escaping characters
There are some characters that cause problems. For example:

'There's a snake in my boot!'

This code breaks because Python thinks the apostrophe in 'There's' ends the string. We can use the backslash to fix the problem, like this:

'There\'s a snake in my boot!'
---------------------------------------------------------------------
- Access by Index
The string "PYTHON" has six characters,
numbered 0 to 5, as shown below:

+---+---+---+---+---+---+
| P | Y | T | H | O | N |
+---+---+---+---+---+---+
  0   1   2   3   4   5

So if you wanted "Y", you could just type
"PYTHON"[1] (always start counting from 0!)
---------------------------------------------------------------------
- String methods
1. len() - gets the length (the number of characters) of a string!
eg. parrot = "Norwegian Blue"
    print len(parrot)
    => 14

2. lower() - get rid of all the capitalization in your strings.
eg. parrot = "Norwegian Blue".lower()
    print parrot.lower()
    => norwegian blue

3. upper() - A similar method exists to make a string completely upper case.
eg. parrot = "norwegian blue"
    print parrot.upper()
    => NORWEGIAN BLUE

4. str() - turns non-strings into strings!
eg. pi = 3.14
    print str(pi)
    => 3.14
---------------------------------------------------------------------
- Dot Notation
Let’s take a closer look at why you use len(string) and str(object), but dot notation (such as "String".upper()) for the rest.

lion = "roar"
len(lion)
lion.upper()
Methods that use dot notation only work with strings.

On the other hand, len() and str() can work on other data types.
eg. ministry = "The Ministry of Silly Walks"
    print len(ministry)
    print ministry.upper()
    => 27
    THE MINISTRY OF SILLY WALKS
---------------------------------------------------------------------
- String Formatting with %, Part 2

Remember, we used the % operator to replace the %s placeholders with the variables in parentheses.

name = "Mike"
print "Hello %s" % (name)

You need the same number of %s terms in a string as the number of variables in parentheses:

print "The %s who %s %s!" % ("Knights", "say", "Ni")
# This will print "The Knights who say Ni!"
---------------------------------------------------------------------
- Summary

And Now, For Something Completely Familiar
Great job! You’ve learned a lot in this unit, including:

- Three ways to create strings:
'Alpha'
"Bravo"
str(3)

-String methods :
len("Charlie")
"Delta".upper()
"Echo".lower()

- Printing a string:
print "Foxtrot"

- Advanced printing techniques:
g = "Golf"
h = "Hotel"
print "%s, %s" % (g, h)
---------------------------------------------------------------------
- Example
On line 3, create the variable my_string and set it to any string you’d like.
On line 4, use len() to print the length of my_string.
On line 5, print the .upper() case version of my_string.

- Answer:
my_string = 'Adiket'
print len("Adiket")
print my_string.upper()
