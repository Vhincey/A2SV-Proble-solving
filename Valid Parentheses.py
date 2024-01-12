class Solution:
    def isValid(self, s: str) -> bool:
        brack = ['(', '{' , '[']
        stack = []

        for ele in s:
            if ele in brack:
                stack.append(ele)
            else:
                if not stack:
                    return False
                top = stack.pop()
                if (ele == ')' and top != '(') or (ele == '}' and top != '{') or (ele == ']' and top != '['):
                    return False
        
        return not stack
            
