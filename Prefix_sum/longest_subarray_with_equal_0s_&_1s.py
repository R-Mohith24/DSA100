'''Given an array arr of 0s and 1s. Find and return the length of the longest subarray with equal number of 0s and 1s.'''

'''
Input: arr[] = [1, 0, 1, 1, 1, 0, 0]
Output: 6
Explanation: arr[1...6] is the longest subarray with three 0s and three 1s.
'''
class Solution:
    def maxLen(self, arr):
        prefixsum = 0
        mp = {} # prefixsum -- > index
        
        res = 0
        
        for i in range(len(arr)):
            prefixsum += -1 if arr[i] == 0 else 1
            
            if prefixsum == 0:
                res = i + 1
                
                
            if prefixsum in mp:
                res = max(res , i-mp[prefixsum])
                
            else:
                mp[prefixsum] = i
                
        return res
    
    
    
    
    