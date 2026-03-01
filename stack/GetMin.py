"""
Implement a class SpecialStack that supports following operations:

push(x) – Insert an integer x into the stack.
pop() – Remove the top element from the stack.
peek() – Return the top element from the stack. If the stack is empty, return -1.
getMin() – Retrieve the minimum element from the stack in O(1) time. If the stack is empty, return -1.
isEmpty() –  Return true if stack is empty, else false
There will be a sequence of queries queries[][]. The queries are represented in numeric form:

1 x : Call push(x)
2:  Call pop()
3: Call peek()
4: Call getMin()
5: Call isEmpty()


"""

class SpecialStack:

    def __init__(self):
        self.st = []
        self.minele = -1
        
    
    def push(self, x):
        # Add an element to the top of Stack
        if self.st:
            if x >= self.minele:
                self.st.append(x)
            else:
                self.st.append(2*x-self.minele)
                self.minele = x
        else:
            self.minele = x
            self.st.append(x)

    
    def pop(self):
        # Remove the top element from the Stack
        if self.st:
            if self.st[-1] < self.minele:
                temp = self.minele
                self.minele = 2*self.minele - self.st[-1]
                self.st.pop()
                return temp
            else:
                temp = self.st[-1]
                self.st.pop()
                return temp
                

    
    def peek(self):
        # Returns top element of Stack
        if self.st:
            if self.st[-1] < self.minele:
                return self.minele
            else:
                return self.st[-1]
        else:
            return -1
        
    def isEmpty(self):
        if self.st:
            return False
        else:
            return True

    
    def getMin(self):
        # Finds minimum element of Stack
        
        if self.st:
            return self.minele
        else:
            return -1