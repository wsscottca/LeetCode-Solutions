class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        
        for asteroid in asteroids:
            if asteroid > 0:
                stack.append(asteroid)
            
            else:
                if not stack or stack[-1] < 0:
                    stack.append(asteroid)
                    continue
                    
                while stack:
                    if stack[-1] < 0:
                        stack.append(asteroid)
                        break
                    
                    if abs(asteroid) == stack[-1]:
                        stack.pop()
                        break
                    
                    elif abs(asteroid) > stack[-1]:
                        stack.pop()
                        
                        if not stack:
                            stack.append(asteroid)
                            break
                        
                    else:
                        break
                        
        return stack