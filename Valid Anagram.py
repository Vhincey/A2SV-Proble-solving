class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sdict = {}
        tdict = {}
        if len(s) != len(t):
            return False
        
        for letter in s:
            if letter in sdict:
                sdict[letter] += 1
            else:
                sdict[letter] = 1
        for letter in t:
            if letter in tdict:
                tdict[letter] += 1
            else:
                tdict[letter] = 1

        for key in sdict:
            if sdict[key] != tdict.get(key, 0):
                return False
        return True
        
 # time complexity of O(nlogn) and space of O(1)
 # Method 1
        if len(s) != len(t):
            return False
        
        s_sorted = sorted(s)
        t_sorted = sorted(t)
        n = len(s)
        l, r = 0, 0
        
        while l < n:
            if s_sorted[l] != t_sorted[r]:
                return False
            l += 1
            r += 1
        return True
        return s_sorted == t_sorted

    # Method 2
        return sorted(s) == sorted(t)
