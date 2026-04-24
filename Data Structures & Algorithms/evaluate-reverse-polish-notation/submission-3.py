class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        
        for t in tokens:
            if t in "+-*/":
                num1 = stack.pop()
                num2 = stack.pop()
                print(num1)
                print(num2)
                num1 = int(num1)
                num2 = int(num2)
                if t == "+":
                    stack.append(num2+num1)
                elif t == "-":
                    stack.append(num2-num1)
                elif t == "*":
                    stack.append(num2*num1)
                elif t == "/":
                    stack.append(num2/num1)
            else:
                stack.append(t)
        return int(stack.pop())

            