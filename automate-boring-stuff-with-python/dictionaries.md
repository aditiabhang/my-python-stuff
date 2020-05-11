**Dictionaries:**

- Dictionaries contain key-value pairs. Keys are like a list's indexes.
- Dictionaries are mutable. Variables hold references to dictionary values, not the dictionary value itself.
- Dictionaries are unordered. There is no "first" key-value pair in a dictionary.

        >>> picnic = {'Napkins': 3, 'Water': '20 Bottles', 'Chips': 10, 'Food': 'Veg Burgers'}

- The **keys(), values(), and items()** methods will return list-like values of a dictionary's keys, vaues, and both keys and values, respectively.

        >>> picnic.keys()
        dict_keys(['Napkins', 'Water', 'Chips', 'Food'])

        >>> picnic.values()
        dict_values([3, '20 Bottles', 10, 'Veg Burgers'])

        >>> picnic.items()
        dict_items([('Napkins', 3), ('Water', '20 Bottles'), ('Chips', 10), ('Food', 'Veg Burgers')])
- The **get()** method can return a default value if a key doesn't exist. 

        
        >>> picnic.get('Milk', 'Out of stock')
        'Out of stock'

        # If not present, then return what is mentioned

        >>> print("I am bringing " + str(picnic.get('Milk', 0)) + " to the picnic.")
        I am bringing 0 to the picnic.
        >>> print("I am bringing " + str(picnic.get('Napkins', 0)) + " to the picnic.")
        I am bringing 3 to the picnic.
- The **setdefault()** method can set a value if a key doesn't exist.
  - This can be done in 1 line of code.
  
        if 'Drinks' not in picnic:
            picnic.['Drinks'] = 'Juices only' 
            ====\/
        picnic.setdefault('Drinks','Juice only')

  - Doesnt change anything if the key is already present.

- The pprint module's **pprint()** "pretty print" function can display a dictionary value cleanly. 
- The **pformat()** function returns a string value of this output.

PS: Refer 'countCharacter.py'