class Solution:
    def numPairsDivisibleBy60(self, time):
        count = 0
        for i in range(len(time) - 1):
            for j in range(i + 1, len(time)):
                if (time[i] + time[j]) % 60 == 0:
                    count += 1
        
        return count


def numPairsDivisibleBy60(times):
        count = {}
        for time in times:
            count[time%60] = count.get(time%60, 0) + 1
        
        total = 0
        if 30 in count:
            total += count[30] * (count[30] - 1) / 2
            del count[30]
        if 0 in count:
            total += count[0] * (count[0] - 1) / 2
            del count[0]
        
        for i in range(1, 30):
            if i in count and (60 - i) in count:
                total += count[i] * count[60 - i]
        
        return int(total)



def main():
    print(Solution().numPairsDivisibleBy60([30,20,150,100,40]))
    print(numPairsDivisibleBy60([30,20,150,100,40]))


main()