class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        sorted_nums = sorted(nums, reverse = True)
        return sorted_nums[k - 1]


# 2
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = nums[:k]
        heapify(heap)

        for num in nums[k:]:
            if num > heap[0]:
                heappop(heap)
                heappush(heap, num)

        return heap[0]
