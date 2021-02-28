"""
Time Complexity - O(N*logN + N*max(deadline))
Space Complexity - O(max(deadline))
"""
class Solution:
    def JobScheduling(self,Jobs,n):
        '''
        :param Jobs: list of "Job" class defined in driver code, with "profit" and "deadline".
        :param n: total number of jobs
        :return: A list of size 2 having list[0] = count of jobs and list[1] = max profit
        '''
        '''
        {
            class Job:.
            def __init__(self,profit=0,deadline=0):
                self.profit = profit
                self.deadline = deadline
                self.id = 0
        }
        '''
        # code here
        Jobs.sort(key=lambda x: x.profit, reverse=True)
        maxDeadline = max(job.deadline for job in Jobs)
        jobs_array = [-1 for i in range(maxDeadline)]
        profits, jobExecuted = 0, 0
        for job in Jobs:
            position = find_pos(jobs_array, job.deadline - 1)
            if position != -1:
                jobExecuted += 1
                profits += job.profit
                jobs_array[position] = job.id
                
        return (jobExecuted, profits)
            
            
def find_pos(jobs_array, startIndex):
    i = startIndex
    while i >= 0 and jobs_array[i] != -1:
        i -= 1
    
    return i



class Job:
    def __init__(self, _id, deadline=0, profit=0):
        self.profit = profit
        self.deadline = deadline
        self.id = _id



def main():
    # TestCase 1
    Jobs = [Job(1, 4, 20), Job(2, 1, 10), Job(3, 1, 40), Job(4, 1, 30)]
    print(Solution().JobScheduling(Jobs, 4))

    # Testcase 2
    Jobs = [Job(1, 2, 100), Job(2, 1, 19), Job(3, 2, 27)]
    print(Solution().JobScheduling(Jobs, 4))


main()