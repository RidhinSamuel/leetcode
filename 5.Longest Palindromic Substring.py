"""
5. Longest Palindromic Substring

Given a string s, return the longest palindromic substring in s.
Example 1:
Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.
Example 2:
Input: s = "cbbd"
Output: "bb"
"""

class Solution:
    def longestPalindrome(self, s: str) -> str:
        result=""
        resultLength=0
        for i in range(len(s)):
            #Odd case
            l=r=i
            while l>=0 and r <len(s) and s[l]==s[r] :
                if (r-l+1)>resultLength:
                    result=s[l:r+1]
                    resultLength=r-l+1
                l-=1
                r+=1
            #Even Case
            l,r=i,i+1
            while l>=0 and r <len(s) and s[l]==s[r] :
                if (r-l+1)>resultLength:
                    result=s[l:r+1]
                    resultLength=r-l+1
                l-=1
                r+=1
        return result
        
    
s=input()
ob=Solution()
print(ob.longestPalindrome(s))
        
