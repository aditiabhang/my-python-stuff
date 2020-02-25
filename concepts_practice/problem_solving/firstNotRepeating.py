# firstNotRepeating - array - easy - Amazon

# Given a string s consisting of small English letters, 
# find and return the first instance of a non-repeating character in it. 
# If there is no such character, return '_'.

def firstNotRepeating(arr):
    chars = []
    char_count = {}

    for i in arr:
        if i in char_count:
            char_count[i] += 1
        else:
            char_count[i] = 1
            chars.append(i)
    for i in chars:
        if char_count[i] == 1:
            return i
    return "_"

arr = [int(i) for i in input().split()]
print("Given array: ", arr)
print("Output of program: ", firstNotRepeating(arr))