class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k = k % n 
        
        nums[:] = nums[n - k:] + nums[:n - k]


# Method 2
n = len(nums)
        rotated = [0] * n  
        
        for i in range(n):
            rotated[(i + k) % n] = nums[i]  
        
        nums[:] = rotated
