class Solution:
    def isValid(self, s: str) -> bool:
        dicti = {
            '(' : ')' ,
            '{' : '}' ,
            '[' : ']'

        }
        stack = []
        for i in s:
            
            
            if stack and dicti[stack[-1]] == i:
                stack.pop()

            elif i in dicti:
                stack.append(i)

            else:
                return False

        return True if not stack else False