def trace_path(my_dict):  # A Map object
    # Write your code here
    result = []
    opp_dict = {}
    for key, value in my_dict.items():
        opp_dict[value] = key
    
    start = ''
    for key in my_dict:
        if key not in opp_dict:
            start = key
    
    while start in my_dict:
        result.append([start, my_dict[start]])
        start = my_dict[start]

    return result


print(trace_path({"NewYork": "Chicago", "Boston": "Texas", 'Missouri': "NewYork", "Texas": "Missouri"}))