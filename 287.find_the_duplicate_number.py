"""
287. Find the Duplicate Number

Given an array of integers nums containing n + 1 integers where each integer is in the range [1, n] inclusive.

There is only one repeated number in nums, return this repeated number.

You must solve the problem without modifying the array nums and uses only constant extra space.
"""
class Solution:
    def findDuplicate(self,nums):
        d={}
        for i in nums:
            d[i]=d.get(i,0)+1
            if d.get(i,0)>1:
                return i
if __name__=="__main__":
    a=Solution()
    limit=int(input("Enter the limit "))
    l=[int(input()) for _ in range(limit)]
    print("Answer is ",a.findDuplicate(l))
