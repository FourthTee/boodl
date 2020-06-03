# Given an array of integers, return indices of the two numbers such that they add up to a specific target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
# Given nums = 2, 7, 11, 15, target = 9, Because nums[0] + nums[1] = 2 + 7 = 9, return 0, 1.

def sumton(arr, target):

    n = len(arr)

    for i in range(0, n-1):
        for j in range(i + 1, n):
            s = arr[i] + arr[j]
            if s == target:
                return tuple([i, j])
    
