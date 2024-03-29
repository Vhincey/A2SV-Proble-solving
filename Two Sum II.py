class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        index1 = 0
        index2 = len(numbers) - 1

        while index1 < index2:
            current_sum = numbers[index1] + numbers[index2]

            if current_sum == target:
                return [index1 + 1, index2 + 1]  

            if current_sum < target:
                index1 += 1
            else:
                index2 -= 1
