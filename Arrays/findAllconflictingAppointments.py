def find_all_conflicting_appointments(intervals):
  # result array
  result = []

  # Sort the intervals
  intervals.sort(key=lambda x: x[0])
  start, end = 0, 1

  for i in range(1, len(intervals)):
    # Check whether two of the intervals overlap
    if intervals[i][start] < intervals[i - 1][end]:
      result.append([intervals[i], intervals[i - 1]])
  return result


def main():
  print("Can attend all appointments: " + str(find_all_conflicting_appointments([[1, 4], [2, 5], [7, 9]])))
  print("Can attend all appointments: " + str(find_all_conflicting_appointments([[6, 7], [2, 4], [8, 12]])))
  print("Can attend all appointments: " + str(find_all_conflicting_appointments([[4, 5], [2, 3], [3, 6]])))


main()
