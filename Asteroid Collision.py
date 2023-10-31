class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        
        for asteroid in asteroids:
            while stack and asteroid < 0 and stack[-1] > 0:
                if abs(stack[-1]) > abs(asteroid):
                    asteroid = 0  
                elif abs(stack[-1]) == abs(asteroid):
                    stack.pop()  
                    asteroid = 0
                else:
                    stack.pop()  
                
            if asteroid != 0:
                stack.append(asteroid)

        return stack

        # form 2
        stack = []
        
        for asteroid in asteroids:
            while stack and asteroid < 0 and stack[-1] > 0:
                if stack[-1] < abs(asteroid):
                    stack.pop()
                    continue
                elif stack[-1] == abs(asteroid):
                    stack.pop()
                break
            else:
                stack.append(asteroid)

        return stack


