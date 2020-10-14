from collections import deque

"""
Time Complexity - O(V+E) where V is the number of courses and E is the number of prerequisites
Space Complexity - O(V + E) where V is the number of courses and E is the number of prerequisites
"""

def is_possible_to_take_all_courses(courses, prerequisites):
    courseOrder = []
    if courses <= 0:
        return True

    # a. Initialize the graph
    next_courses = { i: [] for i in range(courses) } # next courses list
    prerequisite_count = { i: 0 for i in range(courses) } # number of prerequisite courses before the ith course
  
    # b. Build the graph
    for prerequisite in prerequisites:
      course_1, course_2 = prerequisite
      prerequisite_count[course_2] += 1 # increment prerequisite course
      next_courses[course_1].append(course_2) # put the child into it's parent's list

    # c. Find all courses with no prerequisite
    noPrerequisite_courses = deque()
    for course, count in prerequisite_count.items():
        if count == 0:
            noPrerequisite_courses.append(course)
  
    # d. For each course, add it to the taskOrder and subtract one from all of its prerequisite count
    # if a courses in-degree becomes zero, add it to the no prerequisite courses list
    while noPrerequisite_courses:
        noPrerequisite_course = noPrerequisite_courses.popleft()
        courses_ = next_courses[noPrerequisite_course]  # get the courses next courses to decrement their prerequisiteCount

        for course in courses_:
            prerequisite_count[course] -= 1
            
            if prerequisite_count[course] == 0: 
                noPrerequisite_courses.append(course)

        courseOrder.append(noPrerequisite_course)
 
    # if taskOrder doesn't contain all tasks, there is a cyclic dependency between tasks, therefore, we
    # will not be able to schedule all tasks
    return len(courseOrder) == courses


def main():
  print("Is scheduling possible: " +
        str(is_possible_to_take_all_courses(3, [[0, 1], [1, 2]])))
  print("Is scheduling possible: " +
        str(is_possible_to_take_all_courses(3, [[0, 1], [1, 2], [2, 0]])))
  print("Is scheduling possible: " +
        str(is_possible_to_take_all_courses(6, [[0, 4], [1, 4], [3, 2], [1, 3]])))

main()
