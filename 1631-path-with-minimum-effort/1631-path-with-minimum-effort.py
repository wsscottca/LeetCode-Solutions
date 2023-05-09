class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        rows, cols = len(heights), len(heights[0])

        abs_diffs = [[sys.maxsize] * cols for _ in range(rows)]
        abs_diffs[0][0] = 0
        pq = [(0, 0, 0)]
        while pq:
            effort, row, col = heapq.heappop(pq)

            if row == rows - 1 and col == cols - 1:
                return effort

            for dr, dc in [(1,0), (-1,0), (0,1), (0,-1)]:
                n_row, n_col = row + dr, col + dc

                if 0 <= n_row < rows and 0 <= n_col < cols:
                    diff = abs(heights[n_row][n_col] - heights[row][col])
                    new_abs_diff = max(abs_diffs[row][col], diff)

                    if new_abs_diff < abs_diffs[n_row][n_col]:
                        abs_diffs[n_row][n_col] = new_abs_diff
                        heapq.heappush(pq, (new_abs_diff, n_row, n_col))
        
        return -1