'''
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.
Input: nums = [3,2,4], target = 6
Output: [1,2]
'''
class Solution:
    def twoSum(self , nums, target):
        
        
        
        dict1={}
        for i,value in enumerate(nums):
            remaing=target-value
            if remaing not in dict1:
                dict1[value]=i
            else:
                return [dict1[remaing],i]


  