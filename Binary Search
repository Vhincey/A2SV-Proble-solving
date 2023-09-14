class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        n = len(nums)
        lo, hi = 0, n - 1

        while lo <= hi:
            mid = lo + (hi - lo) // 2

            if nums[mid] < target:
                lo = mid + 1
            elif nums[mid] > target:
                hi = mid - 1
            else:
                return mid
        return -1

        
