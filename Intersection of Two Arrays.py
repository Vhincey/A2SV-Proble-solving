class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        output = set()

        for num in nums1:
            if num in nums2:
                output.add(num)

        return output


# Method 2
        set1 = set(nums1)
        set2 = set(nums2)
        
        common_elements = set1.intersection(set2)
        
        return common_elements
