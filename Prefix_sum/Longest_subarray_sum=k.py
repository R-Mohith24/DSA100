'''Given an array arr[] containing integers and an integer k, your task is to find the length of the longest subarray
where the sum of its elements is equal to the given value k. If there is no subarray with sum equal to k, return 0.'''


'''
Input: arr[] = [10, 5, 2, 7, 1, -10], k = 15
Output: 6
Explanation: Subarrays with sum = 15 are [5, 2, 7, 1], [10, 5] and [10, 5, 2, 7, 1, -10]. 
The length of the longest subarray with a sum of 15 is 6.

'''

class Solution:
    def longestSubarray(self, arr, k):
        mp = {}  # {prefixsum : index}
        prefixsum = 0
        max_lenght = 0
        
        for i in range(len(arr)):
            
            prefixsum += arr[i]
            
            if prefixsum == k:
                max_lenght = i + 1
                
            if (prefixsum - k) in mp:
                lenght = i - mp[prefixsum - k]
                max_lenght = max(max_lenght , lenght)
                
            if (prefixsum) not in mp:
                mp[prefixsum] = i
                
        return max_lenght
    
    '''
    1. We initialize a dictionary `mp` to store the prefix sums and their corresponding indices.
    2. We also initialize `prefixsum` to keep track of the cumulative sum and `max_length` to store the length of the longest subarray found.
    3. We iterate through each element in the array:
       a. We update the `prefixsum` by adding the current element.
       b. If the `prefixsum` equals `k`, it means the subarray from the start to the current index has a sum of `k`, so we update `max_length`.
       c. We check if there exists a prefix sum such that `prefixsum - k` is in the dictionary. If it exists, it means there is a subarray that sums to `k`, and we calculate its length and update `max_length` if it's longer than the current maximum.
       d. We store the current `prefixsum` in the dictionary if it is not already present, along with the current index.
    4. Finally, we return the value of `max_length`.
    '''
    
    