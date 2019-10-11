'''
Given a mobile number and some conditions for a fancy number,
find if the given number is fancy. A 10 digit mobile number is called fancy
if it satisfies any of the following three conditions.

1. A single number occurs three consecutive times. Like 777.
2. Three consecutive digits are either in increasing or decreasing fashion. Like 456 or 987.
3. A single digit occurs four or more times in the number. Like 9859009976 – here the digit 9 occurs 4 times.
'''
import collections 

def cond1(number_str):
    for i in range(len(number_str)-2):
        if (number_str[i] == number_str[i+1] and number_str[i+1] == number_str[i+2]):
            return True
        else:
            return False

def cond2(number_str):
    for i in range(len(number_str)-2):
        if (number_str[i] < number_str[i + 1] and number_str[i + 1] < number_str[i + 2] or number_str[i] > number_str[i + 1] and number_str[i + 1] > number_str[i + 2]):
            return True
        else:
            return False

# def cond3(number_str):
#     countdict = collections.Counter(number_str)
#     for keys in countdict:
#         if countdict[keys] > 4:
#             return True
#         else:
#             return False
    

def isFancy(num_str):
    if (cond1(num_str) or cond2(num_str)):  #or cond3(num_str)
        return True
    else:
        return False



# Driver program
mobile_number = '1746294766666'

if (isFancy(mobile_number)):
    print("Yes. You got a fancy number!")
else:
    print(" Neahh, thats not a fancy number.")


# s = '90999904835545'

# # l2 = []
# # for i in s: 
# #     l2.append(i)
# # print(l2)    

# listy = [n for n in s]

# my_dict = collections.Counter(listy)

# print(my_dict)

# for keys in my_dict:
#     if my_dict[keys] > 4:
#         print("YES")
#     else:
#         print("NO")    




