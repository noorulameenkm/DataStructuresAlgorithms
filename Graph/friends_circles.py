"""
    This is similar to finding the number of connected components in a graph
    Time Complexity - O(n^2)
    Space Complexity - O(n)
"""


def DFS(friends, visited, n, index):
    for j in range(n):
        # A user is in the friend circle if they are friends with the user represented by
        # user index and if they are not already in a friend circle
        if friends[index][j] == 1 and not visited[j]:
            if j != index:
                visited[j] = True
                DFS(friends, visited, n, j)


def friend_circles(friends, n):
    if n == 0:
        return 0

    visited = [False] * n
    number_of_friend_circles = 0

    # Start with the first user and recursively find all other users in their
    # friend circle. Then, do the same thing for the next user that is not already
    # in a friend circle. Repeat until all users are in a friend circle.
    for i in range(n):
        if not visited[i]:
            visited[i] = True
            DFS(friends, visited, n, i)
            number_of_friend_circles += 1

    return number_of_friend_circles


friends = [
    [1, 1, 0, 0],
    [1, 1, 1, 0],
    [0, 1, 1, 0],
    [0, 0, 0, 1]
]

print(friend_circles(friends, 4))
