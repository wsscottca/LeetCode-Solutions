'''
Timestamps:
    Understand and Cases: 1:35
    Design and Verify: 20:00
    Code:

Understand and Cases:
    matrix = [1]
    matrix = [[1,2][3,4][5,6]]
    
Design and Verify:
    top, bottom, left, right
    
    
    top = 2
    bottom = 2
    left = 1
    right = 3
    
    res = [1,2,3,4,8,12,11,10,9,5]
    
    # bound to track current area of spiral
    top, left = 0
    bottom = len(matrix)
    right = len(matrix[0])
    
    # result arr
    res = []
    
    # while our bounds have not flipped
    # we can continue spiraling
    while top < bottom or left < right:
        # get the top row of the current spiral
        for i in range(left, right):
            res.append[top][i]
            top += 1
            if top >= bottom:
                break
        
        # get the right column of the current spiral
        for i in range(top, bottom):
            res.append[i][right - 1]
            right -= 1
            if left >= right:
                break
        
        # get the bottom row of the current spiral
        # in reverse order so it follows spiral structure
        for i in range(right - 1, left - 1, -1):
            res.append[bottom - 1][i]
            bottom -= 1
            if top >= bottom:
                break
        
        # get the left column of the current spiral
        # in reverse order so it follows spiral structure
        for i in range(bottom - 1, top - 1, -1):
            res.append[i][left]
            left += 1
            if left >= right:
                break
    
    return res
        
        
'''


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        # bound to track current area of spiral
        top = 0
        bottom = len(matrix)
        left = 0
        right = len(matrix[0])

        # result arr
        res = []

        # while our bounds have not flipped
        # we can continue spiraling
        while top < bottom or left < right:
            # get the top row of the current spiral
            for i in range(left, right):
                res.append(matrix[top][i])
            top += 1
            if top >= bottom:
                break

            # get the right column of the current spiral
            for i in range(top, bottom):
                res.append(matrix[i][right - 1])
            right -= 1
            if left >= right:
                break

            # get the bottom row of the current spiral
            # in reverse order so it follows spiral structure
            for i in range(right - 1, left - 1, -1):
                res.append(matrix[bottom - 1][i])
            bottom -= 1
            if top >= bottom:
                break

            # get the left column of the current spiral
            # in reverse order so it follows spiral structure
            for i in range(bottom - 1, top - 1, -1):
                res.append(matrix[i][left])
            left += 1
            if left >= right:
                break

        return res