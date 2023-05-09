import heapq

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        cumm_times = [sys.maxsize for _ in range(n + 1)]
        cumm_times[k] = 0        

        adj_list = {}
        for conn in times:
            node_from = conn[0]
            node_to = conn[1]
            time = conn[2]

            if node_from in adj_list:
                adj_list[node_from].append((node_to, time))
            else:
                adj_list[node_from] = [(node_to, time)]
            
            if node_to not in adj_list:
                adj_list[node_to] = []

        pq = [(k, 0)]
        while pq:
            curr, curr_time = heapq.heappop(pq)
            
            if curr not in adj_list:
                continue
            
            for neighbor, time in adj_list[curr]:
                new_time = curr_time + time
                if new_time < cumm_times[neighbor]:
                    cumm_times[neighbor] = new_time
                    heapq.heappush(pq, (neighbor, new_time))
        
        max_time = max(cumm_times[1:])
        if max_time != sys.maxsize:
            return max_time

        return -1