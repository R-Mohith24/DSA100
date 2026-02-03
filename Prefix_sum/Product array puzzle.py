class Solution:
    def productExceptSelf(self, arr):
        n = len(arr)

        prefix = [1] * n
        suffix = [1] * n
        res = [0] * n

        # prefix product
        for i in range(1, n):
            prefix[i] = prefix[i - 1] * arr[i - 1]

        # suffix product
        for i in range(n - 2, -1, -1):
            suffix[i] = suffix[i + 1] * arr[i + 1]

        # result
        for i in range(n):
            res[i] = prefix[i] * suffix[i]

        return res
    
    
'''
Given an array, arr[] construct a product array, res[] where each element in res[i] is the product of all elements in arr[] except arr[i].
Return this resultant array, res[].
Note: Each element is res[] lies inside the 32-bit integer range.



Input: arr[] = [10, 3, 5, 6, 2]
Output: [180, 600, 360, 300, 900]
Explanation: For i=0, res[i] = 3 * 5 * 6 * 2 is 180.
For i = 1, res[i] = 10 * 5 * 6 * 2 is 600.
For i = 2, res[i] = 10 * 3 * 6 * 2 is 360.
For i = 3, res[i] = 10 * 3 * 5 * 2 is 300.
For i = 4, res[i] = 10 * 3 * 5 * 6 is 900.

'''


