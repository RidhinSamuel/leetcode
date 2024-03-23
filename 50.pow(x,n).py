"""Implement pow(x, n), which calculates x raised to the power n (i.e., xn).

Example 1:

Input: x = 2.00000, n = 10
Output: 1024.00000
Example 2:

Input: x = 2.10000, n = 3
Output: 9.26100
Example 3:

Input: x = 2.00000, n = -2
Output: 0.25000
Explanation: 2-2 = 1/22 = 1/4 = 0.25"""
import time,os
import psutil
class Solution:
    def myPow(self, x,n):
        res=float(pow(x,n))
        #res=float(f"{res:.5f}")
        return res
start_time = time.perf_counter_ns()  # High-resolution timer for accuracy
x=float(input())
n=int(input())
print(Solution().myPow(x,n))
end_time = time.perf_counter_ns()
runtime_ms = (end_time - start_time) / 1000000  # Convert to milliseconds
print("Runtime:", runtime_ms, "milliseconds")
process = psutil.Process(os.getpid())
memory_usage = process.memory_info().rss / 1024 / 1024  
print("Memory usage:", memory_usage, "MB")