from heapq import *


"""
Time complexity - O(NlogN + KlogN)
Space Complexity - O(N)
"""

def find_maximum_capital(capital, profits, numberOfProjects, initialCapital):
  minCapitals = []
  maxProfits = []

  # insert all project capitals to a min-heap
  for i in range(len(capital)):
    heappush(minCapitals, (capital[i], i))

  # let's try to find a total of 'numberOfProjects' best projects
  availableCapital = initialCapital
  for _ in range(numberOfProjects):
    # find all projects that can be selected within the available capital and insert them in a max-heap
    while minCapitals and minCapitals[0][0] <= availableCapital:
      capital, index = heappop(minCapitals)
      heappush(maxProfits, (-profits[index], index))

    # terminate if we are not able to find any project that can be completed within the available capital
    if not maxProfits:
      break

    # select the project with the maximum profit
    availableCapital += -heappop(maxProfits)[0]

  return availableCapital


def main():

  print("Maximum capital: " +
        str(find_maximum_capital([0, 1, 2], [1, 2, 3], 2, 1)))
  print("Maximum capital: " +
        str(find_maximum_capital([0, 1, 2, 3], [1, 2, 3, 5], 3, 0)))


main()
