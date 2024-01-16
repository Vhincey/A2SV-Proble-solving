class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        x_string = str(x)

        if x_string == x_string[::-1]:
            return True
        else:
            return False

myObject = Solution()

print(myObject.isPalindrome(124))



# Method 2
str_x = str(x)
    
return str_x == str_x[::-1]
   


        
        
