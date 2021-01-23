def hash_fold(key, chunk_size):
    str_key = str(key)

    hash_val = 0
    for i in range(0, len(str_key), chunk_size):
        if((i + chunk_size) < len(str_key)):
            hash_val += int(str_key[i: i + chunk_size])
        else:
            hash_val += int(str_key[i:])
    
    return hash_val


def main():
    key = 3456789
    chunk_size = 2
    print("Hash Key: " + str(hash_fold(key, chunk_size)))

main()