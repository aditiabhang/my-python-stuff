# ------ DICTIONARIES ------
student = {'name' : 'Aditi', 'degree': 'Graduate', 'courses': ['Algorithms', 'SW Quality']}
print("Dictionary", student)
print("Name", student['name'])

# The keys and values can be any mutable datatype.
# throws an error when try to access a key than doesnt exist

# get() - when we dont want this error and instead want an output as 'none'.
print("Using get method: ", student.get('age'))
# if we want a specific value we add the default value like below
print("Using get method default value: ", student.get('age', 'Not found.'))
print("")

# insert a key-value
student['age'] = 27
print("Inserting a kye-value: ", student)
print("")

# update() - update/ adds the dictionary
student.update({'name': 'Aditi Abhang', 'degree': 'Graduate', 'phone': '666-666-666'})
print("Updated dictionary: ", student)
print("")

# del() - remove a key value
del student['courses']
print("Deleting courses key: ", student)
print("")

# pop() - removes the last key-value
#       - also used in lists
#       - also stores the popped value

popped = student.pop('degree')
print("Popped: ", popped)
print("")

# len() - number of keys in the dictionary
print("Length of the student dictionary: ",len(student))
print("")

# keys() - to view all the keys in the dictionary
print("Keys: ", student.keys())
# value() - to view all the values
print("Values: ", student.values())
# items() - to view the keys-value pairs
print("Items: ", student.items())
print("")

# Looping in the dictionary :-

print("Keys: ")
for keys in student:
    print(keys)
print("")

print("Using items() in loop: ")
for keys, values in student.items():
    print(keys, values)

