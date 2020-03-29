
def calculate_depth(array):

    length = len(array)
    max_depth = 0

    for i in range(length):
        current_depth = 0
        j = i
        while array[j] != -1:
            current_depth += 1
            j = array[j]
        
        if current_depth > max_depth:
            max_depth = current_depth
        

    return max_depth

if __name__ == '__main__':
    array = [-1, 0, 1, 6, 6, 0, 0, 2, 7]
    print(calculate_depth(array))
