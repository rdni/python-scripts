class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        str_x = str(x)
        for i, v in enumerate(str_x):
            if v == str_x[len(str_x)-i-1]:
                pass
            else:
                return False
            
        return True
    
solution = Solution()
print(solution.isPalindrome(121))
print(solution.isPalindrome(1221))
print(solution.isPalindrome(1221))
print(solution.isPalindrome(12221))