class Solution:
    def hIndex(self, citations: List[int]) -> int:
        n = len(citations)
        l, h = 0, n - 1
        h_index = 0

        while l <= h:
            mid = l + (h - l) // 2

            if citations[mid] == n-mid:
                return n - mid
            elif citations[mid] < n - mid:
                l = mid + 1
            else:
                h = mid - 1
        return n - l
