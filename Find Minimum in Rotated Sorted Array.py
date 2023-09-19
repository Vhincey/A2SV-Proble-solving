class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        lo, hi = 0, n - 1

        while lo <= hi:
            mid = lo + (hi - lo) // 2

            if nums[mid] > nums[hi]:
                lo = mid + 1
            elif nums[mid] < nums[mid - 1]:
                return nums[mid]
            else:
                hi = mid - 1

        return nums[lo]
