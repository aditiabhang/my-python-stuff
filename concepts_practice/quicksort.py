# Python code for randomised Quicksort using Hoare's partition scheme.

import random

'''
This funtion implements randomised partition 
array : An array of inputs
low : first index of the array
high : last index of the array
'''
def quick_sort(array, low, high):
    if low < high:
        # Finding the pivot index
        pivotIndex = random_partition(array, low, high)
        quick_sort(array, low, pivotIndex)
        quick_sort(array, pivotIndex + 1, high)
'''
This function generates random pivot, swaps the first 
element with the pivot and calls the partition function.
'''
def random_partition(array, low, high):
    #generating random pivot index between low and high
    random_pivot = random.randrange(low, high)
    array[low], array[random_pivot] = array[random_pivot], array[low]
    return partition(array, low, high)
''' 
This function takes the first element as pivot,  
places the pivot element at the correct position  
in the sorted array. All the elements are re-arranged  
according to the pivot, the elements smaller than  
the pivot is places on the left and the elements 
greater than the pivot is placed to the right of pivot. 
'''
def partition(array, low, high):
    pivot = low
    i = low - 1
    j = high + 1
    while True:
        i = i + 1
        if array[i] >= array[pivot]:
            break
    while True:
        j = j - 1
        if array[j] <= array[pivot]:
            break
    if i >= j:
        array[i], array[j] = array[j], array[i]

# Driver code
if __name__ == '__main__':
    A = [10, 7, 8, 9, 1, 5] 
    n = len(A)-1
    quick_sort(A, 0, n)
    print("Quick Sort Results: ", A)


# Python implementation QuickSort using  
# Hoare's partition Scheme. 
  
# import random 
  
# ''' 
# The function which implements randomised QuickSort, 
# using Haore's partition scheme. 
# arr :- array to be sorted. 
# start :- starting index of the array. 
# stop :- ending index of the array. 
# '''
# def quicksort(arr, start, stop): 
#     if start < stop: 
          
#         # pivotindex is the index where 
#         # the pivot lies in the array 
#         pivotindex = partitionrand(arr, start, stop) 
          
#         # At this stage the array is partially sorted  
#         # around the pivot. seperately sorting the  
#         # left half of the array and the right half of the array. 
#         quicksort(arr , start , pivotindex) 
#         quicksort(arr, pivotindex + 1, stop) 
  
# # This function generates random pivot, swaps the first 
# # element with the pivot and calls the partition fucntion. 
# def partitionrand(arr , start, stop): 
  
#     # Generating a random number between  
#     # the starting index of the array and  
#     # the ending index of the array. 
#     randpivot = random.randrange(start, stop) 
  
#     # Swapping the starting element of  
#     # the array and the pivot 
#     arr[start], arr[randpivot] = arr[randpivot], arr[start] 
#     return partition(arr, start, stop) 
  
# ''' 
# This function takes the first element as pivot,  
# places the pivot element at the correct position  
# in the sorted array. All the elements are re-arranged  
# according to the pivot, the elements smaller than  
# the pivot is places on the left and the elements 
# greater than the pivot is placed to the right of pivot. 
# '''
# def partition(arr,start,stop): 
#     pivot = start # pivot 
#     i = start - 1
#     j = stop + 1
#     while True: 
#         while True: 
#             i = i + 1
#             if arr[i] >= arr[pivot]: 
#                 break
#         while True: 
#             j = j - 1
#             if arr[j] <= arr[pivot]: 
#                 break
#         if i >= j: 
#             return j 
#         arr[i] , arr[j] = arr[j] , arr[i] 
  
# # Driver Code 
# if __name__ == "__main__": 
#     array = [10, 7, 8, 9, 1, 5] 
#     quicksort(array, 0, len(array) - 1) 
#     print("Quick Sort Result: ", array)


