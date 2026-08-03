class Solution:
    def isValid(self, s: str) -> bool:
        dict = {
            '(' : ')' ,
            '{' : '}' ,
            '[' : ']'

        }
        stack = []
        for i in s:
            
            
            if stack and dict[stack[-1]] == i:
                stack.pop()

            elif i in dict:
                stack.append(i)

            else:
                return False

        return True if not stack else False