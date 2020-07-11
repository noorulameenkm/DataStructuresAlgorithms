def find_averages_of_subarrays(arr, k):
    answer = []

    _sum = 0.0
    start = 0
    for end in range(len(arr)):
        _sum += arr[end]

        if end >= k - 1:
            average = _sum / 5
            answer.append(average)
            _sum -= arr[start]
            start += 1
    return answer
        




def main():
  result = find_averages_of_subarrays([1, 3, 2, 6, -1, 4, 1, 8, 2], 5)
  print("Averages of subarrays of size K: " + str(result))


main()