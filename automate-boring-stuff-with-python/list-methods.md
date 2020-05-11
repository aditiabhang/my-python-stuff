**NOTES: Lists**
- You can delete an item from a list:

      start_list = [5, 3, 1, 2, 4]
      del start_list[3]

- The len function concatenation and replication work the same way with with that and the way that they do with strings:
  - int to str conversion.
  - len

            len(name)
            len(name_list)
  - concatenation

            string + string 
            stingstring

            list1 + list2
            list1+2

  - list out string
      
            list('Hello')
            ['H','e','l','l','o']

- IN or NOT IN operators
  
            'Howdy' in ['Hello', 'Hi', 'Howdy', 'Hey']
            True

            'Howdy' not in ['Hello', 'Hi', 'Howdy', 'Hey']
            False

- A for loop technically iterates over the values in a list.
- The range() function returns a list-like value, which can be passed to the list() function if you need an actual list value.
- Variables can swap their values using multiple assignment: 
      
      a, b = b, a
- Augmented assignment operators like += are used as shortcuts.

-------------------------------------------------------

**List Methods**
- Method: A method is the same thing as a function except it's attached or cold on a certain value.

- Index()

        >>> spam = ['Hi', 'Hello', 'Hey']
        >>> spam.index('Hi')
        0
  - _Python doesn't know which list you're trying to find the index to. That's why you have to call it on a value._

- Append() - Adds value at the end of the list.

        >>> spam.append('Ola')
        >>> spam
        ['Hi', 'Hello', 'Hey', 'Ola']       
- Insert() - Inserts value at an index
        
        >>> spam.insert(2, 'Namaste')
        >>> spam
        ['Hi', 'Hello', 'Namaste', 'Hey', 'Ola']

****NOTE: The Append and insert methods are list methods and can only be called on list values. 
They can't be called on values such as strings or integers.****

- remove()

        >>> spam.remove('Ola')
        >>> spam
        ['Hi', 'Hello', 'Namaste', 'Hey']
- sort() -  List with number values or list with string values can be sorted with the sort method.

        >>> spam.sort()
        >>> spam
        ['Hello', 'Hey', 'Hi', 'Namaste']
        >>> spamint = [9, 3, 6, 1]
        >>> spamint.sort()
        >>> spamint
        [1, 3, 6, 9]

  - sort in reverse order. 

            >>> spam.sort(reverse=True)
            >>> spam
            ['Namaste', 'Hi', 'Hey', 'Hello']

  - Can't sort lists that have both numbers and string values since Python doesn't really know how to compare these values.
  - Follows ASCII- Betical order means, uppercase characters come before lowercase characters.

RECAP

- Methods are functions that are "called on" values.
- The index() list method returns the index of an item in the list.
- The append() list method adds a value to the end of a list.
- The insert() list method adds a value anywhere inside a list.
- The remove() list method removes an item, specified by the value, from a list.
- The sort() list method sorts the items in a list.
- The sort() method's reverse=True keyword argument can make the sort() method sort in reverse order.
- These list methods operate on the list "in place", rather than returning a new list value.

-------------------------------------------------------

**SIMILARITIES: List & Strings**

- Strings can do a lot of the same things lists can do, but strings are immutable.
- Immutable values like strings and tuples cannot be modified "in place".
- Mutable values like lists can be modified in place.
Variables don't contain lists, they contain references to lists.
- When passing a list argument to a function, you are actually passing a list reference.
- Changes made to a list in a function will affect the list outside the function.
- The \ line continuation character can be used to stretch Python instruction across multiple lines.

Note: 

        import copy
        copy_spam = copy.deepcopy(spam) 
        # makes an entire new copy instead of referencing.