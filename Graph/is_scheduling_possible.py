from collections import deque

"""
Time Complexity - O(V+E) where V is the number of tasks and E is the number of prerequisites
Space Complexity - O(V + E) where V is the number of tasks and E is the number of prerequisites
"""

def is_scheduling_possible(tasks, prerequisites):
  taskOrder = []
  if tasks <= 0:
      return True

  # a. Initialize the graph
  next_tasks = { i: [] for i in range(tasks) } # next tasks list
  prerequisite_count = { i: 0 for i in range(tasks) } # number of prerequisite courses before the ith task
  
  # b. Build the graph
  for prerequisite in prerequisites:
      task_1, task_2 = prerequisite
      prerequisite_count[task_2] += 1 # increment prerequisite tasks
      next_tasks[task_1].append(task_2) # put the child into it's parent's list

  # c. Find all tasks with no prerequisite
  noPrerequisite_tasks = deque()
  for course, count in prerequisite_count.items():
      if count == 0:
            noPrerequisite_tasks.append(course)
  
  # d. For each task, add it to the taskOrder and subtract one from all of its prerequisite count
  # if a task in-degree becomes zero, add it to the no prerequisite tasks list
  while noPrerequisite_tasks:
      noPrerequisite_task = noPrerequisite_tasks.popleft()
      tasks_ = next_tasks[noPrerequisite_task]  # get the tasks next task to decrement their prerequisiteCount

      for task in tasks_:
            prerequisite_count[task] -= 1
            
            if prerequisite_count[task] == 0: 
                  noPrerequisite_tasks.append(task)

      taskOrder.append(noPrerequisite_task)
 
  # if taskOrder doesn't contain all tasks, there is a cyclic dependency between tasks, therefore, we
  # will not be able to schedule all tasks
  return len(taskOrder) == tasks


def main():
  print("Is scheduling possible: " +
        str(is_scheduling_possible(3, [[0, 1], [1, 2]])))
  print("Is scheduling possible: " +
        str(is_scheduling_possible(3, [[0, 1], [1, 2], [2, 0]])))
  print("Is scheduling possible: " +
        str(is_scheduling_possible(6, [[0, 4], [1, 4], [3, 2], [1, 3]])))

main()
