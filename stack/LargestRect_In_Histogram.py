def nextLargerElement(self, arr):
        n = len(arr)
        Next_smaller = [0]*n
        prev_smaller = [0]*n
        stack = []
        for i in range(n-1,-1,-1):
            while stack and arr[i] <= arr[stack[-1]]:
                
                stack.pop()
                
            if stack:          
                Next_smaller[i] = stack[-1]
            else:
                Next_smaller[i] = n
                
            stack.append(i)
            
        while stack:
            stack.pop()
            
        for i in range(0,n):
            while stack and arr[i] <= arr[stack[-1]]:
                
                stack.pop()
                
            if stack:          
                prev_smaller[i] = stack[-1]
            else:
                prev_smaller[i] = -1
                
            stack.append(i)
            
        ans = 0
        for i in range(0,n):
            ans = max(ans , arr[i]*(Next_smaller[i]-prev_smaller[i]-1))
            

        