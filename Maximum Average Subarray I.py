class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        n = len(nums) + 1
        res = 0
        sub_a = n * [0]

        for i in range(1, n):
            sub_a[i] = sub_a[i - 1] + nums[i - 1]
    
        res = sub_a[k] / k 

        for i in range(k, n ):
            res = max(res, (sub_a[i] - sub_a[i - k]) / k)

        return res

   
     
      
