class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #  Brute Force
        n = len(nums)
        for i in range(n - 1):
            for j in range(i + 1, n):
                if nums[i] + nums[j] == target:
                    return i , j
                else:
                    continue

# Method 2
        my_map = {}
        for idx, num in enumerate(nums):
            diff = target - num
            if diff in my_map:
                return [my_map[diff], idx]
            my_map[num] = idx

# Method 3
        seen = {}  
        for i, num in enumerate(nums):
            complement = target - num
            if complement in seen:
                return [seen[complement], i]
            seen[num] = i
        return [] 

            

            
