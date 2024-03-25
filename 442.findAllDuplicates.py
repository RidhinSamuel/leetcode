"""442. Find All Duplicates in an Array
https://leetcode.com/problems/find-all-duplicates-in-an-array/description/?envType=daily-question&envId=2024-03-25
Given an integer array nums of length n where all the integers of nums are in the range [1, n] and each integer appears once or twice, return an array of all the integers that appears twice.
You must write an algorithm that runs in O(n) time and uses only constant extra space."""
from collections import Counter

def bruteForce(nums):
    d=Counter(nums)
    l=[]
    for i in d:
        if d[i]==2:
            l.append(i)
    return l

limit=int(input())
l=[int(input()) for _ in range(limit)]
print(bruteForce(l))
