#DAY 1
'''
Given an array of integers arr[], the task is to find the first equilibrium point in the array.
The equilibrium point in an array is an index (0-based indexing) such that the sum of all elements
before that index is the same as the sum of elements after it. Return -1 if no such point exists. 
'''

'''
Input: arr[] = [1, 2, 0, 3]
Output: 2 
Explanation: The sum of left of index 2 is 1 + 2 = 3 and sum on right of index 2 is 3.
'''
class Solution:
    def findEquilibrium(self, arr):
        n = len(arr)
        left_sum = 0
        tot_sum = sum(arr)
        for i in range(n):
            right_sum = tot_sum - left_sum - arr[i]
            
            if left_sum == right_sum:
                return i
                
            left_sum += arr[i]
            
        return -1

