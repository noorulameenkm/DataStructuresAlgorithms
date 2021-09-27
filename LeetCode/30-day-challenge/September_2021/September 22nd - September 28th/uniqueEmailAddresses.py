from typing import List


"""
Problem Link:-
"""


class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        set_ = set()
        for email in emails:
            local_name, domain_name = email.split('@')
            local_name = local_name.split('+')[0]
            local_name = local_name.split('.')
            local_name = ''.join(local_name)
            email_ = local_name + '@' + domain_name
            set_.add(email_)
        return len(set_)


print(Solution().numUniqueEmails(
    [
        "test.email+alex@leetcode.com",
        "test.e.mail+bob.cathy@leetcode.com",
        "testemail+david@lee.tcode.com"
    ]
))
print(Solution().numUniqueEmails(
    [
        "a@leetcode.com",
        "b@leetcode.com",
        "c@leetcode.com"
    ]
))
