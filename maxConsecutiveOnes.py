from typing import List
"""485. Max Consecutive Ones
https://leetcode.com/problems/max-consecutive-ones/description/
Given a binary array nums, return the maximum number of consecutive 1's in the array."""
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        maxCount=0
        count=0
        for n in nums:
            if n!=1:
                if count>maxCount:
                    maxCount=count
                count=0
            else:
                count+=1
        return max(maxCount,count)
if __name__=="__main__":
    obj=Solution()
    limit=int(input())
    l=[int(input()) for _ in range(limit)]
    print(obj.findMaxConsecutiveOnes(l))