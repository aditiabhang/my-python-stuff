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