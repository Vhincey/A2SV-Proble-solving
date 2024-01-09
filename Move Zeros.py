class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        j = 0
        for i in range(n):
            if nums[i] != 0:
                nums[j] = nums[i]
                j += 1
        for i in range(j, n):
            nums[i] = 0
        return nums

# Method 2
        n = len(nums)
        l, r = 0, n - 1

        while l <= r:
            if nums[l] == 0:
                nums.pop(l)
                nums.append(0)
                r -= 1
            else:
                l += 1
