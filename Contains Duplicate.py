class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:

      num_counts = {}  

      for num in nums:
        if num in num_counts:
            return True 
        else:
            num_counts[num] = 1

      return False 
