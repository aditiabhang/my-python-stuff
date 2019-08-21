## **Dictionaries**
- A dictionary is similar to a list, but you access values by looking up a key instead of an index. A key can be any string or number. Dictionaries are enclosed in curly braces, like so:
      d = {'key1' : 1, 'key2' : 2, 'key3' : 3}
    - This is a dictionary called d with three key-value pairs. The key 'key1' points to the value 1, 'key2' to 2, and so on.
- Example
      residents = {'Puffin' : 104, 'Sloth' : 105, 'Burmese Python' : 106}
      print residents['Puffin'] //Prints Puffin's room number
- Like Lists, Dictionaries are mutable. This means they can be changed after they are created. One advantage of this is that we can add new key/value pairs to the dictionary after it is created like so:
      dict_name[new_key] = new_value
- Example:
      menu = {} # Empty dictionary
      // Your code here: Add some dish-price pairs to menu!
      menu['Dosa'] = 6.99
      menu['Idli Sambhar'] = 4.99
      menu['Medu Wada'] = 5.99
      print "There are " + str(len(menu)) + " items on the menu."
      print menu

      Output:
      There are 4 items on the menu.
      {'Idli Sambhar': 4.99, 'Chicken Alfredo': 14.5, 'Dosa': 6.99, 'Medu Wada': 5.99}
- Items can be removed from a dictionary with the del command:
      del dict_name[key_name]
- A new value can be associated with a key by assigning a value to the key, like so:
      dict_name[key] = new_value
- Sometimes you need to remove something from a **list**.
      beatles = ["john","paul","george","ringo","stuart"]
      beatles.remove("stuart")
---------------------------------------------
- Let’s go over a few last notes about dictionaries.
      inventory = {
        'gold' : 500,
        'pouch' : ['flint', 'twine', 'gemstone'],
        //Assigned a new list to 'pouch' key
        'backpack' : ['xylophone','dagger', 'bedroll','bread loaf'] }
- Above is a dictionary made of key-values set of ints and list.
      //Adding a key 'burlap bag' and assigning a list to it.
      inventory['burlap bag'] = ['apple', 'small ruby', 'three-toed sloth']

      // Sorting the list found under the key 'pouch'
      inventory['pouch'].sort()

      // removing the dagger
      inventory['backpack'].remove('dagger')

      // Add 50 to the number stored under the 'gold' key
      inventory['gold'] += 50
