class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """

        longest = 0
        visited = set()
        left = 0 

        for right in range(len(s)):
            while s[right] in visited:
                visited.remove(s[left])
                left += 1
            visited.add(s[right])
            longest = max(longest, right - left + 1)

        return longest


# Method 2
        char_index_map = {}
        start = 0
        max_length = 0

        for end in range(len(s)):
            if s[end] in char_index_map and char_index_map[s[end]] >= start:
                start = char_index_map[s[end]] + 1

            char_index_map[s[end]] = end
            max_length = max(max_length, end - start + 1)

        return max_length
