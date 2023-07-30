class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        indegrees = [0 for _ in range(numCourses)]
        
        for prereq in prerequisites:
            indegrees[prereq[0]] += 1
        
        to_visit = []
        for i in range(numCourses):
            if indegrees[i] == 0:
                to_visit.append(i)
        
        topological = []
        while(to_visit):
            node = to_visit.pop()
            topological.append(node)
            for prereq in prerequisites:
                if prereq[1] == node:
                    indegrees[prereq[0]] -= 1
                    if indegrees[prereq[0]] == 0:
                        to_visit.append(prereq[0])
        
        print(topological)
        return len(topological) == numCourses