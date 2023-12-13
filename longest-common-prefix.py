class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ""

        prefix = strs[0]  # Initialize the prefix with the first string

        for string in strs[1:]:
            # Keep removing characters from the prefix until it becomes a prefix of the current string
            while string.find(prefix) != 0:
                prefix = prefix[:-1]

            if not prefix:  # If prefix becomes empty, there is no common prefix
                return ""

        return prefix
