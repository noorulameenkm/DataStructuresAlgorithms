def firstMissingPositive(A):
        ptr = 0
        n = len(A)

        # Check if 1 is present in array or not
        for i in range(n):
            if A[i] == 1:
                ptr = 1
                break
        
        # If 1 is not present
        if ptr == 0:
            return 1
        
        # Changing values to 1
        for i in range(n):
            if A[i] <= 0 or A[i] > n:
                A[i] = 1
        

        # Updating indices according to values
        for i in range(n):
            A[(A[i] - 1) % n] += n
        
        # Finding which index has value less than n
        for i in range(n):
            if A[i] <= n:
                return i + 1
        
        # If array has values from 1 to n
        return n + 1



def main():
    print(firstMissingPositive([1,2,0]))
    print(firstMissingPositive([3,4,-1,1]))
    print(firstMissingPositive([-8,-7,-6]))


main()