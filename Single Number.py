class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        else:
            dict = {}
           
            for num in nums:
                if num not in dict:
                   dict[num] = 1
                else:
                    dict[num] += 1

            for num, count in dict.items():
                if count == 1:
                    return num          

# Method 2
 result = 0
        for num in nums:
            result ^= num  # XOR operation
        return result

                

                    
