class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if not needle:
            return 0
        
        for idx in range(len(haystack) - len(needle) + 1):
            if haystack[idx:idx + len(needle)] == needle:
                return idx
            
        return -1
