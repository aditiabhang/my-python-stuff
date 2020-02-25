# rotate2DArray - array - easy - Amazon, Apple, Microsoft.

# Note: Try to solve this task in-place (with O(1) additional memory), 
# since this is what you'll be asked to do during an interview.

# You are given an n x n 2D matrix that represents an image. 
# Rotate the image by 90 degrees (clockwise).

def rotate2DArray(arr):
    rotatedarray = []
    for i in range(len(arr)):
        rotatedarray.append([])
    for i in range(len(arr)):
        for j in range(len(arr)):
            # counterwise
            rotatedarray[i].append(arr[j].pop(-1))
            # counter clockwise
            #rotatedarray[i].insert(0, arr[j].pop(0))
    return rotatedarray

myNewArray = [[1,2,3],[4,5,6],[7,8,9]]
myRotatedArray = rotate2DArray(myNewArray)
print("Counter wise rotated array:")
for i in myRotatedArray:
    print(i)
