from collections import deque

class Solution:
    def decodeString(self, s):
        stack =  deque([])
        length = len(s)
        i = 0
        while i < len(s):
            char = s[i]
            
            if char == '[' or char == ']':
                if char == ']':
                    pop_str = stack.popleft()
                    pop_number = stack.popleft()
                    evaluated_val = pop_str * pop_number
                    if stack and not str(stack[0]).isdigit():
                        stack.appendleft(stack.popleft() + evaluated_val)
                    else:
                        stack.appendleft(evaluated_val)
                    
                    
            elif char.isdigit():
                number = 0
                while i < length and s[i].isdigit():
                    number = (number * 10) + int(s[i])
                    i += 1
                
                stack.appendleft(number)
                i -= 1
            else:
                str_ = ''
                while i < length and not s[i].isdigit() and s[i] != '[' and s[i] != ']':
                    str_ += s[i]
                    i += 1
                
                if stack and not str(stack[0]).isdigit():
                    stack.appendleft(stack.popleft() + str_)
                else:
                    stack.appendleft(str_)
                    
                i -= 1
            
            i += 1
            
        
        result = ''
        while stack:
            pop = stack.popleft()
            result = pop + result
        
        
        return result



def main():
    print(Solution().decodeString("3[a2[c]]"))
    print(Solution().decodeString("2[abc]3[cd]ef"))


main()
        
        
            
        