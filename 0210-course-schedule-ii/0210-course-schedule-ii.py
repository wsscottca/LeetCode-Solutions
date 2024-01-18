'''
Timestamps:
    Cases: 2:03
    Design: 11:00
    Verify: 15:51
    Code:

Understand and Cases:
    [a, b]
    b BEFORE a
    
    numCourses = 2, prerequisites = []
    numCourses = 7, prerequisites = [[3,4], [4,3]]
    
Design:
    Topological sort
    
    # create our helper structures
    in_bound = [0 for _ in range(numCourse)]
    out_bound = {}
    
    # for each prerequisite, count the inbound
    # and create an adj_matrix of the courses
    # neighbors that come after it
    for course, prereq in prerequisites:
        in_bound[course] += 1
        
        if prereq in out_bound:
            out_bound[prereq].append(course)
        else:
            out_bound[prereq] == [course]
    
    # add all our courses without prerequisites to our
    # to be visited array
    to_visit = []
    for i in range(len(in_bound)):
        if in_bound[i] == 0:
            to_visit.append(i)
    
    # visit each node in our to be visited array
    ans = []
    while to_visit:
        course = to_visit.pop()
        ans.append(course)
        
        # for each course that needed our current course
        # as a prerequisite, remove 1 from it's inbound
        # and if it was the last prerequisite, add it to
        # our to be visited arr
        for neighbor in out_bound[course]:
            in_bound[neighbor] -= 1
            if in_bound[neighbor] == 0:
                to_visit.append(neighbor)
    
    # if the length of our answer array is the same as the number
    # of courses we successfully took every course so if not
    # return an empty array as we cannot take all course
    if len(ans) != numCourses:
        return []
    
    return ans
'''


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # create our helper structures
        in_bound = [0 for _ in range(numCourses)]
        out_bound = {}

        # for each prerequisite, count the inbound
        # and create an adj_matrix of the courses
        # neighbors that come after it
        for course, prereq in prerequisites:
            in_bound[course] += 1

            if prereq in out_bound:
                out_bound[prereq].append(course)
            else:
                out_bound[prereq] = [course]

        # add all our courses without prerequisites to our
        # to be visited array
        to_visit = []
        for i in range(len(in_bound)):
            if in_bound[i] == 0:
                to_visit.append(i)

        # visit each node in our to be visited array
        ans = []
        while to_visit:
            course = to_visit.pop()
            ans.append(course)

            # for each course that needed our current course
            # as a prerequisite, remove 1 from it's inbound
            # and if it was the last prerequisite, add it to
            # our to be visited arr
            if course in out_bound:
                for neighbor in out_bound[course]:
                    in_bound[neighbor] -= 1
                    if in_bound[neighbor] == 0:
                        to_visit.append(neighbor)

        # if the length of our answer array is the same as the number
        # of courses we successfully took every course so if not
        # return an empty array as we cannot take all course
        if len(ans) != numCourses:
            return []

        return ans