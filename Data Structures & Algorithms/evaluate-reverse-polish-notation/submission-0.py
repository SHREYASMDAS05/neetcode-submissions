
import operator
class Solution:
    
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        dops = {
            '+': operator.add,
            '-': operator.sub,
            '*': operator.mul,
            '/': lambda a, b: int(operator.truediv(a, b))
            }
        for i in tokens:
            if i in dops:
                a = stack.pop()
                b = stack.pop()
                res = dops[i](b , a)
                stack.append(res)
            else:
                stack.append(int(i))

        return stack[-1]


        