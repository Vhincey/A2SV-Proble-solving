class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:

       # Brute Force
      # n = len(nums)
      # for i in range(n - 1):
      #     for j in range(i + 1, n):
      #         if nums[i] == nums[j]:
      #             return True
      # return False

      # Time complexity of n(logn)
      # n = len(nums)
      # nums.sort()

      # for i in range(n - 1):
      #   if nums[i] == nums[i + 1]:
      #     return True
      # return False

      # Time complexity of O(n) with space of O(n)
      # num_counts = {}  

      # for num in nums:
      #   if num in num_counts:
      #       return True 
      #   else:
      #       num_counts[num] = 1

      # return False 

      #  Using Hashsets
      hashset = set()

      for num in nums:
        if num in hashset:
          return True
        hashset.add(num)
      return False

     
