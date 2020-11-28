
class Solution:
    def calculate(self, s):
        operators, operands = [], []
        
        s = s.replace(' ', '')
        i = 0
        
        while i < len(s):
            char = s[i]
            
            if char.isdigit():
                number = 0
                while i < len(s) and s[i].isdigit():
                    number = (number * 10) + int(s[i])
                    i += 1
                
                i -= 1
                
                operands.append(number)
                
            else:
                while (len(operators) != 0 and self.getPrecedence(operators[-1]) >= self.getPrecedence(char)):
                    op = operators.pop()
                    op2 = operands.pop()
                    op1 = operands.pop()
                    
                    result = self.evaluate(op, op1, op2)
                    operands.append(result)
                
                operators.append(char)
            
            i += 1
                
        while len(operators) != 0:
            op = operators.pop()
            op2 = operands.pop()
            op1 = operands.pop()
            result = self.evaluate(op, op1, op2)
            operands.append(result)
        
        return operands[0]

        
        
    def getPrecedence(self, operator):
        priority = {
            '+': 1,
            '-': 1,
            '*': 2,
            '/': 2
        }
        
        return priority[operator]
    
    def evaluate(self, operator, operand1, operand2):
        expressions = {
            '+': operand1 + operand2,
            '-': operand1 - operand2,
            '*': operand1 * operand2,
            '/': 0 if operand2 == 0 else operand1 // operand2
        }
        
        result = expressions[operator]
        
        return result
        

# Driver Code
if __name__ == "__main__":
     
    print(Solution().calculate("10 + 2 * 6"))
    print(Solution().calculate("100 * 2 + 12"))