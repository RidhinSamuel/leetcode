class Solution:
    def longestCommonPrefix(self, strs):
        smallest_string=""
        len_of_smallest_string=len(strs[0])
        for i in strs:
            if len(i)<len_of_smallest_string:
                len_of_smallest_string=len(i)
                smallest_string=i
        for i in range(0,len_of_smallest_string-1):
            flag=1
            for j in strs:
                if j[i]
