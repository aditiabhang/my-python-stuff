### Basics:

- Regular expressions are mini-language for specifying text patterns. Writing code to do pattern matching without regular expressions is a huge pain.
- Regex strings often use backslashes (like \d), so they are often written using raw strings: **r'\d'**
- **\d** is the regex for a numeric digit character.
- Import the re module first.
- Call the re.compile() function to create a regex object.
- Call the regex object's search() method to create a match object.
- Call the match object's group() method to get the matched string.

_NOTE: refer non-regex_phoneNumber.py and regex_phoneNumber.py_