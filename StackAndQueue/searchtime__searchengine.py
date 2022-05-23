
"""
    Time complexity - O(n)
    Space Complexity - O(n)
"""
def service_time(n, logs):
    stack = []
    serve_times = [0] * n
    serv = logs[0].split(":")
    stack.append(int(serv[0]))
    time = int(serv[2])
    for i in range(0, len(logs)):
        serv = logs[i].split(":")
        if "start" in serv[1]:
            if stack:
                serve_times[stack[-1]] += int(serv[2]) - time

            stack.append(int(serv[0]))
            time = int(serv[2])
        else:
            serve_times[stack[-1]] += int(serv[2]) - time + 1
            stack.pop()
            time = int(serv[2]) + 1
        
    return serve_times


print(service_time(2, ["0:start:0","0:start:2","0:end:5","1:start:6","1:end:6","0:end:7"]))

