'''
Find Intersection
Have the function FindIntersection(strArr) read the array of strings stored in strArr which will contain 2 elements: 
the first element will represent a list of comma-separated numbers sorted in ascending order, 
the second element will represent a second list of comma-separated numbers (also sorted). 
Your goal is to return a comma-separated string containing the numbers that occur in elements of strArr in sorted order. 
If there is no intersection, return the string false.

Examples
Input: ["1, 3, 4, 7, 13", "1, 2, 4, 13, 15"]
Output: 1,4,13

Input: ["1, 3, 9, 10, 17, 18", "1, 4, 9, 10"]
Output: 1,9,10

'''
def FindIntersection(strArr):
  first_list = strArr[0].split(', ')
  second_list =strArr[1].split(', ')
  final_list = []
  string = ''
  if len(set(first_list) & set(second_list)) == 0:
    return 'false'
  else:
    for i in set(first_list) & set(second_list):
      final_list.append(int(i))
    for j in sorted(final_list):
      string = string + str(j) + ','
    return string[:-1]

# keep this function call here 
strArray = ["1, 3, 4, 7, 13", "1, 2, 4, 13, 15"]
print(FindIntersection(strArray))