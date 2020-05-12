### Advanced Strings

- Strings are enclosed by a pair of single quotes or double quotes (as long as the same kind are used).
- Escape characters let you put quotes and other characters that are hard to type inside strings.
- Raw strings (which have the r prefix before the first quote) will literally print any backslashes in the string and ignore escape characters.
   - format:

            >>> r'My name is Adi'
            'My name is Adi'
- Multiline strings begin and end with three quotes, and can span multiple lines.
- Indexes, slices, and the "in" and "not in" operators all work with strings.

### String Methods

- Strings methods are mutable, meaning the string methods can be modief in place.
- 
‘Hello world'.split() returns a list of strings split from the string it's called on.
rjust() ,ljust(), center() returns a string padded with spaces.
strip(), rstrip(), lstrip() returns a string with whitespace stripped off the sides.
replace() will replace all occurrences of the first string argument with the second string argument.
Pyperclip has copy() and paste() functions for getting and putting strings on the clipboard.

- upper() and lower() return an uppercase or lowercase string:

        >>> name = 'aditi'
        >>> name.upper()
        'ADITI'

- supper(), islower(), isalpha(), isalnum(), isdecimal(), isspace(), istitle() returns True or False if the string is that uppercase, lowercase, alphabetical letters, and so on.

        >>> name.isupper()
        False
- startswith() and endswith() also return bools.

        >>> "Aditi Abhang".startswith('Aditi')
        True

- join() returns a string that combines the strings in the given list.

        >>> ",".join(['cat','dog'])
        'cat,dog'

        >>> "\n\n".join(['Apple', 'Banana', 'Cherry'])
        'Apple\n\nBanana\n\nCherry'
        >>> print("\n\n".join(['Apple', 'Banana', 'Cherry']))
        Apple

        Banana

        Cherry

- ‘Hello world'.split() returns a list of strings split from the string it's called on.

        >>> 'cat dog'.split()
        ['cat', 'dog']

        >>> 'Mississippi'.split('s')
        ['Mi', '', 'i', '', 'ippi']

- rjust() ,ljust(), center() returns a string padded with spaces.

        >>> 'Hello'.rjust(10)
        '     Hello'
        >>> 'Goodbye'.ljust(10)
        'Goodbye   '
        >>> 'My Friend'.center(15)
        '   My Friend   '
        >>> 'YOUniverse'.center(20,'*')
        '*****YOUniverse*****'
        >>> 'YOUniverse'.center(20,'-')
        '-----YOUniverse-----'

- strip(), lstrip(), rstrip removes whitespaces.

        >>> name = 'Manaca'.center(20)
        >>> name.strip()
        'Manaca'
        >>> name.rstrip()
        '       Manaca'
        >>> name.lstrip()
        'Manaca 

- replace('string to look', 'string to replace')

        >>> name = 'Manacaaaa'
        >>> name.replace('c','k')
        'Manakaaaa'
