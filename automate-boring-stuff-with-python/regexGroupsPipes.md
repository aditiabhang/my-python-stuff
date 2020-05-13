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