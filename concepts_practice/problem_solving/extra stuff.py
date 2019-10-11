# a = [5, 6, 7]
# b = [3, 6, 10]


# def compareTriplets(a, b):
#     alice = 0
#     bob = 0
#     for i in range(3):
#         if a[i] > b[i]:
#             alice += 1
#         elif a[i] < b[i]:
#             bob += 1
#     print(alice, bob)

# compareTriplets(a, b)
#---------------------------------------------------------------
# ar = {1000000001, 1000000002, 1000000003, 1000000004, 1000000005}
# n = len(ar)

# def aVeryBigSum(ar):
#     total = sum(ar)
#     print (total)

# aVeryBigSum(ar)
#---------------------------------------------------------------
'''
Sample Input :
3
1 5
3 10
999 -34343

Sample Output :
6
13
-33344
'''             
# Add the two numbers

n = int(input())
for i in range(n):
    a, b = input().strip().split(' ')
    print (int(a) + int(b))
