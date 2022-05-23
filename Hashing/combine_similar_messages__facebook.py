from collections import defaultdict


"""
    Time Complexity - O(n * l)
    Space Complexity - O(n)
"""
def combine_messages(messages):

    def generate_key(message):
        key = ''
        for i in range(1, len(message)):
            diff = ord(message[i]) - ord(message[i - 1])
            if diff < 0:
                diff += 26

            key += str(diff) + ','

        return key.strip(',')

    messages_groups = defaultdict(list)
    for message in messages:
        key_ = generate_key(message)
        messages_groups[key_].append(message)

    return messages_groups


# Driver code
messages = ["lmn", "mno", "azb", "bac", "yza", "bdfg"]
groups = combine_messages(messages)
print("The Grouped Messages are:\n")
for group in groups:
    print(groups[group])
