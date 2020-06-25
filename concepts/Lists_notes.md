### **Lists**
- Lists are a datatype you can use to store a collection of different pieces of information as a sequence under a single variable name.

        zoo_animals = ["pangolin", "cassowary", "sloth", "Dog" ];
        if len(zoo_animals) > 3:
        print "The first animal at the zoo is the " + zoo_animals[0]
        print "The second animal at the zoo is the " + zoo_animals[1]
        print "The third animal at the zoo is the " + zoo_animals[2]
        print "The fourth animal at the zoo is the " + zoo_animals[3]

- You can access an individual item on the list by its index.

        numbers = [5, 6, 7, 8]
        print "Adding the numbers at indices 0 and 2..."
        print numbers[0] + numbers[2]

    ```
    Output:
    Adding the numbers at indices 0 and 2...
    12
    ```
    
- A list index behaves like any other variable name! It can be used to access as well as assign values.

- A list doesn’t have to have a fixed length. You can add items to the end of a list any time you like!
      letters = ['a', 'b', 'c']
      letters.append('d')
      print len(letters)
  
- Sometimes, you only want to access a portion of a list.
First, we create a list called letters.
Then, we take a subsection of the list and store it in the slice list. We do this by defining the indices we want to include after the name of the list: letters[1:3]. In Python, when we specify a portion of a list in this manner, we include the element with the first index, 1, but we exclude the element with the second index, 3.
  
  - Means, we call the first element as 0:1, second as 1:2, third as 2:3 and so on. (Only for sub-selection purpose)
  
- You can slice a string exactly like a list!

- If your list slice includes the very first or last item in a list (or a string), the index for that item doesn’t have to be included.

      animals = "catdogfrog"
      # The first three characters of animals
      cat = animals[:3]
      # The fourth through sixth characters
      dog = animals[3:6]
      # From the seventh character to the end
      frog = animals[6:]
  
- Sometimes you need to search for an item in a list.
      
      animals = ["aardvark", "badger", "duck", "emu", "fennec fox"]
      duck_index = animals.index("duck")

      # We can also insert items into a list.
      animals.insert(duck_index,"cobra")

- NOTE - In slice, new list items start at the first index and go up to but don't include the second index.
--------------------------------------------------
**For loop**
- A variable name follows the for keyword; it will be assigned the value of each list item in turn.
Then in list_name designates list_name as the list the loop will work on. The line ends with a colon (:) and the indented code that follows it will be executed once per item in the list.
      for variable in list_name:
      // Do stuff!
- Example
  -  Write a for-loop that iterates over start_list and .append()s each number squared (x ** 2) to square_list. Then sort square_list.

            start_list = [5, 3, 1, 2, 4]square_list = []

            # Your code here!
            
            for x in start_list:
            square_list.append(x ** 2)
            square_list.sort()
            print square_list
--------------------------------------------------

**NOTES from: Automate boring stuff with python**
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