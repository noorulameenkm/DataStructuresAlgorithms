"""
    Problem Link:- https://leetcode.com/problems/verify-preorder-serialization-of-a-binary-tree/
"""


class Solution:
    def isValidSerialization(self, preorder: str) -> bool:
        slots = 1
        for node_val in preorder.split(","):
            if slots <= 0:
                return False

            slots += -1 if node_val == '#' else 1

        return slots == 0


print(Solution().isValidSerialization(preorder="9,3,4,#,#,1,#,#,2,#,6,#,#"))
print(Solution().isValidSerialization(preorder="1,#"))
print(Solution().isValidSerialization(preorder="9,#,#,1"))
