import heapq

class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start: int, end: int) -> float:
        cumm_prob = [-sys.maxsize for _ in range(n)]
        cumm_prob[start] = 1        

        adj_list = {}
        for conn, prob in zip(edges, succProb):
            if conn[0] in adj_list:
                adj_list[conn[0]].append((conn[1], prob))
            else:
                adj_list[conn[0]] = [(conn[1], prob)]

            if conn[1] in adj_list:
                adj_list[conn[1]].append((conn[0], prob))
            else:
                adj_list[conn[1]] = [(conn[0], prob)]
        
        pq = [(-1, start)]
        while pq:
            curr_prob, curr = heapq.heappop(pq)    
            curr_prob *= -1            
      
            if curr == end:
                return curr_prob

            if curr not in adj_list:
                continue

            for neighbor, prob in adj_list[curr]:
                new_prob = curr_prob * prob
                if new_prob > cumm_prob[neighbor]:
                    cumm_prob[neighbor] = new_prob
                    heapq.heappush(pq, (-new_prob, neighbor))
        
        return 0.0
        