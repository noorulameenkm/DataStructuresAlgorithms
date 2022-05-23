
"""
    Time Complexity - O(1)
    Space Complexity - O(R) R=>the number of requests received
"""

class RequestLimiter:
    def __init__(self):
        self.requests = {}

    def request_approver(self, timestamp, request):
        if request not in self.requests or timestamp - self.requests[request] >= 5:
            self.requests[request] = timestamp
            print("Request Accepted")
            return True
        else:
            print("Request Rejected")
            return False


# Driver code

obj = RequestLimiter()
obj.request_approver(1, "send_message")
obj.request_approver(2, "block")
obj.request_approver(3, "send_message")
obj.request_approver(8, "block")
obj.request_approver(10, "send_message")
obj.request_approver(11, "send_message")
