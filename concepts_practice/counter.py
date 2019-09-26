# ------ COUNTER ---------

# Counter - is s a container that keeps a track of how many time a value has been added. 
# We have to import collections

# ---- [A] Initialisation -----

# There  are 3 ways. (1) using list, (2) dictionary (3) argument = values
import collections
print ("(1) Using Lists: ", collections.Counter(['a', 'b', 'c', 'c', 'a', 'a']))
print("(2) Using Dictionary: ", collections.Counter({'a': 2, 'b': 1, 'c': 2}))
print("(3) Using Arguments: ", collections.Counter(a = 2, b = 1, c = 2))
print("")
# The results of all three forms of initialization are the same.

# An empty Counter can be constructed with no arguments and populated via the update() method.
c = collections.Counter()
print("Empty counter: ", c)
c.update('adbabccaac')
print("Sequence counter update: ", c)
c.update({'a': 4, 'b': 2, 'c': 2, 'd': 1})
print("Dictionary Counter update:", c)
print("")

# NOTE: The count values are increased based on the new data, rather than replaced.
# In this example, the count for a goes from 3 to 4.

# ---- [B] Accessing counts -----
# Once counter has been populated we can be retrieved using dictionary API
print("Accessing counts: ")
new_c = collections.Counter('adibcaadi')
for letter in 'abcdei':
    print("%s: %d" % (letter, new_c[letter]))

# NOTE: Counter does not raise KeyError for unknown items. It simply returns 0.

### elements() - method returns an iterator that produces all of the items known to the Counter.
print(list(new_c.elements()))

# NOTE: The order of elements is not guaranteed, and items with counts less than zero are not included.

# Use most_common() to produce a sequence of the n most frequently encountered input values and their respective counts.

# import collections

# c = collections.Counter()
# with open('/usr/share/dict/words', 'rt') as f:
#     for line in f:
#         c.update(line.rstrip().lower())

# print 'Most common:'
# for letter, count in c.most_common(3):
#     print '%s: %7d' % (letter, count)

# This example counts the letters appearing in all of the words in the system dictionary to produce a frequency distribution, then prints the three most common letters.
# Leaving out the argument to most_common() produces a list of all the items, in order of frequency.

# ---- [C] Arithmatics with counters -----
# Counter instances supports arithmation and set operations for aggregate results.

counter1 = collections.Counter(['a','d', 'i', 't', 'i', 'a', 'a'])
counter2 = collections.Counter('iamaditi')
print("\nArithmatic operations with Counters:")
print ("Counter 1: ", counter1)
print("Counter 2: ", counter2)
print("Addition: ", counter1 + counter2)
print("Substraction: ", counter2 - counter1)
print("Intersection: ", counter1 & counter2)
print("Union: ", counter1 | counter2)
