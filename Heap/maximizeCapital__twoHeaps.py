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



"""
While selecting projects we have two constraints:

1. We can select a project only when we have the required capital.
2. There is a maximum limit on how many projects we can select.
Since we don’t have any constraint on time, we should choose a project, among the projects for which we have enough capital, which gives us a maximum profit. Following this greedy approach will give us the best solution.

While selecting a project, we will do two things:

1. Find all the projects that we can choose with the available capital.
2. From the list of projects in the 1st step, choose the project that gives us a maximum profit.
We can follow the Two Heaps approach similar to Find the Median of a Number Stream. Here are the steps of our algorithm:

Add all project capitals to a min-heap, so that we can select a project with the smallest capital requirement.
Go through the top projects of the min-heap and filter the projects that can be completed within our available capital. Insert the profits of all these projects into a max-heap, so that we can choose a project with the maximum profit.
Finally, select the top project of the max-heap for investment.
Repeat the 2nd and 3rd steps for the required number of projects.

"""

