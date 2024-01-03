class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits = int("".join(map(str, digits)))   
        # print(digits)

        digits += 1

        digits = [int(d) for d in str(digits)]

        return digits
