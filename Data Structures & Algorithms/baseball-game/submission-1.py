class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        for i in operations:
            
            if i == '+':
                val = stack[-1] + stack[-2]
                stack.append(val)

            elif i == 'C':
                stack.pop()

            elif i == 'D':
                val = 2 * stack[-1]
                stack.append(val)

            else:
                stack.append(int(i))

        return sum(stack)