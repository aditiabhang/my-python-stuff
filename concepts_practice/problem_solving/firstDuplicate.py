## firstDuplicate - arrays - easy - by Google.

# Given an array a that contains only numbers in the range from 1 to a.length, 
# find the first duplicate number for which the second occurrence has the minimal index. 
# In other words, if there are more than 1 duplicated numbers, 
# return the number for which the second occurrence has a smaller index than the second occurrence of the other number does. 
# If there are no such elements, return -1. 

def firstDuplicate(arr):
    dict = {}
    found = 0

    for i in range(len(arr)):
        if arr[i] in dict:
            dict[arr[i]] += 1
        else:
            dict[arr[i]] = 1

        if dict[arr[i]] == 2:
            return arr[i]

    if not found:
        return -1

x = [int (i) for i in input().split()]
print("Given array: ", x)
print("Output of program: ", firstDuplicate(x))
