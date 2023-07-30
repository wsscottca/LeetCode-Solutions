class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_area = 0
        left = 0
        right = len(height) - 1
        
        while left < right:
            area = min(height[left], height[right]) * (right - left)
            max_area = max(max_area, area)
            
            if height[left] > height[right]:
                min_height = height[right]
                
                while height[right] <= min_height:
                    if left >= right:
                        break
                        
                    right -= 1
            
            else:
                min_height = height[left]
                
                while height[left] <= min_height:
                    if left >= right:
                        break
                        
                    left += 1
        
        return max_area