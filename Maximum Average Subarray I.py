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

        # Form 2
class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        n = len(nums)
        max_avg = float('-inf')
        window_sum = sum(nums[:k])

        max_avg = window_sum / k

        for i in range(k, n):
            window_sum += nums[i] - nums[i-k]
            avg = window_sum / k
            max_avg = max(max_avg, avg)
        return max_avg
   
     
      

   
     
      
