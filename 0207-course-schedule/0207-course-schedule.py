class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        indegrees = [0 for _ in range(numCourses)]
        outdegrees = {}
        
        for i in range(numCourses):
            outdegrees[i] = []
        
        for prereq in prerequisites:
            indegrees[prereq[0]] += 1
            outdegrees[prereq[1]].append(prereq[0])
        
        to_visit = []
        for i in range(numCourses):
            if indegrees[i] == 0:
                to_visit.append(i)
        
        topological = []
        while(to_visit):
            node = to_visit.pop()
            topological.append(node)
            for neighbor in outdegrees[node]:
                    indegrees[neighbor] -= 1
                    if indegrees[neighbor] == 0:
                        to_visit.append(neighbor)
        
        return len(topological) == numCourses