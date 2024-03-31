"""136. Single Number
https://leetcode.com/problems/single-number/description/
Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.

You must implement a solution with a linear runtime complexity and use only constant extra space."""
from collections import defaultdict
from typing import List
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        d=defaultdict(int)
        for i  in nums:
            d[i]+=1
        for i in d:
            if d[i]==1:
                return i
    def singleNumberOptimal(self, nums: List[int]) -> int:
        xor=0
        for i in nums:
            xor^=i
        return xor
if __name__=="__main__":
    nums = [2,2,1]
    obg=Solution()
    print(obg.singleNumber(nums))