class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
      n = len(nums)
      lo = 0
      hi = n - 1
      nums.append(float("-inf"))

      while lo <= hi:
        mid = lo + (hi - lo) // 2
        
        if nums[mid] < nums[mid + 1]:
          lo = mid + 1
        elif nums[mid] > nums[mid - 1] and nums[mid] > nums[mid + 1]:
          return mid
        else:
          hi = mid - 1
      return lo
        
        
