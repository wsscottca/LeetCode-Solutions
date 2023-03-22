class Solution:
    def maxArea(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1
        maxContainer = 0
        while left < right:
            container = (right-left) * min(height[right], height[left])
            if (container > maxContainer):
                maxContainer = container
                
            if (height[right] > height[left]):
                left += 1
            else:
                right -= 1
                
        return maxContainer