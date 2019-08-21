- Pig Latin
/----------------------------------/
It is a language game, where you move the first letter of the word to the end and add “ay.” So “Python” becomes “ythonpay.” To write a Pig Latin translator in Python, here are the steps we’ll need to take:

Ask the user to input a word in English.
Make sure the user entered a valid word.
Convert the word from English to Pig Latin.
Display the translation result.
----------------------------------------------------------------------
- Taking user input:
/----------------------------------/
- Example:
name = raw_input("What's your name?")
print name
/----------------------------------/
In the above example, raw_input() accepts a string, prints it, and then waits for the user to type something and press Enter (or Return).

In the interpreter, Python will ask:
/----------------------------------/
What's your name?
/----------------------------------/
Once you type in your name and hit Enter, it will be stored in name.

- Another Example to check the string input:

original = raw_input("Enter a word: ")
print original

if len(original) > 0:
  print original
else:
  print "empty"

=> .isalpha() which returns False since the string contains non-letter characters.
You can use .isalpha() to check that a string doesn’t contain any non-letter characters, isdigit(), to check the string contains numbers.
----------------------------------------------------------------------
- Slice

s = "Charlie"

print s[0]
# will print "C"

print s[1:4]
# will print "har"
First we create a variable s and give it the string "Charlie"
Next we access the first letter of "Charlie" using s[0]. Remember letter positions start at 0.
Then we access a slice of "Charlie" using s[1:4]. This returns everything from the letter at position 1 up till position 4.

- example
pyg = 'ay'

original = raw_input('Enter a word:')

if len(original) > 0 and original.isalpha():
  word = original.lower()
  first = word[0]
  new_word = word + first + pyg
  new_word = new_word[1:len(new_word)]
  print new_word
else:
  print 'empty'
----------------------------------------------------------------------
