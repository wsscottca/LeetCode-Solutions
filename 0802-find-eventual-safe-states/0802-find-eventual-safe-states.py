class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        indegree = [[] for _ in range(len(graph))]
        outdegree = [0] * len(graph)
        for i in range(len(graph)):
            outdegree[i] = len(graph[i])
            for j in range(len(graph[i])):
                indegree[graph[i][j]].append(i)

        queue = []
        for i in range(len(outdegree)):
            if outdegree[i] == 0:
                queue.append(i)

        res = []
        while queue:
            node = queue.pop(0)
            res.append(node)
            if indegree[node]:
                for rest in indegree[node]:
                    outdegree[rest] -= 1
                    if outdegree[rest] == 0:
                        queue.append(rest)

        return sorted(res)