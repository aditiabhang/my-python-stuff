##------ LISTS ------ 
courses = ['Algorithms and Data Analysis', 'Software Quality', 'Formal Languages', 'Python Self Study']
print("Printing the list: ",courses)
print("Printing the length of the list: ",len(courses))
print("Printing the last element of the list: ",courses[3])
print("Printing the second last element of the list using negative indexing: ",courses[-2])
print("")
# If we try to access the index that doesnt exist, an error is occured saying;
# -> IndexError: list out of range

# accesing only the part of the list
print("Accessing part of list: ", courses[0:2])
# First part of index in inclusive but the second is NOT.
courses.append('PHP Project')
print("Appending to the list: ", courses)
print("")

# inserting an element to a specifix index
courses.insert(2, 'Survey of SW Engg')
print("Inserting new course at the index 2: ", courses)
print("")

# we can even add list within a list, like below
print("List within a list:")
courses_1 = ['Masters', 'CompSci']
courses.insert(0, courses_1)
print(courses)
print("")

# adding values of second list to original list
print("Extending the list with other list:")
courses_2 = ['Library', 'TSU']
courses_1.extend(courses_2)
print(courses_1)
print("")

# NOTE:
# append() adds up the entire list (inclusing the brackets) to the list.
# extend() adds the each individual elements of a list to the original list.

# Simple methods: -
# remove(value) - to remove the value
# pop() - to remove the last value of the list
#       - we can check which value is popped by simply applying the method to a variable
popped = courses.pop()
print("Popped value: ",popped)
print("")

# reverse() - reverse the order of the list
# sort() - sorts the list alphabetically or numerically ascending order
# sort(reverse = True) - to sort the list in reverse/descending order
nums = [3, 6, 33, 9, 66, 13]
courses_1.reverse()
courses_1.sort()
courses_1.sort(reverse = True)
nums.sort(reverse = True)
print("Reverse alphabets: ", courses_1)
print("Sorting list of courses: ", courses_1)
print("Sorting the list in reverse order: ", courses_1)
print("Sorting the number list in reverse order: ", nums)
print("")

# NOTE: sort() and sorted()
# sort() method changes the list
# sorted method doesnt change the list instead shows the version of sorted list. 
# A variable is created to keep the sorted version of list.

# More simple methonds: -
# min(), max(), and sum().
# The name implies the meaning.

# index() - returns the index of the value
print("At what index is the value - Masters? It is at: ", courses_1.index('Masters'))
print("")

# in - to check if the value is in the list
print("Is Library keyword value in the list?: ", 'Library' in courses_1)

# loop to print each item in the list
for item in courses_1:
    print(item)
print("")

# enumerate function: -
# - Access the index as well as values of the list
# - returns index and the value
for index, item in enumerate(courses):
    print(index,item)
print("")

# If we dont want to start at 0, and start at 1, we simple do as follows:
for index, item in enumerate(courses, start = 1):
    print(index,item)
print("")

# join() -
# - convert the list into string separated by a certain value
courses_str = ', '.join(courses_1)      # used '.' as a separater
courses_str1 = ' - '.join(courses_2)     # used '-' as a separater
print(courses_str)
print(courses_str1)

# split() -
# - splits the list separated by a certain value
courses_str2 = courses_str.split('-')       #this has to be done on join
print(courses_str2) 
print("") 

## ------ TUPLES ------
# - Lists are mutable but tuples are NOT mutable
# Proof: lists are mutable
print("Lists are mutable.")
list1 = ['Amazon', 'IBM', 'Facebook', 'Google']
list2 = list1
print (list2)
list1[0] = 'Apple'
print("List 1: ", list1)
print("List 2: ",list2)
print("")
# If we want to update/change the object, we use lists. Hence, mutable.

# Proof: tuples are not mutable
print("Tuples are immutable.")
tuple1 = ('Amazon', 'IBM', 'Facebook', 'Google')
tuple2 = tuple1
print (tuple2)
# tuple1[0] = 'Apple'
print("Tuple 1: ", tuple1)
print("Tuple 2: ", tuple2)
print("When we try to change the tuple like we did in the lists above, we get the above error.")
print("")

# Difference between lists and tuple:
# - we cant append, insert, or remove any elements in a tuple, like we can do it list.
# Other than this difference, list and tuple behaves the same.
# We can loops through lists and tuples, access the elements, etc. 

## ------ SETS ------
# Sets are sets of ordered or unordered values, has no duplicates.
# Has curly braces.
# Every time we print a set, it is displayed in different order.
# Bcz, sets dont care about the order, it is mainly used to see if the value is a part of
# a set, also used to remove duplicate values.

set1 = {'Amazon', 'IBM', 'Google', 'Facebook', 'Facebook'}
# When we print a set with duplicate values, the duplicate value will be thrown away, and
# display only one value. 
print(set1)

# Membership test - checks if a value is part of the set.
# Sets performs this better than lists or tuples
print(" Is Amazon in set1?", 'Amazon' in set1)

# Sets determine what values they share or dont share with other sets
# intersection() - determines the common.
set2 = {'Amazon', 'Facebook', 'Intel', 'Dell'}
print("Intersection of sets: ", set1.intersection(set2))
# difference() - What is in set1 but not in set2?
print("Difference: ", set1.difference(set2))
# union() - combine all the values in both sets
print("Union: ", set1.union(set2))

# Tip: Creatig empty set of lists, tuples and sets.
empty_list = []
empty_list = list[]

empty_tuple = ()
empty_tuple = tuple()

empty_set = ()  # this is not correct. It creates an empty dictionary
empty_set = set()