
#from geeksforgeeks stack next greater element problem


class Solution:
    def nextLargerElement(self, arr):
        n = len(arr)
        res = [-1]*n
        stack = []
        for i in range(n-1,-1,-1):
            while stack and arr[i] >= arr[stack[-1]]:
                
                stack.pop()
                
            if stack:
                
                res[i] = arr[stack[-1]]
                
            stack.append(i)
            
        return res