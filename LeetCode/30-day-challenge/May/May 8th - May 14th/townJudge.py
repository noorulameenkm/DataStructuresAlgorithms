class Solution:
    def findJudge(self, N, trust):
        
        if len(trust) == 0:
            if N > 1:
                return -1
            else:
                return N
        
        d = {}
        trusters = []
        for trustees in trust:
            
            trusters.append(trustees[0])
            
            if trustees[1] not in trusters:
                if trustees[1] in d:
                    d[trustees[1]].append(trustees[0])
                else:
                    d[trustees[1]] = [trustees[0]]
            
            if trustees[0] in d:
                del d[trustees[0]]
                
        
        if len(d.keys()) == 0:
            return -1
        
        for key in d.keys():
            if len(d[key]) == N - 1:
                return key
        
        return -1


print(f'Trusted judge fo N = 2 and trustees = [[1,2]] is {Solution().findJudge(2, [[1,2]])}')
            
        