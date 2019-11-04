test_cases = int(input())
for test_case in range(test_cases):
    input_line = input()
    n = int(input_line.split(" ")[0])
    x = int(input_line.split(" ")[1])
    input_line_numbers = input()
    try:
        input_numbers_array = [int(num) for num in input_line_numbers.split(" ") if num != '']
        # distinctType(input_numbers_array, x)
        distinct_numbers_set = set(input_numbers_array)
        set_length = len(distinct_numbers_set)
        if set_length == x:
            print("Good")
        elif set_length < x:
            print("Bad")
        else:
            print("Average")
    except:
        pass