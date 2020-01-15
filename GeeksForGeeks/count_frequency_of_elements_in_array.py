# https://www.geeksforgeeks.org/count-frequencies-elements-array-o1-extra-space-time/
# problem has been asked by vmware
# .items() on dictionary will return array of tuples, where each
# tuples first element will be the dictionary 'key' and second
# element will be the dictionary 'value' associated with the key

def getFrequency(array):
    count = {}
    for k in array:
        if k in list(count.keys()):
            count[k] = count[k] + 1
        else:
            count[k] = 1

    return count


if __name__ == '__main__':
    array = [int(i) for i in input().split(' ') if i != '' and i != ' ']
    count = getFrequency(array)
    for key, value in count.items():
        print('Frequency of %d is %d' % (key, value))