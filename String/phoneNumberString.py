from typing import List


"""
    Time complexity - O(2 ^ N)
"""

def letter_combinations_of_phone_number(digits: str) -> List[str]:
        # WRITE YOUR BRILLIANT CODE HERE
        def dfs(current, result):
                if len(current) == len(digits):
                       result.append(''.join(current))
                       return

                next_number = digits[len(current)]
                for letter in KEYBOARD[next_number]:
                        current.append(letter)
                        dfs(current, result)
                        current.pop()

        
        res = []
        dfs([], res)

        return res



KEYBOARD = {
    '2': 'abc',
    '3': 'def',
    '4': 'ghi',
    '5': 'jkl',
    '6': 'mno',
    '7': 'pqrs',
    '8': 'tuv',
    '9': 'wxyz',
}


inputs = ["56", "23", "235", "82966556"]
for i in range(len(inputs)):
    print("Letter combinations of a phone number :",sorted(letter_combinations_of_phone_number(inputs[i])))