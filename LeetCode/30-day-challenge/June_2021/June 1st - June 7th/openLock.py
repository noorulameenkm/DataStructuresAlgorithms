from collections import deque
from functools import update_wrapper
from io import open_code

def openLock(dead_ends, target):
    queue = deque([])

    current_string = "0000"
    dead_ends = set(dead_ends)
    if current_string in dead_ends:
        return -1
    
    if current_string == target:
        return 0
    
    queue.append(current_string)

    moves = 0 

    while queue:
        length = len(queue)

        for _ in range(length):

            current_string = queue.popleft()
            if current_string in dead_ends:
                continue
                
            if current_string == target:
                return moves

            dead_ends.add(current_string)
            
            for i in range(4):

                lower_digit = (int(current_string[i]) + 9) % 10
                upper_digit = (int(current_string[i]) + 1) % 10

                for digit in (upper_digit, lower_digit):
                    new_string = ''.join([str(digit) if j == i else current_string[j] for j in range(4)])

                    queue.append(new_string)
            
        
        moves += 1
    
    return -1



print(openLock(dead_ends = ["0201","0101","0102","1212","2002"], target = "0202"))
print(openLock(dead_ends = ["8888"], target = "0009"))
print(openLock(dead_ends = ["8887","8889","8878","8898","8788","8988","7888","9888"], target = "8888"))
print(openLock(dead_ends = ["0000"], target = "8888"))



def openLock2(dead_ends, target):
    current_string = "0000"

    if current_string in dead_ends:
        return -1

    if current_string == target:
        return 0

    
    p = deque([])
    q = deque([])
    moves = 1

    p_dead_ends = set(dead_ends + ["0000"])
    q_dead_ends = set(dead_ends + [target])
    p_visited = set(["0000"])
    q_visited = set([target])

    def rotate(current):
        rotates = []
        for i in range(4):
            digits_up = (int(current[i]) + 1) % 10
            digits_down = (int(current[i]) + 9) % 10

            for digit in (digits_down, digits_up):
                rotates.append(''.join([str(digit) if j == i else current[j] for j in range(4)]))
        
        return rotates

    p.extend(rotate(current_string))
    q.extend(rotate(target))
    
    while p and q:

        p_len = len(p)
        q_len = len(q)

        for _ in range(p_len):
            current_1 = p.popleft()

            if current_1 in p_dead_ends:
                continue

            if current_1 in q_visited:
                return moves
            
            p_visited.add(current_1)
            p_dead_ends.add(current_1)
            rotates = rotate(current_1)
            p.extend(rotates)
        
        moves += 1

        for _ in range(q_len):
            current_2 = q.popleft()

            if current_2 in q_dead_ends:
                continue

            if current_2 in p_visited:
                return moves
            
            q_visited.add(current_2)
            q_dead_ends.add(current_2)

            rotates = rotate(current_2)
            q.extend(rotates)
        
        moves += 1
    
    return -1
                

print(openLock2(dead_ends = ["0201","0101","0102","1212","2002"], target = "0202"))
print(openLock2(dead_ends = ["8888"], target = "0009"))
print(openLock2(dead_ends = ["8887","8889","8878","8898","8788","8988","7888","9888"], target = "8888"))
print(openLock2(dead_ends = ["0000"], target = "8888"))
            