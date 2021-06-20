

"""
Time Complexity - O(1)
"""
def evenOrOdd(n):
    return "EVEN" if (n & 1) == 0 else "ODD"



print(evenOrOdd(125))
print(evenOrOdd(8))