from collections import defaultdict


"""
Time complexity:
We use an adjacency list representation to build the graph in the algorithm. The complexity of doing a DFS on an adjacency list data structure is O(|V| + |E|)
. Here, let n be the total number of accounts and m be the total number of all email addresses (not unique), then |V| = n
and |E| = m. Therefore, the complexity of finding the connected components will be O(m + n).

Space complexity:
The space complexity will be O(m + n) because even if there are no email addresses, we still need O(n) space and in total. We are storing the n
names and O(m) email addresses.
"""
def accountsMerge(accounts):
    email_to_name = {}
    graph = defaultdict(set)

    for account in accounts:
        name = account[0]
        for email in account[1:]:
            graph[account[1]].add(email)
            graph[email].add(account[1])
            email_to_name[email] = name
        
    
    visited = set()
    ans = []
    
    for email in graph:
        if email not in visited:
            visited.add(email)
            stack = [email]
            component = []
            while stack:
                node = stack.pop()
                component.append(node)
                for neighbour in graph[node]:
                    if neighbour not in visited:
                        visited.add(neighbour)
                        stack.append(neighbour)
            
            ans.append([email_to_name[email]] + sorted(component))
    
    return ans



# Driver code
accounts = [["Sarah", "sarah22@email.com", "sarah@gmail.com", "sarahhoward@email.com"],
            ["Alice", "alicexoxo@email.com", "alicia@email.com", "alicelee@gmail.com"],
            ["Sarah", "sarah@gmail.com", "sarah10101@gmail.com"],
            ["Sarah", "sarah10101@gmail.com", "misshoward@gmail.com"]]
print(accountsMerge(accounts))