from Queue import Queue



def generateBinaryNumbers(n):
    queue = Queue()
    result = []
    queue.enqueue(1)

    for i in range(n):
        result.append(queue.dequeue())

        str1 = str(result[i]) + '0'
        str2 = str(result[i]) + '1'

        queue.enqueue(str1)
        queue.enqueue(str2)

    return result




def main():
    # first test case
    n = 3
    print(generateBinaryNumbers(n))
    n = 10
    print(generateBinaryNumbers(n))



main()