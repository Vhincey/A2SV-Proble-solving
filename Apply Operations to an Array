class Solution(object):
    def applyOperations(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        
        n = len(nums)
        zeros = 0
        
        for i in range(n - 1):
            if nums[i] == nums[i + 1]:
                nums[i] *= 2
                nums[i + 1] = 0
            elif nums[i] == 0:
                zeros += 1
        
        i = 0
        for j in range(n):
            if nums[j] != 0:
                nums[i] = nums[j]
                i += 1
        
        for j in range(i, n):
            nums[j] = 0
        
        return nums
