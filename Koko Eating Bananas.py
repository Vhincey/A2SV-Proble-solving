class Solution(object):
    def minEatingSpeed(self, piles, h):
        """
        :type piles: List[int]
        :type h: int
        :rtype: int
        """
       
        left, right = 1, max(piles)

        while left < right:
            mid = left + (right - left) // 2
            total_hours = sum((pile + mid - 1) // mid for pile in piles)

            if total_hours > h:
                left = mid + 1
            else:
                right = mid
        return left
