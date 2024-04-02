"""205. Isomorphic Strings
https://leetcode.com/problems/isomorphic-strings/description/?envType=daily-question&envId=2024-04-02
Given two strings s and t, determine if they are isomorphic.
Two strings s and t are isomorphic if the characters in s can be replaced to get t.

All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character, but a character may map to itself."""
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s)!=len(t): return False
        d={}
        for i in zip(s,t):
            if (i[0] not in d):
                if (i[1] in d.values()):
                    return False
                d[i[0]]=i[1]
            if (i[0] in d and d[i[0]]!=i[1]):
                return False
        return True


if __name__=='__main__':
    # a=input()
    # b=input()
    a=Solution()
    print(a.isIsomorphic("egg","add"))