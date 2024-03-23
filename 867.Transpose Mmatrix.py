"""867. Transpose Matrix

Given a 2D integer array matrix, return the transpose of matrix.

The transpose of a matrix is the matrix flipped over its main diagonal, switching the matrix's row and column indices.

Example 1:

Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [[1,4,7],[2,5,8],[3,6,9]]
Example 2:

Input: matrix = [[1,2,3],[4,5,6]]
Output: [[1,4],[2,5],[3,6]]"""
import time,os
import psutil
class Solution:
    def transpose(self, matrix):
        row=len(matrix)
        col=len(matrix[0])
        trans=[]
        for i in range(col):
            trans.append([])
        #print(trans)
        for i in range(row):
            k=0
            for j in range(col):
                trans[k].append(matrix[i][j])
                #print(trans)
                k+=1
        return trans
        
start_time = time.perf_counter_ns()  # High-resolution timer for accuracy
process = psutil.Process(os.getpid())
memory_usage = process.memory_info().rss / 1024 / 1024  
row,col=map(int,input("Enter Row And Column").split())
matrix=[]
for i in range(row):
    l=[]
    for j in range(col):
        num=int(input("Enter Element"))
        l.append(num)
    matrix.append(l)

solution=Solution()
print(solution.transpose(matrix))
end_time = time.perf_counter_ns()
process = psutil.Process(os.getpid())
#memory_usage = process.memory_info().rss / 1024 / 1024  
runtime_ms = (end_time - start_time) / 1000000  # Convert to milliseconds
print("Runtime:", runtime_ms, "milliseconds")
print("Memory usage:", memory_usage, "MB")