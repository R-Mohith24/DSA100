'''
Given a string s containing only three types of characters: '(', ')' and '*', return true if s is valid.

The following rules define a valid string:

Any left parenthesis '(' must have a corresponding right parenthesis ')'.
Any right parenthesis ')' must have a corresponding left parenthesis '('.
Left parenthesis '(' must go before the corresponding right parenthesis ')'.
'*' could be treated as a single right parenthesis ')' or a single left parenthesis '(' or an empty string "".

'''

class Solution(object):
    def checkValidString(self, s):
        
        Min = Max = 0
        
        for i in s:
            if i =="(":
                Min += 1
                Max += 1
            elif i == ')':
                Min -= 1
                Max -= 1
            else:
                Min -= 1
                Max += 1
            if Max < 0:
                return False
            if Min < 0:
                Min = 0
            
        return Min == 0            
        
        