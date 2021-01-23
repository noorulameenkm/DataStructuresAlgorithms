def hash_modular(key, length):
    return key % length




def main():
    # index = key % size

    lst = [None] * 10  # List of size 10
    key = 35
    index = hash_modular(key, len(lst))  # Fit the key into the list size
    print("The index for key " + str(key) + " is " + str(index))


main()