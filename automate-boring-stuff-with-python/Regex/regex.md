### Group()

- Groups are created in regex strings with parentheses.
- The first set of parentheses is group 1, the second is 2, and so on.
- Calling **group()** or **group(0)** returns the full matching string, group(1) returns group 1's matching string, and so on.
- Use **\(** and **\)** to match literal parentheses in the regex string.

        import re
        phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d)-(\d\d\d\d)')
        mo = phoneNumRegex.search("My number is 213-321-2132")
        print(mo.group())
        print("Area code:", mo.group(1))

### Pipe

- The **|** pipe can match one of many possible groups.

        >>> batRegex = re.compile(r'Bat(man|mobile|copter|butler)')
        >>> mo = batRegex.search("Batmobile lost a wheel")
        >>> mo.group()
        'Batmobile'

----------------------------------------------------------
### Repetition and Greedy/Non-Greedy Matching:

- The **?** says the group matches **zero or one** times.

        >>> batRegex = re.compile(r'Bat(wo)?man')
        >>> mo = batRegex.search("The Adventures of Batwoman")
        >>> mo.group()
        'Batwoman'
        >>> mo = batRegex.search("The Adventures of Batman")
        >>> mo.group()
        'Batman'

- The ' * ' says the group matches **zero or more** times.

        >>> batRegex = re.compile(r'Bat(wo)*man')
        >>> mo = batRegex.search("The Adventures of Batwowowowoman")
        >>> mo.group()
        'Batwowowowoman'

- The **+** says the group matches **one or more** times.

        'Batwowowowoman'

- The curly braces can match a specific number of times.

        >>> haRegex = re.compile(r'(Ha){3}')
        >>> mo = haRegex.search("He said HaHaHa later")
        >>> mo.group()
        'HaHaHa'

- The curly braces with two numbers matches a minimum and maximum number of times.

- Leaving out the first or second number in the curly braces says there is no minimum or maximum.

        >>> haRegex = re.compile(r'(Ha){3,4}')

- "Greedy matching" matches the *longest string possible*, "nongreedy matching" (or "lazy matching") matches the *shortest string possible*.

- Putting a question mark after the curly braces makes it do a nongreedy/lazy match.

----------------------------------------------------------
### Regex Caret/ Dollar character and Dot-Star:

- **^** means the string must start with pattern.

        >>> BeginwithHello = re.compile(r'^Hello')
        >>> mo = BeginwithHello.search("Hello, there!") 
        >>> mo.group()
        'Hello'

        >>> BeginwithHello.search("Oh hello, there!")==None 
        True

- **$** means the string must end with the pattern. Both means the entire string must match the entire pattern.

        >>> endswithWorld = re.compile(r'World!$')
        >>> mo = endswithWorld.search('Hello World!')
        >>> mo.group()
        'World!

        # _Extra example_:
        # One or more digits, starts with and ends with a digit
        >>> allDigits = re.compile(r'^\d+$')
        >>> allDigits.search('1223784782')
        <re.Match object; span=(0, 10), match='1223784782'>

- The **.** dot is a wildcard; it matches any character except newlines. - Anything.

        >>> anything = re.compile(r'.at')       #only 1 character before 'at'
        >>> anything.findall('The cat sat in the hat on the flat mat')
        ['cat', 'sat', 'hat', 'lat', 'mat']     #flat not present so we do as below;

        >>> anything = re.compile(r'.{1,2}at')  # min 2 max 3
        >>> anything.findall('The cat sat in the hat on the flat mat')
        [' cat', ' sat', ' hat', 'flat', ' mat']

        >>> nameRegex = re.compile(r'First name: (.*) Last name: (.*)')
        >>> nameRegex.findall('First name: Aditi Last name: Abhang')
        [('Aditi', 'Abhang')]

  - Greedy match - **.*** is a greedy match
  - Non-Greedy match - **.?** is a non-greedy match

        >>> serve = '<To serve humans> for dinner>'
        >>> nongreedy = re.compile(r'<(.*?)>')
        ['To serve humans']

        >>> >>> greedy.findall(serve)
        ['To serve humans> for dinner']

- Pass **re.DOTALL** as the second argument to re.compile() to make the . dot match newlines as well.

        >>> prime = 'Serve the public trust.\nProtect the innocent.\nUpload the law.'
        >>> print(prime)
        Serve the public trust.
        Protect the innocent.
        Upload the law.
        >>> dotstar = re.compile(r'.*', re.DOTALL)
        >>> dotstar.search(prime)
        <re.Match object; span=(0, 61), match='Serve the public trust.\nProtect the innocent.\nU>

- Pass **re.I** as the second argument to re.compile() to make the matching ***case-insensitive***.

        >>> vowelRegex = re.compile(r'[aeiou]')
        >>> vowelRegex.findall('Why does this course talking so much about All robocop')
        ['o', 'e', 'i', 'o', 'u', 'e', 'a', 'i', 'o', 'u', 'a', 'o', 'u', 'o', 'o', 'o']
        >>> vowelRegex = re.compile(r'[aeiou]', re.I)
        >>> vowelRegex.findall('Why does this course talking so much about All robocop')
        ['o', 'e', 'i', 'o', 'u', 'e', 'a', 'i', 'o', 'u', 'a', 'o', 'u', 'A', 'o', 'o', 'o']
---------------------------------------------------------
### Sub() method and Verbose:

- The sub() regex method will substitute matches with some other text.

        >>> import re
        >>> namesRegex = re.compile(r'Agent \w+')
        >>> namesRegex.findall("Agent Alice gave all the documents to Agent Bob.")
        ['Agent Alice', 'Agent Bob']

        >>> namesRegex.sub('REDACTED', "Agent Alice gave all the documents to Agent Bob.")
        'REDACTED gave all the documents to REDACTED.'

  - Using \1, \2 and so will substitute group 1, 2, etc in the regex pattern.

        >>> namesRegex = re.compile(r'Agent (\w)\w*')
        >>> namesRegex.findall("Agent Alice gave all the documents to Agent Bob.")
        ['A', 'B']

        >>> namesRegex.sub(r'Agent \1****', "Agent Alice gave all the documents to Agent Bob.")
        'Agent A**** gave all the documents to Agent B****.

- Passing re.VERBOSE lets you **add whitespace and comments to the regex string passed to re.compile()**.


- If you want to pass multiple arguments (re.DOTALL , re.IGNORECASE, re.VERBOSE), combine them with the | bitwise operator.

        phoneNumRegex = (r'''
        (\d\d\d-)|      # area-code (w/o paren with dash)
        (\(\d\d\d\) )   # -or- area-code (with parenand no dash)
        \d\d\d          # first 3 digits
        -               # second dash
        \d\d\d\d        # last 4 digits
        \sx\d{2,4}      # space and extension''', re.VERBOSE | re.IGNORECASE | re.DOTALL)