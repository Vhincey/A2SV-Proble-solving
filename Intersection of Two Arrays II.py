class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        output = []
        count_nums1 = Counter(nums1)
        count_nums2 = Counter(nums2)

        for num, count in count_nums1.items():
            if num in count_nums2:
                output.extend([num] * min(count, count_nums2[num]))

        return output


# Method 2
        count_nums1 = Counter(nums1)
        output = []
        
        for num in nums2:
            if num in count_nums1 and count_nums1[num] > 0:
                output.append(num)
                count_nums1[num] -= 1
        
        return output
