def hash_truc(key):
    return key % 1000



def main():
    key = 123456
    index = hash_truc(key)
    print("The index for key " + str(key) + " is " + str(index))

main()