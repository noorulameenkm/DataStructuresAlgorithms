from collections import deque

"""
Time Complexity - O(V+E) where V is the number of tasks and E is the number of prerequisites
Space Complexity - O(V + E) where V is the number of tasks and E is the number of prerequisites
"""

def find_order(tasks, prerequisites):
  sortedOrder = []
  if tasks <= 0:
    return sortedOrder

  # a. Initialize the graph
  in_degrees = { i: 0 for i in range(tasks) } # next tasks list
  childrens = { i: [] for i in range(tasks) } # number of prerequisite tasks before the ith task

  # b. Build the graph
  for prerequisite in prerequisites:
    task_1, task_2 = prerequisite
    in_degrees[task_2] += 1 # increment prerequisite tasks
    childrens[task_1].append(task_2) # put the child into it's parent's list

  # c. Find all tasks with no prerequisite
  noPrerequisite_tasks = deque()
  for task, degrees in in_degrees.items():
    if degrees == 0:
      noPrerequisite_tasks.append(task)

  # d. For each task, add it to the taskOrder and subtract one from all of its prerequisite count
  # if a task in-degree becomes zero, add it to the no prerequisite tasks list
  while noPrerequisite_tasks:
    noPrerequisite_task = noPrerequisite_tasks.popleft()

    childrens_ = childrens[noPrerequisite_task] # get the tasks next task to decrement their prerequisiteCount

    for children in childrens_:
      in_degrees[children] -= 1
      if in_degrees[children] == 0:
        noPrerequisite_tasks.append(children)

    sortedOrder.append(noPrerequisite_task)

  # if taskOrder doesn't contain all tasks, there is a cyclic dependency between tasks, therefore, we
  # will not be able to schedule all tasks
  if len(sortedOrder) != tasks:
    return []

  return sortedOrder


def main():
  print("Is scheduling possible: " + str(find_order(3, [[0, 1], [1, 2]])))
  print("Is scheduling possible: " +
        str(find_order(3, [[0, 1], [1, 2], [2, 0]])))
  print("Is scheduling possible: " +
        str(find_order(6, [[2, 5], [0, 5], [0, 4], [1, 4], [3, 2], [1, 3]])))


main()
