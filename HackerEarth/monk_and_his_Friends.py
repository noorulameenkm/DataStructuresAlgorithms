def findExistOrNot(num_set, num):
    if num in num_set:
        print("YES")
    else:
        print("NO")
        num_set.add(num)

    return num_set


test_cases = int(input())
for t in range(test_cases):
    line = input()
    n = int(line.split(" ")[0])
    m = int(line.split(" ")[1])
    tot = n + m
    input_line = input()
    input_array = [int(k) for k in input_line.split(" ")]
    num_set = set()

    # Adding N students to the set
    for i in range(n):
        num_set.add(input_array[i])

    # Checking whether each one is there or not
    for k in range(n, tot):
        num_set = findExistOrNot(num_set,input_array[k])
        
